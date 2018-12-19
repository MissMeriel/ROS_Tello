;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::FlightData)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'FlightData (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::FLIGHTDATA")
  (make-package "BEGINNER_TUTORIALS::FLIGHTDATA"))

(in-package "ROS")
;;//! \htmlinclude FlightData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass beginner_tutorials::FlightData
  :super ros::object
  :slots (_header _battery_low _battery_lower _battery_percentage _battery_state _camera_state _down_visual_state _drone_battery_left _drone_fly_time_left _drone_hover _em_open _em_sky _em_ground _east_speed _electrical_machinery_state _factory_mode _fly_mode _fly_speed _fly_time _front_in _front_lsc _front_out _gravity_state _ground_speed _height _imu_calibration_state _imu_state _light_strength _north_speed _outage_recording _power_state _pressure_state _smart_video_exit_mode _temperature_height _throw_fly_timer _wifi_disturb _wifi_strength _wind_state ))

(defmethod beginner_tutorials::FlightData
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:battery_low __battery_low) nil)
    ((:battery_lower __battery_lower) nil)
    ((:battery_percentage __battery_percentage) 0)
    ((:battery_state __battery_state) nil)
    ((:camera_state __camera_state) 0)
    ((:down_visual_state __down_visual_state) nil)
    ((:drone_battery_left __drone_battery_left) 0)
    ((:drone_fly_time_left __drone_fly_time_left) 0)
    ((:drone_hover __drone_hover) nil)
    ((:em_open __em_open) nil)
    ((:em_sky __em_sky) nil)
    ((:em_ground __em_ground) nil)
    ((:east_speed __east_speed) 0)
    ((:electrical_machinery_state __electrical_machinery_state) 0)
    ((:factory_mode __factory_mode) nil)
    ((:fly_mode __fly_mode) 0)
    ((:fly_speed __fly_speed) 0)
    ((:fly_time __fly_time) 0)
    ((:front_in __front_in) nil)
    ((:front_lsc __front_lsc) nil)
    ((:front_out __front_out) nil)
    ((:gravity_state __gravity_state) nil)
    ((:ground_speed __ground_speed) 0)
    ((:height __height) 0)
    ((:imu_calibration_state __imu_calibration_state) 0)
    ((:imu_state __imu_state) nil)
    ((:light_strength __light_strength) 0)
    ((:north_speed __north_speed) 0)
    ((:outage_recording __outage_recording) nil)
    ((:power_state __power_state) nil)
    ((:pressure_state __pressure_state) nil)
    ((:smart_video_exit_mode __smart_video_exit_mode) 0)
    ((:temperature_height __temperature_height) nil)
    ((:throw_fly_timer __throw_fly_timer) 0)
    ((:wifi_disturb __wifi_disturb) 0)
    ((:wifi_strength __wifi_strength) 0)
    ((:wind_state __wind_state) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _battery_low __battery_low)
   (setq _battery_lower __battery_lower)
   (setq _battery_percentage (round __battery_percentage))
   (setq _battery_state __battery_state)
   (setq _camera_state (round __camera_state))
   (setq _down_visual_state __down_visual_state)
   (setq _drone_battery_left (round __drone_battery_left))
   (setq _drone_fly_time_left (round __drone_fly_time_left))
   (setq _drone_hover __drone_hover)
   (setq _em_open __em_open)
   (setq _em_sky __em_sky)
   (setq _em_ground __em_ground)
   (setq _east_speed (round __east_speed))
   (setq _electrical_machinery_state (round __electrical_machinery_state))
   (setq _factory_mode __factory_mode)
   (setq _fly_mode (round __fly_mode))
   (setq _fly_speed (round __fly_speed))
   (setq _fly_time (round __fly_time))
   (setq _front_in __front_in)
   (setq _front_lsc __front_lsc)
   (setq _front_out __front_out)
   (setq _gravity_state __gravity_state)
   (setq _ground_speed (round __ground_speed))
   (setq _height (round __height))
   (setq _imu_calibration_state (round __imu_calibration_state))
   (setq _imu_state __imu_state)
   (setq _light_strength (round __light_strength))
   (setq _north_speed (round __north_speed))
   (setq _outage_recording __outage_recording)
   (setq _power_state __power_state)
   (setq _pressure_state __pressure_state)
   (setq _smart_video_exit_mode (round __smart_video_exit_mode))
   (setq _temperature_height __temperature_height)
   (setq _throw_fly_timer (round __throw_fly_timer))
   (setq _wifi_disturb (round __wifi_disturb))
   (setq _wifi_strength (round __wifi_strength))
   (setq _wind_state __wind_state)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:battery_low
   (&optional __battery_low)
   (if __battery_low (setq _battery_low __battery_low)) _battery_low)
  (:battery_lower
   (&optional __battery_lower)
   (if __battery_lower (setq _battery_lower __battery_lower)) _battery_lower)
  (:battery_percentage
   (&optional __battery_percentage)
   (if __battery_percentage (setq _battery_percentage __battery_percentage)) _battery_percentage)
  (:battery_state
   (&optional __battery_state)
   (if __battery_state (setq _battery_state __battery_state)) _battery_state)
  (:camera_state
   (&optional __camera_state)
   (if __camera_state (setq _camera_state __camera_state)) _camera_state)
  (:down_visual_state
   (&optional __down_visual_state)
   (if __down_visual_state (setq _down_visual_state __down_visual_state)) _down_visual_state)
  (:drone_battery_left
   (&optional __drone_battery_left)
   (if __drone_battery_left (setq _drone_battery_left __drone_battery_left)) _drone_battery_left)
  (:drone_fly_time_left
   (&optional __drone_fly_time_left)
   (if __drone_fly_time_left (setq _drone_fly_time_left __drone_fly_time_left)) _drone_fly_time_left)
  (:drone_hover
   (&optional __drone_hover)
   (if __drone_hover (setq _drone_hover __drone_hover)) _drone_hover)
  (:em_open
   (&optional __em_open)
   (if __em_open (setq _em_open __em_open)) _em_open)
  (:em_sky
   (&optional __em_sky)
   (if __em_sky (setq _em_sky __em_sky)) _em_sky)
  (:em_ground
   (&optional __em_ground)
   (if __em_ground (setq _em_ground __em_ground)) _em_ground)
  (:east_speed
   (&optional __east_speed)
   (if __east_speed (setq _east_speed __east_speed)) _east_speed)
  (:electrical_machinery_state
   (&optional __electrical_machinery_state)
   (if __electrical_machinery_state (setq _electrical_machinery_state __electrical_machinery_state)) _electrical_machinery_state)
  (:factory_mode
   (&optional __factory_mode)
   (if __factory_mode (setq _factory_mode __factory_mode)) _factory_mode)
  (:fly_mode
   (&optional __fly_mode)
   (if __fly_mode (setq _fly_mode __fly_mode)) _fly_mode)
  (:fly_speed
   (&optional __fly_speed)
   (if __fly_speed (setq _fly_speed __fly_speed)) _fly_speed)
  (:fly_time
   (&optional __fly_time)
   (if __fly_time (setq _fly_time __fly_time)) _fly_time)
  (:front_in
   (&optional __front_in)
   (if __front_in (setq _front_in __front_in)) _front_in)
  (:front_lsc
   (&optional __front_lsc)
   (if __front_lsc (setq _front_lsc __front_lsc)) _front_lsc)
  (:front_out
   (&optional __front_out)
   (if __front_out (setq _front_out __front_out)) _front_out)
  (:gravity_state
   (&optional __gravity_state)
   (if __gravity_state (setq _gravity_state __gravity_state)) _gravity_state)
  (:ground_speed
   (&optional __ground_speed)
   (if __ground_speed (setq _ground_speed __ground_speed)) _ground_speed)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:imu_calibration_state
   (&optional __imu_calibration_state)
   (if __imu_calibration_state (setq _imu_calibration_state __imu_calibration_state)) _imu_calibration_state)
  (:imu_state
   (&optional __imu_state)
   (if __imu_state (setq _imu_state __imu_state)) _imu_state)
  (:light_strength
   (&optional __light_strength)
   (if __light_strength (setq _light_strength __light_strength)) _light_strength)
  (:north_speed
   (&optional __north_speed)
   (if __north_speed (setq _north_speed __north_speed)) _north_speed)
  (:outage_recording
   (&optional __outage_recording)
   (if __outage_recording (setq _outage_recording __outage_recording)) _outage_recording)
  (:power_state
   (&optional __power_state)
   (if __power_state (setq _power_state __power_state)) _power_state)
  (:pressure_state
   (&optional __pressure_state)
   (if __pressure_state (setq _pressure_state __pressure_state)) _pressure_state)
  (:smart_video_exit_mode
   (&optional __smart_video_exit_mode)
   (if __smart_video_exit_mode (setq _smart_video_exit_mode __smart_video_exit_mode)) _smart_video_exit_mode)
  (:temperature_height
   (&optional __temperature_height)
   (if __temperature_height (setq _temperature_height __temperature_height)) _temperature_height)
  (:throw_fly_timer
   (&optional __throw_fly_timer)
   (if __throw_fly_timer (setq _throw_fly_timer __throw_fly_timer)) _throw_fly_timer)
  (:wifi_disturb
   (&optional __wifi_disturb)
   (if __wifi_disturb (setq _wifi_disturb __wifi_disturb)) _wifi_disturb)
  (:wifi_strength
   (&optional __wifi_strength)
   (if __wifi_strength (setq _wifi_strength __wifi_strength)) _wifi_strength)
  (:wind_state
   (&optional __wind_state)
   (if __wind_state (setq _wind_state __wind_state)) _wind_state)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _battery_low
    1
    ;; bool _battery_lower
    1
    ;; int8 _battery_percentage
    1
    ;; bool _battery_state
    1
    ;; int8 _camera_state
    1
    ;; bool _down_visual_state
    1
    ;; int16 _drone_battery_left
    2
    ;; int16 _drone_fly_time_left
    2
    ;; bool _drone_hover
    1
    ;; bool _em_open
    1
    ;; bool _em_sky
    1
    ;; bool _em_ground
    1
    ;; int16 _east_speed
    2
    ;; int16 _electrical_machinery_state
    2
    ;; bool _factory_mode
    1
    ;; int8 _fly_mode
    1
    ;; int16 _fly_speed
    2
    ;; int16 _fly_time
    2
    ;; bool _front_in
    1
    ;; bool _front_lsc
    1
    ;; bool _front_out
    1
    ;; bool _gravity_state
    1
    ;; int16 _ground_speed
    2
    ;; int16 _height
    2
    ;; int8 _imu_calibration_state
    1
    ;; bool _imu_state
    1
    ;; int8 _light_strength
    1
    ;; int16 _north_speed
    2
    ;; bool _outage_recording
    1
    ;; bool _power_state
    1
    ;; bool _pressure_state
    1
    ;; int16 _smart_video_exit_mode
    2
    ;; bool _temperature_height
    1
    ;; int8 _throw_fly_timer
    1
    ;; int8 _wifi_disturb
    1
    ;; int8 _wifi_strength
    1
    ;; bool _wind_state
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _battery_low
       (if _battery_low (write-byte -1 s) (write-byte 0 s))
     ;; bool _battery_lower
       (if _battery_lower (write-byte -1 s) (write-byte 0 s))
     ;; int8 _battery_percentage
       (write-byte _battery_percentage s)
     ;; bool _battery_state
       (if _battery_state (write-byte -1 s) (write-byte 0 s))
     ;; int8 _camera_state
       (write-byte _camera_state s)
     ;; bool _down_visual_state
       (if _down_visual_state (write-byte -1 s) (write-byte 0 s))
     ;; int16 _drone_battery_left
       (write-word _drone_battery_left s)
     ;; int16 _drone_fly_time_left
       (write-word _drone_fly_time_left s)
     ;; bool _drone_hover
       (if _drone_hover (write-byte -1 s) (write-byte 0 s))
     ;; bool _em_open
       (if _em_open (write-byte -1 s) (write-byte 0 s))
     ;; bool _em_sky
       (if _em_sky (write-byte -1 s) (write-byte 0 s))
     ;; bool _em_ground
       (if _em_ground (write-byte -1 s) (write-byte 0 s))
     ;; int16 _east_speed
       (write-word _east_speed s)
     ;; int16 _electrical_machinery_state
       (write-word _electrical_machinery_state s)
     ;; bool _factory_mode
       (if _factory_mode (write-byte -1 s) (write-byte 0 s))
     ;; int8 _fly_mode
       (write-byte _fly_mode s)
     ;; int16 _fly_speed
       (write-word _fly_speed s)
     ;; int16 _fly_time
       (write-word _fly_time s)
     ;; bool _front_in
       (if _front_in (write-byte -1 s) (write-byte 0 s))
     ;; bool _front_lsc
       (if _front_lsc (write-byte -1 s) (write-byte 0 s))
     ;; bool _front_out
       (if _front_out (write-byte -1 s) (write-byte 0 s))
     ;; bool _gravity_state
       (if _gravity_state (write-byte -1 s) (write-byte 0 s))
     ;; int16 _ground_speed
       (write-word _ground_speed s)
     ;; int16 _height
       (write-word _height s)
     ;; int8 _imu_calibration_state
       (write-byte _imu_calibration_state s)
     ;; bool _imu_state
       (if _imu_state (write-byte -1 s) (write-byte 0 s))
     ;; int8 _light_strength
       (write-byte _light_strength s)
     ;; int16 _north_speed
       (write-word _north_speed s)
     ;; bool _outage_recording
       (if _outage_recording (write-byte -1 s) (write-byte 0 s))
     ;; bool _power_state
       (if _power_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _pressure_state
       (if _pressure_state (write-byte -1 s) (write-byte 0 s))
     ;; int16 _smart_video_exit_mode
       (write-word _smart_video_exit_mode s)
     ;; bool _temperature_height
       (if _temperature_height (write-byte -1 s) (write-byte 0 s))
     ;; int8 _throw_fly_timer
       (write-byte _throw_fly_timer s)
     ;; int8 _wifi_disturb
       (write-byte _wifi_disturb s)
     ;; int8 _wifi_strength
       (write-byte _wifi_strength s)
     ;; bool _wind_state
       (if _wind_state (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _battery_low
     (setq _battery_low (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _battery_lower
     (setq _battery_lower (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _battery_percentage
     (setq _battery_percentage (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _battery_percentage 127) (setq _battery_percentage (- _battery_percentage 256)))
   ;; bool _battery_state
     (setq _battery_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _camera_state
     (setq _camera_state (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _camera_state 127) (setq _camera_state (- _camera_state 256)))
   ;; bool _down_visual_state
     (setq _down_visual_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16 _drone_battery_left
     (setq _drone_battery_left (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _drone_fly_time_left
     (setq _drone_fly_time_left (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _drone_hover
     (setq _drone_hover (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _em_open
     (setq _em_open (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _em_sky
     (setq _em_sky (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _em_ground
     (setq _em_ground (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16 _east_speed
     (setq _east_speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _electrical_machinery_state
     (setq _electrical_machinery_state (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _factory_mode
     (setq _factory_mode (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _fly_mode
     (setq _fly_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _fly_mode 127) (setq _fly_mode (- _fly_mode 256)))
   ;; int16 _fly_speed
     (setq _fly_speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _fly_time
     (setq _fly_time (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _front_in
     (setq _front_in (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _front_lsc
     (setq _front_lsc (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _front_out
     (setq _front_out (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _gravity_state
     (setq _gravity_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16 _ground_speed
     (setq _ground_speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _height
     (setq _height (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int8 _imu_calibration_state
     (setq _imu_calibration_state (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _imu_calibration_state 127) (setq _imu_calibration_state (- _imu_calibration_state 256)))
   ;; bool _imu_state
     (setq _imu_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _light_strength
     (setq _light_strength (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _light_strength 127) (setq _light_strength (- _light_strength 256)))
   ;; int16 _north_speed
     (setq _north_speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _outage_recording
     (setq _outage_recording (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _power_state
     (setq _power_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _pressure_state
     (setq _pressure_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16 _smart_video_exit_mode
     (setq _smart_video_exit_mode (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _temperature_height
     (setq _temperature_height (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _throw_fly_timer
     (setq _throw_fly_timer (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _throw_fly_timer 127) (setq _throw_fly_timer (- _throw_fly_timer 256)))
   ;; int8 _wifi_disturb
     (setq _wifi_disturb (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _wifi_disturb 127) (setq _wifi_disturb (- _wifi_disturb 256)))
   ;; int8 _wifi_strength
     (setq _wifi_strength (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _wifi_strength 127) (setq _wifi_strength (- _wifi_strength 256)))
   ;; bool _wind_state
     (setq _wind_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get beginner_tutorials::FlightData :md5sum-) "8c659bf934436b7cb2d969ddd123268a")
(setf (get beginner_tutorials::FlightData :datatype-) "beginner_tutorials/FlightData")
(setf (get beginner_tutorials::FlightData :definition-)
      "Header header
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

")



(provide :beginner_tutorials/FlightData "8c659bf934436b7cb2d969ddd123268a")


