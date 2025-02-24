#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/generate_results_chart.py
#                                                                             
# PROGRAMMER: Camelia Vasilov
# DATE CREATED: 21 February 2025                                 
# REVISED DATE: 21 February 2025
# PURPOSE: Create two tables summarizing the results:
# 1) table counting the dog and not-dog images to be classified and
# 2) table showing the performance of the 3 classification models.

import os
import re
import matplotlib.pyplot as plt
import pandas as pd
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Generate results chart from model outputs.")
parser.add_argument("--dir", type=str, required=True, help="Path to the directory containing result files.")
args = parser.parse_args()

# Use the provided directory
path = args.dir

# Define function to extract statistics from text files
def extract_results(file_path):
    if not os.path.exists(file_path):  # Prevent errors if file is missing
        print(f"ERROR: File {file_path} not found!")
        return None

    with open(file_path, "r") as f:
        content = f.read()
    
    # Extract relevant statistics using regex
    try:
        num_images = int(re.search(r"Number of Images: (\d+)", content).group(1))
        num_dogs = int(re.search(r"Number of Dog Images: (\d+)", content).group(1))
        num_notdogs = int(re.search(r"Number of Non-Dog Images: (\d+)", content).group(1))
        pct_match = float(re.search(r"pct_match: (\d+\.\d+)%", content).group(1))
        pct_correct_dogs = float(re.search(r"pct_correct_dogs: (\d+\.\d+)%", content).group(1))
        pct_correct_breed = float(re.search(r"pct_correct_breed: (\d+\.\d+)%", content).group(1))
        pct_correct_notdogs = float(re.search(r"pct_correct_notdogs: (\d+\.\d+)%", content).group(1))
    except AttributeError:
        print(f"ERROR: Could not extract data from {file_path}. Check the file format.")
        return None  # If extraction fails, return None

    return {
        "num_images": num_images,
        "num_dogs": num_dogs,
        "num_notdogs": num_notdogs,
        "pct_match": pct_match,
        "pct_correct_dogs": pct_correct_dogs,
        "pct_correct_breed": pct_correct_breed,
        "pct_correct_notdogs": pct_correct_notdogs,
    }

# Extract results from each model output
resnet_results = extract_results(os.path.join(path, "resnet_pet-images.txt"))
alexnet_results = extract_results(os.path.join(path, "alexnet_pet-images.txt"))
vgg_results = extract_results(os.path.join(path, "vgg_pet-images.txt"))

# Stop if any results are missing
if None in [resnet_results, alexnet_results, vgg_results]:
    print("Some results could not be extracted. Fix errors and try again.")
    exit()

# Extract total image counts from one of the models (all models should have the same count)
num_images = resnet_results["num_images"]
num_dogs = resnet_results["num_dogs"]
num_notdogs = resnet_results["num_notdogs"]

# **Fixed Small Table Structure**
summary_df = pd.DataFrame({
    "Type": ["# Total Images", "# Dog Images", "# Not-a-Dog Images"],
    "Count": [num_images, num_dogs, num_notdogs]
})

# Create DataFrame for Model Performance Table
df = pd.DataFrame({
    "CNN Model Architecture": ["ResNet", "AlexNet", "VGG"],
    "% Not-a-Dog Correct": [resnet_results["pct_correct_notdogs"], alexnet_results["pct_correct_notdogs"], vgg_results["pct_correct_notdogs"]],
    "% Dogs Correct": [resnet_results["pct_correct_dogs"], alexnet_results["pct_correct_dogs"], vgg_results["pct_correct_dogs"]],
    "% Breeds Correct": [resnet_results["pct_correct_breed"], alexnet_results["pct_correct_breed"], vgg_results["pct_correct_breed"]],
    "% Match Labels": [resnet_results["pct_match"], alexnet_results["pct_match"], vgg_results["pct_match"]]
})

# Convert percentages to string format
df.iloc[:, 1:] = df.iloc[:, 1:].astype(str) + "%"

# Generate results table image
fig, ax = plt.subplots(figsize=(12, 4))

ax.axis("off")


# Add Title
plt.text(0.5, 1.1, "Results from Pet Images", fontsize=12, fontweight="bold", ha="center", va="top", transform=ax.transAxes)

# Set column labels for the small table
table_top = ax.table(cellText=summary_df.values, 
                     colLabels=summary_df.columns, 
                     cellLoc="center", 
                     loc="upper center")

# Scale down the small table to keep it compact
table_top.scale(0.4, 1.2)  

# Create the large model performance table below
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")
table.scale(1, 1.5)  

# Highlight best-performing model in blue
for i in range(len(df)):
    for j in range(1, len(df.columns)):  # Start at column index 1 to exclude model names
        value = float(df.iloc[i, j].replace("%", ""))
        if value == max(df.iloc[:, j].astype(str).str.replace("%", "").astype(float)):
            table[(i+1, j)].set_text_props(weight="bold", color="blue")
    
# Save table as an image
output_path = os.path.join(path, "results_summary.png")
plt.savefig(output_path, bbox_inches="tight", dpi=300)

print(f"Results table saved as {output_path}")




