import numpy as np

def median_filter(image, kernel_order = 3):
    '''
    Applies median filter to image
    Returns:
        (np.array(dtype: uint8)) filtered image array
    Parameters:
        image (np.array(dtype: uint8)) - input grayscale image array
        kernel_order (uint - must be odd) (Default: 3) - the order of kernel window
    ''' 
    output_image = np.copy(image) # Copy image to keep original image intact

    # Get offset to left or right and up or down of a pixel to be considered as part of filter window
    offset = int(np.floor(kernel_order / 2))

    # Pad the image with edge values
    padded_image = np.pad(output_image, offset, 'edge')

    # Loop over all pixels
    for row, i in enumerate(image):
        for col, j in enumerate(image[1]):
            window = padded_image[row:row + 2*offset + 1, col:col + 2*offset + 1] # Get the window pixels
            sorted_neighbors = np.sort(window.flatten()) # Flatten window pixels into a 1D array and sort them in increasing order 
            median_index = int((len(sorted_neighbors) + 1) / 2) # Get the index of the median
            output_image[row][col] = np.array(sorted_neighbors)[median_index - 1] # Assign the median of the window to the central pixel

    return output_image