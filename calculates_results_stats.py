#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Camelia Vasilov based on Udacity instructions
# DATE CREATED: 22 December 2024                                 
# REVISED DATE: 21 February 2025
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = {}
    
    n_images = 0 # number of images
    n_dogs_img = 0 # number of dog images
    n_notdogs_img = 0 # number of NON-dog images
    n_match = 0 # number of matches between pet & classifier labels
    n_correct_dogs = 0 # number of correctly classified dog images
    n_correct_notdogs = 0 # number of correctly classified NON-dog images
    n_correct_breed = 0 # number of correctly classified dog breeds
    pct_match = 0 # percentage of correct matches
    pct_correct_dogs = 0 # percentage of correctly classified dogs
    pct_correct_breed = 0 # percentage of correctly classified dog breeds
    pct_correct_notdogs = 0 # percentage of correctly classified NON-dogs
    
    # Iterate through the results dictionary to calculate counts
    # I know that using results_dic.values() is possible here but I like the clear IF structure allowed by calling the 'file_name'  
    for file_name, value in results_dic.items():
        true_label = value[0]
        classifier_label = value[1]
        match = value[2]
        match_dogfile_true = value[3]
        match_dogfile_classifier = value[4]

        if file_name:
            n_images += 1
            
        # Match count (true_label matches classifier_label)
        if match == 1:
            n_match += 1

        # Count of correctly classified dog images
        if match_dogfile_true == 1 and match_dogfile_classifier == 1:
            n_correct_dogs += 1

        # Count of correctly classified dog breeds
        if match_dogfile_true == 1 and match_dogfile_classifier == 1 and match == 1:
            n_correct_breed += 1

        # Count of correctly classified non-dog images
        if match_dogfile_true == 0 and match_dogfile_classifier == 0:
            n_correct_notdogs += 1

        # Count of dog images and non-dog images
        if match_dogfile_true == 1:
            n_dogs_img += 1
        else:
            n_notdogs_img += 1

    # Calculate percentages accounting for the possibility of zero denominator
    pct_match = (n_match / n_images) * 100 if n_images > 0 else 0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100 if n_dogs_img > 0 else 0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100 if n_dogs_img > 0 else 0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100 if n_notdogs_img > 0 else 0

    # Populate the results stats dictionary
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['pct_match'] = pct_match
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs
    
    # Print check
    print()
    print('MY PRINT CHECK TO DO #5 - Create dictionary summarizing the results dictionary')
    
    print(f"Summary dictionary has {len(results_stats_dic)} key-value pairs.")
    print('Statistic -> [value]')
    print("Dictionary after checking labels in the dogfile text list:")
    for key, value in results_stats_dic.items():
        print(f"{key} -> {value}")
    
    print('MY PRINT CHECK TO DO #5 - END')
    print()

    return results_stats_dic
