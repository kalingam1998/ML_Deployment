import pandas as pd
import streamlit as st
import joblib



st.title('Bandora Loan Approval Dashboard')

st.header("Borrower's Information")

st.subheader('Personal Background')
Language = st.selectbox('Language',("Estonian","English", "Russian","Finnish", "German","Spanish","Slovakian"))
HomeOwnershipType = st.selectbox('Home Ownership Type',("Homeless","Owner","Living with parents","Tenant","pre-furnished property","Tenant", 
                                                        "unfurnished property","Council house","Joint tenant","Joint ownership","Mortgage",
                                                        "Owner with encumbrance","Other"))
Restructured = st.selectbox('Restructured',("Yes","No"))
LiabilitiesTotal = st.text_input('Total Liabilities')

st.subheader('Loan Details')
LoanDuration = st.text_input('Loan Duration (in months)') 
AppliedAmount = st.text_input('Applied Loan Amount')
EMI = st.text_input('Equated Monthly Installment')

st.subheader('Payment Details')
PrincipalPaymentsMade = st.text_input('Principal Payments Made') 
InterestAndPenaltyPaymentsMade = st.text_input('Interest and Penalty Payments Made')

st.subheader('Other')
Rating = st.selectbox('Rating',("a","aa", "b","c", "d","e","f","hr"))



