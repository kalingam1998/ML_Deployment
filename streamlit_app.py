import pandas as pd
import streamlit as st
import joblib
import sklearn
import time

classifier_pipeline = joblib.load('RFC_pipeline_FINAL.joblib')
#Regressor_pipeline = joblib.load('RR_pipeline_FINAL.joblib')

def create_input_Dataframe():
  
  input_dictionary = {
    "LanguageCode" : Language,
    "HomeOwnershipType": HomeOwnershipType,
    "Restructured" : Restructured,
    "IncomeTotal" : IncomeTotal,
    "LiabilitiesTotal" : LiabilitiesTotal,
    "LoanDuration" : LoanDuration,
    "AppliedAmount" : AppliedAmount,
    "Amount": Amount,
    "Interest":Interest,
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
  
  DF = pd.DataFrame(input_dictionary,index=[0])
  return DF

def Classifier():
  input = create_input_Dataframe()
  prediction = classifier_pipeline.predict(input)
  if prediction==1:
    result = "Defaulter"
  if prediction==0:
    result = "Not Defaulter"
  
  return result

def Regressor():
  # code here for regressor predictions
  #
  #

st.title('Bandora Loan Approval Dashboard')
st.header("Borrower's Information")

st.subheader('Personal Background')
Language = st.selectbox('Language',("estonian","english", "russian","finnish", "german","spanish","slovakian"))
HomeOwnershipType = st.selectbox('Home Ownership Type',("homeless","owner","living with parents","tenant, pre-furnished property",
                                                        "tenant, unfurnished property","council house","joint tenant","joint ownership","mortgage",
                                                        "owner with encumbrance","other"))
Restructured = st.selectbox('Restructured',("yes","no"))
IncomeTotal = st.text_input('Total Icome')
LiabilitiesTotal = st.text_input('Total Liabilities')

st.subheader('Loan Details')
LoanDuration = st.text_input('Loan Duration (in months)') 
AppliedAmount = st.text_input('Applied Loan Amount')
Amount = st.text_input('Amount (granted)')
Interest = st.text_input('Interest')
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
  with st.spinner('Analyzing the Provided Information ...'):
    time.sleep(5)
  result = Classifier()
  st.spinner(text="Analyzing the Information")
  
  if result=="Defaulter":
    st.write("Based on details provided, the user may default so loan is not approved, Thanks!")
    with st.spinner('Predicting preferred Loan details ...'):
      time.sleep(5)
      
      # Regressor code goes below
      #
      #
      
  if result=="Not Defaulter":
    st.write("Congratulations! Your loan is Approved!")
  


