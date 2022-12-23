# Credit Risk Analysis for peer to peer lending firm Bandora
The credit risk is analyzed to measure the possibility of loss as result of borrower failing to repay a loan or meeting the loan obligations. The more the credit risk the more it has a negative impact on performance of bank. The credit risk analysis is important because it allows the bank to plan strategies to avoid a negative outcome ahead in future.
- In this project we analyzed the credit risk on individual loans, maximizing the Return on Investment (ROI) by predicting an Eligible Loan Amount and minimizing the financial risk between the lending firm Bandora and the borrowers.

## Understanding the Dataset
Data for the study has been retrieved from a publicly available data set of a leading European P2P lending platform  ([**Bondora**](https://www.bondora.com/en/public-reports#dataset-file-format))

- The dataset contains the individual loan details from **2009** to **2019** having both the **defaulted** and **non-defaulted** loans
- The dataset does not contain any target attributes for 
  - defaulted, non-defauted borrowers
  - Eligible Loan Amount (ELA)
  - Return on Investment (ROI)
  - Equated Monthly Installment (EMI) 
- These 4 target attributes will be created using feature engineering

The dataset has 112 attributes intially. The attributes definition of dataset can be found here ([**Data Understanding**](https://drive.google.com/file/d/1l9YjhV4IRDHCohIDsRGKL9ADNTPaVA69/view?usp=sharing)), it will help you understand the dataset better.

## Preprocessing
As the dataset is not clean, so preprocessing techniques were used to clean the dataset and make it ready for Exploratory Data Analysis (EDA).
- The attributes having greater than 40% missing values were filtered out.
- There are some features which have no role in targets, so they are also removed:
  - 'ReportAsOfEOD', 'LoanId', 'LoanNumber', 'ListedOnUTC', 'DateOfBirth' (because age is already present), 'BiddingStartedOn','UserName','NextPaymentNr','NrOfScheduledPayments','IncomeFromPrincipalEmployer', 'IncomeFromPension', 'IncomeFromFamilyAllowance', 'IncomeFromSocialWelfare','IncomeFromLeavePay', 'IncomeFromChildSupport', 'IncomeOther' (As Total income is already present which is total of all these income), 'LoanApplicationStartedDate','ApplicationSignedHour', 'ApplicationSignedWeekday','ActiveScheduleFirstPaymentReached', 'PlannedInterestTillDate', 'LastPaymentOn', 'ExpectedLoss', 'LossGivenDefault', 'ExpectedReturn', 'ProbabilityOfDefault', 'PrincipalOverdueBySchedule', 'StageActiveSince', 'ModelVersion','WorseLateCategory'
- As no time series analysis is involved in our project, so some attributes involving date-time are removed:
   - 'LoanDate', 'FirstPaymentDate','MaturityDate_Original','MaturityDate_Last','LastPaymentOn'
   - note that attribute 'DefaultDate' is not removed, because it contains the default date for those borrowers who defaulted and - for those borrowers who didn't default. This attribute will help us in creating the our 1st target attribute (defaulted, non-defauted borrowers).
-  There are some attributes in numeric form in the dataset but they are actually categorical attributes as per data description such as :
   -  Verification Type, Language Code, Gender, Use of Loan, Education, Marital Status,EmployementStatus, OccupationArea, 
   - These attributes are converted to categorial type by using the respective attribute definition, to make these variables correct for Exploratory Data Analysis (EDA).
   - Like for Gender attribute replacing [0,1,2] by ["Male","Woman","Undefined"] as per attribute definition of Gender.
   - When the data distribution is checked for these attributes, there are some unreplacable values like :
      - 22, 15, 10, 13, 7, 21 in 'LanguageCode' attribute.
      - -1 in 'UseOfLoan'
      -  0, -1 in 'Education'
      - -1 in 'MaritalStatus'
      - -1, 0, 6 in 'EmploymentStatus'
      - -1, 0 in 'OccupationArea'
      - -1 in 'HomeOwnershipType'

- To perform the Credit Risk Analysis, We need to create the 4 Target attributes, 1 for Classification and 3 for Regression
  1) For Classification, we need to create a Default/non-Default binary class Target attribute:
    - Here, status is the variable which help us in creating target variable. The reason for not making status as target variable is that it has three unique values current, Late and repaid. There is no default feature but there is a feature default date which tells us when the borrower has defaulted means on which date the borrower defaulted. So, we will be combining Status and Default date features for creating target variable.The reason we cannot simply treat Late as default because it also has some records in which actual status is Late but the user has never defaulted i.e., default date is null. So we will first filter out all the current status records because they are not matured yet they are current loans.
    - The Status attribute consists of three classes : Current, Late, Repaid
    - So filtering out those rows in dataset where status is either Late or Repaid
    - Creating a new variable DefaultTarget, by assigning 1 to those rows where there is a value for defaultDate attribute and 0 to other.
    - It means those borrowers having default date belong to defaulted class in our target attribute
  2) **For Regression, we need to calculate Equated Monthly Installment, Eligible Loan Amount (ELA), Return On investment ROI (Risk to get profit)**
    - The **EMI** is calculated based on the following mathematical formula: **EMI = P × r × (1 + r) ^ n / ((1 + r) ^ n – 1)**
      - Where P = Loan amount. "Amount", r = Rate of interest, which is calculated on a monthly-basis-Interest, n = Loan tenure (in months).
  3) **Eligible Loan Amount**, ELA = Assets (Income) - Liabilities of the borrower
    - **Assets**:
      -  **FreeCash** = ELA
      -   **TotalIncome** - **LiabilitiesTotal** = ELA
      -   Under Concsideration, Eligible Loan Amount means, with respect to a Mortgage Loan that is an Eligible Loan, the lesser of:
        - the Principal Balance of such Eligible Loan, AppliedAmount
        - the Market Value of such Eligible Loan PurchasePrice | BidPrinciple
    -  **Approach Followed :**
        - Calculate AppliedAmount + AppliedAmount*Interest = Total Liabilities Amount
        - Divide by the loan tenure (months)
        - If the result is less than (TotalIncome- LiabilitiesTotal)*30/100
        - Then allow the Applied Amount, If not allow only the result of the previous calculation.
  4) **Preferred ROI**
    - We weren't able to determine the procedure of handling Risk related to loan in order to determine Preferred ROI.
    - In order to complete the task in hand and complete it, we'll calculate ROI instead : 
      - **ROI = Investment Gain / Investment Base**
      - **ROI = Amount lended * interest/100**



