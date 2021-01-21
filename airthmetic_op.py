import numpy as np;
from PIL import Image;

'''
description :  readImg(imgPath) returns the binary equivalent 2D matrix of the 
			   image specified by the imgPath
'''
def readImgAsBinary(imgPath):
	# open file --> convert to gray scale --> divide each pixel by 255 --> return img as binary matrix
	img = Image.open(imgPath).convert("L").point(lambda i:i/255)
	imgData = np.asarray(img)	
	return imgData;

'''
desc : saveImg(x,y) takes x(binary image matrix) and save it as an gray scale png image ("y".png)
'''
def saveImg(imgMatrix,imgPath) :
	# binary image Matrix --> image object --> gray scale image --> save img with name "imgPath.png"
	data = Image.fromarray((imgMatrix*255).astype(np.uint8))
	data.save(imgPath+".png")
	print("saved "+imgPath+".png")

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

# not operation
def notOperation(imgMatrix) :
	#unify numpy function for element wise manipulation
	mynot = np.frompyfunc(lambda a:1^a,1,1)
	return mynot(imgMatrix)
	
# and operation 
def andOperation(img1,img2) :
	if img1.shape != img2.shape : 
		print("error : input images have different dimensions")
	myand = np.frompyfunc(lambda a,b : a & b ,2,1)	
	return myand(img1,img2)	

# or Operation
def orOperation(img1,img2) :
	if img1.shape != img2.shape : 
		print("error : input images have different dimensions")
	myor = np.frompyfunc(lambda a,b : a | b ,2,1)	
	return myor(img1,img2)	

# xor operation
def xorOperation(img1,img2) :
	if img1.shape != img2.shape : 
		print("error : input images have different dimensions")
	myxor = np.frompyfunc(lambda a,b: a^b, 2,1)
	return myxor(img1,img2)

#-----------------main()-----------------------------#
def main() :
	imgMatrix1 = readImgAsBinary("img1.png")
	imgMatrix2 = readImgAsBinary("img2.png")
	imgMatrix3 = readImgAsBinary("img3.png")

	notimg3 = notOperation(imgMatrix3)
	img3andimg1 = andOperation(imgMatrix3,imgMatrix1)
	img3orimg1 = orOperation(imgMatrix3,imgMatrix1)
	img3xorimg1 = xorOperation(imgMatrix3,imgMatrix1)
	
	saveImg(notimg3,"notImg3")
	saveImg(img3andimg1,"img3andimg1")
	saveImg(img3orimg1,"img3orimg1")
	saveImg(img3xorimg1,"img3xorimg1")
	
if __name__ == "__main__" :
	main()
	
	
	
