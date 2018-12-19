; Auto-generated. Do not edit!


(cl:in-package tello_dronet-msg)


;//! \htmlinclude CNN_out.msg.html

(cl:defclass <CNN_out> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (steering_angle
    :reader steering_angle
    :initarg :steering_angle
    :type cl:float
    :initform 0.0)
   (collision_prob
    :reader collision_prob
    :initarg :collision_prob
    :type cl:float
    :initform 0.0))
)

(cl:defclass CNN_out (<CNN_out>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CNN_out>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CNN_out)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tello_dronet-msg:<CNN_out> is deprecated: use tello_dronet-msg:CNN_out instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <CNN_out>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tello_dronet-msg:header-val is deprecated.  Use tello_dronet-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'steering_angle-val :lambda-list '(m))
(cl:defmethod steering_angle-val ((m <CNN_out>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tello_dronet-msg:steering_angle-val is deprecated.  Use tello_dronet-msg:steering_angle instead.")
  (steering_angle m))

(cl:ensure-generic-function 'collision_prob-val :lambda-list '(m))
(cl:defmethod collision_prob-val ((m <CNN_out>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tello_dronet-msg:collision_prob-val is deprecated.  Use tello_dronet-msg:collision_prob instead.")
  (collision_prob m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CNN_out>) ostream)
  "Serializes a message object of type '<CNN_out>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'steering_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'collision_prob))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CNN_out>) istream)
  "Deserializes a message object of type '<CNN_out>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steering_angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'collision_prob) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CNN_out>)))
  "Returns string type for a message object of type '<CNN_out>"
  "tello_dronet/CNN_out")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CNN_out)))
  "Returns string type for a message object of type 'CNN_out"
  "tello_dronet/CNN_out")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CNN_out>)))
  "Returns md5sum for a message object of type '<CNN_out>"
  "4a4cbb1fa95c6b93b88486210c46f9c1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CNN_out)))
  "Returns md5sum for a message object of type 'CNN_out"
  "4a4cbb1fa95c6b93b88486210c46f9c1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CNN_out>)))
  "Returns full string definition for message of type '<CNN_out>"
  (cl:format cl:nil "Header header~%float32 steering_angle~%float32 collision_prob~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CNN_out)))
  "Returns full string definition for message of type 'CNN_out"
  (cl:format cl:nil "Header header~%float32 steering_angle~%float32 collision_prob~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CNN_out>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CNN_out>))
  "Converts a ROS message object to a list"
  (cl:list 'CNN_out
    (cl:cons ':header (header msg))
    (cl:cons ':steering_angle (steering_angle msg))
    (cl:cons ':collision_prob (collision_prob msg))
))
