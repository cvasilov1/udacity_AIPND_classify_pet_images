#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                              
# PROGRAMMER: Camelia Vasilov based on Udacity instructions
# DATE CREATED: 22 December 2024                                 
# REVISED DATE: 21 February 2025
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
import os

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Get the current working directory dynamically
    base_path = os.getcwd()

    # Create 3 command line arguments as mentioned above using add_argument() from ArgumentParser method 
    parser.add_argument('--dir', type=str, 
                        default=os.path.join(base_path, 'pet_images'), 
                        help="Path to the folder of pet images")     
    parser.add_argument('--arch', type=str, default = "vgg")  
    parser.add_argument('--dogfile', type=str, 
                        default=os.path.join(base_path, 'dognames.txt'),
                        help="Path to the file containing valid dog names")

    # Parse arguments first for my print check
    my_args_check = parser.parse_args()
    
    # Print check (show debug statements before returning)
    print()
    print('MY PRINT CHECK TO DO #1 - Get input arguments for image folder directory, model architecture to be used and dog breeds textfile')
    
    print(f"Directory: {my_args_check.dir},\n" 
          f"Architecture: {my_args_check.arch},\n" 
          f"Dogfile: {my_args_check.dogfile}.")
          
    print('MY PRINT CHECK TO DO #1 - END')    
    print()
    
    # Replace None with parser.parse_args() parsed argument collection that you created with this function 
    return parser.parse_args()
