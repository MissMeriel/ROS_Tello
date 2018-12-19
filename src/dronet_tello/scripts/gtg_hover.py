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


<<<<<<< HEAD
goal_x = float(sys.argv[1])
goal_y = sys.argv[2]
=======
goal_x = int(sys.argv[1])
goal_y = int(sys.argv[2])
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
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
	global obs_x, obs_y, obs_z, obs_angle
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle = data.transform.rotation.z


def main():
	global goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid
	rospy.init_node("gtg_hover", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	#obstacle_markers_subscriber = rospy.Subscriber("vicon/markers", Marker, obstacle_markers, queue_size=10)
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
	obstacle_threshold = 0.5
	angle_threshold = math.degrees(45)#0.55 #31deg
	detection_distance = 1
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 0.0

	while not rospy.is_shutdown():

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
			velocity_publisher.publish(vel)
			break

		print("")
		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)
		distance_drone_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		distance_obs_to_goal = math.sqrt((obs_x - final_goal_x)**2 + (obs_y - final_goal_y)**2)

		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		angle_obs_to_goal = math.atan2((final_goal_y - obs_y), (final_goal_x - obs_x))
		angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
		angle_drone_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x) - curr_angle
		angle_dronepos_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x)
		paths_align = abs(angle_dronepos_to_goal - angle_obs_to_goal) < angle_threshold
		obstacle_in_path = paths_align and distance_drone_to_obstacle <= detection_distance and distance_to_final_goal >  distance_obs_to_goal
		print("start goal: "+str(goal_x)+", "+str(goal_y))
		print("obstacle_in_path: "+str(obstacle_in_path))
		print("\tpaths_align: "+str(paths_align))
		print("\tdistance_drone_to_obstacle <= detection_distance: "+str(distance_drone_to_obstacle <= detection_distance))
		print("\tdistance_to_final_goal >  distance_obs_to_goal: "+str(distance_to_final_goal >  distance_obs_to_goal))
		#print("\tangle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
		print("\tangle_dronepos_to_goal: "+str(math.degrees(angle_dronepos_to_goal)))
		print("\tangle_obs_to_goal: "+str(math.degrees(angle_obs_to_goal)))
		
		print("\tdistance to final goal: "+ str(distance_to_final_goal))
		print("\tdistance to curr goal: "+ str(distance_to_goal))
		print("\tdistance to obstacle: "+ str(distance_drone_to_obstacle))
		print("\tdistance from obstacle to goal: "+ str(distance_obs_to_goal))
		str_msg = "distance to goal: "+ str(distance_to_goal)
		obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_final_goal < threshold):
			if(hover_count < 5):
				print("GOAL REACHED with threshold "+str(distance_to_final_goal))
				str_msg = "GOAL REACHED with threshold "+str(distance_to_final_goal)
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				hover_count += 1
			else:
				exit()

		else:
			print("NOT @ FINAL GOAL")
			if(obstacle_in_path):
				print("AND OBS IIN PATH")
				if(abs(distance_drone_to_obstacle - detection_distance) < threshold):
					angle_obs_to_drone = math.pi + angle_drone_to_obs #math.atan2(curr_y-obs_y, curr_x-obs_x)
					#print("angle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
					hover_point_x = obs_x + obstacle_threshold * math.cos(math.pi + angle_obs_to_goal)
					hover_point_y = obs_y + obstacle_threshold * math.sin(math.pi + angle_obs_to_goal)
					goal_x = hover_point_x
					goal_y = hover_point_y
					print("goal set to hover_point: "+str(hover_point_x)+", "+str(hover_point_y))
					error = 0
					integral = 0
					previous_error = 0

				distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
				if(distance_to_goal <= 0.5):
					vel.linear.x = 0
					vel.linear.y = 0
					while(sent < 5):
						obstacle_publisher.publish(Bool(True))
						sent += 1
					if(hover_count > 20):
						vel.linear.x = 0
						vel.linear.y = 0
						vel.linear.z = -200
						print("LANDING NOW")
					elif(hover_count > 50):
						exit()
					print("HOVERED "+str(hover_count)+" seconds")
					hover_count += dt
					velocity_publisher.publish(vel)
					rate.sleep()
					continue
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

		print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		print("goal: "+str(goal_x)+", "+str(goal_y))
		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()



if __name__ == "__main__":
    main()
