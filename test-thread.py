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
	# 	#threadLock.acquire()
	# 	f=open(path,'a')

	# 	endtime = datetime.datetime.now()
	# 	now=(endtime - starttime).seconds
	# 	nowtime=str("fly time  "+str(now)+"s\n")
	# 	print(nowtime)
	# 	f.write(nowtime)
	# 	# gt=client.simGetPositionWRTOrigin()
	# 	# print("gl \n")
	# 	# print(gt)
	# 	# print("m \n")

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

	# 	# key = ord(msvcrt.getch())
	# 	# # print (key)
	# 	# if key == 113:
	# 	# 	break

	# 	time.sleep(1)
	
		#threadLock.release()

# moveByVelocityAsync(float vx, float vy, float vz, float duration,

def fly():
	while True:
# #strart-cube2
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(1.57), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(0.00), float( 65), float( 0), float( 10))
# 		time.sleep(10)
# 		print("cube2\n")
# 		getstate()
# #cube2-3
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(220.00), float( 65), float( 0), float( 10))
# 		time.sleep(26)
# 		print("cube3\n")
# 		getstate()

# #cube3-4
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(1.57), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(220.00), float( 260), float( 0), float( 10))
# 		time.sleep(25)
# 		print("cube4\n")
# 		getstate()

# #cube4-5
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
# 		time.sleep(5)
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(-120), float(0), float(10))
# 		time.sleep(25)
# 		print("qifei\n")
# 		getstate()
# 		client.hoverAsync()
		client.moveByAngleZAsync(float(0.0), float(0.0), float(50), float(0), float(10))
		time.sleep(15)
		client.hoverAsync()
		#client.moveToPositionAsync(float(450.00), float( 260), float( -120), float( 10))
		#client.moveToPositionAsync(float(450.00), float( 260), float( -10), float( 10))
		client.moveByVelocityAsync(float(10.0), float(0.0), float(0), float(10))
		time.sleep(10)
		print("stay\n")
		client.moveByAngleZAsync(float(0.0), float(0.0), float(50), float(1.57), float(10))
		time.sleep(5)
		client.moveByVelocityAsync(float(0.0), float(10.0), float(0), float(10))
		time.sleep(10)
		print("cube5\n")
		time.sleep(30)
		print("cube5\n")
		getstate()


# #start
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
# 		time.sleep(2)

# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(0), float(10))
# 		time.sleep(8)

# #cube2
# 		client.moveToPositionAsync(float(1590.00), float( 0), float( 0), float( 10))
# 		time.sleep(185)
# #cube3
# 		client.moveToPositionAsync(float(1690.00), float( 0), float( 70), float( 10))
# 		time.sleep(20)
# 		client.moveToPositionAsync(float(1690.00), float( 0), float( 70), float( 10))
# 		time.sleep(10)
# 		# client.moveByAngleZAsync(float(0.0), float(0.0), float(0), float(-1.57), float(10))
# 		# time.sleep(5)
# 		# client.moveToPositionAsync(float(0.00), float( -156), float( 0), float( 10))
# 		# time.sleep(20)

# #cube4
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(70), float(-1.57), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(1690.00), float( -156), float( 70), float( 10))
# 		time.sleep(25)
# 		client.moveToPositionAsync(float(1690.00), float( -156), float( 70), float( 10))
# 		time.sleep(10)

# #cube5
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(70), float(0), float(10))
# 		time.sleep(8)
# 		client.moveToPositionAsync(float(1890.00), float( -156), float( 70), float( 10))
# 		time.sleep(25)
# 		client.moveToPositionAsync(float(1890.00), float( -156), float( 70), float( 10))
# 		time.sleep(10)

# #cube6
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(70), float(-1.57), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(1890.00), float( -260), float( 70), float( 10))
# 		time.sleep(13)
# #cube7
# 		client.moveByAngleZAsync(float(0.0), float(0.0), float(70), float(0), float(10))
# 		time.sleep(5)
# 		client.moveToPositionAsync(float(2100.00), float( -260), float( -20), float( 10))
# 		time.sleep(40)



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
