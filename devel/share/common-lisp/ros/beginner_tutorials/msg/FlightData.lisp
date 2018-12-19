; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude FlightData.msg.html

(cl:defclass <FlightData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (battery_low
    :reader battery_low
    :initarg :battery_low
    :type cl:boolean
    :initform cl:nil)
   (battery_lower
    :reader battery_lower
    :initarg :battery_lower
    :type cl:boolean
    :initform cl:nil)
   (battery_percentage
    :reader battery_percentage
    :initarg :battery_percentage
    :type cl:fixnum
    :initform 0)
   (battery_state
    :reader battery_state
    :initarg :battery_state
    :type cl:boolean
    :initform cl:nil)
   (camera_state
    :reader camera_state
    :initarg :camera_state
    :type cl:fixnum
    :initform 0)
   (down_visual_state
    :reader down_visual_state
    :initarg :down_visual_state
    :type cl:boolean
    :initform cl:nil)
   (drone_battery_left
    :reader drone_battery_left
    :initarg :drone_battery_left
    :type cl:fixnum
    :initform 0)
   (drone_fly_time_left
    :reader drone_fly_time_left
    :initarg :drone_fly_time_left
    :type cl:fixnum
    :initform 0)
   (drone_hover
    :reader drone_hover
    :initarg :drone_hover
    :type cl:boolean
    :initform cl:nil)
   (em_open
    :reader em_open
    :initarg :em_open
    :type cl:boolean
    :initform cl:nil)
   (em_sky
    :reader em_sky
    :initarg :em_sky
    :type cl:boolean
    :initform cl:nil)
   (em_ground
    :reader em_ground
    :initarg :em_ground
    :type cl:boolean
    :initform cl:nil)
   (east_speed
    :reader east_speed
    :initarg :east_speed
    :type cl:fixnum
    :initform 0)
   (electrical_machinery_state
    :reader electrical_machinery_state
    :initarg :electrical_machinery_state
    :type cl:fixnum
    :initform 0)
   (factory_mode
    :reader factory_mode
    :initarg :factory_mode
    :type cl:boolean
    :initform cl:nil)
   (fly_mode
    :reader fly_mode
    :initarg :fly_mode
    :type cl:fixnum
    :initform 0)
   (fly_speed
    :reader fly_speed
    :initarg :fly_speed
    :type cl:fixnum
    :initform 0)
   (fly_time
    :reader fly_time
    :initarg :fly_time
    :type cl:fixnum
    :initform 0)
   (front_in
    :reader front_in
    :initarg :front_in
    :type cl:boolean
    :initform cl:nil)
   (front_lsc
    :reader front_lsc
    :initarg :front_lsc
    :type cl:boolean
    :initform cl:nil)
   (front_out
    :reader front_out
    :initarg :front_out
    :type cl:boolean
    :initform cl:nil)
   (gravity_state
    :reader gravity_state
    :initarg :gravity_state
    :type cl:boolean
    :initform cl:nil)
   (ground_speed
    :reader ground_speed
    :initarg :ground_speed
    :type cl:fixnum
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:fixnum
    :initform 0)
   (imu_calibration_state
    :reader imu_calibration_state
    :initarg :imu_calibration_state
    :type cl:fixnum
    :initform 0)
   (imu_state
    :reader imu_state
    :initarg :imu_state
    :type cl:boolean
    :initform cl:nil)
   (light_strength
    :reader light_strength
    :initarg :light_strength
    :type cl:fixnum
    :initform 0)
   (north_speed
    :reader north_speed
    :initarg :north_speed
    :type cl:fixnum
    :initform 0)
   (outage_recording
    :reader outage_recording
    :initarg :outage_recording
    :type cl:boolean
    :initform cl:nil)
   (power_state
    :reader power_state
    :initarg :power_state
    :type cl:boolean
    :initform cl:nil)
   (pressure_state
    :reader pressure_state
    :initarg :pressure_state
    :type cl:boolean
    :initform cl:nil)
   (smart_video_exit_mode
    :reader smart_video_exit_mode
    :initarg :smart_video_exit_mode
    :type cl:fixnum
    :initform 0)
   (temperature_height
    :reader temperature_height
    :initarg :temperature_height
    :type cl:boolean
    :initform cl:nil)
   (throw_fly_timer
    :reader throw_fly_timer
    :initarg :throw_fly_timer
    :type cl:fixnum
    :initform 0)
   (wifi_disturb
    :reader wifi_disturb
    :initarg :wifi_disturb
    :type cl:fixnum
    :initform 0)
   (wifi_strength
    :reader wifi_strength
    :initarg :wifi_strength
    :type cl:fixnum
    :initform 0)
   (wind_state
    :reader wind_state
    :initarg :wind_state
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass FlightData (<FlightData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FlightData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FlightData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<FlightData> is deprecated: use beginner_tutorials-msg:FlightData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:header-val is deprecated.  Use beginner_tutorials-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'battery_low-val :lambda-list '(m))
(cl:defmethod battery_low-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:battery_low-val is deprecated.  Use beginner_tutorials-msg:battery_low instead.")
  (battery_low m))

(cl:ensure-generic-function 'battery_lower-val :lambda-list '(m))
(cl:defmethod battery_lower-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:battery_lower-val is deprecated.  Use beginner_tutorials-msg:battery_lower instead.")
  (battery_lower m))

(cl:ensure-generic-function 'battery_percentage-val :lambda-list '(m))
(cl:defmethod battery_percentage-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:battery_percentage-val is deprecated.  Use beginner_tutorials-msg:battery_percentage instead.")
  (battery_percentage m))

(cl:ensure-generic-function 'battery_state-val :lambda-list '(m))
(cl:defmethod battery_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:battery_state-val is deprecated.  Use beginner_tutorials-msg:battery_state instead.")
  (battery_state m))

(cl:ensure-generic-function 'camera_state-val :lambda-list '(m))
(cl:defmethod camera_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:camera_state-val is deprecated.  Use beginner_tutorials-msg:camera_state instead.")
  (camera_state m))

(cl:ensure-generic-function 'down_visual_state-val :lambda-list '(m))
(cl:defmethod down_visual_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:down_visual_state-val is deprecated.  Use beginner_tutorials-msg:down_visual_state instead.")
  (down_visual_state m))

(cl:ensure-generic-function 'drone_battery_left-val :lambda-list '(m))
(cl:defmethod drone_battery_left-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:drone_battery_left-val is deprecated.  Use beginner_tutorials-msg:drone_battery_left instead.")
  (drone_battery_left m))

(cl:ensure-generic-function 'drone_fly_time_left-val :lambda-list '(m))
(cl:defmethod drone_fly_time_left-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:drone_fly_time_left-val is deprecated.  Use beginner_tutorials-msg:drone_fly_time_left instead.")
  (drone_fly_time_left m))

(cl:ensure-generic-function 'drone_hover-val :lambda-list '(m))
(cl:defmethod drone_hover-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:drone_hover-val is deprecated.  Use beginner_tutorials-msg:drone_hover instead.")
  (drone_hover m))

(cl:ensure-generic-function 'em_open-val :lambda-list '(m))
(cl:defmethod em_open-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:em_open-val is deprecated.  Use beginner_tutorials-msg:em_open instead.")
  (em_open m))

(cl:ensure-generic-function 'em_sky-val :lambda-list '(m))
(cl:defmethod em_sky-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:em_sky-val is deprecated.  Use beginner_tutorials-msg:em_sky instead.")
  (em_sky m))

(cl:ensure-generic-function 'em_ground-val :lambda-list '(m))
(cl:defmethod em_ground-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:em_ground-val is deprecated.  Use beginner_tutorials-msg:em_ground instead.")
  (em_ground m))

(cl:ensure-generic-function 'east_speed-val :lambda-list '(m))
(cl:defmethod east_speed-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:east_speed-val is deprecated.  Use beginner_tutorials-msg:east_speed instead.")
  (east_speed m))

(cl:ensure-generic-function 'electrical_machinery_state-val :lambda-list '(m))
(cl:defmethod electrical_machinery_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:electrical_machinery_state-val is deprecated.  Use beginner_tutorials-msg:electrical_machinery_state instead.")
  (electrical_machinery_state m))

(cl:ensure-generic-function 'factory_mode-val :lambda-list '(m))
(cl:defmethod factory_mode-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:factory_mode-val is deprecated.  Use beginner_tutorials-msg:factory_mode instead.")
  (factory_mode m))

(cl:ensure-generic-function 'fly_mode-val :lambda-list '(m))
(cl:defmethod fly_mode-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:fly_mode-val is deprecated.  Use beginner_tutorials-msg:fly_mode instead.")
  (fly_mode m))

(cl:ensure-generic-function 'fly_speed-val :lambda-list '(m))
(cl:defmethod fly_speed-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:fly_speed-val is deprecated.  Use beginner_tutorials-msg:fly_speed instead.")
  (fly_speed m))

(cl:ensure-generic-function 'fly_time-val :lambda-list '(m))
(cl:defmethod fly_time-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:fly_time-val is deprecated.  Use beginner_tutorials-msg:fly_time instead.")
  (fly_time m))

(cl:ensure-generic-function 'front_in-val :lambda-list '(m))
(cl:defmethod front_in-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:front_in-val is deprecated.  Use beginner_tutorials-msg:front_in instead.")
  (front_in m))

(cl:ensure-generic-function 'front_lsc-val :lambda-list '(m))
(cl:defmethod front_lsc-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:front_lsc-val is deprecated.  Use beginner_tutorials-msg:front_lsc instead.")
  (front_lsc m))

(cl:ensure-generic-function 'front_out-val :lambda-list '(m))
(cl:defmethod front_out-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:front_out-val is deprecated.  Use beginner_tutorials-msg:front_out instead.")
  (front_out m))

(cl:ensure-generic-function 'gravity_state-val :lambda-list '(m))
(cl:defmethod gravity_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:gravity_state-val is deprecated.  Use beginner_tutorials-msg:gravity_state instead.")
  (gravity_state m))

(cl:ensure-generic-function 'ground_speed-val :lambda-list '(m))
(cl:defmethod ground_speed-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:ground_speed-val is deprecated.  Use beginner_tutorials-msg:ground_speed instead.")
  (ground_speed m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:height-val is deprecated.  Use beginner_tutorials-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'imu_calibration_state-val :lambda-list '(m))
(cl:defmethod imu_calibration_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:imu_calibration_state-val is deprecated.  Use beginner_tutorials-msg:imu_calibration_state instead.")
  (imu_calibration_state m))

(cl:ensure-generic-function 'imu_state-val :lambda-list '(m))
(cl:defmethod imu_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:imu_state-val is deprecated.  Use beginner_tutorials-msg:imu_state instead.")
  (imu_state m))

(cl:ensure-generic-function 'light_strength-val :lambda-list '(m))
(cl:defmethod light_strength-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:light_strength-val is deprecated.  Use beginner_tutorials-msg:light_strength instead.")
  (light_strength m))

(cl:ensure-generic-function 'north_speed-val :lambda-list '(m))
(cl:defmethod north_speed-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:north_speed-val is deprecated.  Use beginner_tutorials-msg:north_speed instead.")
  (north_speed m))

(cl:ensure-generic-function 'outage_recording-val :lambda-list '(m))
(cl:defmethod outage_recording-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:outage_recording-val is deprecated.  Use beginner_tutorials-msg:outage_recording instead.")
  (outage_recording m))

(cl:ensure-generic-function 'power_state-val :lambda-list '(m))
(cl:defmethod power_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:power_state-val is deprecated.  Use beginner_tutorials-msg:power_state instead.")
  (power_state m))

(cl:ensure-generic-function 'pressure_state-val :lambda-list '(m))
(cl:defmethod pressure_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:pressure_state-val is deprecated.  Use beginner_tutorials-msg:pressure_state instead.")
  (pressure_state m))

(cl:ensure-generic-function 'smart_video_exit_mode-val :lambda-list '(m))
(cl:defmethod smart_video_exit_mode-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:smart_video_exit_mode-val is deprecated.  Use beginner_tutorials-msg:smart_video_exit_mode instead.")
  (smart_video_exit_mode m))

(cl:ensure-generic-function 'temperature_height-val :lambda-list '(m))
(cl:defmethod temperature_height-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:temperature_height-val is deprecated.  Use beginner_tutorials-msg:temperature_height instead.")
  (temperature_height m))

(cl:ensure-generic-function 'throw_fly_timer-val :lambda-list '(m))
(cl:defmethod throw_fly_timer-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:throw_fly_timer-val is deprecated.  Use beginner_tutorials-msg:throw_fly_timer instead.")
  (throw_fly_timer m))

(cl:ensure-generic-function 'wifi_disturb-val :lambda-list '(m))
(cl:defmethod wifi_disturb-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:wifi_disturb-val is deprecated.  Use beginner_tutorials-msg:wifi_disturb instead.")
  (wifi_disturb m))

(cl:ensure-generic-function 'wifi_strength-val :lambda-list '(m))
(cl:defmethod wifi_strength-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:wifi_strength-val is deprecated.  Use beginner_tutorials-msg:wifi_strength instead.")
  (wifi_strength m))

(cl:ensure-generic-function 'wind_state-val :lambda-list '(m))
(cl:defmethod wind_state-val ((m <FlightData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:wind_state-val is deprecated.  Use beginner_tutorials-msg:wind_state instead.")
  (wind_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FlightData>) ostream)
  "Serializes a message object of type '<FlightData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'battery_low) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'battery_lower) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'battery_percentage)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'battery_state) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'camera_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'down_visual_state) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'drone_battery_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'drone_fly_time_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'drone_hover) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'em_open) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'em_sky) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'em_ground) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'east_speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'electrical_machinery_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'factory_mode) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'fly_mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'fly_speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'fly_time)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'front_in) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'front_lsc) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'front_out) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'gravity_state) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'ground_speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'imu_calibration_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'imu_state) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'light_strength)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'north_speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'outage_recording) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'power_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'pressure_state) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'smart_video_exit_mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'temperature_height) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'throw_fly_timer)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'wifi_disturb)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'wifi_strength)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wind_state) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FlightData>) istream)
  "Deserializes a message object of type '<FlightData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:slot-value msg 'battery_low) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'battery_lower) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'battery_percentage) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'battery_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'camera_state) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'down_visual_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'drone_battery_left) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'drone_fly_time_left) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'drone_hover) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'em_open) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'em_sky) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'em_ground) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'east_speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'electrical_machinery_state) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'factory_mode) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fly_mode) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fly_speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fly_time) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'front_in) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'front_lsc) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'front_out) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'gravity_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ground_speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'imu_calibration_state) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'imu_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'light_strength) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'north_speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'outage_recording) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'power_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'pressure_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'smart_video_exit_mode) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'temperature_height) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'throw_fly_timer) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wifi_disturb) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wifi_strength) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'wind_state) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FlightData>)))
  "Returns string type for a message object of type '<FlightData>"
  "beginner_tutorials/FlightData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FlightData)))
  "Returns string type for a message object of type 'FlightData"
  "beginner_tutorials/FlightData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FlightData>)))
  "Returns md5sum for a message object of type '<FlightData>"
  "8c659bf934436b7cb2d969ddd123268a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FlightData)))
  "Returns md5sum for a message object of type 'FlightData"
  "8c659bf934436b7cb2d969ddd123268a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FlightData>)))
  "Returns full string definition for message of type '<FlightData>"
  (cl:format cl:nil "Header header~%bool battery_low~%bool battery_lower~%int8 battery_percentage~%bool battery_state~%int8 camera_state~%bool down_visual_state~%int16 drone_battery_left~%int16 drone_fly_time_left~%bool drone_hover~%bool em_open~%bool em_sky~%bool em_ground~%int16 east_speed~%int16 electrical_machinery_state~%bool factory_mode~%int8 fly_mode~%int16 fly_speed~%int16 fly_time~%bool front_in~%bool front_lsc~%bool front_out~%bool gravity_state~%int16 ground_speed~%int16 height~%int8 imu_calibration_state~%bool imu_state~%int8 light_strength~%int16 north_speed~%bool outage_recording~%bool power_state~%bool pressure_state~%int16 smart_video_exit_mode~%bool temperature_height~%int8 throw_fly_timer~%int8 wifi_disturb~%int8 wifi_strength~%bool wind_state~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FlightData)))
  "Returns full string definition for message of type 'FlightData"
  (cl:format cl:nil "Header header~%bool battery_low~%bool battery_lower~%int8 battery_percentage~%bool battery_state~%int8 camera_state~%bool down_visual_state~%int16 drone_battery_left~%int16 drone_fly_time_left~%bool drone_hover~%bool em_open~%bool em_sky~%bool em_ground~%int16 east_speed~%int16 electrical_machinery_state~%bool factory_mode~%int8 fly_mode~%int16 fly_speed~%int16 fly_time~%bool front_in~%bool front_lsc~%bool front_out~%bool gravity_state~%int16 ground_speed~%int16 height~%int8 imu_calibration_state~%bool imu_state~%int8 light_strength~%int16 north_speed~%bool outage_recording~%bool power_state~%bool pressure_state~%int16 smart_video_exit_mode~%bool temperature_height~%int8 throw_fly_timer~%int8 wifi_disturb~%int8 wifi_strength~%bool wind_state~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FlightData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     1
     1
     1
     1
     2
     2
     1
     1
     1
     1
     2
     2
     1
     1
     2
     2
     1
     1
     1
     1
     2
     2
     1
     1
     1
     2
     1
     1
     1
     2
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FlightData>))
  "Converts a ROS message object to a list"
  (cl:list 'FlightData
    (cl:cons ':header (header msg))
    (cl:cons ':battery_low (battery_low msg))
    (cl:cons ':battery_lower (battery_lower msg))
    (cl:cons ':battery_percentage (battery_percentage msg))
    (cl:cons ':battery_state (battery_state msg))
    (cl:cons ':camera_state (camera_state msg))
    (cl:cons ':down_visual_state (down_visual_state msg))
    (cl:cons ':drone_battery_left (drone_battery_left msg))
    (cl:cons ':drone_fly_time_left (drone_fly_time_left msg))
    (cl:cons ':drone_hover (drone_hover msg))
    (cl:cons ':em_open (em_open msg))
    (cl:cons ':em_sky (em_sky msg))
    (cl:cons ':em_ground (em_ground msg))
    (cl:cons ':east_speed (east_speed msg))
    (cl:cons ':electrical_machinery_state (electrical_machinery_state msg))
    (cl:cons ':factory_mode (factory_mode msg))
    (cl:cons ':fly_mode (fly_mode msg))
    (cl:cons ':fly_speed (fly_speed msg))
    (cl:cons ':fly_time (fly_time msg))
    (cl:cons ':front_in (front_in msg))
    (cl:cons ':front_lsc (front_lsc msg))
    (cl:cons ':front_out (front_out msg))
    (cl:cons ':gravity_state (gravity_state msg))
    (cl:cons ':ground_speed (ground_speed msg))
    (cl:cons ':height (height msg))
    (cl:cons ':imu_calibration_state (imu_calibration_state msg))
    (cl:cons ':imu_state (imu_state msg))
    (cl:cons ':light_strength (light_strength msg))
    (cl:cons ':north_speed (north_speed msg))
    (cl:cons ':outage_recording (outage_recording msg))
    (cl:cons ':power_state (power_state msg))
    (cl:cons ':pressure_state (pressure_state msg))
    (cl:cons ':smart_video_exit_mode (smart_video_exit_mode msg))
    (cl:cons ':temperature_height (temperature_height msg))
    (cl:cons ':throw_fly_timer (throw_fly_timer msg))
    (cl:cons ':wifi_disturb (wifi_disturb msg))
    (cl:cons ':wifi_strength (wifi_strength msg))
    (cl:cons ':wind_state (wind_state msg))
))
