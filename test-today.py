import setup_path
import airsim

import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# MultirotorClient.wait_key('Press any key to takeoff')
print("Taking off")
client.takeoffAsync().join()
print("Ready")
while True:	
	state=client.simGetGroundTruthKinematics().position
	print(state)
	#time.sleep(1)
	client.moveToPositionAsync(float(5000.00), float( 0), float( 0), float( 10))
	time.sleep(5)
	# state=client.simGetGroundTruthKinematics().position
	# print(state)
	# time.sleep(1)
	# client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(-3.14), float(10))
	# time.sleep(6)
	# client.moveToPositionAsync(float(-5000.00), float( 0), float( 0), float( 10))
	# time.sleep(100)
	# client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	# time.sleep(6)
# client.simSetCameraOrientation("0", airsim.to_quaternion(-0.5, -0.5, -0.1))