import numpy as np

def add_sp_noise(image, prob_salt, prob_pepper):
    '''
    Adds Salt and Pepper Noise to a GRAYSCALE image
    Returns:
        (np.array(dtype: uint8)) image array with salt and pepper noise
    Parameters:
        image (np.array(dtype: uint8)) - input grayscale image array
        prob_salt (float) - probability of salt noise
        prob_pepper (float) - probability of pepper noise
    ''' 
    image_size = image.size # Total No. of pixels
    
    #noise_density: Probability that a pixel is corrupted by salt or pepper noise
    noise_density = prob_salt + prob_pepper

    output_image = np.copy(image) # Copy image to keep original image intact

    ## Number of Salt Pixels
    # Number of noisy pixels = noise_density * no. of pixels
    # Number of salt noise pixels = Number of pixels * salt noise probability
    num_salt_pixels = int(np.ceil(image_size * prob_salt))
    
    ## Number of Pepper Pixels
    # Number of noisy pixels = noise_density * no. of pixels
    # Number of pepper noise pixels = Number of pixels * (noise density - salt noise probability)
    num_pepper_pixels = int(np.ceil(image_size * (noise_density - prob_salt)))

    ## Add Salt Noise
    # Generate 'num_salt_pixels' number of random coordinates
    # And assign 255 (salt noise) to those coordinates
    coords = [np.random.randint(0, i - 1, num_salt_pixels) for i in image.shape]
    output_image[tuple(coords)] = 255

    ## Add Pepper Noise
    # Generate 'num_pepper_pixels' number of random coordinates
    # And assign 0 (pepper noise) to those coordinates
    coords = [np.random.randint(0, i - 1, num_pepper_pixels) for i in image.shape]
    output_image[tuple(coords)] = 0
    
    return output_image