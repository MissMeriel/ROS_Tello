input-language C/C++
decl-version 2.0
var-comparability implicit


ppt ..main():::ENTER
	ppt-type enter

ppt ..main():::EXIT0
	ppt-type subexit
	variable return
		var-kind variable
		rep-type int
		dec-type int
		comparability 1

ppt ../user_input_next(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../user_input_next(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ../vicon/TELLO/TELLO_next(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/TELLO/TELLO_next(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../obstacle_detector_next(std_msgs/Bool):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1

ppt ../obstacle_detector_next(std_msgs/Bool):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1


ppt ../vicon/OBSTACLE/OBSTACLE_next(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/OBSTACLE/OBSTACLE_next(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../velocity_next(geometry_msgs/Twist):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../velocity_next(geometry_msgs/Twist):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		comparability 1
	variable return.linear.y
		var-kind field linear.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.x
		var-kind field linear.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.z
		var-kind field linear.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.y
		var-kind field angular.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.x
		var-kind field angular.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.z
		var-kind field angular.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../state_next(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../state_next(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ../user_input_eventually(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../user_input_eventually(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ../vicon/TELLO/TELLO_eventually(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/TELLO/TELLO_eventually(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../obstacle_detector_eventually(std_msgs/Bool):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1

ppt ../obstacle_detector_eventually(std_msgs/Bool):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1


ppt ../vicon/OBSTACLE/OBSTACLE_eventually(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/OBSTACLE/OBSTACLE_eventually(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../velocity_eventually(geometry_msgs/Twist):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../velocity_eventually(geometry_msgs/Twist):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		comparability 1
	variable return.linear.y
		var-kind field linear.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.x
		var-kind field linear.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.z
		var-kind field linear.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.y
		var-kind field angular.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.x
		var-kind field angular.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.z
		var-kind field angular.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../state_eventually(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../state_eventually(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ../user_input_until(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../user_input_until(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ../vicon/TELLO/TELLO_until(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/TELLO/TELLO_until(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../obstacle_detector_until(std_msgs/Bool):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1

ppt ../obstacle_detector_until(std_msgs/Bool):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1


ppt ../vicon/OBSTACLE/OBSTACLE_until(geometry_msgs/TransformStamped):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../vicon/OBSTACLE/OBSTACLE_until(geometry_msgs/TransformStamped):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
		comparability 1
	variable param0.header.seq
		var-kind field header.seq
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.child_frame_id
		var-kind field child_frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.header.frame_id
		var-kind field header.frame_id
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable param0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var param0
		rep-type int
		dec-type int
		comparability 1
	variable param0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field header.seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field header.frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../velocity_until(geometry_msgs/Twist):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1

ppt ../velocity_until(geometry_msgs/Twist):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
		comparability 1
	variable param0.linear.y
		var-kind field linear.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.x
		var-kind field linear.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.linear.z
		var-kind field linear.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.y
		var-kind field angular.y
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.x
		var-kind field angular.x
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable param0.angular.z
		var-kind field angular.z
		enclosing-var param0
		rep-type float
		dec-type float
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		comparability 1
	variable return.linear.y
		var-kind field linear.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.x
		var-kind field linear.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.z
		var-kind field linear.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.y
		var-kind field angular.y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.x
		var-kind field angular.x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.z
		var-kind field angular.z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ../state_until(std_msgs/String):::ENTER
	ppt-type enter
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1

ppt ../state_until(std_msgs/String):::EXIT0
	ppt-type subexit
	variable param0
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
		comparability 1
	variable param0.data
		var-kind field data
		enclosing-var param0
		rep-type string
		dec-type string
		comparability 1
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
