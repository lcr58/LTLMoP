#!/usr/bin/env python

import roslib;

import rospy, math, subprocess, os, sys

from geometry_msgs.msg import Twist

"""
==================================================================
youBotLocomotionCommand.py - youBot Locomotion Command Handler
==================================================================

Send forward, side, and angular velocity commands to the Nao.
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
		self.pub = rospy.Publisher(velocityTopic, Twist)
		rospy.init_node("LTLMoP_control")
		# for youBot, use /cmd_vel
	except:
		print 'Problem setting up Locomotion Command Node'

    def sendCommand(self, cmd):
	#Twist is the message type and consists of linear velocities x,y,z
	# and roll, pitch, yaw orientation velocities (x,y,z)

	twist = Twist()
	#Positive x is forward
	twist.linear.x = cmd[0]
	twist.linear.y = cmd[1]
	twist.angular.z = 0.0

	#publish command to robot
	self.pub.publish(twist)

	
        #self.youbotInitHandler = shared_data['YOUBOT_INIT_HANDLER']
