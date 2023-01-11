# Open images and labels
# import cv2
import numpy as np
import json
import math
import os

# Do this in a function
def get_labels_and_image(camera_name, img_name):
    # Open image file
    # join path
    # img = cv2.imread(os.path.join('dataset', "images",  camera_name, '{}.JPG'.format(img_name)))
    # Open json label file
    labels = open(os.path.join('dataset', 'CompleteAnnotations_2016-07-11', '{}.json'.format(camera_name)), 'r')
    # Parse json file
    labels = json.load(labels)
    recs = []
    for i in labels["dots"]:
        if i["imName"] == img_name:
            recs.append(i)
    return recs

# Create a function to save the labels
def save_labels(squares, camera_name, img_name):
    # Create a file
    # Check if the directory exists if not, create it recursively
    if not os.path.exists(os.path.join('dataset', 'labels', camera_name)):
        os.makedirs(os.path.join('dataset', 'labels', camera_name))
        
    f = open(os.path.join('dataset', 'labels', camera_name, '{}.txt'.format(img_name)), 'w')
    # Write the labels
    for i in range(len(squares)):
        # Square center
        x, y = (squares[i][0]), (squares[i][1])
        # Square width and height
        w, h = squares[i][2], squares[i][3]
        f.write('0 {} {} {} {}\n'.format(x, y, w, h))

# Create a function to process the labels
def process_labels(camera_name, img_name):
    # Get the image and the labels
    recs = get_labels_and_image(camera_name, img_name)

    if recs[0]["xy"] == [] or recs[0]["xy"] == None or recs[0]["xy"] == "_NaN_":
        return

    # Squares
    squares = []
    visited = False
    for i in recs[0]["xy"]:
        # If i is not a list, or enpty, skip it
        if type(i) != list or i == [] or i == None or i == "_NaN_" or i == [''] or i == '':
            continue

        if not visited:
            for j in i:
                if type(j) != list or j == [] or j == None or j == "_NaN_" or j == [''] or j == '':
                    continue
        
                # plt.scatter(j[0], j[1], color='r', s=10)
                # Each square for a given point is proportional to what is the y value of that point. Initating from 0 to the height of the image
                # There is a linear relationship between the y value of the point and the area of the square
                # The area of the square is proportional to the y value of the point
                # To calculate the area of the square, we need to know the height of the image
                # Get the height of the image
                height = 1536
                width = 2048
                # Get the y value of the point
                y = j[1]
                # Calculate the area of the square
                area = ((y/height) + 0.1) * 120000 - 12000
                
                # Save the square
                if area > 0:
                    # Turn the area into a percentage of the image                    
                    x = j[0] / width
                    y = j[1] / height
                    w = math.sqrt(area) / width
                    h = math.sqrt(area) / height
                    squares.append((x, y, w, h))
                    visited = True

    # Save the labels
    save_labels(squares, camera_name, img_name)
    return squares

def main():
    # Use Tqdm to show the progress
    from tqdm import tqdm

    camera_name = 'BAILa'
    # Get all the images
    images = os.listdir("dataset/images/{}".format(camera_name))
    print("Processing camera: {}".format(camera_name))

    # Process the labels for each image
    for img in tqdm(images):
        # If the image is not a .JPG file, skip it
        if img[-3:] != 'JPG':
            continue
        # Process the labels
        process_labels(camera_name, img[:-4])

if __name__ == '__main__':
    main()