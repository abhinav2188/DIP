import numpy as np;
from PIL import Image;

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
	data = Image.fromarray(imgMatrix).point(lambda i:i*255)
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

#-----------------main()-----------------------------#
def main() :
	imgMatrix = readImg("img3.png")
	displayMatrix(imgMatrix);
	saveImg(imgMatrix,"dummy1");

	
if __name__ == "__main__" :
	main()
	
	
	
