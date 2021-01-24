import numpy as np

def normalize(f,k) : 
	min = np.min(f)
	max = np.max(f)-min
	g = ((f-min)/max)*k;
	return g.astype(np.uint8);
	
def main() :
	# sample image matrix
	f = np.linspace(100,1500,120).reshape(12,10).astype(int);	
	print(f)
	print(normalize(f,255))		
	
	
if __name__ == "__main__" :
	main()