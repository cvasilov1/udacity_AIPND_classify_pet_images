**🐶 Pet Image Classifier - Udacity AI Programming with Python**

**Project Overview**

This project classifies pet images using a **pre-trained Convolutional Neural Network (CNN)**. It determines whether the images contain dogs and identifies their breeds using three different CNN models: **VGG, AlexNet, and ResNet**. The script compares the model predictions to the actual labels derived from filenames and generates a summary of performance statistics.

The project is structured to run via command-line scripts (.bat for Windows and .sh for Linux/macOS) to ensure automation and reproducibility.

**🏠 Project Structure**

pet-image-classifier/

│── pet_images/ # Preloaded dataset of pet images

│── uploaded_images/ # User-uploaded images for testing

│── dognames.txt # List of dog breeds

│── check_images.py # Main script for image classification

│── generate_results_chart.py # Generates a summary results image

│── run_models_batch.sh # Linux/macOS batch script

│── run_models_batch.bat # Windows batch script

│── run_models_batch_uploaded.sh # Linux/macOS batch script for uploaded images

│── run_models_batch_uploaded.bat # Windows batch script for uploaded images

│── requirements.txt # Required Python dependencies

│── README.md # Documentation

│── adjust_results4_isadog.py # Adjusts classification results to check if an image is a dog

│── calculates_results_stats.py # Computes accuracy and statistics of classification

│── classify_images.py # Uses CNN to classify images

│── classifier.py # CNN model wrapper

│── get_input_args.py # Handles command-line arguments

│── get_pet_labels.py # Extracts pet labels from filenames

│── print_results.py # Prints the final classification results

│── print_functions_for_lab_checks.py # Utility functions for debugging

│── test_classifier.py # Tests classifier functions

│── results_summary.png # Generated summary image of results (output file)

│── resnet_pet-images.txt # ResNet model results (output file)

│── alexnet_pet-images.txt # AlexNet model results (output file)

│── vgg_pet-images.txt # VGG model results (output file)

│── resnet_uploaded-images.txt # ResNet model results for uploaded images (output file)

│── alexnet_uploaded-images.txt # AlexNet model results for uploaded images (output file)

│── vgg_uploaded-images.txt # VGG model results for uploaded images (output file)

**🚀 Installation**

**1️. Clone the Repository**

git clone <https://github.com/YOUR_USERNAME/pet-image-classifier.git>

cd pet-image-classifier

**2️. Install Dependencies**

This project was developed using Python **3.11**. Install required packages:

pip install -r requirements.txt

Or, if using Anaconda and assuming you wish to run the pet image classifier in a new environment:

conda create --name pet_env python=3.11 -y

conda activate pet_env

pip install -r requirements.txt

| Library | Version | Reason | Installation Required? |
| --- | --- | --- | --- |
| argparse | 3.10.0 | Parses command-line arguments (--dir, --arch, etc.). | Yes |
| matplotlib | 3.10.0 | Used for plotting and saving images. | Yes |
| numpy | 1.26.4 | Handles numerical computations. | Yes |
| pandas | 2.2.3 | Reads and manipulates structured data (DataFrame). | Yes |
| Pillow | 11.0.0 | Opens and processes images (PIL.Image). | Yes |
| torch | 2.3.1 | Required for PyTorch model loading and inference. | Yes |
| torchvision | 0.18.1a0 | Provides pre-trained models like ResNet, AlexNet, and VGG. | Yes |
| re  | 2.2.1 | Built-in Python library. | No  |
| os  | No version | Built-in Python library. | No  |
| time | No version | Built-in Python library. | No  |
| ast | No version | Built-in Python library. | No  |

**📂 How the Code Works**

**1️. Running the Classification Script (check_images.py)**

There are **40 images** provided by Udacity in the **Location:** pet_images/

The core of this project is check_images.py, which:

1. **Extracts true pet labels** from the filenames of the 40 images.
2. **Uses a pre-trained CNN** (ResNet, AlexNet, or VGG) to classify images.
3. **Compares the predicted label to the actual pet label.**
4. **Determines if the classified image is a dog or not** using the provided list of breeds dognames.txt.
5. **Generates statistics** on accuracy, including:
    - Percentage of correct classifications
    - Correctly classified dog images
    - Correctly classified non-dog images
    - Accuracy of breed classification
6. **Prints the results** and **saves them in text files**.

**2️. Running All Models Automatically**

You can automate classification for all three CNN models using batch scripts.

**Windows Users:** run_models_batch.bat

**Linux/macOS Users:** sh run_models_batch.sh

This will:

- Run check_images.py **three times** (once per model) for the provided images.
- Save results into:
  - resnet_pet-images.txt
  - alexnet_pet-images.txt
  - vgg_pet-images.txt
- Additionally, this script runs generate_results_chart.py, which takes as input the results from the 3 above txt files and generates a summary image: **results_summary.png**

**3️. Running Custom Tests on Uploaded Images**

You can also test newly uploaded images:

- I added 4 new images under **Location:** uploaded_images/
- **Example images:** A dog (original + horizontally flipped), A non-dog animal and An object.

Run the script for uploaded images:

**Windows Users:** run_models_batch_uploaded.bat

**Linux/macOS Users:** sh run_models_batch_uploaded.sh

This will:

- Run check_images.py **three times** (once per model) for the newly uploaded images.
- Save results into:
  - resnet_uploaded-images.txt
  - alexnet_uploaded-images.txt
  - vgg_uploaded-images.txt

**🛠️ Troubleshooting**

**Common Issues & Fixes**

| **Issue** | **Solution** |
| --- | --- |
| ModuleNotFoundError for a package | Run pip install -r requirements.txt |
| FileNotFoundError: dognames.txt | Ensure you're running from the correct folder |
| OSError: No such file or directory | Use the correct --dir argument |

**📝 License**

This project is based on **Udacity's AI Programming with Python** course. 

MIT License

Copyright (c) 2018 Udacity

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


**🤖 Acknowledgment**

AI assistance was used for explaining concepts, for refining already written code (chiefly adding comments) and for outputting this README but the **code structure, logic, and implementation were independently designed**.