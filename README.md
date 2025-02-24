**🐶 Pet Image Classifier - Udacity AI Programming with Python**

**Project Overview**

This project classifies pet images using a **pre-trained Convolutional Neural Network (CNN)**. It determines whether the images contain dogs and identifies their breeds using three different CNN models: **VGG, AlexNet, and ResNet**. The script compares the model predictions to the actual labels derived from filenames and generates a summary of performance statistics.

The project is structured to run via command-line scripts (.bat for Windows and .sh for Linux/macOS) to ensure automation and reproducibility.

**🏠 Project Structure**

udacity_AIPND_classify_pet_images/

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

**🚀 Installation Guide**

This project was developed using **Python 3.11**. Before proceeding, ensure Python is installed on your system.

Open a terminal and verify your Python version:

python3 --version # macOS/Linux

python --version # Windows

If Python is not installed, download and install it from [python.org](https://www.python.org/).

1. **Clone the Repository**

Open a terminal **(Command Prompt/PowerShell for Windows, Terminal for macOS/Linux)** and navigate to the directory where you want to clone the repository (e.g., Downloads):

cd ~/Downloads # macOS/Linux

cd %USERPROFILE%\\Downloads # Windows

Clone the repository:

git clone <https://github.com/cvasilov1/udacity_AIPND_classify_pet_images.git>

Move into the project folder:

cd udacity_AIPND_classify_pet_images

**📝 Note for Git Bash** **users:**

Git Bash behaves similarly to macOS/Linux when running commands. If you are using **Git Bash on Windows**, generally follow the macOS/Linux commands, not the Windows-specific ones.

2. **Set Up a Virtual Environment & Install Dependencies**

You can set up your environment in two ways: Python Virtual Environment (venv) or Anaconda (conda).

**🔹 Option 1: Using Python's Built-in Virtual Environment (venv)**

For users not using Anaconda:

➡ **macOS/Linux (from Terminal)**

python3 -m venv pet_env # Create virtual environment

source pet_env/bin/activate # Activate virtual environment

pip install -r requirements.txt # Install dependencies

pip list # Verify installed packages

➡ **Windows (from Command Prompt/PowerShell)**

python -m venv pet_env # Create virtual environment

pet_env\\Scripts\\activate # Activate virtual environment

pip install -r requirements.txt # Install dependencies

pip list # Verify installed packages

**🔹 Option 2: Using Anaconda (from the Anaconda Prompt)**

conda create --name pet_env python=3.11 -y # Create virtual environment specifying the Python version

conda activate pet_env # Activate virtual environment

conda install --file requirements.txt # Install dependencies from Conda

conda list # Verify installed packages

**📝 Note for Git Bash** **users:**  

For Windows: Git Bash behaves like macOS/Linux, so use **source pet_env/bin/activate** instead of the Windows activation command.

For Anaconda: Git Bash supports conda activate, but you might need to enable it first with: **conda init bash**

| Library       | Version  | Purpose  | Installation Required? |
|--------------|---------|----------|------------------------|
| matplotlib   | 3.10.0  | Generates plots and saves images. | Yes |
| numpy        | 1.26.4  | Supports numerical operations. | Yes |
| pandas       | 2.2.3   | Reads, processes, and manipulates structured data. | Yes |
| Pillow       | 11.0.0  | Handles image loading and manipulation. | Yes |
| torch        | 2.6.0^  | Provides PyTorch functionality. | Yes |
| torchvision  | 0.21.0^^ | Supplies pre-trained models (ResNet, VGG, AlexNet). | Yes |
| argparse     | 3.10.0  | Built-in command-line argument parser (--dir, --arch, etc.). | No (Built into Python) |
| re          | 2.2.1   | Used for handling regular expressions (e.g., pattern matching). | No (Built into Python) |
| os          | N/A     | Provides OS-related functions (e.g., file path handling). | No (Built into Python) |
| time        | N/A     | Used for measuring execution time and implementing delays. | No (Built into Python) |
| ast         | N/A     | Supports parsing and analyzing Python expressions safely. | No (Built into Python) |

^The project used torch==2.3.1 for development.
^^The project used torchvision==0.18.1a0 for development.

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

AI assistance was used for explaining concepts, for refining already written code (chiefly adding comments) and for outputting this README but the **code structure, logic, and implementation were independently designed by cvasilov1**.
