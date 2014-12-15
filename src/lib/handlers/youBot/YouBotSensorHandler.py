#!/usr/bin/env python
"""
====================================================
youBotSensors.py - Sensor handler for the KUKA youBot
====================================================
"""

import lib.handlers.handlerTemplates as handlerTemplates

class YouBotSensorHandler(handlerTemplates.SensorHandler):
    def __init__(self, executor, shared_data):
        self.youbotInitHandler = shared_data['YOUBOT_INIT_HANDLER']
