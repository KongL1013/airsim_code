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


# global i
#i=0









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
	time.sleep(3)
	print("start\n")

	# client.rotateByYawRateAsync(-1.57,10)
	# print("rotateToYawAsync")
	# time.sleep(5)
#3
#start-cibe2  120
	print("start-cibe2")
	client.moveByVelocityAsync(float(20), float(0), float(0), float(115))
	time.sleep(117)
	print("daoladaola")
	getstate()
# 120
# 	print("go down")
# 	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(8))
# 	time.sleep(8)

#cube2-3
	print("cube2-3")
	client.moveByVelocityAsync(float(0), float(0), float(10), float(30))
	time.sleep(30)
	getstate()
	client.moveByAngleZAsync(float(0.0), float(0.0), float(155), float(-1.57), float(10))
	time.sleep(5)
	getstate()

#155
#cube3-4
	print("cube3-4")
	client.moveByVelocityAsync(float(0), float(-20), float(0), float(10))
	time.sleep(10)
	getstate()
	client.moveByAngleZAsync(float(0.0), float(0.0), float(155), float(0), float(5))  #z154
	time.sleep(5)
	getstate()


#cube4-5
	print("cube4-5")
	client.moveByVelocityAsync(float(20), float(0), float(0), float(22))
	time.sleep(22)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(155), float(-1.57), float(10)) #z154
	time.sleep(3)


#cube5-6
	print("cube5-6")
	client.moveByVelocityAsync(float(0), float(-20), float(0), float(11))
	time.sleep(11)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(155), float(0), float(10))  #z154
	time.sleep(3)

#cube6-7
	print("cube6-7")
	client.moveByVelocityAsync(float(0), float(0), float(-10), float(22))
	time.sleep(22)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	time.sleep(5)


#cube7-8
	client.moveToPositionAsync(float(4000.00), float( -490), float( 0), float( 10))
	time.sleep(140)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(1.57), float(10))
	time.sleep(5)


#cube8-9
	client.moveToPositionAsync(float(4000.00), float( 0), float( 0), float( 10))
	time.sleep(55)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(3.14), float(10))
	time.sleep(5)

#cube9-10
	client.moveToPositionAsync(float(200.00), float( 0), float( 0), float( 10))
	time.sleep(380)
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	time.sleep(5)



	while 	True:
		client.moveToPositionAsync(float(3900.00), float( 0), float( 0), float( 10))
		time.sleep(370)
		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(3.14), float(10))
		time.sleep(5)
		client.moveToPositionAsync(float(200.00), float( 0), float( 0), float( 10))
		time.sleep(370)
		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
		time.sleep(5)


# _thread.start_new_thread(printlocate,("Thread-1",))
# _thread.start_new_thread(fly,("Thread-2",))
#threadLock=threading.Lock()




threads = []
path="E:/UE4PROJECT/test1/time.txt"


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
