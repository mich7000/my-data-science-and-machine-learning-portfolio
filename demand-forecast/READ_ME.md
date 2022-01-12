<h3>Demand  Forecast for the next (3) months of sales.</h3>

**Overview**

This machine learning project was to  build a model to forecast the sales of items for the next (3) months period.

Here I did not use any of the **parametric** method of time series forecast, I used the **non-parametric** method that is the use of supervised machine learning algorithms. i formulated the time series problem as a regression problem and used a regression model to make the next (3) months sales forecast.

I used the **Light Gradient Boosted Machine** because is fast in computation and also more accurate than the traditional machine learning models, because it used gradient descents to boosted trees to corrects itself, therefore improving models performance in a  whole.





**Data**

The data was collected from kaggle datasets (it was part of a data science competion which was organized in 2018)

The data contains 5 years of store-item sales data, and I have been asked to predict the 3 months of sales for 50 diffrent items at 10 different stores.



**Data Description**

The objective of this competition is to predict 3 months of item-level sales data at different store locations.

*File descriptions*

```python
train.csv - Training data
test.csv - Test data (Note: the Public/Private split is time based)
sample_submission.csv - a sample submission file in the correct format
```

*Data fields*

```python
date - Date of the sale data. There are no holiday effects or store closures.
store - Store ID
item - Item ID
sales - Number of items sold at a particular store on a particular date.
```



**Tools and Methodology**

Tools: Python - Anaconda distribution with Jupyter notebook, pandas, numpy, pyplot, sci-kit learn etc.

Methods:

- Data loading and inspection
- Data cleaning 
- Missing value handling
- Feature engineering creation
- Model fiting 
- Model evaluation and selection
- Tuning of best model
- Forecasting with the best model.
- model serialization





