import pandas as pd
import streamlit as st
import joblib



st.title('Welcome to Bandora')
st.header('A peer to peer lending firm')

# following lines create boxes in which user can enter data required to make prediction 
Language = st.selectbox('Language',("Estonian","English", "Russian","Finnish", "German","Spanish","Slovakian"))
LoanDuration = st.number_input('Loan Duration (in months)') 
HomeOwnershipType = st.selectbox('Home Ownership Type',("Homeless","Owner","Living with parents","Tenant","pre-furnished property","Tenant", 
                                                        "unfurnished property","Council house","Joint tenant","Joint ownership","Mortgage",
                                                        "Owner with encumbrance","Other"))
Restructured = st.selectbox('Restructured',("Yes","No"))
