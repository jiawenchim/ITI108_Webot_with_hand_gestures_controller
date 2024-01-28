"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard

CRUISING_SPEED= 5.0
TURN_SPEED = CRUISING_SPEED/2.0
TIME_STEP = 64

# create the Robot instance.
robot = Robot()
left_wheel = robot.getDevice('left wheel')
right_wheel = robot.getDevice('right wheel')
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)


keyboard = Keyboard()
keyboard.enable(TIME_STEP)



def command_motor(cmd):
	left_wheel.setVelocity(cmd[0])
	right_wheel.setVelocity(cmd[1])


while robot.step(TIME_STEP) != -1:
	key = keyboard.getKey()
	if(key == ord('W')):
		left_wheel.setVelocity(CRUISING_SPEED)
		right_wheel.setVelocity(CRUISING_SPEED)
	elif key == ord('S'):
		left_wheel.setVelocity(-CRUISING_SPEED)
		right_wheel.setVelocity(-CRUISING_SPEED)
	elif (key ==  ord('A')):
		left_wheel.setVelocity(-TURN_SPEED)
		right_wheel.setVelocity(TURN_SPEED)
	elif (key ==  ord('D')):
		left_wheel.setVelocity(TURN_SPEED)
		right_wheel.setVelocity(-TURN_SPEED)
	elif (key ==  ord('E')):
		left_wheel.setVelocity(0.0)
		right_wheel.setVelocity(0.0)
	else:
		pass
	