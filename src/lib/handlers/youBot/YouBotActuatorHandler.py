#!/usr/bin/env python
"""
===============================================
youBotActuator.py - youBot Actuator Handler
===============================================

Control predefined youBot motion
"""

import time
import threading

import lib.handlers.handlerTemplates as handlerTemplates

class YouBotActuatorHandler(handlerTemplates.ActuatorHandler):
    def __init__(self, executor, shared_data):
        """

        """
        self.youbotInitHandler = shared_data['YOUBOT_INIT_HANDLER']
