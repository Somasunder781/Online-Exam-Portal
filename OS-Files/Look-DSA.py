
from heapq import *

# hp is initial head position and requests is the list of requests , no of cylinders is 200

def LOOK(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=max(requests)
	start=min(requests)
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)

	#seek back to start
	for i in range(end,start-1,-1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	print(time)
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

if __name__=='__main__':
	print("DISK SCHEDULING:")
	print("Provide number of I/O requests")
	#n is the number of I/O requests
	n = int(input())
	print("Provide initial position of disc arm (total cylinders=200)")
	hp = int(input())
	while hp>200:
		print("!!! INVALID !!! try again")
		hp = int(input())
	print("Provide positions to visit : max is 200")
	requests = []
	for i in range(n):
		req = int(input())
		requests.append(req)

	print(requests)
    
	#calling the functions
	print("  -------     LOOK      -------")
	print("Avg seek time for  look was ", LOOK(hp,requests))
