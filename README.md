# **CropChain - Predicting Crop Yields Using Machine Learning**

**CropChain** is an end-to-end machine learning pipeline designed to predict crop yields efficiently by leveraging modern data science techniques. This project demonstrates how to integrate data processing, model training, and deployment to deliver actionable insights that enhance agricultural productivity.

## **Table of Contents**

- [**CropChain - Predicting Crop Yields Using Machine Learning**](#cropchain---predicting-crop-yields-using-machine-learning)
  - [**Table of Contents**](#table-of-contents)
  - [**Project Overview**](#project-overview)
  - [**Folder Structure**](#folder-structure)
  - [**Key Features**](#key-features)
  - [**Setup and Installation**](#setup-and-installation)
  - [**How to Run**](#how-to-run)
  - [**Usage**](#usage)
  - [**Results**](#results)
  - [**License**](#license)
  - [**Support 💬**](#support-)
  - [**Acknowledgments 🙏**](#acknowledgments-)

## **Project Overview**
CropChain is designed to assist farmers, agronomists, and researchers in predicting crop yields using historical and environmental data. The project integrates key components like data preprocessing, machine learning model training, and a web-based deployment using Flask.

## **Folder Structure**

```                  
 crops/
    ├── data/
    │   ├── labeled/            # Labeled data for model training
    │   ├── processed/          # Preprocessed data for model input
    │   └── raw/                # Raw data files
    ├── deployment/             
    │   ├── __init__.py         # Initialization file for deployment
    │   └── app.py              # stremlit app for deployment
    ├── models/                 # Saved machine learning models
    ├── notebook/
    │   ├── data_analysis.ipynb # Jupyter notebook for data exploration and analysis
    │   ├── data_preprocessing.ipynb  # Data preprocessing steps
    │   └── model_training.ipynb      # Model training process
    ├── scripts/
    │   ├── __init__.py         # Initialization for scripts module
    │   ├── data_preprocessing.py  # Python script for data cleaning and processing
    │   ├── flask_pre.py        # Flask app for deployment
    │   ├── plotting.py         # Functions for plotting data and results
    │   ├── prediction.py       # Script for making predictions
    │   └── train.py            # Script for training the machine learning model
    ├── tests/                  # Unit and integration tests
    └── utils/                  # Utility functions and scripts
    ├── .gitignore                  # Files and directories to ignore in version control
    ├── Dockerfile                  # Docker configuration for containerizing the application
    ├── LICENSE                     # Project license
    ├── README.md                   # This readme file
    ├── requirements.txt            # Python dependencies
```

## **Key Features**
- **Data Preprocessing:** Handles raw data, cleaning, labeling, and preprocessing for model training.
- **Model Training:** Uses machine learning algorithms to train a model for crop yield prediction.
- **Visualization Tools:** Plotting scripts for visualizing the data and prediction results.
- **Web Deployment:** Deploys the model using a Flask web application for real-time predictions.
- **Scalable Deployment:** Easily deployable via Docker to ensure scalability and environment consistency.

## **Setup and Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cropchain.git
   cd cropchain
   ```

2. **Install dependencies:**

   It is recommended to use [Pipenv](https://pipenv.pypa.io/en/latest/) or a virtual environment. To install required packages, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Using Docker:**

   To run the project using Docker, build the Docker image:

   ```bash
   docker build -t crop_app .
   ```

   Then, run the container:

   ```bash
   docker run -p 9696:9696 crop_app
   ```

## **How to Run**

1. **Data Preprocessing:**
   
   To preprocess the data, use the `data_preprocessing.py` script:

   ```bash
   python scripts/data_preprocessing.py
   ```

2. **Model Training:**

   Train the machine learning model using the `train.py` script:

   ```bash
   python scripts/train.py
   ```

3. **Run the Flask or streamlit App:**

   Deploy the web app for real-time predictions:

   ```bash
   python deployment/streamlit run app.py
   ```
  The application will run on [http://localhost:8501](http://localhost:8501).
  
   ```
   docker run -it --rm -p 9696:9696 crop_app:latest
   ```

   The application will run on [http://localhost:9696](http://localhost:9696).

## **Usage**

- Use the web interface to input environmental data and predict crop yields.
- The notebooks in the `notebook` folder can be used to explore and analyze the data or fine-tune the model further.
- Use the provided plotting scripts to visualize data trends and model performance.

## **Results**
- Best Model: RandomForestRegressor
- R^2 score: 0.943
- MSE score: 0;001
- MAE score: 0.018


## **License**

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
## **Support 💬**
If you encounter any issues or have questions, feel free to open an issue in the repository or contact me at [aarongebremariam.94@gmail.com](Email)

## **Acknowledgments 🙏**
- Scikit-learn for machine learning algorithms.
- Flask for the web framework.
- Docker for containerization.



