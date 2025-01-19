#!/bin/bash

# Step 1: Download Miniconda3
echo "Downloading Miniconda3..."
MINICONDA_INSTALLER=Miniconda3-latest-Linux-x86_64.sh
curl -O https://repo.anaconda.com/miniconda/$MINICONDA_INSTALLER

# Step 2: Install Miniconda3
echo "Installing Miniconda3..."
bash $MINICONDA_INSTALLER -b -p $HOME/miniconda3

# Step 3: Initialize Miniconda
echo "Initializing Miniconda..."
$HOME/miniconda3/bin/conda init

# Step 4: Update conda to the latest version
echo "Updating Conda..."
$HOME/miniconda3/bin/conda update -y conda

# Step 5: Create a new conda environment (Optional)
# Replace 'myenv' with your desired environment name
echo "Creating a conda environment..."
$HOME/miniconda3/bin/conda create -y -n myenv python=3.11

# Step 6: Activate the environment
echo "Activating the environment..."
source $HOME/miniconda3/bin/activate myenv

# Step 7: Install dependencies from requirements.txt
echo "Installing packages from requirements.txt..."
pip install -r requirements.txt

# Step 8: Run the server
echo "Running the server..."
python app.py

# End of script
echo "Server started."
