# AnimalGates: Cat Breed Classification System

## Code Documentation

For detailed code documentation, refer to [Code Documentation](<https://mahsageshvadi.github.io/AnimalGates/AnimalGateCodeDocumentation.pdf>).

## Setup Guide

To set up and run the project, follow the instructions in the [Setup Guide](<https://mahsageshvadi.github.io/AnimalGates/AnimalGateSetupGuide.pdf>).

## Project Overview

The AnimalGates project focuses on developing a system for classifying different cat breeds using a Raspberry Pi and a machine learning model. The system utilizes the Cats and Dogs Breeds Classification Oxford Dataset from Kaggle, which contains both cat and dog breeds. Our goal is to accurately identify and classify cat breeds while eliminating the dog data from the dataset.

## Data Preparation

To facilitate the training process, we implemented a Python script called `prepareData` in `trainModel.py`. This script automatically eliminates dog images and organizes the cat data into separate folders. The prepared data is crucial for training a robust model.

## Model Training

For the classification task, we employed a ResNet model. The `trainModel.py` script trains the model on the preprocessed cat data and provides insights into the training accuracy. The choice of ResNet ensures the model's ability to capture intricate features, leading to better performance in breed classification.

## Model Evaluation

To assess the model's performance, we created the `AnimalGateTesting.ipynb` notebook. This notebook compares the accuracy of our trained ResNet model with pre-existing pretrained models using the same dataset. This step helps validate the effectiveness of our custom model.

## Breed Detection

The `DetectCatModel` component of our system takes an image sample as input and prints the model's classification results to the console. This real-time detection capability is essential for the Animal Gate to make informed decisions based on the identified cat breed.

## How to Use

To replicate our results, follow these steps:

1. Run `prepareData` in `trainModel.py` to organize and preprocess the cat data.
2. Execute `trainModel.py` to train the ResNet model and obtain training accuracy insights.
3. Use the `AnimalGateTesting.ipynb` notebook to compare the performance of our model with pretrained models.
4. Employ the `DetectCatModel` component to perform real-time breed detection on image samples.

