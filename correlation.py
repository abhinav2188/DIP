import numpy as np

#coorelation

def padding(img,dim):
	(m,n) = dim
	(M,N) = img.shape
	f = np.zeros((M+m-1,N+n-1),dtype='i')
	for id,x in np.ndenumerate(img) :
		f[(id[0]+m//2,id[1]+n//2)] = x
	print(f)
	return f

def main() :
	f = np.linspace(0,255,100).reshape(10,10).astype(np.uint8);
	fpadded = padding(f,(3,3))	
	filter = np.array([[1,2,3],[9,8,7],[2,1,0]])
	fsum = np.sum(filter)
	(m,n) = filter.shape
	(M,N) = fpadded.shape
	
	g = np.zeros_like(f)
	
	for i in range(m//2,M-m//2):
		for j in range(n//2,N-n//2):
			fpatch=fpadded[i-m//2:i+m//2+1,j-n//2:j+n//2+1]
			print(fpatch,i,j)
			g[(i-m//2,j-n//2)] = (np.sum(fpatch*filter))/fsum
	print(g)

if __name__ == "__main__" :
	main()