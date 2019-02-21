#!/usr/bin/env python
import rospy
import sys
import Queue
import traceback
import math
import time

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TransformStamped
#from geometry_msgs.msg import Pose
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Int64
#from vicon_bridge import Marker


goal_array_x = sys.argv[1]
goal_array_y = sys.argv[2]
goal_x = -200
goal_y = -200
obs_x = -20
obs_y = -20
obs_corner_x = 0
obs_corner_y = 0
obs_angle = 0
curr_x = 0
curr_y = 0
curr_z = 0
#curr_angle: yaw relative to global frame
curr_angle = 0
publishing = True
avoid = False
testing=True


def process_sysargs():
	global goal_array_x, goal_array_y
	goal_array_x = goal_array_x.split(",")
	goal_array_y = goal_array_y.split(",")
	for i in range(0,len(goal_array_x)):
		goal_array_x[i] = float(goal_array_x[i])
		goal_array_y[i] = float(goal_array_y[i])

def vicon_data(data):
	global curr_x, curr_y, curr_z, curr_angle
	global publishing
	curr_x = data.transform.translation.x
	curr_y = data.transform.translation.y
	curr_z = data.transform.translation.z
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

def user_input(data):
	global avoid
	strdata = str(data)
	if("y" in strdata or "Y" in strdata):
		avoid=True
	else:
		avoid=False

