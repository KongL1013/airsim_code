import threading
import setup_path
import airsim
import math
import time
import datetime
import msvcrt
import sys
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# MultirotorClient.wait_key('Press any key to takeoff')
print("Taking off")
client.takeoffAsync().join()
print("Ready")



def getstate():
	state=client.simGetGroundTruthKinematics().position
	x=round(state.x_val)
	y=round(state.y_val)
	z=round(state.z_val)
	print("now state"+'\n')
	print("x="+str(x)+'\n')
	print("y="+str(y)+'\n')
	print("z="+str(z)+'\n')

def quit():
	while True:
		key = ord(msvcrt.getch())
			# print (key)
		if key == 113  or key == 27:
			
			client.enableApiControl(False)
			client.armDisarm(False)
			break

def printlocate():
	pass
	# while True:
	# 	getstate()
	# 	time.sleep(1)
	# while True:
	# 	#threadLock.acquire()
	# 	f=open(path,'a')

	# 	endtime = datetime.datetime.now()
	# 	now=(endtime - starttime).seconds
	# 	nowtime=str("fly time  "+str(now)+"s\n")
	# 	print(nowtime)
	# 	f.write(nowtime)

	# 	state=client.simGetGroundTruthKinematics().position
	# 	x=round(state.x_val)
	# 	y=round(state.y_val)
	# 	z=round(state.z_val)
	# 	print("x="+str(x)+'\n')
	# 	print("y="+str(y)+'\n')
	# 	print("z="+str(z)+'\n')
		
	# 	f.write("x="+str(x)+'\n')
	# 	f.write("y="+str(y)+'\n')
	# 	f.write("z="+str(z)+'\n')
		
	# 	f.close()

	# 	time.sleep(1)

		#threadLock.release()
# moveByAngleZAsync(float pitch, float roll, float z, float yaw, float duration, const std::string& vehicle_name = "");
# moveByVelocityAsync(float vx, float vy, float vz, float duration,
# rotateToYawAsync(float yaw, float timeout_sec = Utils::max<float>(), float margin = 5, const std::string& vehicle_name = "");
def fly():
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	time.sleep(1)
	print("start\n")
	client.moveByVelocityAsync(float(20), float(0), float(0), float(190))
	time.sleep(190)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(3.14), float(10))
	time.sleep(5)
	while 	True:
		client.moveByVelocityAsync(float(-20), float(0), float(0), float(180))
		time.sleep(180)
		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
		time.sleep(5)
		client.moveByVelocityAsync(float(20), float(0), float(0), float(180))
		time.sleep(180)
		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(3.14), float(10))
		time.sleep(5)


threads = []
# path="E:/UE4PROJECT/test1/time.txt"


starttime = datetime.datetime.now()

thread1=threading.Thread(target=printlocate,args=())
thread2=threading.Thread(target=fly,args=())
thread3=threading.Thread(target=quit,args=())

thread2.daemon=True
thread1.daemon=True

thread1.start()
thread2.start()
thread3.start()



threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

thread3.join()

# for t in threads:
#     t.join()
