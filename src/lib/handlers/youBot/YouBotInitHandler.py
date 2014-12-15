#!/usr/bin/env python
"""
=================================================
youBotInit.py - youBot Initialization Handler
=================================================

Initialize the proxies to access Nao modules
"""
import os
import lib.handlers.handlerTemplates as handlerTemplates

class youBotInitHandler(handlerTemplates.InitHandler):
    def __init__(self, executor, listenhot="10.0.0.128",listenport=11311):
	"""
        initialize youbot
        listenhost (string) ip address of youbot
        listenport (int) port of youbot (default=11311)
	"""
	os.putenv('ROS_MASTER_URI','http://{}:{}'.format(listenhost,listenport))
    
    def getSharedData(self):
        return {'YOUBOT_INIT_HANDLER': self}

if __name__ == "__main__":
    pass
    #h = youBotInitHandler(None, "10.0.0.128", port=11311)
