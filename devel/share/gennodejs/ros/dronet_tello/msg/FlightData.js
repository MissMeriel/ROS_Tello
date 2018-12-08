// Auto-generated. Do not edit!

// (in-package dronet_tello.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class FlightData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.battery_low = null;
      this.battery_lower = null;
      this.battery_percentage = null;
      this.battery_state = null;
      this.camera_state = null;
      this.down_visual_state = null;
      this.drone_battery_left = null;
      this.drone_fly_time_left = null;
      this.drone_hover = null;
      this.em_open = null;
      this.em_sky = null;
      this.em_ground = null;
      this.east_speed = null;
      this.electrical_machinery_state = null;
      this.factory_mode = null;
      this.fly_mode = null;
      this.fly_speed = null;
      this.fly_time = null;
      this.front_in = null;
      this.front_lsc = null;
      this.front_out = null;
      this.gravity_state = null;
      this.ground_speed = null;
      this.height = null;
      this.imu_calibration_state = null;
      this.imu_state = null;
      this.light_strength = null;
      this.north_speed = null;
      this.outage_recording = null;
      this.power_state = null;
      this.pressure_state = null;
      this.smart_video_exit_mode = null;
      this.temperature_height = null;
      this.throw_fly_timer = null;
      this.wifi_disturb = null;
      this.wifi_strength = null;
      this.wind_state = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('battery_low')) {
        this.battery_low = initObj.battery_low
      }
      else {
        this.battery_low = false;
      }
      if (initObj.hasOwnProperty('battery_lower')) {
        this.battery_lower = initObj.battery_lower
      }
      else {
        this.battery_lower = false;
      }
      if (initObj.hasOwnProperty('battery_percentage')) {
        this.battery_percentage = initObj.battery_percentage
      }
      else {
        this.battery_percentage = 0;
      }
      if (initObj.hasOwnProperty('battery_state')) {
        this.battery_state = initObj.battery_state
      }
      else {
        this.battery_state = false;
      }
      if (initObj.hasOwnProperty('camera_state')) {
        this.camera_state = initObj.camera_state
      }
      else {
        this.camera_state = 0;
      }
      if (initObj.hasOwnProperty('down_visual_state')) {
        this.down_visual_state = initObj.down_visual_state
      }
      else {
        this.down_visual_state = false;
      }
      if (initObj.hasOwnProperty('drone_battery_left')) {
        this.drone_battery_left = initObj.drone_battery_left
      }
      else {
        this.drone_battery_left = 0;
      }
      if (initObj.hasOwnProperty('drone_fly_time_left')) {
        this.drone_fly_time_left = initObj.drone_fly_time_left
      }
      else {
        this.drone_fly_time_left = 0;
      }
      if (initObj.hasOwnProperty('drone_hover')) {
        this.drone_hover = initObj.drone_hover
      }
      else {
        this.drone_hover = false;
      }
      if (initObj.hasOwnProperty('em_open')) {
        this.em_open = initObj.em_open
      }
      else {
        this.em_open = false;
      }
      if (initObj.hasOwnProperty('em_sky')) {
        this.em_sky = initObj.em_sky
      }
      else {
        this.em_sky = false;
      }
      if (initObj.hasOwnProperty('em_ground')) {
        this.em_ground = initObj.em_ground
      }
      else {
        this.em_ground = false;
      }
      if (initObj.hasOwnProperty('east_speed')) {
        this.east_speed = initObj.east_speed
      }
      else {
        this.east_speed = 0;
      }
      if (initObj.hasOwnProperty('electrical_machinery_state')) {
        this.electrical_machinery_state = initObj.electrical_machinery_state
      }
      else {
        this.electrical_machinery_state = 0;
      }
      if (initObj.hasOwnProperty('factory_mode')) {
        this.factory_mode = initObj.factory_mode
      }
      else {
        this.factory_mode = false;
      }
      if (initObj.hasOwnProperty('fly_mode')) {
        this.fly_mode = initObj.fly_mode
      }
      else {
        this.fly_mode = 0;
      }
      if (initObj.hasOwnProperty('fly_speed')) {
        this.fly_speed = initObj.fly_speed
      }
      else {
        this.fly_speed = 0;
      }
      if (initObj.hasOwnProperty('fly_time')) {
        this.fly_time = initObj.fly_time
      }
      else {
        this.fly_time = 0;
      }
      if (initObj.hasOwnProperty('front_in')) {
        this.front_in = initObj.front_in
      }
      else {
        this.front_in = false;
      }
      if (initObj.hasOwnProperty('front_lsc')) {
        this.front_lsc = initObj.front_lsc
      }
      else {
        this.front_lsc = false;
      }
      if (initObj.hasOwnProperty('front_out')) {
        this.front_out = initObj.front_out
      }
      else {
        this.front_out = false;
      }
      if (initObj.hasOwnProperty('gravity_state')) {
        this.gravity_state = initObj.gravity_state
      }
      else {
        this.gravity_state = false;
      }
      if (initObj.hasOwnProperty('ground_speed')) {
        this.ground_speed = initObj.ground_speed
      }
      else {
        this.ground_speed = 0;
      }
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = 0;
      }
      if (initObj.hasOwnProperty('imu_calibration_state')) {
        this.imu_calibration_state = initObj.imu_calibration_state
      }
      else {
        this.imu_calibration_state = 0;
      }
      if (initObj.hasOwnProperty('imu_state')) {
        this.imu_state = initObj.imu_state
      }
      else {
        this.imu_state = false;
      }
      if (initObj.hasOwnProperty('light_strength')) {
        this.light_strength = initObj.light_strength
      }
      else {
        this.light_strength = 0;
      }
      if (initObj.hasOwnProperty('north_speed')) {
        this.north_speed = initObj.north_speed
      }
      else {
        this.north_speed = 0;
      }
      if (initObj.hasOwnProperty('outage_recording')) {
        this.outage_recording = initObj.outage_recording
      }
      else {
        this.outage_recording = false;
      }
      if (initObj.hasOwnProperty('power_state')) {
        this.power_state = initObj.power_state
      }
      else {
        this.power_state = false;
      }
      if (initObj.hasOwnProperty('pressure_state')) {
        this.pressure_state = initObj.pressure_state
      }
      else {
        this.pressure_state = false;
      }
      if (initObj.hasOwnProperty('smart_video_exit_mode')) {
        this.smart_video_exit_mode = initObj.smart_video_exit_mode
      }
      else {
        this.smart_video_exit_mode = 0;
      }
      if (initObj.hasOwnProperty('temperature_height')) {
        this.temperature_height = initObj.temperature_height
      }
      else {
        this.temperature_height = false;
      }
      if (initObj.hasOwnProperty('throw_fly_timer')) {
        this.throw_fly_timer = initObj.throw_fly_timer
      }
      else {
        this.throw_fly_timer = 0;
      }
      if (initObj.hasOwnProperty('wifi_disturb')) {
        this.wifi_disturb = initObj.wifi_disturb
      }
      else {
        this.wifi_disturb = 0;
      }
      if (initObj.hasOwnProperty('wifi_strength')) {
        this.wifi_strength = initObj.wifi_strength
      }
      else {
        this.wifi_strength = 0;
      }
      if (initObj.hasOwnProperty('wind_state')) {
        this.wind_state = initObj.wind_state
      }
      else {
        this.wind_state = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FlightData
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [battery_low]
    bufferOffset = _serializer.bool(obj.battery_low, buffer, bufferOffset);
    // Serialize message field [battery_lower]
    bufferOffset = _serializer.bool(obj.battery_lower, buffer, bufferOffset);
    // Serialize message field [battery_percentage]
    bufferOffset = _serializer.int8(obj.battery_percentage, buffer, bufferOffset);
    // Serialize message field [battery_state]
    bufferOffset = _serializer.bool(obj.battery_state, buffer, bufferOffset);
    // Serialize message field [camera_state]
    bufferOffset = _serializer.int8(obj.camera_state, buffer, bufferOffset);
    // Serialize message field [down_visual_state]
    bufferOffset = _serializer.bool(obj.down_visual_state, buffer, bufferOffset);
    // Serialize message field [drone_battery_left]
    bufferOffset = _serializer.int16(obj.drone_battery_left, buffer, bufferOffset);
    // Serialize message field [drone_fly_time_left]
    bufferOffset = _serializer.int16(obj.drone_fly_time_left, buffer, bufferOffset);
    // Serialize message field [drone_hover]
    bufferOffset = _serializer.bool(obj.drone_hover, buffer, bufferOffset);
    // Serialize message field [em_open]
    bufferOffset = _serializer.bool(obj.em_open, buffer, bufferOffset);
    // Serialize message field [em_sky]
    bufferOffset = _serializer.bool(obj.em_sky, buffer, bufferOffset);
    // Serialize message field [em_ground]
    bufferOffset = _serializer.bool(obj.em_ground, buffer, bufferOffset);
    // Serialize message field [east_speed]
    bufferOffset = _serializer.int16(obj.east_speed, buffer, bufferOffset);
    // Serialize message field [electrical_machinery_state]
    bufferOffset = _serializer.int16(obj.electrical_machinery_state, buffer, bufferOffset);
    // Serialize message field [factory_mode]
    bufferOffset = _serializer.bool(obj.factory_mode, buffer, bufferOffset);
    // Serialize message field [fly_mode]
    bufferOffset = _serializer.int8(obj.fly_mode, buffer, bufferOffset);
    // Serialize message field [fly_speed]
    bufferOffset = _serializer.int16(obj.fly_speed, buffer, bufferOffset);
    // Serialize message field [fly_time]
    bufferOffset = _serializer.int16(obj.fly_time, buffer, bufferOffset);
    // Serialize message field [front_in]
    bufferOffset = _serializer.bool(obj.front_in, buffer, bufferOffset);
    // Serialize message field [front_lsc]
    bufferOffset = _serializer.bool(obj.front_lsc, buffer, bufferOffset);
    // Serialize message field [front_out]
    bufferOffset = _serializer.bool(obj.front_out, buffer, bufferOffset);
    // Serialize message field [gravity_state]
    bufferOffset = _serializer.bool(obj.gravity_state, buffer, bufferOffset);
    // Serialize message field [ground_speed]
    bufferOffset = _serializer.int16(obj.ground_speed, buffer, bufferOffset);
    // Serialize message field [height]
    bufferOffset = _serializer.int16(obj.height, buffer, bufferOffset);
    // Serialize message field [imu_calibration_state]
    bufferOffset = _serializer.int8(obj.imu_calibration_state, buffer, bufferOffset);
    // Serialize message field [imu_state]
    bufferOffset = _serializer.bool(obj.imu_state, buffer, bufferOffset);
    // Serialize message field [light_strength]
    bufferOffset = _serializer.int8(obj.light_strength, buffer, bufferOffset);
    // Serialize message field [north_speed]
    bufferOffset = _serializer.int16(obj.north_speed, buffer, bufferOffset);
    // Serialize message field [outage_recording]
    bufferOffset = _serializer.bool(obj.outage_recording, buffer, bufferOffset);
    // Serialize message field [power_state]
    bufferOffset = _serializer.bool(obj.power_state, buffer, bufferOffset);
    // Serialize message field [pressure_state]
    bufferOffset = _serializer.bool(obj.pressure_state, buffer, bufferOffset);
    // Serialize message field [smart_video_exit_mode]
    bufferOffset = _serializer.int16(obj.smart_video_exit_mode, buffer, bufferOffset);
    // Serialize message field [temperature_height]
    bufferOffset = _serializer.bool(obj.temperature_height, buffer, bufferOffset);
    // Serialize message field [throw_fly_timer]
    bufferOffset = _serializer.int8(obj.throw_fly_timer, buffer, bufferOffset);
    // Serialize message field [wifi_disturb]
    bufferOffset = _serializer.int8(obj.wifi_disturb, buffer, bufferOffset);
    // Serialize message field [wifi_strength]
    bufferOffset = _serializer.int8(obj.wifi_strength, buffer, bufferOffset);
    // Serialize message field [wind_state]
    bufferOffset = _serializer.bool(obj.wind_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FlightData
    let len;
    let data = new FlightData(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [battery_low]
    data.battery_low = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [battery_lower]
    data.battery_lower = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [battery_percentage]
    data.battery_percentage = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [battery_state]
    data.battery_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [camera_state]
    data.camera_state = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [down_visual_state]
    data.down_visual_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [drone_battery_left]
    data.drone_battery_left = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [drone_fly_time_left]
    data.drone_fly_time_left = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [drone_hover]
    data.drone_hover = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [em_open]
    data.em_open = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [em_sky]
    data.em_sky = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [em_ground]
    data.em_ground = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [east_speed]
    data.east_speed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [electrical_machinery_state]
    data.electrical_machinery_state = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [factory_mode]
    data.factory_mode = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [fly_mode]
    data.fly_mode = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [fly_speed]
    data.fly_speed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [fly_time]
    data.fly_time = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [front_in]
    data.front_in = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [front_lsc]
    data.front_lsc = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [front_out]
    data.front_out = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [gravity_state]
    data.gravity_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ground_speed]
    data.ground_speed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [height]
    data.height = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [imu_calibration_state]
    data.imu_calibration_state = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [imu_state]
    data.imu_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [light_strength]
    data.light_strength = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [north_speed]
    data.north_speed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [outage_recording]
    data.outage_recording = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [power_state]
    data.power_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [pressure_state]
    data.pressure_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [smart_video_exit_mode]
    data.smart_video_exit_mode = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [temperature_height]
    data.temperature_height = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [throw_fly_timer]
    data.throw_fly_timer = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [wifi_disturb]
    data.wifi_disturb = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [wifi_strength]
    data.wifi_strength = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [wind_state]
    data.wind_state = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 47;
  }

  static datatype() {
    // Returns string type for a message object
    return 'dronet_tello/FlightData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8c659bf934436b7cb2d969ddd123268a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    bool battery_low
    bool battery_lower
    int8 battery_percentage
    bool battery_state
    int8 camera_state
    bool down_visual_state
    int16 drone_battery_left
    int16 drone_fly_time_left
    bool drone_hover
    bool em_open
    bool em_sky
    bool em_ground
    int16 east_speed
    int16 electrical_machinery_state
    bool factory_mode
    int8 fly_mode
    int16 fly_speed
    int16 fly_time
    bool front_in
    bool front_lsc
    bool front_out
    bool gravity_state
    int16 ground_speed
    int16 height
    int8 imu_calibration_state
    bool imu_state
    int8 light_strength
    int16 north_speed
    bool outage_recording
    bool power_state
    bool pressure_state
    int16 smart_video_exit_mode
    bool temperature_height
    int8 throw_fly_timer
    int8 wifi_disturb
    int8 wifi_strength
    bool wind_state
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FlightData(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.battery_low !== undefined) {
      resolved.battery_low = msg.battery_low;
    }
    else {
      resolved.battery_low = false
    }

    if (msg.battery_lower !== undefined) {
      resolved.battery_lower = msg.battery_lower;
    }
    else {
      resolved.battery_lower = false
    }

    if (msg.battery_percentage !== undefined) {
      resolved.battery_percentage = msg.battery_percentage;
    }
    else {
      resolved.battery_percentage = 0
    }

    if (msg.battery_state !== undefined) {
      resolved.battery_state = msg.battery_state;
    }
    else {
      resolved.battery_state = false
    }

    if (msg.camera_state !== undefined) {
      resolved.camera_state = msg.camera_state;
    }
    else {
      resolved.camera_state = 0
    }

    if (msg.down_visual_state !== undefined) {
      resolved.down_visual_state = msg.down_visual_state;
    }
    else {
      resolved.down_visual_state = false
    }

    if (msg.drone_battery_left !== undefined) {
      resolved.drone_battery_left = msg.drone_battery_left;
    }
    else {
      resolved.drone_battery_left = 0
    }

    if (msg.drone_fly_time_left !== undefined) {
      resolved.drone_fly_time_left = msg.drone_fly_time_left;
    }
    else {
      resolved.drone_fly_time_left = 0
    }

    if (msg.drone_hover !== undefined) {
      resolved.drone_hover = msg.drone_hover;
    }
    else {
      resolved.drone_hover = false
    }

    if (msg.em_open !== undefined) {
      resolved.em_open = msg.em_open;
    }
    else {
      resolved.em_open = false
    }

    if (msg.em_sky !== undefined) {
      resolved.em_sky = msg.em_sky;
    }
    else {
      resolved.em_sky = false
    }

    if (msg.em_ground !== undefined) {
      resolved.em_ground = msg.em_ground;
    }
    else {
      resolved.em_ground = false
    }

    if (msg.east_speed !== undefined) {
      resolved.east_speed = msg.east_speed;
    }
    else {
      resolved.east_speed = 0
    }

    if (msg.electrical_machinery_state !== undefined) {
      resolved.electrical_machinery_state = msg.electrical_machinery_state;
    }
    else {
      resolved.electrical_machinery_state = 0
    }

    if (msg.factory_mode !== undefined) {
      resolved.factory_mode = msg.factory_mode;
    }
    else {
      resolved.factory_mode = false
    }

    if (msg.fly_mode !== undefined) {
      resolved.fly_mode = msg.fly_mode;
    }
    else {
      resolved.fly_mode = 0
    }

    if (msg.fly_speed !== undefined) {
      resolved.fly_speed = msg.fly_speed;
    }
    else {
      resolved.fly_speed = 0
    }

    if (msg.fly_time !== undefined) {
      resolved.fly_time = msg.fly_time;
    }
    else {
      resolved.fly_time = 0
    }

    if (msg.front_in !== undefined) {
      resolved.front_in = msg.front_in;
    }
    else {
      resolved.front_in = false
    }

    if (msg.front_lsc !== undefined) {
      resolved.front_lsc = msg.front_lsc;
    }
    else {
      resolved.front_lsc = false
    }

    if (msg.front_out !== undefined) {
      resolved.front_out = msg.front_out;
    }
    else {
      resolved.front_out = false
    }

    if (msg.gravity_state !== undefined) {
      resolved.gravity_state = msg.gravity_state;
    }
    else {
      resolved.gravity_state = false
    }

    if (msg.ground_speed !== undefined) {
      resolved.ground_speed = msg.ground_speed;
    }
    else {
      resolved.ground_speed = 0
    }

    if (msg.height !== undefined) {
      resolved.height = msg.height;
    }
    else {
      resolved.height = 0
    }

    if (msg.imu_calibration_state !== undefined) {
      resolved.imu_calibration_state = msg.imu_calibration_state;
    }
    else {
      resolved.imu_calibration_state = 0
    }

    if (msg.imu_state !== undefined) {
      resolved.imu_state = msg.imu_state;
    }
    else {
      resolved.imu_state = false
    }

    if (msg.light_strength !== undefined) {
      resolved.light_strength = msg.light_strength;
    }
    else {
      resolved.light_strength = 0
    }

    if (msg.north_speed !== undefined) {
      resolved.north_speed = msg.north_speed;
    }
    else {
      resolved.north_speed = 0
    }

    if (msg.outage_recording !== undefined) {
      resolved.outage_recording = msg.outage_recording;
    }
    else {
      resolved.outage_recording = false
    }

    if (msg.power_state !== undefined) {
      resolved.power_state = msg.power_state;
    }
    else {
      resolved.power_state = false
    }

    if (msg.pressure_state !== undefined) {
      resolved.pressure_state = msg.pressure_state;
    }
    else {
      resolved.pressure_state = false
    }

    if (msg.smart_video_exit_mode !== undefined) {
      resolved.smart_video_exit_mode = msg.smart_video_exit_mode;
    }
    else {
      resolved.smart_video_exit_mode = 0
    }

    if (msg.temperature_height !== undefined) {
      resolved.temperature_height = msg.temperature_height;
    }
    else {
      resolved.temperature_height = false
    }

    if (msg.throw_fly_timer !== undefined) {
      resolved.throw_fly_timer = msg.throw_fly_timer;
    }
    else {
      resolved.throw_fly_timer = 0
    }

    if (msg.wifi_disturb !== undefined) {
      resolved.wifi_disturb = msg.wifi_disturb;
    }
    else {
      resolved.wifi_disturb = 0
    }

    if (msg.wifi_strength !== undefined) {
      resolved.wifi_strength = msg.wifi_strength;
    }
    else {
      resolved.wifi_strength = 0
    }

    if (msg.wind_state !== undefined) {
      resolved.wind_state = msg.wind_state;
    }
    else {
      resolved.wind_state = false
    }

    return resolved;
    }
};

module.exports = FlightData;
