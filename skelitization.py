
#-----------------------------skelization using various distance measures---------------------#

import numpy as np;
from PIL import Image;
import math;

'''
description :  readImg(imgPath) returns the binary equivalent 2D matrix of the 
			   image specified by the imgPath
'''
def readImg(imgPath):
	# open file --> convert to gray scale --> divide each pixel by 255 --> return img as binary matrix
	img = Image.open(imgPath).convert("L").point(lambda i:i/255)
	imgData = np.asarray(img)	
	return imgData;

'''
desc : saveImg(x,y) takes x(binary image matrix) and save it as an gray scale png image ("y".png)
'''
def saveImg(imgMatrix,imgPath) :
	# binary image Matrix --> image object --> gray scale image --> save img with name "imgPath.png"
	maxI = max(imgMatrix.flat);
	print(maxI)
	x = imgMatrix.astype(float)
	displayMatrix(x)
	data = Image.fromarray(x).point(lambda i: i)
	data.save(imgPath+".png");


'''
desc: display image matrix
'''
def displayMatrix(m) :
	print()
	for r in m:
		for c in r:
			print(c, end=" ")
		print()	
	print()

'''
	getCityBlockDist(pt1,pt2) calcutates city block distance b/w two points in the image matrix
	pt1, pt2 are arrays of form [x,y] where x,y are the coordinates of these points
'''
def getCityBlockDist(pt1,pt2) :
	# d = |x1-x2| + |y1-y2|
	return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
	
'''
	getChessBoradDist(pt1,pt2) calcutates chessboard distance b/w two points in the image matrix
	pt1, pt2 are arrays of form [x,y] where x,y are the coordinates of these points
'''
def getChessBoardDist(pt1,pt2) :
	# d = max( |x1-x2| , |y1-y2| )
	return max(abs(pt1[0]-pt2[0]), abs(pt1[1]-pt2[1]))
	
'''
	getEuclideanDist(pt1,pt2) calcutates chessboard distance b/w two points in the image matrix
	pt1, pt2 are arrays of form [x,y] where x,y are the coordinates of these points
'''
def getEuclideanDist(pt1,pt2) :
	# d = max( |x1-x2| , |y1-y2| )
	return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

def get8N(pt,dim) : 
	pts = []
	x = pt[0]
	y = pt[1]
	m = dim[0]
	n = dim[1]
	if x!=0 and y!=0 : pts.append([x-1,y-1])
	if x!=0 : pts.append([x-1,y])
	if x!=0 and y!=n-1 : pts.append([x-1,y+1])
	if y!=0 : pts.append([x,y-1])
	if y!=n-1 : pts.append([x,y+1])
	if x!=m-1 and y!=0 : pts.append([x+1,y-1])
	if x!=m-1 : pts.append([x+1,y])
	if x!=m-1 and y!=n-1 : pts.append([x+1,y+1])
	return pts

def getBoundaryPts(imgMatrix) : 
	pts = []
	dim = imgMatrix.shape
	for i in range(dim[0]) :
		for j in range(dim[1]) :
			if imgMatrix[i][j] == 1:
				flag = 0
				for [a,b] in get8N([i,j],dim) :
					if imgMatrix[a][b] == 0 : 
						flag = 1
						break
				if flag : pts.append([i,j])
	return pts
	
def getSurroundingPts(pt,imgMatrix) :
	pts = []
	x = pt[0]
	y = pt[1]
	dim = imgMatrix.shape; 
	
	#leftmost sp
	i = y;
	while i<=dim[1]-1 and imgMatrix[x][i] != 1 : i+=1
	if i==dim[1] : i-=1
	if imgMatrix[x][i] == 1 : pts.append([x,i])

	#rightmost sp
	i = y
	while i>=0 and imgMatrix[x][i] != 1 : i-=1 
	if i==-1 : i=0
	if imgMatrix[x][i] == 1 : pts.append([x,i])

	#topmost
	i = x
	while i>=0 and imgMatrix[i][y] != 1 : i-=1 
	if i==-1 : i=0
	if imgMatrix[i][y] == 1 : pts.append([i,y])

	#bottom 
	i = x
	while i<=dim[0]-1 and imgMatrix[i][y] != 1 : i+=1 
	if i==dim[1] : i-=1
	if imgMatrix[i][y] == 1 : pts.append([i,y])
	
	#diagonal surrounding points
	i=x
	j=y
	while i<=dim[0]-1 and j<=dim[1]-1 and imgMatrix[i][j] != 1 : 
		i+=1
		j+=1
	if i==dim[0] : i-=1
	if j==dim[1] : j-=1
	if imgMatrix[i][j] == 1 : pts.append([i,j])
	
	i=x; j=y
	while i<=dim[0]-1 and j>=0 and imgMatrix[i][j] != 1: 
		i+=1
		j-=1
	if i==dim[0] : i-=1
	if j==-1 : j+=1
	if imgMatrix[i][j] == 1 : pts.append([i,j])

	i=x; j=y
	while i>=0 and j<=dim[1]-1 and imgMatrix[i][j] != 1: 
		i-=1
		j+=1
	if i==-1 : i+=1
	if j==dim[1] : j-=1
	if imgMatrix[i][j] == 1 : pts.append([i,j])

	i=x; j=y
	while i>=0 and j>=0 and imgMatrix[i][j] != 1: 
		i-=1
		j-=1
	if i==-1 : i+=1
	if j==-1 : j+=1
	if imgMatrix[i][j] == 1 : pts.append([i,j])

	return pts

def distanceTransform(imgMatrix) : 
	dim = imgMatrix.shape
	bpts = getBoundaryPts(imgMatrix)
	skel = np.zeros(dim,int)
	for [a,b] in bpts : skel[a][b] = 1

	print("-------------------------boundary pts-----------------------");
	displayMatrix(skel)
	
	for i in range(dim[0]) :
		for j in range(dim[1]) :
			if [i,j] not in bpts and imgMatrix[i][j] == 1:
				spts = getSurroundingPts([i,j],skel)
				#print(spts)
				if len(spts) == 8 : 
					dm = []
					for [a,b] in spts : 
						dm.append(getCityBlockDist([i,j],[a,b])+1)
					skel[i][j] = min(dm)
	print("-----------------------distance transformation matrix using cityblock distance------------------")
	displayMatrix(skel)
	
#-----------------main()-----------------------------#
def main() :

	imgMatrix = readImg("img1.png")
	print("-----------------------input matrix------------------")
	displayMatrix(imgMatrix);
	distanceTransform(imgMatrix)
	
	m = 9;
	ex = np.zeros((m,m),int)
	pt1 = [4,4]
	for i in range(m) :
		for j in range(m) :
			pt2 = [i,j]
			if pt1!=pt2 : ex[i][j] = getCityBlockDist(pt1,pt2)
	
	print("city block distance demo:")
	displayMatrix(ex);
	
	for i in range(m) :
		for j in range(m) :
			pt2 = [i,j]
			if pt1!=pt2 : ex[i][j] = getChessBoardDist(pt1,pt2)
	
	print("chessboard distance demo:")
	displayMatrix(ex);

	for i in range(m) :
		for j in range(m) :
			pt2 = [i,j]
			if pt1!=pt2 : ex[i][j] = getEuclideanDist(pt1,pt2)
	
	print("euclidean distance demo:")
	displayMatrix(ex);


if __name__ == "__main__" :
	main()
	
	
	
