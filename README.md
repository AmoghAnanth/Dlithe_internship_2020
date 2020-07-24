# Dlithe_internship_2020
Assignment during Online Internship with DLithe(www.dlithe.com). 
Theme: Engineering.
Topic: Price prediction of secondhand cars in india.
The data is got from: https://www.kaggle.com/mayankpatel14/second-hand-used-cars-data-set-linear-regression

1. Spyder was used for coding. 

2. The libraries used are Pandas for data collection. Seaborn for Visualisation and data analysis. And sklearn for Machine learning algorithm selection.

3. The process starts with gathering the data from kaggle on secondhand car dataset.

4. Cleansing the data checking for any missing values. Removing the unwanted columns from dataset using drop command.
5. Selecting independent variables in x array. And dependent variables or target variable to y array. Since the target variablre is continuous Linear Regression is planned to be used for prediction.
6. Split universal dataset to trainset and testset using library sklearn,module:model_selection, class : train_test_split. Test size of 0.3 was used with random state of 350. The train set was named x_train, y_train and test set was assigned as x_test, y_test.
7. Linear regression was used as Algorithm Selection for training and predicting the y_test named as y_pred. Using the Library: sklearn, module : Linear_model, class  : LinearRegression.
8. Checking the accuracy of y_train andy_pred was done using the Library: sklearn, module : metrics, class  : r2score
