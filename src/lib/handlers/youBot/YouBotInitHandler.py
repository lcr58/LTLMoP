#!/usr/bin/env python
"""
=================================================
youBotInit.py - youBot Initialization Handler
=================================================

Initialize the proxies to access the youBot
"""
import os
import lib.handlers.handlerTemplates as handlerTemplates

class youBotInitHandler(handlerTemplates.InitHandler):
    def __init__(self, executor, listenhost="10.0.0.128",listenport=11311):
	"""
        initialize youbot
        listenhost (string) ip address of youbot
        listenport (int) port of youbot (default=11311)
	"""
	#set the environmental variable ROS_MASTER_URI to enable connection between the LTLMoP computer and the youBot onboard PC
	os.putenv('ROS_MASTER_URI','http://{}:{}'.format(listenhost,listenport))
    
    def getSharedData(self):
        return {'YOUBOT_INIT_HANDLER': self}

if __name__ == "__main__":
    pass
