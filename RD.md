- Key questions asked and answered of the data are shared in the final report notebook.
    Key Questions: 'What are the key question'
    





- You should ask questions of the data using natural language that speaks to the business stakeholders
in markdown cells, ideally a header prior to the visualization or statistical test, that you then explore. 
    - This does not take the place of stating your null hypothesis/alternative hypothesis when doing a statistical test, 
    but those hypotheses are generally for you. By writing questions that you intend to answer with visualizations and statistical tests in natural language, like 'Are office supplies leading to differences in profit in Texas?', you are able to guide both yourself and your reader through the highlights of your analysis. You ask a question, create a visual, run a statistical test (if appropriate), and wrap it nicely with a markdown cell that contains a clear answer in layman's terms. 






- You do all that before moving to the next question.



Viz's/tests wrapped in a formed Q & A
6 pts
Y
ou called out at least four of the questions you asked of the data and 
provided a clear answer using natural language in markdown cells in your final report.





------------------------------------

Pipeline breakdown

# Define the problem: The problem is to predict the property tax assessed values of single family properties that had a transaction during 2017. Additionally, we need to identify the states and counties where these properties are located.

# Collect and preprocess the data: The first step is to collect the data on single family properties that had a transaction during 2017, along with their property tax assessed values. We also need to identify the states and counties where these properties are located. Once the data has been collected, we need to preprocess it by cleaning the data, dealing with missing values and outliers, and performing feature engineering to create new variables that may be useful in predicting property tax assessed values.

# Explore the data: Next, we can perform exploratory data analysis (EDA) to gain insights into the data and identify any patterns or trends. This could involve visualizing the data, identifying correlations between variables, and identifying any outliers or anomalies in the data.

# Feature engineering: Based on the insights gained from EDA, we can create new features from the existing variables that may improve the model's performance. For example, we could create a feature that calculates the distance to the nearest school, or a feature that calculates the average income in the property's neighborhood.

# Model selection: Once the data has been preprocessed and the features have been engineered, we can begin building and testing models to predict property tax assessed values. We could try a variety of models, such as linear regression, decision trees, random forests, and neural networks. We could also try using non-linear regression algorithms or ensemble methods to improve the model's performance.

# Model evaluation: Once we have built and trained the models, we can evaluate their performance using metrics such as root mean squared error (RMSE) or R-squared. We can compare the performance of different models and select the one that performs best on our data.

# Deployment: Finally, once we have selected a model that performs well, we can deploy it in a production environment to make predictions on new data.

# Identify states and counties: To identify the states and counties where these properties are located, we can use the information available in the dataset, such as zip codes or addresses, and cross-reference it with a database of U.S. counties and states. Alternatively, we could use a geocoding API to convert the addresses to latitude and longitude coordinates and then identify the states and counties based on those coordinates.


