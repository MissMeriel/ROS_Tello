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


goal_x = float(sys.argv[1])
goal_y = float(sys.argv[2])
obs_x = -20
obs_y = -20
obs_z = -20
obs_angle = -20
obs_corner_x = 0
obs_corner_y = 0

obs_angle = 0
curr_x = 0
curr_y = 0
#curr_angle: yaw relative to global frame
curr_angle = 0
publishing = True
avoid = False
init=True
obstacle_dyn = False
testing = True
state = ""

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
	global testing
	global obs_x, obs_y, obs_z, obs_angle, obstacle_dyn
	x_change = abs(obs_x - data.transform.translation.x) > 0.0023
	y_change = abs(obs_y - data.transform.translation.y) > 0.0023
	z_change = abs(obs_z - data.transform.translation.z) > 0.001
	rot_change = abs(obs_angle - data.transform.rotation.z) > 0.025
	if(x_change or y_change or z_change or rot_change):
		obstacle_dyn = True
	else:
		obstacle_dyn = False
	#if(testing):
		#print("x_change: "+str(x_change))
		#print("y_change: "+str(y_change))
		#print("z_change: "+str(z_change))
		#print("rot_change: "+str(rot_change))
		#print("obstacle_dyn: "+str(obstacle_dyn))
		#print("")
	obs_x = data.transform.translation.x
	obs_y = data.transform.translation.y
	obs_z = data.transform.translation.z
	obs_angle = data.transform.rotation.z
	
def process_state(data):
	global state
	state=str(data)

def user_input(data):
	global avoid
	if("y" in str(data) or "Y" in str(data)):
		avoid = True

def main():
	global goal_x, goal_y
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid, obstacle_dyn, state
	global testing
	rospy.init_node("gtg_dyn", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	state_subscriber = rospy.Subscriber("/state", String, process_state, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	obstacle_dyn_publisher = rospy.Publisher("/obstacle_dyn", Bool, queue_size=1)
	key_enabler = rospy.Publisher("/keys_enabled", Bool, queue_size=1)
	position_subscriber = rospy.Subscriber("/vicon/TELLO/TELLO", TransformStamped, vicon_data, queue_size=10)
	obstacle_subscriber = rospy.Subscriber("vicon/OBSTACLE/OBSTACLE", TransformStamped, vicon_obstacle, queue_size=10)
	process_killer = rospy.Publisher("/killswitch", Bool, queue_size=5)
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
	Kp = 0.12
	Ki = 0.003
	Kd = 0.008

	publishing_count = 0
	avoid = False
	final_goal_x = goal_x
	final_goal_y = goal_y
	threshold = 0.075
	obstacle_threshold = 0.72
	angle_threshold = math.radians(15)
	detection_distance = 1
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 0.0
	avoid_count = 0.0
	control_count = 0.0
	keys_enabled=False
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
			process_killer.publish(True)
			continue
		if(publishing_count > 10):
			exit()

		distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
		distance_to_final_goal = math.sqrt((final_goal_x - curr_x)**2 + (final_goal_y - curr_y)**2)
		distance_drone_to_obstacle = math.sqrt((obs_x - curr_x)**2 + (obs_y - curr_y)**2)
		distance_obs_to_goal = math.sqrt((obs_x - final_goal_x)**2 + (obs_y - final_goal_y)**2)
<<<<<<< HEAD
		angle_obs_to_goal = math.atan2((final_goal_y - obs_y), (final_goal_x - obs_x))
		angle_drone_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x)
		paths_align = abs(angle_drone_to_goal - angle_obs_to_goal) < angle_threshold
=======

		angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)
		angle_obs_to_goal = math.atan2((final_goal_y - obs_y), (final_goal_x - obs_x))
		angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
		angle_drone_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x) - curr_angle
		angle_dronepos_to_goal = math.atan2(final_goal_y-curr_y, final_goal_x-curr_x)
		paths_align = abs(angle_dronepos_to_goal - angle_obs_to_goal) < angle_threshold
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
		obstacle_in_path = paths_align and distance_drone_to_obstacle <= detection_distance and distance_to_final_goal >  distance_obs_to_goal
		if(testing):
			print("")
			#print("start goal: "+str(goal_x)+", "+str(goal_y))
			print("obstacle_in_path: "+str(obstacle_in_path))
			#print("\tpaths_align: "+str(paths_align))
			#print("\tdistance_drone_to_obstacle <= detection_distance: "+str(distance_drone_to_obstacle <= detection_distance))
			#print("\tdistance_to_final_goal >  distance_obs_to_goal: "+str(distance_to_final_goal >  distance_obs_to_goal))
<<<<<<< HEAD
			#print("\tangle_obs_to_goal: "+str(math.degrees(angle_obs_to_goal)))
