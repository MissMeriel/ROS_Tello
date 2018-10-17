import datetime
import socket
import struct
import sys
import threading
import time
from tellopy.utils import crc8, crc16


class TelloMessage:
    MESSAGE_START = 0x00cc
    WIFI_MESSAGE = 0x001a
    # VIDEO_RATE_QUERY = 0x0028
    LIGHT_MESSAGE = 0x0035
    FLIGHT_MESSAGE = 0x0056
    LOG_MESSAGE = 0x1050
    DATE_TIME_MESSAGE = 0x0046
    ALT_LIMIT_MESSAGE = 0x1056


class TelloCommand:
    REQ_ALT_LIMIT = 0x481056
    REQ_VIDEO_SPS_PPS = 0x600025
    # VIDEO_ENCODER_RATE = 0x0020
    # VIDEO_START = 0x0025
    # EXPOSURE = 0x0034
    # TIME = 0x0046
    STICK = 0x600050
    TAKEOFF = 0x680054
    LAND = 0x680055
    # FLIP = 0x005c
    # THROW_TAKEOFF = 0x005d
    # PALM_LAND = 0x005e
    # BOUNCE = 0x1053

    # class FlipType:
    #     FRONT = 0x00
    #     LEFT = 0x01
    #     BACK = 0x02
    #     RIGHT = 0x03
    #     FORWARD_LEFT = 0x04
    #     BACK_LEFT = 0x05
    #     FORWARD_RIGHT = 0x06
    #     BACK_RIGHT = 0x07


class FlightData:
    def __init__(self, data):
        assert len(data) >= 24, "Flight data packet of invalid length: %s" % len(data)
        self.height = struct.unpack("<h", data[:2])[0]
        self.north_speed = struct.unpack("<h", data[2:4])[0]
        self.east_speed = struct.unpack("<h", data[4:6])[0]
        self.ground_speed = struct.unpack("<h", data[6:8])[0]
        self.fly_time = struct.unpack("<h", data[8:10])[0]
        tmp_data = struct.unpack("<B", data[10:11])[0]
        self.imu_state = bool(tmp_data & 0x1)
        self.pressure_state = bool(tmp_data >> 1 & 0x1)
        self.down_visual_state = bool(tmp_data >> 2 & 0x1)
        self.power_state = bool(tmp_data >> 3 & 0x1)
        self.battery_state = bool(tmp_data >> 4 & 0x1)
        self.gravity_state = bool(tmp_data >> 5 & 0x1)
        self.wind_state = bool(tmp_data >> 7 & 0x1)
        self.imu_calibration_state = struct.unpack("<b", data[11:12])[0]
        self.battery_percentage = struct.unpack("<b", data[12:13])[0]
        self.drone_fly_time_left = struct.unpack("<h", data[13:15])[0]
        self.drone_battery_left = struct.unpack("<h", data[15:17])[0]
        tmp_data = struct.unpack("<B", data[17:18])[0]
        self.em_sky = bool(tmp_data & 0x1)
        self.em_ground = bool(tmp_data >> 1 & 0x1)
        self.em_open = bool(tmp_data >> 2 & 0x1)
        self.drone_hover = bool(tmp_data >> 3 & 0x1)
        self.outage_recording = bool(tmp_data >> 4 & 0x1)
        self.battery_low = bool(tmp_data >> 5 & 0x1)
        self.battery_lower = bool(tmp_data >> 6 & 0x1)
        self.factory_mode = bool(tmp_data >> 7 & 0x1)
        self.fly_mode = struct.unpack("<b", data[18:19])[0]
        self.throw_fly_timer = struct.unpack("<b", data[19:20])[0]
        self.camera_state = struct.unpack("<b", data[20:21])[0]
        self.electrical_machinery_state = struct.unpack("<b", data[21:22])[0]
        tmp_data = struct.unpack("<B", data[22:23])[0]
        self.front_in = bool(tmp_data & 0x1)
        self.front_out = bool(tmp_data >> 1 & 0x1)
        self.front_lsc = bool(tmp_data >> 2 & 0x1)
        tmp_data = struct.unpack("<B", data[23:24])[0]
        self.temperature_height = bool(tmp_data & 0x1)

    def __repr__(self):
        string = "FlightData(\n"
        for name, value in sorted(self.__dict__.items()):
            if not name.startswith("_"):
                string += "  %s: %s\n" % (name, value)
        return string + ")"


def get_datetime():
    now = datetime.datetime.now()
    return struct.pack(
        "<BBBH", now.hour, now.minute, now.second, int(now.microsecond / 15.259)
    )


