# Dlithe_internship_2020

Assignments during Online Internship with DLithe(www.dlithe.com). 

Assignment 1

Theme: Engineering.

Topic: Price prediction of secondhand cars in india.

The data is got from: https://www.kaggle.com/mayankpatel14/second-hand-used-cars-data-set-linear-regression

1. Spyder was used for coding. 

2. The libraries used are Pandas for data collection. Seaborn for Visualisation and data analysis. And sklearn for Machine learning algorithm selection.

3. The process starts with gathering the data from kaggle on secondhand car dataset.

4. Cleansing the data checking for any missing values. Removing the unwanted columns from dataset using drop command is part of data processing.

5. Selecting independent variables in x array i.e on road old, on road now, years, km, rating, condition,economy,top speed, hp, torque. And dependent variables or target variable to y array i.e current price. Since the target variable is continuous Linear Regression is planned to be used for prediction.

6. Split universal dataset to trainset and testset using library sklearn,module:model_selection, class : train_test_split. Test size of 0.3 was used with random state of 350. The train set was named x_train, y_train and test set was assigned as x_test, y_test.

7. Linear regression was used as Algorithm Selection for training and predicting the y_test named as y_pred. Using the Library: sklearn, module : Linear_model, class  : LinearRegression.

8. Checking the accuracy of y_train andy_pred was done using the Library: sklearn, module : metrics, class  : r2score



Assignment 2

Theme: Engineering.

Topic: Predicitng the revenue earned in market from different sales representative for different products in different regions.

The data is got from: https://www.kaggle.com/seetzz/market-segmentation was used for coding.

1. Spyder was used for coding.

2. The libraries used are Pandas for data collection and assigning binary values to categorical attribute. Seaborn for Visualisation and data analysis. And sklearn for Machine learning algorithm selection.

3. The process starts with gathering the data from kaggle.

4. Checking for any missing values. And replace the columns reps, product,region as they are categorical variable into 0 for not the actual variable and 1 for the actual variable. This comprises the data processsing step.

5. Selecting independent variables in x array i.e reps,product,qty,region. And dependent variables or target variable to y array i.e revenue. Since the target variable is continuous Linear Regression is planned to be used for prediction.

6. Split universal dataset to trainset and testset using library sklearn,module:model_selection, class : train_test_split. Test size of 0.3 was used with random state of 2500. The train set was named x_train, y_train and test set was assigned as x_test, y_test.

7. Linear regression was used as Algorithm Selection for training and predicting the y_test named as y_pred. Using the Library: sklearn, module : Linear_model, class : LinearRegression.

8. Checking the accuracy of y_train andy_pred was done using the Library: sklearn, module : metrics, class : r2score
