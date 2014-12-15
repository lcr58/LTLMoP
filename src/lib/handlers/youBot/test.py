import lib.handlers.youBot.YouBotInitHandler as YouBotInitHandler
import lib.handlers.youBot.YouBotLocomotionControlHandler as YouBotLocomotionControlHandler
import time

youbotinit = YouBotInitHandler.youBotInitHandler(None, "10.0.0.128", 11311)
youbotinit.getSharedData()

youbotloco = YouBotLocomotionHandler.youBotLocomotionHandler(None, youbotinit.getSharedData(), '/cmd_vel')

#v = [.01,0,0]
#w = [0,0,0]
cmd = [.01, 0]

youbotloco.sendCommand(cmd)

time.sleep(10)
cmd = [0,0]
youbotloco.sendCommand(cmd)
