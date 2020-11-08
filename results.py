import matplotlib.pyplot as plt

def add_subplot(figure, plot, title, image, subplot_args):
    '''
    Adds subplots to a figure
    '''
    ax = figure.add_subplot(subplot_args)
    ax.set_title(title)
    plot.imshow(image, cmap = plt.cm.gray)
    plot.axis("off")


def get_results(original_image, noisy_image, restored_image, diff, mse, title, savefile):
    '''
    Plots the given result and saves them to a local directory
    Parameters:
        np.array(dtype: uint8) - original_image, noisy_image, restored_image, diff
        mse, title - Parameters to show in results
        savefile - filepath to which the result is to be saved
    '''
    fig = plt.figure(title, (14 ,14)) # Define a figure
    plt.suptitle("Mean Square Error: %.2f" % mse) # Add MSE to title

    # Plot the images
    add_subplot(fig, plt, "Original Image", original_image, 221)
    add_subplot(fig, plt, "Image with Noise", noisy_image, 222)
    add_subplot(fig, plt, title, restored_image, 223)
    add_subplot(fig, plt, "Difference", diff, 224)
    
    plt.savefig(savefile)