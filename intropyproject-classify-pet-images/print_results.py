#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Julien Blocman
# DATE CREATED: May 25, 2021
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    

    print("Out of {} images, incuding {} images of dogs, the CNN model {} correctly classified:"
          .format(results_stats_dic['n_images'],
                  results_stats_dic['n_dogs_img'],
                  model))
    print("{}% of the dogs, {}% of the breed, and {}% of the non-dogs"
          .format(results_stats_dic['pct_correct_dogs'],
                  results_stats_dic['pct_correct_breed'],
                  results_stats_dic['pct_correct_notdogs']))

    if print_incorrect_dogs:

        wrong_dogs = {}

        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                wrong_dogs[results_dic[key][0]] = wrong_dogs. get(results_dic[key][0], 0) + 1

        for mistake in wrong_dogs:
            if wrong_dogs[mistake] == 1:
                print("There was 1 image of {} not identified as a dog".format(mistake))
            else:
                print("There were {} images of {} not identified as dogs".format(wrong_dogs[mistake], mistake))


    if print_incorrect_breed:

        wrong_breed = {}

        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0:
                wrong_breed[results_dic[key][0]] = wrong_breed. get(results_dic[key][0], 0) + 1

        for mistake in wrong_breed:
            if wrong_breed[mistake] == 1:
                print("There was 1 image of {} identified as another breed".format(mistake))
            else:
                print("There were {} images of {} identified as another breed".format(wrong_breed[mistake], mistake))


