# Credit Risk Analysis for peer to peer lending firm Bandora
The credit risk is analyzed to measure the possibility of loss as result of borrower failing to repay a loan or meeting the loan obligations. The more the credit risk the more it has a negative impact on performance of bank. The credit risk analysis is important because it allows the bank to plan strategies to avoid a negative outcome ahead in future.
- In this project we analyzed the credit risk on individual loans, maximizing the Return on Investment (ROI) by predicting an Eligible Loan Amount and minimizing the financial risk between the lending firm Bandora and the borrowers.

## Understanding the Dataset
Data for the study has been retrieved from a publicly available data set of a leading European P2P lending platform  ([**Bondora**](https://www.bondora.com/en/public-reports#dataset-file-format))

- The dataset contains the individual loan details from **2009** to **2019** having both the **defaulted** and **non-defaulted** loans
- The dataset does not contain any target attributes for 
- - defaulted, non-defauted classes
- - Eligible Loan Amount (ELA)
- - Return on Investment (ROI)
- - Equated Monthly Installment (EMI) 
- These 4 target attributes will be created using feature engineering

The dataset has 112 attributes intially. The attributes definition of dataset can be found here ([**Data Understanding**](https://drive.google.com/file/d/1l9YjhV4IRDHCohIDsRGKL9ADNTPaVA69/view?usp=sharing)), it will help you understand the dataset better.

## Preprocessing
As the dataset is not clean, so preprocessing techniques were used to clean the dataset and make it ready for Exploratory Data Analysis (EDA).
- The attributes having greater than 40% missing values were filtered out.
- There are some features which have no role in targets, so they are also removed:
- - 'ReportAsOfEOD', 'LoanId', 'LoanNumber', 'ListedOnUTC', 'DateOfBirth' (because age is already present), 'BiddingStartedOn','UserName','NextPaymentNr','NrOfScheduledPayments','IncomeFromPrincipalEmployer', 'IncomeFromPension', 'IncomeFromFamilyAllowance', 'IncomeFromSocialWelfare','IncomeFromLeavePay', 'IncomeFromChildSupport', 'IncomeOther' (As Total income is already present which is total of all these income), 'LoanApplicationStartedDate','ApplicationSignedHour', 'ApplicationSignedWeekday','ActiveScheduleFirstPaymentReached', 'PlannedInterestTillDate', 'LastPaymentOn', 'ExpectedLoss', 'LossGivenDefault', 'ExpectedReturn', 'ProbabilityOfDefault', 'PrincipalOverdueBySchedule', 'StageActiveSince', 'ModelVersion','WorseLateCategory'


## EDA
**Introduction:**

- **merged_data** dataset comprises of 1989 rows and 57 columns.
- Dataset comprises of continious variable and float data type. 
- Dataset column varaibales 'Open', 'Close', 'High', 'Low', 'Volume', 'Adj Close' are the stock variables from historical dataset and other variables are showing polarity and subjectivity of news which are the derived variables using sentiment analysis as discussed in above section.

**Information of Dataset:**

Using countplot on target variable **Label** we could see that Label 0 has '924' values and Label 1 has '1065'. By this information we could conclude that there is no imbalanced in the data and hence balancing of data is not required.

**Univariate Analysis:**

Plotted histogram to see the distribution of data for each column and found that few variables are normally distributed. However, we can't really say about that which variables needed to be studied. Since, Subjectivity and polarity variable are derived ones and other historical stock variables required to sudy more that how they are related to each oyher.

**Descriptive Statistics:**

Using **describe()** we could get the following result for the numerical features

||Open|Close|High|Low|Volume|Adj Close|
| :-- |:---------------:| -----:|-------:|:---------------:| -----:|------:|
|count|1989.000000|1989.000000|1989.000000|1989.000000|1.989000e+03|1989.000000|
|mean|13459.116049|13463.032255|13541.303173|13372.931728|1.628110e+08|13463.032255|
|std|3143.281634|3144.006996|3136.271725|3150.420934|9.392343e+07|3144.006996|
|min|6547.009766|6547.049805|6709.609863|6469.950195|8.410000e+06|6547.049805|
|25%|10907.339840|10913.379880|11000.980470|10824.759770|1.000000e+08|10913.379880|
|50%|13022.049810|13025.580080|13088.110350|12953.129880|1.351700e+08|13025.580080|
|75%|16477.699220|16478.410160|16550.070310|16392.769530|1.926000e+08|16478.410160|
|max|18315.060550|18312.390630|18351.359380|18272.560550|6.749200e+08|18312.390630|

**Correlation Plot of Numerical Variables:**

All the continuous variables are positively correlated with each other with correlation coefficient of 1 except **Volume** which has negative correlation of around 0.7 with all other variables

**Visualisation of Variables:**

- For a particular day, the opening and closing cost does not have much difference.
- Upon plotting box plot between **Volume** and **Label** we could see that there are outliers. Other numnerical features doesnot have any outliers in them.
- Observed outliers in few categorical columns as well.
 
 
## Preprocessing Again

Now, after observing the outliers in **polarity** of a lot of topics, we decided to concatenate all the 25 topics in one paragraph,
then we can get only one column for **polarity** and one for **subjectivity**.

So, we merged these data again with the stock market numerical information and got **merged_data2** dataframe, then scaled it.


## Model Building

#### Metrics considered for Model Evaluation
**Accuracy , Precision , Recall and F1 Score**
- Accuracy: What proportion of actual positives and negatives is correctly classified?
- Precision: What proportion of predicted positives are truly positive ?
- Recall: What proportion of actual positives is correctly classified ?
- F1 Score : Harmonic mean of Precision and Recall

#### Logistic Regression
- Logistic Regression helps find how probabilities are changed with actions.
- The function is defined as P(y) = 1 / 1+e^-(A+Bx) 
- Logistic regression involves finding the **best fit S-curve** where A is the intercept and B is the regression coefficient. The output of logistic regression is a probability score.

#### Random Forest Classifier
- The random forest is a classification algorithm consisting of **many decision trees.** It uses bagging and features randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.
- **Bagging and Boosting**: In this method of merging the same type of predictions. Boosting is a method of merging different types of predictions. Bagging decreases variance, not bias, and solves over-fitting issues in a model. Boosting decreases bias, not variance.
- **Feature Randomness**:  In a normal decision tree, when it is time to split a node, we consider every possible feature and pick the one that produces the most separation between the observations in the left node vs. those in the right node. In contrast, each tree in a random forest can pick only from a random subset of features. This forces even more variation amongst the trees in the model and ultimately results in lower correlation across trees and more diversification.

#### Linear Discriminant Analysis
- Linear Discriminant Analysis, or LDA, uses the information from both(selection and target) features to create a new axis and projects the data on to the new axis in such a way as to **minimizes the variance and maximizes the distance between the means of the two classes.**
- Both LDA and PCA are linear transformation techniques: LDA is supervised whereas PCA is unsupervised – PCA ignores class labels. LDA chooses axes to maximize the distance between points in different categories.
- PCA performs better in cases where the number of samples per class is less. Whereas LDA works better with large dataset having multiple classes; class separability is an important factor while reducing dimensionality.
- Linear Discriminant Analysis fails when the covariances of the X variables are a function of the value of Y.


### Choosing the features
After choosing LDA model based on confusion matrix here where **choose the features** taking in consideration the deployment phase.

We know from the EDA that all the features are highly correlated and almost follows the same trend among the time.
So, along with polarity and subjectivity we choose the open price with the assumption that the user knows the open price but not the close price and wants to figure out if the stock price will increase or decrease.

When we apply the **logistic regression** model the accuracy dropped from 80% to 55%.
When we apply **random forest** model the accuracy dropped from 71% to 62%.
When we apply **linear discriminate analysis** the accuracy dropped from 92% to 79%.

So, we will use both **Open** and **Close** and exclude **High,	Low, Volume, Adj Close**.
```
merged_data2 = merged_data2[['Label', 'polarity', 'subjectivity', 'Open', 'Close']]
```
#### 1. Applying Linear Discriminant Analysis on the Selected Features
Now, we splitted the new data to train of 80% and validation of 20%, then scaled them using **StandardScaler**, too.

By applying LDA on the selected features, the accuracy got from the confusion matrix increased to 93%.


#### 2. Applying XG Boost Classifier on the Selected Features
By applyying the XGBoost Classifier on the selected features, we got an accuracy of 82%


Now, we will apply PCA transformation without scaling the data.

### PCA transformation
We reduced the 4 features to be only 3.
~~~
from sklearn.decomposition import PCA

pca = PCA(n_components=3)
pca.fit(X_train2)
trained = pca.transform(X_train2)
transformed = pca.transform(X_valid2)
~~~

#### 1. Applying Linear Discriminant Analysis on PCA columns
By applying LDA on the 3 PCA columns, the accuracy got from the confusion matrix remained as 93%.

#### 2. Applying XG Boost Classifier on PCA columns
By applying XGBoost Classifier on the 3 PCA columns, with n_estimators=500, and max_depth=3, 
the accuracy got from the confusion matrix became 98%.


## Deployment
you can access our app by following this link [stock-price-application-streamlit](https://stock-price-2.herokuapp.com/) or by click [stock-price-application-flask](https://stock-price-flask.herokuapp.com/)
### Streamlit
- It is a tool that lets you creating applications for your machine learning model by using simple python code.
- We write a python code for our app using Streamlit; the app asks the user to enter the following data (**news data**, **Open**, **Close**).
- The output of our app will be 0 or 1 ; 0 indicates that stock price will decrease while 1 means increasing of stock price.
- The app runs on local host.
- To deploy it on the internt we have to deploy it to Heroku.

### Heroku
We deploy our Streamlit app to [ Heroku.com](https://www.heroku.com/). In this way, we can share our app on the internet with others. 
We prepared the needed files to deploy our app sucessfully:
- Procfile: contains run statements for app file and setup.sh.
- setup.sh: contains setup information.
- requirements.txt: contains the libraries must be downloaded by Heroku to run app file (stock_price_App_V1.py)  successfully 
- stock_price_App_V1.py: contains the python code of a Streamlit web app.
- stock_price_xg.pkl : contains our XGBClassifier model that built by modeling part.
- X_train2.npy: contains the train data of modeling part that will be used to apply PCA trnsformation to the input data of the app.

### Flask 
We also create our app   by using flask , then deployed it to Heroku . The files of this part are located into (Flask_deployment) folder. You can access the app by following this link : [stock-price-application-flask](https://stock-price-flask.herokuapp.com/)