## Data Wrangling
Using the techniques of data wrangling, errors were removed, gaps in the dataset were indentified, the data imputation was done to make the data ready for Exploratory Data Analysis (EDA).
- Incorrect data entry is checked for the categorical attributes.
  - City and County
    - Upon exploring the city attribute and checking the distribution
    - The two major cities with counts are Tallinn : 6467 , TALLINN : 5395
    - As we can see these two cities are same, so typing error exists in our dataset.
  - By removing the trailing space (_*) and converting to lower case, the inconsistent data entry is corrected.
- Columns with missing values are indentified:
  - VerificationType 0.058 %, Gender 0.058 %, MonthlyPayment 8.56 %, County 26.5 %, City 6.51 %, Education 0.058 %
  - MaritalStatus 0.058 %, EmploymentStatus 0.25 %, EmploymentDurationCurrentEmployer 1.12 %, OccupationArea 0.11 % 
  - HomeOwnershipType 2.13 %, DebtToIncome 0.058 %, FreeCash 0.05 %, Rating 3.52 %, CreditScoreEsMicroL 33.83 %
  - PreviousRepaymentsBeforeLoan 24.95 %
- Data Imputation
  - The missing values are imputed with different approach for numerical and categorical attributes.
    - After checking the distribution of numerical attributes, it is observed that majority of attributes have highly skewed distribution
    - So to replace the missing values, the median of respective attribute is used instead of mean() because for skewed attributes, we don't use mean() for imputation
    - The missing values in categorical attributes are imputed with the mode() of respective attributes.

## Exploratory Data Analysis
**Introduction:**

- The dataset after data wrangling comprises of 77394 rows and 41 features and 4 targets.
- Dataset comprises of int, float and object data types. 
- In EDA, three type of analysis are performed
  - Univariate Analysis
  - Bivariate Analysis
  - Multivariate Analysis

**Univariate Analysis:**
- In univaraite analysis, each feature is analyzed and explored individually to get hidden insights into it.
- The categorical features are analyzed and explored using Seaborn countplot. The countplot is like an histogram for categorical attributes
- The numerical features are analyzed and explored using Seaborn kdeplot and Displot
- A custom function was coded to calculate the percentage_of_top_n_classes of any categorical column given the n and the column's data
- **The Final Observations are :**
  - The 53.6% customers have 'income and expenses verified' followed by 33.11% customers having 'income unverified'. And the remaining percentages include customers having 'income verified','income unverified, cross-referenced by phone','not set'
  - 66% percent customers are 'male', followed by 27% 'female' and remaining 7% undefined
