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
from std_msgs.msg import Int64
#from vicon_bridge import Marker


goal_x = -200#float(sys.argv[1])
goal_y = -200#float(sys.argv[2])
final_goal_x = -200#float(sys.argv[1])
final_goal_y = -200#float(sys.argv[2])
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
landing = False
hover_count = 0
manual = False
testing=True

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

def user_input(data):
	global goal_x, goal_y, final_goal_x, final_goal_y
	global hover_count
	global landing, manual, avoid
	strdata = str(data)
	strdata = strdata.rstrip('\n')
	strdata = strdata.replace("\\n", "")
	strdata = strdata.replace("data: ", "")
	strdata = strdata.replace("\"", "")
	print("user_input callback data: "+str(strdata))
	if("," in strdata):
		result = [x.rstrip() for x in strdata.split(',')]
		try:
			print(result)
			goal_x = float(result[0])
			goal_y = float(result[1])
			final_goal_x = goal_x
			final_goal_y = goal_y
			print("NEW GOAL: "+str(goal_x)+", "+str(goal_y))
			#send out state msg?
			hover_count = 0
		except Exception as e:
			print("Invalid goal from user input. Landing.")
			landing = True
	elif("user" in strdata):
		print("manual mode")
		manual=True
	elif("y" in strdata or "Y" in strdata):
		avoid=True

