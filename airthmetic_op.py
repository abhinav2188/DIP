from PIL import Image
import numpy as np

#desc : function reads a image,convert it to GRAY SCALE specfied by 'imgPath' , return its gray scale matrix
def readGrayImg(imgPath) :
	img = Image.open(imgPath).convert('L')
	data = np.asarray(img)
	return data

#desc : function displays a gray scale image matrix	
def displayGray(imgMatrix) :
	print()
	for x in imgMatrix:
		for y in x:
			print(f"{ y : <4}",end="")
		print()
	print()

#desc : function saves a gray scale image with the specified path
def saveGrayImg(imgMatrix,imgPath):
	data = Image.fromarray(imgMatrix.astype(np.uint8))
	data.save(imgPath)
	print("saved "+imgPath)

	
# arithmetic and operation 
def aradd(img1,img2) :
	myadd = np.frompyfunc(lambda a,b:(a+b)//2, 2,1)
	return myadd(img1,img2)

# arithmetic substraction operation 
def arsub(img1,img2) :
	myadd = np.frompyfunc(lambda a,b:a-b, 2,1)
	return myadd(img1,img2)

def addScalar(img,factor) :
	return img+factor
	
def subScalar(img,factor) :
	return img-factor
	
def multiplyScalar(img,factor) :
	return img*factor
	
def divideScalar(img,factor) :
	return img/factor

def main() :
	img1 = readGrayImg("gray1.png")
	img2 = readGrayImg("gray2.png")
	img3 = np.arange(100).reshape(10,10)
	img4 = np.linspace(0,255,100).reshape(10,10).astype(np.uint8)
	
	print("-----------image 1----------------")
	print(img3)
	print("-----------image 2-----------------")
	print(img4)

	print("-------------airthmetic addition--------------")
	print(img4+img3)
	print("-------------airthmetic substraction--------------")
	print(img4-img3)
	
	'''
	g1addg2 = np.add(img1,img2)
	saveGrayImg(g1addg2,"g1addg2.png")
	g1subg2 = arsub(img1,img2)
	#displayGray(g1subg2)
	saveGrayImg(g1subg2,"g1subg2.png")
	
	g1scalarAdd = addScalar(img1,30);
	#displayGray(g1scalarAdd)
	saveGrayImg(g1scalarAdd,"g1scalarAdd.png")
	'''
	print("-------------scalar addition--------------")
	print(img3+10)
	print("-------------scalar substraction--------------")
	print(img3-10)
	print("-------------scalar multiplication--------------")
	print(img3*10)
	print("-------------scalar division--------------")
	print((img3/10).astype(np.uint8))

if __name__ == "__main__" :
	main()