Majority of loan applicants are male
  - Majority of customers have 'MonthlyPayment' between 0 and 350
  - There is great diversity for County feature.
    - 38% customers have county 'Harju maakond', followed by 10% having 'HARJU' as county.
    - No hard insights can be taken from such diverse feature
  - There is great diversity for City feature similar to County feature.
    - Customers belong to 5438 unique cities.
    - only 15% customers are from 'Tallin' city, Other cities have very low percentages of customers
    - No hard insights can be taken from such diverse feature
  - Majority of customers have secondary education (37%), followed by 'higher education' with 27% customers.A very low no of customers have undefined education
  - 57.15% of customers have undefined marital status, followed by 14.86 % customers who are single, then 12.38% customers who are married and 10.96% customers who are cohabitant.A very small % of customers are divorced (3.98) and widow (0.67).
  - Major distribution include 59.53% of customers with undefined employment status, followed by 35.29% customers who are 'fully employed'. A small 8 % of customers have one of these status ; entrepneur, retireee, self employed and partially employed.
  - Major distribution include 39.02% of customers with 'more than 5 years' duration, followed by 18.46% customers who have duration of 'up to 1 year' and 17.8% having 'up to 5 years' duration. The remaining % of customers have one of these duration ; 'up to 2 years', 'up to 3 years', 'retiree', 'other' ' up to 4 years' and 'trail period'.
  - Major distribution include 33.91% customers who are 'owner' followed by 21.76% having 'tenant, pre-furnished property', 16.51% who are 'living with parents' and 11.32% who have 'mortgage'.The remaining % of customers lie among 'other', 'joint ownership', 'joint tenant' etc
  - Major distribution of customers lie between 0 and 70 DebtToIncome range. A less percentage of customers also have DebtToIncome up to 200.
  - Major distribution of customers have 0 freecash, followed by some percentages having around 250 to 300. A less percentage of customers also have freecash up to 158748 approx.
  - The major distribution of Rating is that 23% customers have rating 'f', 16% have 'hr' rating, '15% have 'e', 15% have 'd' followed by 13% having 'c'.
  - The major distribution of this attrbute is such that 84.5% customers have no creditscoreesmicroL. Only 5.32 % have m1 score, 3% have m5, 2 % have m2 and another 2% have m3 score.
  - 63.14% customers are new Credit Customers. 36.86% of customers are existing Credit Customers.
  - The majority of customers have BidsPortfolioManger in range of 0 and 3000.
  - The major percent of customers have age aroung 23 to 60 years.
  - The major percent of customers have LoanDuration of 60 and around 36 months.
  - The major ExistingLiabilities of customer are in range of 0 and 12.
  - Majority of Customers have 0 RefinanceLiabilities, with some having up to 25.
  - The customers have MonthlyPaymentDay high in number at 1st day,10th day, 15th day and overall the distribution is spread along the month.
  - Majority of customers have no NoOfPreviousLoansBeforeLoan, followed some having up 24 no of previous loans.
  - PreviousEarlyRepaymentsCountBeforeLoans for customer is in higher percentage at 0 value while some having up to 11 value.
  - The Defualted customers are more in number than undefualted customers. The defualted ones are more than 40k and undefaulted are around 35k
  - Major % of customers have 0 BidsApi, while some have up to around 7500.
  - BidsManual attriute has major customers in 0 to 1500 range.
  - No of customers who applied for less amounts are more than such customers who applied for normal aur high amounts.
  - The Amount borrower received has same distribution as AppliedAmount the borrower applied for.
  - The major distribution of Max interest rate accepted is between 0 and 70 as clear from Interest plot.
  - The MonthlyPayment has more density from 0 to 400 range.  
  - The incomeTotal has major of customers lying in range 0 to 3000.
  - The DebtToIncome attribute has more customers in range 0 to around 65.
  - Majority of customer have 0 freecash while some customers have upto around 160000.
  - The PrincipalPaymentsMade are more in range 0 to 4000.
  - InterestAndPenaltyPaymentsMade are more in range 0 to 3000.
  - High % customers have principalbalance in range of 0 to 4000.
  - InterestAndPenaltyBalance has more customers in range 0 to 9000.
  - More customers have AmountOfPreviousLoansBeforeLoan in range 0 to 15000.
  - PreviousRepaymentsBeforeLoan have high customers density in range 0 5000.
  