=======
			#print("\tangle_dronepos_to_goal: "+str(math.degrees(angle_dronepos_to_goal)))
			#print("\tangle_obs_to_goal: "+str(math.degrees(angle_obs_to_goal)))
			#print("\tangle_drone_to_obs: "+str(math.degrees(angle_drone_to_obs)))
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
			print("\tDistance to final goal: "+ str(distance_to_final_goal))
			print("\tDynamic obstacle?: "+str(obstacle_dyn))
			#print("\tdistance to curr goal: "+ str(distance_to_goal))
			#print("\tdistance to obstacle: "+ str(distance_drone_to_obstacle))
			#print("\tdistance from obstacle to goal: "+ str(distance_obs_to_goal))
		str_msg = "GO TO GOAL; distance to goal: "+ str(distance_to_goal)

<<<<<<< HEAD
		if(obstacle_dyn and obstacle_in_path):
=======
		if(obstacle_dyn):
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
			print("GO TO GOAL; DYNAMIC OBSTACLE IN PATH")
			str_msg="GO TO GOAL; DYNAMIC OBSTACLE IN PATH; TRANSFERRING CONTROL TO USER 1"
			obstacle_dyn_publisher.publish(True)
			key_enabler.publish(True)
			if(control_count < 4):
				vel.linear.x = 0
				vel.linear.y = 0
				velocity_publisher.publish(vel)
				obstacle_dyn_publisher.publish(True)
				key_enabler.publish(True)
				keys_enabled=True
			elif(control_count > 10 and not avoid and not keys_enabled):
				print("USER INPUT TIMEOUT; LANDING")
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				velocity_publisher.publish(vel)
		elif(obstacle_in_path and not obstacle_dyn):
			control_count = 0
			obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_final_goal < threshold):
			if(hover_count < 5):
				print("GOAL REACHED with threshold "+str(distance_to_final_goal))
				str_msg = "GO TO GOAL; GOAL REACHED with threshold "+str(distance_to_final_goal)
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				hover_count += 1
			else:
				process_killer.publish(True)
				exit()
		elif(avoid):
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
<<<<<<< HEAD
			#interpolated goal offset from obstacle radius	
			angle_drone_to_obs = math.atan2(obs_y-curr_y, obs_x-curr_x)		
			#avoid_angle = angle_drone_to_obs - curr_angle
			avoid_angle = angle_drone_to_obs - curr_angle + math.pi / 2.0
			vel.linear.x = math.cos(avoid_angle) * (0.22)
			vel.linear.y = math.sin(avoid_angle) * (0.22)
=======
			#interpolated goal offset from obstacle radius			
			avoid_angle = angle_drone_to_obs - curr_angle
			vel.linear.x = math.sin(avoid_angle) * (0.22)
			vel.linear.y = math.cos(avoid_angle) * (0.22)
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
			if(testing):
				print("Following avoid angle: "+str(math.degrees(avoid_angle)))
				print("Angle from drone to obstacle: "+str(math.degrees(angle_drone_to_obs)))
			avoid_count += dt
			if(not obstacle_in_path and avoid_count > 3.5):
				avoid = False
				print("OBSTACLE NO LONGER IN PATH")
				avoid_count = 0

		else:
			print("NOT @ FINAL GOAL")
			if(obstacle_in_path):
				print("AND OBS IIN PATH")
				if(abs(distance_drone_to_obstacle - detection_distance) < threshold):
<<<<<<< HEAD
					#angle_obs_to_drone = math.pi + angle_drone_to_obs
					angle_obs_to_drone = math.atan2(curr_y-obs_y, curr_x-obs_x)
=======
					angle_obs_to_drone = math.pi + angle_drone_to_obs
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927
					hover_point_x = obs_x + obstacle_threshold * math.cos(math.pi + angle_obs_to_goal)
					hover_point_y = obs_y + obstacle_threshold * math.sin(math.pi + angle_obs_to_goal)
					goal_x = hover_point_x
					goal_y = hover_point_y
					print("goal set to hover_point: "+str(hover_point_x)+", "+str(hover_point_y))
					error = 0
					integral = 0
					previous_error = 0

				distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
				if(distance_to_goal <= 0.5 and not keys_enabled):
					vel.linear.x = 0
					vel.linear.y = 0
					while(sent < 4):
						obstacle_publisher.publish(Bool(True))
						sent += 1
					if(hover_count > 5):
						vel.linear.z=-200
						hover_count = 0
					if(hover_count > 10):
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

<<<<<<< HEAD
			vel_x = math.cos(angle_drone_to_goal - curr_angle) * w
			#negative sin due to how Tello interprets roll (right = pos)
			vel_y = -math.sin(angle_drone_to_goal - curr_angle) * w
=======
			vel_x = math.cos(angle_drone_to_goal) * w
			#negative sin due to how Tello interprets roll (right = pos)
			vel_y = -math.sin(angle_drone_to_goal) * w
>>>>>>> 60b5fb2a3458a5dda8913c26cd99366274a52927

			previous_error = error

			if(testing):
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

		if(testing):
			print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
			print("goal: "+str(goal_x)+", "+str(goal_y))
		velocity_publisher.publish(vel)
		state_publisher.publish(str_msg)
		publishing = False
		rate.sleep()



if __name__ == "__main__":
    main()
