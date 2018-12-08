#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import Bool
from std_msgs.msg import String
#from vicon_bridge import Marker


goal_x = 1
goal_y = 1
obs_x = -20
obs_y = -20
obs_corner_x = 0
obs_corner_y = 0
obs_angle = 0
curr_x = 0
curr_y = 0
#curr_angle: yaw relative to global frame
curr_angle = 0
publishing = True
avoid = False
prev_data = TransformStamped
obstacle_dyn = False
obs_angle_prev = obs_angle


def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	# quaternions to radians
	siny_cosp = +2.0 * (data.transform.rotation.w * data.transform.rotation.z + data.transform.rotation.x * data.transform.rotation.y);
	cosy_cosp = +1.0 - 2.0 * (data.transform.rotation.y * data.transform.rotation.y + data.transform.rotation.z * data.transform.rotation.z);  
	curr_angle = math.atan2(siny_cosp, cosy_cosp);
	publishing = True


def vicon_obstacle(data):
	global obs_x, obs_y, obs_z, obs_angle, obstacle_dyn
	if(abs(obs_x - data.transform.translation.x) > 0.2 or abs(obs_y - data.transform.translation.y) > 0.2 or abs(obs_z - data.transform.translation.z) > 0.2 or abs(obs_angle - data.transform.rotation.z) > 0.2):
		obstacle_dyn = True
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle_prev = obs_angle
	obs_angle = data.transform.rotation.z


def user_input(data):
	global avoid
	if(len(data) == 0 or "y" not in data):
		avoid = False
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = -200
		print("Landing")
	else:
		avoid = True


def obstacle_markers(data):
	#get peripheral points of obstacle and decide which is nearest to current position
	if(data.subject_name == "OBSTACLE"):
		print("OBSTACLE Marker data:")
		print(data.translation)
		print("")


