# Simple Python script to resize a specific image in a directory to a specified size.

# Import the required modules.
import cv2
import os

# Define the directory where the images are located.
while True:
    print('This is a script to resize images in a directory to a specified size.')
    
    path=input("Enter the path of the image: ") # or if the image is in the same directory as the script, just type the name of the image


    # read the image in color, change to 0 for grayscale
    img=cv2.imread(path,1) 

    # To resize the image, we need to specify the size of the image.
    width=int(input("Enter the width of the image: "))
    height=int(input("Enter the height of the image: "))

    # Resize the image.
    resized_image = cv2.resize(img, (width,height))

    path2=input("Enter the path to save the image: ") # or if the image is in the same directory as the script, just type the name of the image
    cv2.imwrite(path2,resized_image)
    cv2.waitKey(0)
    print('Image saved successfully')
    cv2.destroyAllWindows()
    
    

