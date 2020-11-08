import cv2
import os, datetime

from noise import add_sp_noise
from image_filter import median_filter    
from compare import compare_images
from results import get_results

def main():
    input_image = cv2.imread('image2.tiff', cv2.IMREAD_GRAYSCALE) # Read local image in grayscale
    image_with_sp = add_sp_noise(input_image, prob_salt=0.2, prob_pepper=0.2) # Add salt and pepper noise

    cv2.imshow('Original Image', input_image) # Display Original image
    cv2.imshow('Noisy Image', image_with_sp) # Display image with Salt and Pepper Noise

    num_passes=5 # number of passes for filtering
    
    # Make results directory with timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists('results/'):
        os.mkdir('results/')
    os.mkdir('results/' + timestamp)

    # Carry out median filtering
    for i in range(num_passes):
        if i==0:
            restored_image = median_filter(image_with_sp) # apply filter to noisy image
        else:
            restored_image = median_filter(restored_image) # apply filter to result of previous pass
        mse, diff = compare_images(input_image, restored_image) # compare images to get mean square error and difference

        # Call the get results function with the required data
        get_results(input_image, image_with_sp, restored_image, diff, mse, 'Pass %d'%(i+1), 'results/' + timestamp + '/pass_%d.png'%(i+1))

    cv2.imshow('Restored: Pass-%d'%num_passes, restored_image) # Display the final restored image
    cv2.imshow('Difference', diff) # Display the difference between the original image and final restored image

    cv2.waitKey(0) # Press any key to terminate window
    cv2.destroyAllWindows() # Terminate all windows to end the program


# Call the main function to start the program
main()
