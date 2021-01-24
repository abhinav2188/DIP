import numpy as np

#getpadding(img,dim) takes input as a image matrix and a grid dimension, return the padded image matrix with zeros
def getpadding(img,dim):
	(m,n) = dim
	(M,N) = img.shape
	f = np.zeros((M+m-1,N+n-1),dtype='i')
	for id,x in np.ndenumerate(img) :
		f[(id[0]+m//2,id[1]+n//2)] = x
	return f

def spatialAvg(f,grid):
	(m,n) = grid
	#get padded image
	fpadded = getpadding(f,(m,n))		
	(M,N) = fpadded.shape
	
	#created new image matrix
	g = np.zeros_like(f)
	
	#defing new image matrix 
	for i in range(m//2,M-m//2):
		for j in range(n//2,N-n//2):
			fpatch=fpadded[i-m//2:i+m//2+1,j-n//2:j+n//2+1]
			g[(i-m//2,j-n//2)] = np.mean(fpatch)

	return g

def spatialMax(f,grid):
	(m,n) = grid
	#get padded image
	fpadded = getpadding(f,(m,n))		
	(M,N) = fpadded.shape
	
	#created new image matrix
	g = np.zeros_like(f)
	
	#defing new image matrix 
	for i in range(m//2,M-m//2):
		for j in range(n//2,N-n//2):
			fpatch=fpadded[i-m//2:i+m//2+1,j-n//2:j+n//2+1]
			g[(i-m//2,j-n//2)] = np.max(fpatch)

	return g

def spatialMin(f,grid):
	(m,n) = grid
	#get padded image
	fpadded = getpadding(f,(m,n))		
	(M,N) = fpadded.shape
	
	#created new image matrix
	g = np.zeros_like(f)
	
	#defing new image matrix 
	for i in range(m//2,M-m//2):
		for j in range(n//2,N-n//2):
			fpatch=fpadded[i-m//2:i+m//2+1,j-n//2:j+n//2+1]
			g[(i-m//2,j-n//2)] = np.min(fpatch)

	return g

def main() :

	# sample image matrix
	f = np.linspace(0,255,100).reshape(10,10).astype(np.uint8);
	
	#taking grid as input
	m = input("enter number of rows in grid ")
	n = input("enter number of columns in grid ")
	m = int(m)
	n = int(n)

	gavg = spatialAvg(f,(m,n))
	gmax = spatialMax(f,(m,n))
	gmin = spatialMin(f,(m,n))

	print(gavg)
	print(gmax)
	print(gmin)

if __name__ == "__main__" :
	main()