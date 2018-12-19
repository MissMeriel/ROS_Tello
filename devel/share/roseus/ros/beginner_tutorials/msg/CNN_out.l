;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::CNN_out)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'CNN_out (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::CNN_OUT")
  (make-package "BEGINNER_TUTORIALS::CNN_OUT"))

(in-package "ROS")
;;//! \htmlinclude CNN_out.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass beginner_tutorials::CNN_out
  :super ros::object
  :slots (_header _steering_angle _collision_prob ))

(defmethod beginner_tutorials::CNN_out
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:steering_angle __steering_angle) 0.0)
    ((:collision_prob __collision_prob) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _steering_angle (float __steering_angle))
   (setq _collision_prob (float __collision_prob))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:steering_angle
   (&optional __steering_angle)
   (if __steering_angle (setq _steering_angle __steering_angle)) _steering_angle)
  (:collision_prob
   (&optional __collision_prob)
   (if __collision_prob (setq _collision_prob __collision_prob)) _collision_prob)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _steering_angle
    4
    ;; float32 _collision_prob
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _steering_angle
       (sys::poke _steering_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _collision_prob
       (sys::poke _collision_prob (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _steering_angle
     (setq _steering_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _collision_prob
     (setq _collision_prob (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get beginner_tutorials::CNN_out :md5sum-) "4a4cbb1fa95c6b93b88486210c46f9c1")
(setf (get beginner_tutorials::CNN_out :datatype-) "beginner_tutorials/CNN_out")
(setf (get beginner_tutorials::CNN_out :definition-)
      "Header header
float32 steering_angle
float32 collision_prob

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



(provide :beginner_tutorials/CNN_out "4a4cbb1fa95c6b93b88486210c46f9c1")


