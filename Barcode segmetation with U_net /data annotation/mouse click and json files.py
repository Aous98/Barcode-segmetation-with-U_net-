# import os
# os.system("type C:\\Users\\Aous\\PycharmProjects\\barcode_test\\*.json > C:\\Users\\Aous\\PycharmProjects\\barcode_test\\coor1_6.csv")

import cv2
import os
import json


# Function to handle mouse clicks
def handle_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Record the clicked coordinates
        click_coordinates.append(x)
        click_coordinates.append(y)
        # Draw a red dot at the clicked point
        cv2.circle(image, (x, y), 15, (0, 0, 255), 2)
        cv2.imshow("Image", image)


# Path to the directory containing images
image_dir = '/home/aous/Desktop/MIPT'  # Replace with your image directory path

# Directory for saving JSON files
json_dir = "/home/aous/Desktop/MIPT/project/full data resized/predict/rr"   # Replace with the desired directory path

# List to store all the click coordinates
click_coordinates = []

# Create the JSON directory if it doesn't exist
if not os.path.exists(json_dir):
    os.makedirs(json_dir)

# Loop through the images in the directory
for file in os.listdir(image_dir):
    # for file in files:
        if file.lower().endswith(('.png', '.jpg')):
            # Read the image
            image_path = os.path.join(image_dir, file)
            image = cv2.imread(image_path)
            if image is not None:
                # cv2.resizeWindow("Image", 200, 400)
                height, width, _ = image.shape
                click_coordinates.append(width)
                click_coordinates.append(height)
                # Create a window with a name (e.g., 'Image')
                cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

                # Set the window to allow resizing
                cv2.resizeWindow('Image', width, height)
                cv2.imshow("Image", image)
                cv2.setMouseCallback("Image", handle_click)
                cv2.waitKey(20000)
                cv2.destroyAllWindows()

                # Save coordinates for this image to a JSON file in the specified directory
                json_filename = os.path.join(json_dir, f"{file.split('.')[0]}.json")
                with open(json_filename, 'w') as json_file:
                    json.dump(click_coordinates, json_file)

                # Clear the coordinates for the next image
                click_coordinates = []
                cv2.imwrite("/home/aous/Desktop/MIPT/1.png",image)
