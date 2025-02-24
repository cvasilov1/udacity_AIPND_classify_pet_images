#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Camelia Vasilov based on Udacity instructions
# DATE CREATED: 22 December 2024                                 
# REVISED DATE: 21 February 2025
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    
    # 1) Read dog names from file into a set   
    print(f"Dog file path: {dogfile}") 

    dognames_set = set()

    with open(dogfile, 'r') as f:
        print("Successfully opened dogfile.")

        for i, line in enumerate(f):
            # print(f"{i+1}: {line.strip()}")  
           
            # Process each line
            line = line.strip().lower()
            synonyms = [syn.strip() for syn in line.split(',')]
            dognames_set.update(synonyms)

    print("\nFinal Extracted dog Nnmes set:")
    print(dognames_set)


    # 2) Update indexes [3] & [4] in results_dic
    for filename, value in results_dic.items():
        pet_label = value[0].lower().strip()
        classifier_label = value[1].lower().strip()

        # For classifier_label, split on commas
        classifier_sub_labels = [lbl.strip() for lbl in classifier_label.split(',')]

        # Check the pet label directly (assuming it’s a single name)
        if pet_label in dognames_set:
            is_dog_pet = 1
        else:
            is_dog_pet = 0

        # Check if ANY sub-label is in the dog set
        is_dog_classifier = 1 if any(sub in dognames_set for sub in classifier_sub_labels) else 0

        value.extend([is_dog_pet, is_dog_classifier])


    # Print check
    print()
    print('MY PRINT CHECK TO DO #4 - Extend the dictionary after checking in the dogfile whether the labels correspond to dog breed names')
    
    print(f"Final Pet Image Label Dictionary has {len(results_dic)} key-value pairs.")
    print('Image file -> [true pet label, classifier pet label, match true label=classifier label, match true labe l IS dogbreed, match classifier label IS dogbreed]')
    print("Dictionary after checking labels in the dogfile text list:")
    for key, value in results_dic.items():
        print(f"{key} -> {value}")
    
    print('MY PRINT CHECK TO DO #4 - END')
    print()
    
    # No return needed
