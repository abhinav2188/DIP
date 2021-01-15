
#--------------------	Connected components labelling : using 4 connected -----------------------#

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
	desc :  getCC4N(x) takes x as an binary image matrix, 
			displays the labels before and after postprocessing,
			returns number of connected components
'''
def getCC4N(imgMatrix) :

	dim = imgMatrix.shape
	labelMatrix = np.zeros(dim, dtype=int)
	label = [];
	equalLabel = [];
	
	def assignNewLabel(x,y) :
		if label == [] : 
			labelMatrix[x][y] = 1
			label.append(1);
		else :
			lb = label[len(label) - 1] #last label
			label.append(lb+1);
			labelMatrix[x][y] = lb+1
			
	def assignLabel(x,y,l) :
		labelMatrix[x][y] = l
		
	#displayMatrix(labelMatrix)
	for i in range(dim[0]) :
		for j in range(dim[1]) :
			if imgMatrix[i][j] == 1 :	
				tp = imgMatrix[i-1][j] #top_pixel
				lp = imgMatrix[i][j-1] #left_pixel
				tl = labelMatrix[i-1][j]; #top_label
				ll = labelMatrix[i][j-1]; #left_label
				
				if not tp and not lp  :
					# 00 case --> assign new label
					#print("00", end =" | ");
					assignNewLabel(i,j)
				elif not tp and lp :
					# 01 case --> label = leftNeighbourlabel
					#print("01",end =" | ");
					assignLabel(i,j,ll)
				elif tp and not lp :
					#print("10",end =" | ");
					# 10 case --> label = topNeighbourlabel
					assignLabel(i,j,tl)
				else :
					# 11 case --> if both label are same => assign else a entey of same labels
					#print("11",end =" | ");
					assignLabel(i,j,tl)
					if tl!=ll and [tl,ll] not in equalLabel : equalLabel.append([tl,ll]);						
					
				#print(tp,lp,end=" | ");

	print("___________before postprocessing________________");
	displayMatrix(labelMatrix)
	print("labels ",label);
	print("equal labels ",equalLabel);
	
	#equating labels
	for i in range(dim[0]) :
		for j in range(dim[1]) :
			for [a,b] in equalLabel:
				p = labelMatrix[i][j];
				if p == b : labelMatrix[i][j] = a 
				
	for [a,b] in equalLabel:
		if b in label: label.remove(b)
			
	print("___________after postprocessing________________");
	displayMatrix(labelMatrix)
	print("labels ",label);
	
	return len(label)

	

#-----------------main()-----------------------------#
def main() :
	imgMatrix = readImg("img1.png")
	print("__________________input binary image matrix____________________")
	displayMatrix(imgMatrix);
	c = getCC4N(imgMatrix);
	print("number of connected components = ",c);
	

	
if __name__ == "__main__" :
	main()
	
	
	
