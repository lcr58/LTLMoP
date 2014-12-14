RobotName: #Robot Name
basic youbot

Type: #Robot type
youBot

ActuatorHandler: #Robot default actuator handler with default argument values

DriveHandler: # Robot default drive handler with default argument values
share.Drive.HolonomicDriveHandler(multiplier=0.01,maxspeed=0.1)

InitHandler: # Robot default init handler with default argument values
youBot.YouBotInitHandler()

LocomotionCommandHandler: # Robot default locomotion command handler with default argument values
youBot.YouBotLocomotionCommandHandler(velocityTopic="/cmd_vel")

MotionControlHandler: # Robot default motion control handler with default argument values
share.MotionControl.VectorControllerHandler()

PoseHandler: # Robot default pose handler with default argument values
share.Pose.ViconPoseHandler(host='10.0.0.102',port=800,x_VICON_name="KUKAyouBot2:main body <t-X>",y_VICON_name="KUKAyouBot2:main body <t-Y>",theta_VICON_name="KUKAyouBot2:main body <a-Z>")
