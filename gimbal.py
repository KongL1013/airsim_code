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



#screen = pygame.display.set_mode((800,600))
#pygame.display.set_caption("control")

client.moveToPositionAsync(float(-50.00), float( 50.26), float( -20.58), float( 3.5))
time.sleep(4)
client.simSetCameraOrientation("0", airsim.to_quaternion(0.5, 0.5, 0.1))
client.moveToPositionAsync(float(50.00), float( -50.26), float( -10.58), float( 3.5))
time.sleep(4)
client.simSetCameraOrientation("0", airsim.to_quaternion(-0.5, -0.5, -0.1))




