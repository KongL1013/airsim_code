import multiprocessing
import setup_path
import airsim
import sys
import time
import msvcrt


def exit_event(flag):
	
	while True:
		key = ord(msvcrt.getch())
		# print (key)

		if key == 113:
			flag[0] = 1
			break


# def check_flag(flag):
# 	if flag[0] == 1:
# 		print ("exit")
# 		return True
# 	else:
# 		return False

def wait(timesec, flag):
	interval = 0.2
	counter = 0
	max_times = timesec / interval

	while counter < max_times:
		counter += 1
		time.sleep(interval)

		if flag[0] == 1:
			return True

	return False


def send(flag):
	# connect to the AirSim simulator
	client = airsim.MultirotorClient()

	client.confirmConnection()
	client.enableApiControl(True)
	client.armDisarm(True)

	#MultirotorClient.wait_key('Press any key to takeoff')
	print("Taking off")
	client.takeoffAsync().join()
	print("Ready")

	# MultirotorRpcLibClient* moveToPositionAsync(float x, float y, float z, float velocity, float timeout_sec = Utils::max<float>(),
	#         DrivetrainType drivetrain = DrivetrainType::MaxDegreeOfFreedom, const YawMode& yaw_mode = YawMode(), 
	#         float lookahead = -1, float adaptive_lookahead = 1, const std::string& vehicle_name = "");

	# MultirotorRpcLibClient* rotateToYawAsync(float yaw, float timeout_sec = Utils::max<float>(), float margin = 5, const std::string& vehicle_name = "");
	# MultirotorRpcLibClient* moveByAngleZAsync(float pitch, float roll, float z, float yaw, float duration, const std::string& vehicle_name = "");
	
	while True:

		client.moveByAngleZAsync(float(0.0), float(0.0), float(-45), float(0), float(10))
		if(wait(11, flag)):
			break

		client.moveToPositionAsync(float(1800.00), float( 0), float( -45), float(10))
		if(wait(245, flag)):
			break

		client.moveByAngleZAsync(float(0.0), float(0.0), float(-45), float(-3.14), float(10))
		if(wait(5, flag)):
			break

		client.moveToPositionAsync(float(0.00), float( 0), float( -45), float( 10))
		if(wait(245, flag)):
			break
		# client.moveToPositionAsync(float(-1800.00), float( 0), float( -45), float(10))
		# if(wait(10, flag)):
		# 	break
		

if __name__ == '__main__':
	
    exit_flag = multiprocessing.Manager().list([0])

    pool = multiprocessing.Pool(processes = 2)
   
    pool.apply_async(exit_event, (exit_flag, ))
    pool.apply_async(send, (exit_flag, ))

    pool.close()
    pool.join()    # behind close() or terminate()
    print("Exited!")
    



