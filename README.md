Location-Based Services Power Optimization

Overview:
This project focuses on optimizing power consumption in location-based services, using a dataset from mobile sensors. The code is structured to perform data analysis, visualization, and machine learning model training. It employs a Multinomial Logistic Regression model to dynamically reduce power consumption based on features such as signal strength and position fixes.

Data: 
Contains the dataset "rerun.csv" for analysis and model training.

data_analysis.ipynb: Explores the dataset, visualizes key features, and analyzes power consumption, accuracy, and signal strength.
classification_model.ipynb: Trains the Multinomial Logistic Regression model and evaluates its accuracy.

Visualizations:
Includes plots showing power consumption by different position technologies, accuracy in meters, signal strength, and the impact of frequency of position fixes on accuracy and power consumption.

Model Training:
The logistic regression model is trained on the dataset, aiming to dynamically optimize power consumption. The accuracy of the model is evaluated using a test set.

Results:
The model achieves an accuracy of 93.95%, showcasing its effectiveness in optimizing power consumption in location-based services.
