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

ppt ..is_user_watching_drone(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64,\_geometry_msgs/Twist,\_std_msgs/String):::ENTER
	ppt-type enter
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
	variable /velocity3.linear.y
		var-kind field linear.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.x
		var-kind field linear.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.z
		var-kind field linear.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.angular.y
		var-kind field angular.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.x
		var-kind field angular.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.z
		var-kind field angular.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /state4
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
	variable /state4.data
		var-kind field data
		enclosing-var /state4
		rep-type string
		dec-type string
		comparability 11

ppt ..is_user_watching_drone(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64,\_geometry_msgs/Twist,\_std_msgs/String):::EXIT0
	ppt-type subexit
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
	variable /velocity3.linear.y
		var-kind field linear.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.x
		var-kind field linear.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.z
		var-kind field linear.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.angular.y
		var-kind field angular.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.x
		var-kind field angular.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.z
		var-kind field angular.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /state4
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
	variable /state4.data
		var-kind field data
		enclosing-var /state4
		rep-type string
		dec-type string
		comparability 11
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
		comparability 8

ppt ..viconTELLOTELLO():::ENTER
	ppt-type enter

ppt ..viconTELLOTELLO():::EXIT0
	ppt-type subexit
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		comparability 1
	variable return.header.seq
		var-kind field seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 2
	variable return.transform.rotation.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 3
	variable return.child_frame_id
		var-kind field child_frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 4
	variable return.header.frame_id
		var-kind field frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 4
	variable return.transform.rotation.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 3
	variable return.header.stamp.secs
		var-kind field secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 5
	variable return.transform.translation.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 6
	variable return.header.stamp.nsecs
		var-kind field nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 7
	variable return.transform.translation.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 6
	variable return.transform.translation.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 6
	variable return.transform.rotation.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 3
	variable return.transform.rotation.w
		var-kind field w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 3

ppt ..state(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64):::ENTER
	ppt-type enter
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9

ppt ..state(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64):::EXIT0
	ppt-type subexit
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
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
		comparability 11

ppt ..distance_to_user(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64,\_geometry_msgs/Twist,\_std_msgs/String):::ENTER
	ppt-type enter
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
	variable /velocity3.linear.y
		var-kind field linear.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.x
		var-kind field linear.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.z
		var-kind field linear.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.angular.y
		var-kind field angular.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.x
		var-kind field angular.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.z
		var-kind field angular.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /state4
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
	variable /state4.data
		var-kind field data
		enclosing-var /state4
		rep-type string
		dec-type string
		comparability 11

ppt ..distance_to_user(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64,\_geometry_msgs/Twist,\_std_msgs/String):::EXIT0
	ppt-type subexit
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		flags is_param
	variable /velocity3.linear.y
		var-kind field linear.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.x
		var-kind field linear.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.linear.z
		var-kind field linear.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 9
	variable /velocity3.angular.y
		var-kind field angular.y
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.x
		var-kind field angular.x
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /velocity3.angular.z
		var-kind field angular.z
		enclosing-var /velocity3
		rep-type float
		dec-type float
		comparability 10
	variable /state4
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/String
		flags is_param
	variable /state4.data
		var-kind field data
		enclosing-var /state4
		rep-type string
		dec-type string
		comparability 11
	variable return
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		comparability 1
	variable return.data
		var-kind field data
		enclosing-var return
		rep-type float
		dec-type float
		comparability 9

ppt ..velocity(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64):::ENTER
	ppt-type enter
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9

ppt ..velocity(geometry_msgs/TransformStamped,\_std_msgs/Bool,\_std_msgs/Float64):::EXIT0
	ppt-type subexit
	variable /vicon/TELLO/TELLO0
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/TransformStamped
		flags is_param
	variable /vicon/TELLO/TELLO0.header.seq
		var-kind field header.seq
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 2
	variable /vicon/TELLO/TELLO0.transform.rotation.y
		var-kind field transform.rotation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.child_frame_id
		var-kind field child_frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.header.frame_id
		var-kind field header.frame_id
		enclosing-var /vicon/TELLO/TELLO0
		rep-type string
		dec-type string
		comparability 4
	variable /vicon/TELLO/TELLO0.transform.rotation.z
		var-kind field transform.rotation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.header.stamp.secs
		var-kind field header.stamp.secs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 5
	variable /vicon/TELLO/TELLO0.transform.translation.z
		var-kind field transform.translation.z
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.header.stamp.nsecs
		var-kind field header.stamp.nsecs
		enclosing-var /vicon/TELLO/TELLO0
		rep-type int
		dec-type int
		comparability 7
	variable /vicon/TELLO/TELLO0.transform.translation.x
		var-kind field transform.translation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.translation.y
		var-kind field transform.translation.y
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 6
	variable /vicon/TELLO/TELLO0.transform.rotation.x
		var-kind field transform.rotation.x
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /vicon/TELLO/TELLO0.transform.rotation.w
		var-kind field transform.rotation.w
		enclosing-var /vicon/TELLO/TELLO0
		rep-type float
		dec-type float
		comparability 3
	variable /is_user_watching_drone1
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Bool
		flags is_param
	variable /is_user_watching_drone1.data
		var-kind field data
		enclosing-var /is_user_watching_drone1
		rep-type boolean
		dec-type boolean
		comparability 8
	variable /distance_to_user2
		var-kind variable
		rep-type hashcode
		dec-type std_msgs/Float64
		flags is_param
	variable /distance_to_user2.data
		var-kind field data
		enclosing-var /distance_to_user2
		rep-type float
		dec-type float
		comparability 9
	variable return
		var-kind variable
		rep-type hashcode
		dec-type geometry_msgs/Twist
		comparability 1
	variable return.linear.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 9
	variable return.linear.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 9
	variable return.linear.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 9
	variable return.angular.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 10
	variable return.angular.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 10
	variable return.angular.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 10
