#!/usr/bin/env python

import rospy, sys

from geometry_msgs.msg import Twist

"""
==================================================================
youBotLocomotionCommand.py - youBot Locomotion Command Handler
==================================================================

Send translational and longitudinal velocity commands to the youBot.
"""

import lib.handlers.handlerTemplates as handlerTemplates
class YouBotLocomotionCommandHandler(handlerTemplates.LocomotionCommandHandler):
    def __init__(self, executor, shared_data, velocityTopic='/cmd_vel'):
        """
        Locomotion Command handler for KUKA youBot robot.
	velocityTopic (str): The topic which handles velocities, /cmd_vel for the youBot.
        """
	try:
	    #open a publisher for the topic
    	    #youbot velocity topic is /cmd_vel
	    self.pub = rospy.Publisher(velocityTopic, Twist)
	    # initialize ros node
	    rospy.init_node("LTLMoP_control")
	except:
	    print 'Problem setting up Locomotion Command Node'

    def sendCommand(self, cmd):
	#Twist is the message type and consists of linear velocities x,y,z
	# and roll, pitch, yaw orientation velocities (x,y,z)

	twist = Twist()
	#set x and y velocities, z is 0
	twist.linear.x = cmd[0]
	twist.linear.y = cmd[1]
	twist.linear.z = 0
	
	#set angular velocities to 0
	twist.angular.x = 0
	twist.angular.y = 0
	twist.angular.z = 0

	#publish command to robot
	self.pub.publish(twist)

	