def main():
	global goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid, dynamic_obstacle
	rospy.init_node("gotogoal", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	#http://docs.ros.org/jade/api/vicon_bridge/html/msg/Marker.html
	obstacle_markers_subscriber = rospy.Subscriber("/vicon/markers", Marker, obstacle_markers, queue_size=10)
	key_vel_publisher = rospy.Publisher("/key_vel_enable", Bool, queue_size=1)
	#input_subscriber = rospy.Subscriber("/user_input", String, user_input, queue_size=10)

	vel = Twist()
	vel.linear.x = 0
	vel.angular.z = 0
	
	str_msg = ""

	set_rate = 20
	dt = 1.0/set_rate
	rate = rospy.Rate(set_rate)

	integral = 0
	previous_error = 0
	# Defaults: Kp=0.045; Ki=0.08; Kd=0.075
	# Moderate speed: Kp=0.008; Ki=0.03; Kd=0.06
	Kp = 0.03 
	Ki = 0.003
	Kd = 0.006

	publishing_count = 0
	avoid = False
	final_goal_x = goal_x
	final_goal_y = goal_y
	threshold = 0.1
	obstacle_threshold = 0.275
	angle_threshold = 0.5
	detection_distance = 0.5
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 0

	while not rospy.is_shutdown():
		if(obstacle_in_path and obstacle_dyn):
			key_vel_publisher.publish(True)
			avoid = False
			print("Key vel enabled")
		else:
			key_vel_publisher.publish(False)

		print("")
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)
		distance_drone_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		distance_obs_to_goal = math.sqrt((obs_x - final_goal_x)**2 + (obs_y - final_goal_y)**2)

		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		angle_obs_to_goal = math.atan2((goal_y - obs_y), (goal_x - obs_x))
		angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
		angle_drone_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x) - curr_angle

		paths_align = abs(angle_obs_to_drone - angle_obs_to_goal) < angle_threshold
		obstacle_in_path = paths_align and distance_drone_to_obstacle < detection_distance and distance_to_final_goal >  distance_obs_to_goal

		print("global angle_drone_to_goal: "+str(math.degrees(math.atan2(goal_y-curr_y, goal_x-curr_x))))
		print("angle_obs_to_goal: "+str(math.degrees(angle_obs_to_goal)))
		#print("distance to goal: "+ str(distance_to_goal))
		#print("distance to obstacle: "+ str(distance_drone_to_obstacle))
		print("obstacle_in_path: "+str(obstacle_in_path))
		str_msg = "distance to goal: "+ str(distance_to_goal)
		obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_final_goal < threshold):
			if(hover_count < 5):
				print("GOAL REACHED with threshold "+str(distance_to_goal))
				str_msg = "GOAL REACHED with threshold "+str(distance_to_goal)
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				hover_count += 1
			else:
				exit()
		elif(avoid):
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")

			#interpolated goal offset from obstacle radius
			avoid_angle = angle_drone_to_obs + math.radians(60)
			
			goal_x = curr_x + 5 * math.cos(avoid_angle)
			goal_y = curr_y + 5 * math.sin(avoid_angle) #obs_y + 2
			
			angle_drone_to_goal = math.atan2(goal_y-curr_y, goal_x-curr_x)-curr_angle

			vel_x = math.cos(angle_drone_to_goal) * dt
			vel_y = math.sin(angle_drone_to_goal) * dt

			print("new avoid goal: "+str(goal_x)+", "+str(goal_y))
			count += dt
			if(not obstacle_in_path and count > 3):
				avoid = False
				print("OBSTACLE NO LONGER IN PATH")
				print("OBSTACLE NO LONGER IN PATH")
				print("OBSTACLE NO LONGER IN PATH")
				print("OBSTACLE NO LONGER IN PATH")
				print("OBSTACLE NO LONGER IN PATH")
				print("OBSTACLE NO LONGER IN PATH")
				count = 0
		else:
			print("NOT AVOID")
			if(obstacle_in_path):
				print("AND OBS IIN PATH")
				angle_obs_to_drone = math.pi + angle_drone_to_obs #math.atan2(curr_y-obs_y, curr_x-obs_x)
				#print("angle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
				hover_point_x = obs_x + math.cos(angle_obs_to_drone)
				hover_point_y = obs_y + math.sin(angle_obs_to_drone)
				goal_x = hover_point_x
				goal_y = hover_point_y
				print("goal set to hover_point: "+str(hover_point_x)+", "+str(hover_point_y))
				error = 0
				integral = 0
				previous_error = 0

				distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
				if(distance_to_goal < threshold):
					vel.linear.x = 0
					vel.linear.y = 0
					while(sent < 5):
						obstacle_publisher.publish(Bool(True))
						sent += 1
				if(avoid):
					print("PREPARING TO AVOID")
					print("PREPARING TO AVOID")
					print("PREPARING TO AVOID")
					print("PREPARING TO AVOID")
					print("PREPARING TO AVOID")
					print("PREPARING TO AVOID")
					str_msg = "PREPARING TO AVOID"
					break
				hover_count += dt
				if(hover_count > 6):
					vel.linear.x = 0
					vel.linear.y = 0
					vel.linear.z = -200
			else:
				goal_x = final_goal_x
				goal_y = final_goal_y
				print("OBSTACLE NOT IN_PATH; GO TOWARDS GOAL")

				error = distance_to_goal
				derivative = (error - previous_error) / dt
				integral = integral + (error * dt)
				w = Kp*error + Ki*integral + Kd*derivative

				vel_x = math.cos(angle_drone_to_goal) * w
				#negative sin due to how Tello interprets roll (right = pos)
				vel_y = -math.sin(angle_drone_to_goal) * w

				previous_error = error

				#print("w: "+str(w))
				print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
				print("curr_angle: " + str(curr_angle))
				#print("angle_drone_to_goal: " + str(angle_drone_to_goal))
				#print("actual vel.x, vel.y: "+ str(vel_x)+", "+ str(vel_y))
			
				# max tello speed is +-1
				if(vel_y > 1):
					vel_y = 1
				if(vel_y < -1):
					vel_y = -1
				if(vel_x > 1):
					vel_x = 1
				if(vel_x < -1):
					vel_x = -1
				vel.linear.x = vel_x
				vel.linear.y = vel_y

				# account for deadzone below 0.1
				#if(abs(vel.linear.x) < 0.08):
				#	vel.linear.x *= 1.5
				#elif(abs(vel.linear.x) < 0.01):
				#	vel.linear.x *= 9
				#if(abs(vel.linear.y) < 0.08):
				#	vel.linear.y *= 1.5
				#elif(abs(vel.linear.y) < 0.01):
				#	vel.linear.y *= 9


		#check for lapse in vicon data
		if(not publishing):
			publishing = False
			publishing_count += 1
		else:
			publishing_count = 0
			publishing = True
		if(publishing_count > 5):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -500
			print("NO VICON DATA; LANDING")
			str_msg = "NO VICON DATA; LANDING"

		#print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		print("goal: "+str(goal_x)+", "+str(goal_y))
		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()



if __name__ == "__main__":
    main()
