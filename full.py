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



class go:
	def __init__(self,vx,vy,vz,t,rad):
		self.vx=vx
		self.vy=vy
		self.vz = vz
		self.t = t
		self.rad=rad #for next stage


class target:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z




tar=[
	target(2100,0,0),#cube2
	target(2250,0,-150),#cube3
	target(1,2,3),
	target(2,3,4)
]

vn=[go(20,0,0,105,0),
	go(10,0,10,26,-1.57),
	go(3,20,30,8,1.57),
	go(4,20,30,8,1.57),
	]



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
	# pass
	# while True:
	# 	getstate()
	# 	time.sleep(1)
	while True:
		#threadLock.acquire()
		f=open(path,'a')

		endtime = datetime.datetime.now()
		now=(endtime - starttime).seconds
		nowtime=str("fly time  "+str(now)+"s\n")
		print(nowtime)
		f.write(nowtime)

		state=client.simGetGroundTruthKinematics().position
		x=round(state.x_val)
		y=round(state.y_val)
		z=round(state.z_val)
		print("x="+str(x)+'\n')
		print("y="+str(y)+'\n')
		print("z="+str(z)+'\n')
		
		f.write("x="+str(x)+'\n')
		f.write("y="+str(y)+'\n')
		f.write("z="+str(z)+'\n')
		
		f.close()

		time.sleep(1)

		#threadLock.release()
# moveByAngleZAsync(float pitch, float roll, float z, float yaw, float duration, const std::string& vehicle_name = "");
# moveByVelocityAsync(float vx, float vy, float vz, float duration,
# rotateToYawAsync(float yaw, float timeout_sec = Utils::max<float>(), float margin = 5, const std::string& vehicle_name = "");
def fly():
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	time.sleep(3)
	print("start\n")
	#start-3
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(-1.57), float(10))
	time.sleep(5)
	client.moveByVelocityAsync(float(0), float(-20), float(0), float(47))
	time.sleep(47)
	
#cube3-4   55
	client.moveByVelocityAsync(float(0), float(0), float(10), float(9))
	time.sleep(9)

#cube4-5    64
	client.moveByAngleZAsync(float(0.0), float(0.0), float(80), float(0.3), float(10))
	time.sleep(14)

	client.moveByVelocityAsync(float(20), float(7.45), float(0), float(98))
	time.sleep(98)
	print("end road")
	getstate()

#cube5-2   176
#5-a
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(1.57), float(10))
	time.sleep(8)
#a-b  184
	client.moveByVelocityAsync(float(0), float(20), float(0), float(6))
	time.sleep(4)
#b-2  188
	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
	time.sleep(5)
	client.moveByVelocityAsync(float(20), float(0), float(0), float(12))
	time.sleep(16)
#start-cibe2  120
	# print("start-cibe2")
	# client.moveByVelocityAsync(float(20), float(0), float(0), float(115))
	# time.sleep(117)
	# print("daoladaola")
	# getstate()
# 120
# 	print("go down")
# 	client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(8))
# 	time.sleep(8)

#cube2-3  209
	print("cube2-3")
	client.moveByVelocityAsync(float(0), float(0), float(10), float(20))
	time.sleep(20)
	getstate()
	client.moveByAngleZAsync(float(0.0), float(0.0), float(155), float(-1.57), float(10))
	time.sleep(9)
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
# path="E:/UE4PROJECT/test1/time.txt"


starttime = datetime.datetime.now()

# thread1=threading.Thread(target=printlocate,args=())
thread2=threading.Thread(target=fly,args=())
thread3=threading.Thread(target=quit,args=())

thread2.daemon=True
# thread1.daemon=True

# thread1.start()
thread2.start()
thread3.start()



# threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

thread3.join()

# for t in threads:
#     t.join()
