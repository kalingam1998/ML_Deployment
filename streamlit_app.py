import pandas as pd
import streamlit as st
import joblib
import sklearn

classifier_pipeline = joblib.load('RFC_pipeline_FINAL.joblib')

def create_input_Dataframe():
  
  input_dictionary = {
    "Language" : Language,
    "HomeOwnershipType": HomeOwnershipType,
    "Restructured" : Restructured,
    "IncomeTotal" : IncomeTotal,
    "LiabilitiesTotal" : LiabilitiesTotal,
    "LoanDuration" : LoanDuration,
    "EMI": EMI,
    "PreviousRepaymentsBeforeLoan" : PreviousRepaymentsBeforeLoan,
    "MonthlyPaymentDay" :MonthlyPaymentDay,
    
    "PrincipalPaymentsMade" : PrincipalPaymentsMade,
    "InterestAndPenaltyPaymentsMade" : InterestAndPenaltyPaymentsMade,
    "PrincipalBalance" : PrincipalBalance,
    "InterestAndPenaltyBalance" : InterestAndPenaltyBalance,
    "Bids" : BidsPortfolioManger+BidsApi,
    "Rating" : Rating
  }
  
  DF = pd.DataFrame(input_dictionary)
  
  return DF

def Classifier():
  input = create_input_Dataframe(index=[0])
  prediction = classifier_pipeline.predict(input)
  if prediction==1:
    result = "Defaulter"
  if prediction==0:
    result = "Not Defaulter"
  
  return result

st.title('Bandora Loan Approval Dashboard')

st.header("Borrower's Information")

st.subheader('Personal Background')
Language = st.selectbox('Language',("Estonian","English", "Russian","Finnish", "German","Spanish","Slovakian"))
HomeOwnershipType = st.selectbox('Home Ownership Type',("Homeless","Owner","Living with parents","Tenant","pre-furnished property","Tenant", 
                                                        "unfurnished property","Council house","Joint tenant","Joint ownership","Mortgage",
                                                        "Owner with encumbrance","Other"))
Restructured = st.selectbox('Restructured',("Yes","No"))
IncomeTotal = st.text_input('Total Icome')
LiabilitiesTotal = st.text_input('Total Liabilities')

st.subheader('Loan Details')
LoanDuration = st.text_input('Loan Duration (in months)') 
AppliedAmount = st.text_input('Applied Loan Amount')
EMI = st.text_input('Equated Monthly Installment')

st.subheader('Payment Details')
PreviousRepaymentsBeforeLoan = st.text_input('PreviousRepaymentsBeforeLoan')
MonthlyPaymentDay = st.text_input('MonthlyPaymentDay (digit)')
PrincipalPaymentsMade = st.text_input('Principal Payments Made') 
InterestAndPenaltyPaymentsMade = st.text_input('Interest and Penalty Payments Made')

st.subheader('Balance Details')
PrincipalBalance = st.text_input('PrincipalBalance')
InterestAndPenaltyBalance = st.text_input('InterestAndPenaltyBalance')

st.subheader('Amount of Investment offers made via')
BidsPortfolioManger = st.text_input('BidsPortfolioManger')
BidsApi = st.text_input('BidsApi')

st.subheader('Other')
Rating = st.selectbox('Rating',("a","aa", "b","c", "d","e","f","hr"))

st.header('Loan Application Status')
if st.button(label="Check Status"):
  result = Classifier()
  st.spinner(text="Analyzing the Information")
  
  if result=="Defaulter":
    st.write("Rejected")
  
  if result=="Not Defaulter":
    st.write("Approved")
  


