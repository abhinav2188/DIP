import numpy as np
import math

def scale(u,v,cx,cy) :
	return (cx*u,cy*v)
	
def rotate(u,v,angle) :
	pt = np.array([u,v,1])
	m = np.array([
		[math.cos(angle),math.sin(angle),0],
		[-math.sin(angle),math.cos(angle),0],
		[0,0,1]
		]);
	newpt = pt @ m;
	return newpt[:2]

def translate(u,v,tx,ty) :
	return (u+tx,v+ty)
	
def shaerVertical(u,v,sv) :
	return (u+sv*v,v)
	
def shearHorizontal(u,v,sh) :
	return (u,u*sh+v)

def main() :
	#sample point
	print("point",(2,3),"\n")
	
	print("scale " , scale(2,3,2,3))
	print("rotate " , rotate(2,3,math.pi/3))
	print("translate " , translate(2,3,4,5))
	print("shearVertical " , shaerVertical(2,3,5))
	print("shearHorizontal " , shearHorizontal(2,3,5))
	
	
if __name__ == "__main__" :
	main()