def main():
	global goal_x, goal_y, final_goal_x, final_goal_y
	global hover_count
	global threshold
	global obs_x, obs_y, obs_z, obs_angle
	global curr_x, curr_y, curr_angle
	global publishing, avoid, landing, manual,testing
	rospy.init_node("gtg_transfer", anonymous=True)
	velocity_publisher = rospy.Publisher("/velocity", Twist, queue_size=10)
	state_publisher = rospy.Publisher("/state", String, queue_size=10)
	obstacle_publisher = rospy.Publisher("/obstacle_detector", Bool, queue_size=1)
	process_killer = rospy.Publisher("/killswitch", Bool, queue_size=5)
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
	Kp = 0.13
	Ki = 0.003
	Kd = 0.006

	publishing_count = 0
	avoid = False
	final_goal_x = goal_x
	final_goal_y = goal_y
	threshold = 0.12
	obstacle_threshold = 0.5
	angle_threshold = math.degrees(10)#0.55~31deg
	detection_distance = 1
	count = 0.0
	sent = 0
	vel_x = 0
	vel_y = 0
	hover_count = 0.0
	avoid_count = 0.0
	landing_count = 0.0

	while not rospy.is_shutdown():

		#check for lapse in vicon data
		if(not publishing):
			publishing_count += 1
		else:
			publishing_count = 0
		if(publishing_count > 5):
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			str_msg = "NO VICON DATA; LANDING"
			print(str_msg)
			state_publisher.publish(str_msg)
			velocity_publisher.publish(vel)
			continue
		if(publishing_count > 7):
			process_killer.publish(True)
			process_killer.publish(True)
			process_killer.publish(True)
			process_killer.publish(True)
			process_killer.publish(True)
			exit()

		#force landing
		if(landing):
			str_msg = "INPUT TRIGGERED LANDING"
			print(str_msg)
			state_publisher.publish(str_msg)
			vel.linear.x = 0
			vel.linear.y = 0
			vel.linear.z = -200
			velocity_publisher.publish(vel)
			landing_count += dt
			if(landing_count > 3):
				process_killer.publish(True)
			if(landing_count > 5):
				exit()
			continue

		if(goal_x < -100 and goal_y < -100 and not manual):
			if(hover_count < 13):
				vel.linear.x = 0
				vel.linear.y = 0
				hover_count += dt
				str_msg="WAITING FOR USER INPUT"
				print(str_msg)
				velocity_publisher.publish(vel)
				state_publisher.publish(str_msg)
				rate.sleep()
				continue
			elif(hover_count < 15):
				print("Timeout reached; Landing now")
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				str_msg="USER INPUT TIMEOUT; LANDING"
				velocity_publisher.publish(vel)
				state_publisher.publish(str_msg)
				hover_count += dt
				rate.sleep()
				continue
			else:
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				exit()

		if(manual):
			str_msg="MANUAL MODE"
			state_publisher.publish(str_msg)
			rate.sleep()
			continue

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

		obstacle_publisher.publish(Bool(obstacle_in_path))

		if (distance_to_final_goal < threshold):
			if(hover_count < 5):
				print("GO TO GOAL; GOAL REACHED with threshold "+str(distance_to_final_goal))
				str_msg = "GO TO GOAL"
				print("Waiting for user input")
				vel.linear.x = 0
				vel.linear.y = 0
				hover_count += 1
			elif(hover_count < 15):
				print("Timeout reached; Landing now")
				vel.linear.x = 0
				vel.linear.y = 0
				vel.linear.z = -200
				hover_count += 1
			else:
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				process_killer.publish(True)
				exit()
		elif(avoid):
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			print("OBSTACLE_IN_PATH; AVOID")
			avoid_angle = angle_drone_to_obs + math.radians(60) - curr_angle

			vel.linear.x = math.cos(avoid_angle) * (0.22)
			vel.linear.y = -math.sin(avoid_angle) * (0.22)
			
			print("new avoid goal: "+str(goal_x)+", "+str(goal_y))
			print("new avoid angle: "+str(math.degrees(avoid_angle)))
			print("angle_drone_to_obs: "+str(math.degrees(angle_drone_to_obs)))
			avoid_count += dt
			if(not obstacle_in_path and avoid_count > 5):
				avoid = False
				print("OBSTACLE NO LONGER IN PATH")
				avoid_count = 0

		elif(obstacle_in_path):
			print("NOT @ FINAL GOAL AND OBS IIN PATH")
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
				str_msg = "GO TO GOAL"
				angle_drone_to_hoverpt = math.atan2(goal_y-curr_y, goal_x-curr_x)
				vel.linear.x = 10 * math.cos(angle_drone_to_hoverpt)
				vel.linear.y = 10 * -math.sin(angle_drone_to_hoverpt)
			distance_to_goal = math.sqrt((goal_x - curr_x)**2 + (goal_y - curr_y)**2)
			if(distance_to_goal <= 0.5):
				if hover_count < 10:
					vel.linear.x = 0
					vel.linear.y = 0
					#while(sent < 4):
					obstacle_publisher.publish(Bool(True))
						#sent += 1
					str_msg = "HOVERING AT OBSTACLE; WAITING FOR USER INPUT"
					print("HOVERED "+str(hover_count)+" seconds")
				if(hover_count > 10):
					vel.linear.z=-200
					str_msg = "USER INPUT TIMEOUT; LANDING"
					print(str_msg)
				if(hover_count > 12):
					exit()
				hover_count += dt
			print("vel.x: "+str(vel.linear.x))
			print("vel.y: "+str(vel.linear.y))
			state_publisher.publish(str_msg)
			velocity_publisher.publish(vel)
			rate.sleep()
			continue

		else:
			goal_x = final_goal_x
			goal_y = final_goal_y
			print("OBSTACLE NOT IN_PATH; GO TO GOAL")

			error = distance_to_goal
			derivative = (error - previous_error) / dt
			integral = integral + (error * dt)
			w = Kp*error + Ki*integral + Kd*derivative

			vel_x = math.cos(angle_drone_to_goal) * w
			vel_y = -math.sin(angle_drone_to_goal) * w

			previous_error = error

			print("curr_x, curr_y: "+str(curr_x)+", "+str(curr_y))
			print("curr_angle: " + str(curr_angle))
			#print("angle_drone_to_goal: " + str(angle_drone_to_goal))
	
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

			print("vel.x, vel.y: "+ str(vel.linear.x)+", "+ str(vel.linear.y))
			print("goal: "+str(goal_x)+", "+str(goal_y))
			velocity_publisher.publish(vel)
			state_publisher.publish(str_msg)
			publishing = False
			rate.sleep()



if __name__ == "__main__":
    main()