**Bivariate Analysis:**
- In bivaraite analysis, the features are analyzed and explored with respect to each other to get hidden insights into the relation of different featuers
- The correlation heat map is used to get the insights into the relation among different features
- The categorical features are analyzed and explored using Seaborn countplot. The countplot is like an histogram for categorical attributes
- The numerical features are analyzed and explored using Seaborn kdeplot and Displot
- **The Final Observation are:**
  - The Default/non-default target has a low correlation with BidsPortfolioManager 0.12, LanguageCode 0.14, Country 0.18, Interest 0.17, LoanDuration 0.14
  - Correlation of EmploymentStatus with : BidsPortfolioManager 0.12, BidsApi 0.11, VerificationType 0.3, Gender 0.19
  - Correlation of MaritalStatus with : LanguageCode 0.15, Interest 0.19
  - Correlation of MonthlyPayment with : BidsPortfolioManager 0.32, BidsManual 0.22, NewCreditCustomer 0.15, Country 0.28, AppliedAmount 0.74, Amount 0.6, Interest 0.24
  - Correlation of LoanDuration with : BidsPortfolioManager 0.17, Country 0.21, AppliedAmount 0.31, Amount 0.29, target 0.14
  - Correlation of Interest with : NewCreditCustomer 0.28, LanguageCode 0.5, Country 0.32
  - Correlation of Amount with : BidsPortfolioManager 0.61, BidsManual 0.41, NewCreditCustomer 0.12, Age 0.12, Country 0.23, AppliedAmount 0.89
  - Correlation of AppliedAmount with : BidsPortfolioManager 0.6, BidsManual 0.37, NewCreditCustomer 0.12, Age 0.11, Country 0.23
  - Correlation of Country with : NewCreditCustomer 0.23, LanguageCode 0.2, Age 0.24
  - Correlation of Gender with : NewCreditCustomer 0.12
  - Correlation of LanguageCode with : NewCreditCustomer 0.15
  - Correlation of BidsApi with : BidsPortfolioManager 0.1
  - We can see PrincipalBalance and InterestAndPenaltyBalance attributes have somehow a correlation with target variable of 0.34 and 0.33 respectively.
  - Correlation of Default/non-default Target with : Rating 0.2, Restructured 0.18, CreditScoreEsMicroL 0.16, PrincipalBalance 0.34, InterestAndPenaltyBalance 0.33
  - Correlation of PreviousEarlyRepaymentsCountBeforeLoan with : NoOfPreviousLoansBeforeLoan 0.14, AmountOfPreviousLoansBeforeLoan 0.14, PreviousRepaymentsBeforeLoan 0.14,
  - Correlation of PreviousRepaymentsBeforeLoan with : ExistingLiabitlies 0.15, NoOfPreviousLoansBeforeLoan 0.4, AmountOfPreviousLoansBeforeLoan 0.57, 
  - Correlation of AmountOfPreviousLoansBeforeLoan with : ExistingLiabilities 0.28, MonthlyPaymentDay 0.11, NoOfPreviousLoansBeforeLoan 0.77
  - Correlation of NoOfPreviousLoansBeforeLoan with : ExistingLiabilities 0.33, MonthlyPaymentDay 0.1, 
  - Correlation of InterestAndPenaltyBalance with : ExistingLiabilities 0.19, DebtToIncome 0.21, Rating 0.22, CreditScoreEsMicroL 0.25, PrincipalBalance 0.42,
  - Correlation of PrincipalBalance with : Rating 0.13, InterestAndPenaltyPaymentsMade 0.16 
  - Correlation of InterestAndPenaltyPaymentsMade with : ExistingLiabilities 0.15, RefinanceLiabilities 0.27, DebtToIncome 0.25, Restructured 0.26, PrincipalPaymentsMade 0.46
  - Correlation of PrincipalPaymentsMade with : ExistingLiabilities 0.11, RefinanceLiabilities 0.2, DebtToIncome 0.2,
  - Correlation of CreditScoreEsMicroL with : DebtToIncome 0.14, Rating 0.4
  - Correlation of Restructured with : ExistingLiabilities 0.17, DebtToIncome 0.17
  - Correlation of Freecash with : incomeTotal 0.16
  - Correlation of DebtToIncome with : ExistingLiabilities 0.44, RefinanceLiabilities 0.35, 
  - Correlation of RefinanceLiabilities with : ExistingLiabilities 0.46, 
- **Observations For Categorial Bivariate Analysis**
  - The countplot is like histogram for categorical attributes. So its easy to get insights about such attributes with target attributes
  - New 'NewCreditCustomers' are more likey to default than existing.
  - The customers having 'income and expenses verified', 'income verified' are more likely to default than others.
  - The Estonians are less likely to default and 'finnish','spanish' are more likely to default.
  - The males are more likely to default than females
  - Customers with 'undefined','home improvement''other' use of loan are more likely to default.
  - Customers with vocational education are more likely to default as it has more defualt ratio than other classes.
  - Customers with CredictScoreEsMicroL are more likely to default.
  - Customers with undefined maritalstatus are defaulting more than those with defined maritalstatus.
  - Customers with undefined Employment status are more likely to default than those with defined. SO customers must have defined employmentstatus.
  - Customers with employment duration more than 5 years are defaulting more. so compnany should avoid should customers.
  - Customers with undefined occupationArea are defaulting more.
  - Customrs with 'yes' restructured are more likely to default than others.
  - Tenants, prefurnised property owners are likely to default more as defualt ratio is more this class than owners.
  - The customers with HR rating are defaulting more as this class has more default ratio than F class. we can see from plot of Rating.



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