def build_packet(packet_type, data=bytearray(), sequence_id=0):
    length = len(data) + 11
    header = bytearray(struct.pack("<BH", TelloMessage.MESSAGE_START, length << 3))
    header_checksum = crc8(header)
    header = header + bytearray(struct.pack("<B", header_checksum))
    data_header = bytearray(
        struct.pack("<BHH", packet_type >> 16 & 0xff, packet_type & 0xffff, sequence_id)
    )
    packet = header + data_header + data
    packet_checksum = crc16(packet)
    packet += bytearray(struct.pack("<H", packet_checksum))
    return packet


def parse_packet(packet):
    # print("received: 0x%02x" % packet[0])
    if packet[0] != TelloMessage.MESSAGE_START:
        return 0, bytes()
    message_type = struct.unpack("<H", packet[5:7])[0]  # type: int
    if message_type == TelloMessage.FLIGHT_MESSAGE:
        return TelloMessage.FLIGHT_MESSAGE, FlightData(packet[9:])
    elif message_type == TelloMessage.WIFI_MESSAGE:
        pass
    return message_type, packet[9:-1]


class Tello:
    def __init__(
        self,
        host="192.168.10.1",
        port=8889,
        video_port=6037,
        s_timeout=0.5,
        s_buffersize=1024,
    ):
        self.host, self.port = self.addr = (host, port)
        self.video_port = video_port
        self.connection_string = bytearray(
            b"conn_req:" + struct.pack("<H", self.video_port)
        )
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(s_timeout)
        self.buffersize = s_buffersize
        self.sequence_id = 100

        self.fast = False  # type: bool
        self.throttle = 0.0  # type: float
        self.roll = 0.0  # type: float
        self.pitch = 0.0  # type: float
        self.yaw = 0.0  # type: float

        self._send(self.connection_string)

        self.shutdown_signal = threading.Event()
        self.rx_thread = threading.Thread(
            target=self._recv_loop, args=(self.shutdown_signal,)
        )
        self.rx_thread.start()
        # time.sleep(1.0)
        self.tx_thread = threading.Thread(
            target=self._send_loop, args=(self.shutdown_signal,)
        )
        self.tx_thread.start()
        self._send(build_packet(TelloCommand.REQ_ALT_LIMIT))

        self.flight_data = None

    def shutdown(self):
        self.shutdown_signal.set()
        self.socket.close()

    def _send(self, data):
        self.socket.sendto(bytes(data), self.addr)

    def _send_loop(self, shutdown_signal):
        cnt = 0
        while not shutdown_signal.is_set():
            stick_data = struct.pack(
                "<Q",
                self.fast << 44
                | int(self.yaw * 660) + 1024 << 33
                | int(self.throttle * 660) + 1024 << 22
                | int(self.pitch * 660) + 1024 << 11
                | int(self.roll * 660) + 1024,
            )[:6]
            data = bytearray(stick_data + get_datetime())
            if cnt == 5:
                self._send(build_packet(TelloCommand.REQ_VIDEO_SPS_PPS))
                cnt = 0
            self._send(build_packet(TelloCommand.STICK, data))
            time.sleep(0.2)
            cnt += 1

    def _recv_loop(self, shutdown_signal):
        while not shutdown_signal.is_set():
            try:
                packet = bytearray(self.socket.recv(self.buffersize))
            except socket.timeout as e:
                continue
            except socket.error as e:
                print(e)
                continue
            message_type, data = parse_packet(packet)
            if message_type == TelloMessage.FLIGHT_MESSAGE:
                # sys.stdout.write(repr(data) + "\r\n")
                self.flight_data = data
            elif message_type == TelloMessage.WIFI_MESSAGE:
                pass
            elif message_type == TelloMessage.DATE_TIME_MESSAGE:
                pass
            elif message_type == TelloMessage.LIGHT_MESSAGE:
                pass
            elif message_type == TelloMessage.LOG_MESSAGE:
                pass
            elif message_type == TelloMessage.ALT_LIMIT_MESSAGE:
                print("Altitude limit: %s" % struct.unpack("<H", data[1:3]))
            else:
                print("%s : 0x%x" % (message_type, message_type))

    def send_command(self, data):
        self._send(data.encode())

    def take_off(self):
        self._send(build_packet(TelloCommand.TAKEOFF, sequence_id=self.sequence_id))
        self.sequence_id += 1

    def land(self):
        self._send(
            build_packet(
                TelloCommand.LAND, bytearray([0]), sequence_id=self.sequence_id
            )
        )
        self.sequence_id += 1