def main():
	global goal_array_x, goal_array_y, goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_z, curr_angle
	global publishing, avoid
	global testing

	process_sysargs()

	rospy.init_node("gtg_hover", anonymous=True)
	#loc_publisher = rospy.Publisher("/drone_location", Pose, queue_size=10)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	input_subscriber = rospy.Subscriber("/user_input", String, user_input, queue_size=10)

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
	# Quick speed: Kp=0.13; Ki=0.003; Kd=0.1
	Kp = 0.13
	Ki = 0.003
	Kd = 0.13

	publishing_count = 0
	avoid = False
	final_goal_x = goal_array_x[0]
	final_goal_y = goal_array_y[0]
	goal_x = final_goal_x
	goal_y = final_goal_y
	threshold = 0.12
	obstacle_threshold = 1.25
	angle_threshold = math.radians(25)
	detection_distance = 1.75
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 0.0
	avoid_count = 0.0
	exit_count = 0
	goal_count = 0

	while not rospy.is_shutdown():

		#check for lapse in vicon data
		if(not publishing):
			publishing_count += 1
		else:
			publishing_count = 0
		if(publishing_count > 5):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -500
			str_msg = "NO VICON DATA; LANDING"
			print(str_msg)
			state_publisher.publish(str_msg)
			velocity_publisher.publish(vel)
			continue

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)
		distance_drone_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		distance_obs_to_goal = math.sqrt((obs_x - final_goal_x)**2 + (obs_y - final_goal_y)**2)
		angle_obs_to_goal = math.atan2((final_goal_y - obs_y), (final_goal_x - obs_x))
		angle_drone_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x)

		paths_align = abs(angle_drone_to_goal - angle_obs_to_goal) < angle_threshold
		obstacle_in_path = paths_align and distance_drone_to_obstacle <= detection_distance and distance_to_final_goal >  distance_obs_to_goal

		if(testing):
			print("")
			#print("start goal: "+str(goal_x)+", "+str(goal_y))
			print("obstacle_in_path: "+str(obstacle_in_path))
			print("\tpaths_align: "+str(paths_align))
			print("\tdistance_drone_to_obstacle <= detection_distance: "+str(distance_drone_to_obstacle <= detection_distance))
			print("\t\tdistance to obstacle: "+ str(distance_drone_to_obstacle))
			print("\tdistance_to_final_goal >  distance_obs_to_goal: "+str(distance_to_final_goal >  distance_obs_to_goal))
			print("\t\tdistance to final goal: "+ str(distance_to_final_goal))
			print("\t\tdistance obstacle to goal: "+ str(distance_obs_to_goal))
			print("\tangle_drone_to_goal: "+str(math.degrees(angle_drone_to_goal)))

		str_msg = "GO TO GOAL"
		obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_final_goal < threshold):
			if(hover_count < 5):
				str_msg = "GOAL REACHED"
				print("GOAL REACHED with threshold "+str(distance_to_final_goal))
				vel.linear.x = 0
				vel.linear.y = 0
				hover_count += 1

			if(goal_count == len(goal_array_x)-1 and exit_count < 5):
				str_msg = "Finished behavior"
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				exit_count += 1
				if(exit_count >= 5):
					exit()
			else:
				hover_count = 0
				goal_count +=1
				goal_x = goal_array_x[goal_count]
				goal_y = goal_array_y[goal_count]
				final_goal_x = goal_x
				final_goal_y = goal_y
				integral = 0
				previous_error = 0
		elif(avoid):
			str_msg = "AVOIDING"
			print_count = 0
			while print_count < 5:
				print("OBSTACLE_IN_PATH; AVOID")
				print_count += 1
			#tangent to circle
			#interpolated goal offset from obstacle radius
			#goal_x = curr_x + 0.005 * math.cos(avoid_angle)
			#goal_y = curr_y + 0.005 * math.sin(avoid_angle)
			#0,0->-1,-1=-135; 0,0->1,-1=-45; 0,0->-1,1=135
			angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
			angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
			#avoid_angle = angle_obs_to_drone - math.radians(90) - curr_angle
			avoid_angle = angle_drone_to_obs - math.radians(90) - curr_angle
			vel.linear.x = math.cos(avoid_angle) * (0.3)
			# negative sine bc Tello control is dumb
			vel.linear.y = -math.sin(avoid_angle) * (0.3)
			if(testing):
				print("Following avoid angle: "+str(math.degrees(avoid_angle)))
				print("angle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
				print("angle_drone_to_obs: "+str(math.degrees(angle_drone_to_obs)))
				print("")
			avoid_count += dt
			if(not obstacle_in_path and avoid_count > 5):
				avoid = False
				print("OBSTACLE NO LONGER IN PATH; AVOID TERMINATED")
				str_msg = "GO TO GOAL"
				avoid_count = 0
		else:
			print("NOT @ FINAL GOAL")
			if(obstacle_in_path):
				print("AND OBS IIN PATH")
				if(abs(distance_drone_to_obstacle - detection_distance) < threshold):
					angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
					#angle_obs_to_drone = math.pi + angle_drone_to_obs #math.atan2(curr_y-obs_y, curr_x-obs_x)
					print("angle_obs_to_drone: "+str(math.degrees(angle_obs_to_drone)))
					hover_point_x = obs_x + obstacle_threshold * math.cos(math.pi + angle_obs_to_goal)
					hover_point_y = obs_y + obstacle_threshold * math.sin(math.pi + angle_obs_to_goal)
					goal_x = hover_point_x
					goal_y = hover_point_y
					print("goal set to hover_point: "+str(hover_point_x)+", "+str(hover_point_y))
					str_msg = "GO TO GOAL"
					error = 0
					integral = 0
					previous_error = 0

				distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
				if(distance_to_goal <= 1.5):
					vel.linear.x = 0
					vel.linear.y = 0
					#while(sent < 4):
					obstacle_publisher.publish(Bool(True))
						#sent += 1
					str_msg = "HOVERING AT OBSTACLE; WAITING FOR USER INPUT"
					if(hover_count > 10):
						vel.linear.z=-200
						#hover_count = 0
						str_msg = "USER INPUT TIMEOUT; LANDING"
					print("HOVERED "+str(hover_count)+" seconds")
					hover_count += dt
					state_publisher.publish(str_msg)
					sent = 0
					while(sent < 4):
						velocity_publisher.publish(vel)
						sent += 1
					velocity_publisher.publish(vel)
					rate.sleep()
					continue
			else:
				goal_x = final_goal_x
				goal_y = final_goal_y
				print("OBSTACLE NOT IN_PATH; GO TOWARDS GOAL")
				str_msg = "GO TO GOAL"
			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			vel_x = math.cos(angle_drone_to_goal-curr_angle) * w
			vel_y = -math.sin(angle_drone_to_goal-curr_angle) * w

			previous_error = error

			if(testing):
				#print("w: "+str(w))
				print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
				print("curr_angle: " + str(curr_angle))
				#print("angle_drone_to_goal: " + str(math.degrees(angle_drone_to_goal-curr_angle)))
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

		#if(testing):
		print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
		print("distance to goal: "+str(distance_to_final_goal))
		print("goal: "+str(goal_x)+", "+str(goal_y))

		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()



if __name__ == "__main__":
    main()
