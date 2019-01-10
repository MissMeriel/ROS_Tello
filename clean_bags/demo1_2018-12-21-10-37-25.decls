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

ppt ..flight_data():::ENTER
	ppt-type enter

ppt ..flight_data():::EXIT0
	ppt-type subexit
	variable return
		var-kind variable
		rep-type hashcode
		dec-type dronet_tello/FlightData
		comparability 1
	variable return.gravity_state
		var-kind field gravity_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.battery_state
		var-kind field battery_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.electrical_machinery_state
		var-kind field electrical_machinery_state
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.fly_mode
		var-kind field fly_mode
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.front_out
		var-kind field front_out
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.height
		var-kind field height
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.pressure_state
		var-kind field pressure_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.wifi_strength
		var-kind field wifi_strength
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.outage_recording
		var-kind field outage_recording
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.smart_video_exit_mode
		var-kind field smart_video_exit_mode
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.front_lsc
		var-kind field front_lsc
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.factory_mode
		var-kind field factory_mode
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.fly_time
		var-kind field fly_time
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.down_visual_state
		var-kind field down_visual_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.ground_speed
		var-kind field ground_speed
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.drone_hover
		var-kind field drone_hover
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.em_open
		var-kind field em_open
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.camera_state
		var-kind field camera_state
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.battery_low
		var-kind field battery_low
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.battery_percentage
		var-kind field battery_percentage
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.power_state
		var-kind field power_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.wind_state
		var-kind field wind_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.drone_battery_left
		var-kind field drone_battery_left
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.header.stamp.secs
		var-kind field secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.light_strength
		var-kind field light_strength
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.battery_lower
		var-kind field battery_lower
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.fly_speed
		var-kind field fly_speed
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.east_speed
		var-kind field east_speed
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.imu_calibration_state
		var-kind field imu_calibration_state
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.header.seq
		var-kind field seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.throw_fly_timer
		var-kind field throw_fly_timer
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.em_ground
		var-kind field em_ground
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.imu_state
		var-kind field imu_state
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.header.frame_id
		var-kind field frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.temperature_height
		var-kind field temperature_height
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.wifi_disturb
		var-kind field wifi_disturb
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.front_in
		var-kind field front_in
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.em_sky
		var-kind field em_sky
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.drone_fly_time_left
		var-kind field drone_fly_time_left
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.north_speed
		var-kind field north_speed
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1


ppt ..rosout():::ENTER
	ppt-type enter

ppt ..rosout():::EXIT0
	ppt-type subexit
	variable return
		var-kind variable
		rep-type hashcode
		dec-type rosgraph_msgs/Log
		comparability 1
	variable return.function
		var-kind field function
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.seq
		var-kind field seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.name
		var-kind field name
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.level
		var-kind field level
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.header.stamp.secs
		var-kind field secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.msg
		var-kind field msg
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.file
		var-kind field file
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.line
		var-kind field line
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.header.frame_id
		var-kind field frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1


ppt ..state():::ENTER
	ppt-type enter

ppt ..state():::EXIT0
	ppt-type subexit
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


ppt ..velocity():::ENTER
	ppt-type enter

ppt ..velocity():::EXIT0
	ppt-type subexit
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
		comparability 1
	variable return.linear.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.linear.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.angular.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ..vicon/TELLO/TELLO():::ENTER
	ppt-type enter

ppt ..vicon/TELLO/TELLO():::EXIT0
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
		comparability 1
	variable return.transform.rotation.y
		var-kind field y
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
		var-kind field frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.transform.rotation.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.secs
		var-kind field secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.transform.translation.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.translation.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.transform.rotation.w
		var-kind field w
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1


ppt ..vicon/markers():::ENTER
	ppt-type enter

ppt ..vicon/markers():::EXIT0
	ppt-type subexit
	variable return
		var-kind variable
		rep-type hashcode
		dec-type vicon_bridge/Markers
		comparability 1
	variable return.header.seq
		var-kind field seq
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.markers.marker_name
		var-kind field marker_name
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.header.frame_id
		var-kind field frame_id
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.markers.occluded
		var-kind field occluded
		enclosing-var return
		rep-type boolean
		dec-type boolean
		comparability 1
	variable return.header.stamp.secs
		var-kind field secs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.markers.subject_name
		var-kind field subject_name
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
	variable return.markers.translation.y
		var-kind field y
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.markers.translation.x
		var-kind field x
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.markers.translation.z
		var-kind field z
		enclosing-var return
		rep-type float
		dec-type float
		comparability 1
	variable return.header.stamp.nsecs
		var-kind field nsecs
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.frame_number
		var-kind field frame_number
		enclosing-var return
		rep-type int
		dec-type int
		comparability 1
	variable return.markers.segment_name
		var-kind field segment_name
		enclosing-var return
		rep-type string
		dec-type string
		comparability 1
