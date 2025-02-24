#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Camelia Vasilov based on Udacity instructions
# DATE CREATED: 22 December 2024                                 
# REVISED DATE: 21 February 2025
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import re

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
   
    file_names = [f for f in listdir(image_dir) if f.endswith(".jpg")]
    print('These are the files:')
    print(file_names)
    
    # Initialize an empty dictionary
    results_dic = {}

    # Loop through file names and transform them
    for file_name in file_names:
        # Extract the label using regex (everything before _[number])
        match = re.match(r"^(.*)_[0-9]+", file_name)
        if match:
            pet_label = match.group(1).lower().replace("_", " ")
        else:
            pet_label = file_name.lower().replace("_", " ").split(".jpg")[0]

        # Add the file name and pet label to the dictionary
        results_dic[file_name] = [pet_label]

    # Print check (show debug statements before returning)
    print()
    print("MY PRINT CHECK TO DO #2 - Get true pet labels from the image names")
    
    print(f"The Dictionary has {len(results_dic)} key-value pairs.")
    print('Dictionary created:')
    print('Image file -> [true pet label]')
    for key, value in results_dic.items():
        print(f"{key} -> {value}")
    
    print("MY PRINT CHECK TO DO #2 - END")
    print()
    
    # Replace None with the results_dic dictionary that you created with this function
    return results_dic
    

        