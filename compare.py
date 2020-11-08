import numpy as np

def mean_square_error(image1, image2):
	'''
	Returns:
		(float) 'Mean Squared Error' between two images - the sum of the squared difference between the two images
	Parameters:
		image1, image2 (np.array(dtype: uint8)) - NOTE: The two images must have the same dimension
	'''
	err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
	err /= float(image1.shape[0] * image1.shape[1])
	
	return err


def image_difference(image1, image2):
	'''
	Returns:
		(np.array(dtype: uint8)) Difference between two images
	Parameters:
		image1, image2 (np.array(dtype: uint8)) - NOTE: The two images must have the same dimension
	'''
	
	difference = np.abs(np.subtract(image1, image2,dtype=np.float))
	return difference.astype(np.uint8)


def compare_images(image1, image2):
	mse = mean_square_error(image1, image2) # Get the mean square error
	diff = image_difference(image1, image2) # Get the image difference
	
	return (mse, diff)

