import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer


def benef_label_encode(df):

	# List of columns for label encoding 

	col_list = ['Gender', 'Race', 'RenalDiseaseIndicator',
   				'ChronicCond_Alzheimer', 'ChronicCond_Heartfailure',
   				'ChronicCond_KidneyDisease', 'ChronicCond_Cancer',
   				'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression',
   				'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart',
   				'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis',
   				'ChronicCond_stroke']

	# Label Encoding each column one by one

	for col in col_list:
		label_encoder = preprocessing.LabelEncoder()
		df[col] = label_encoder.fit_transform(df[col])


# def benef_DOD_impute(df):

# 	# Imputing with most frequent value

# 	imputer = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')

# 	df['DOD'] = imputer.fit_transform(df['DOD'].values.reshape(-1,1))[:,0]


def benef_new_feats(df):

	# Creating deceased column

	df['deceased'] = np.where((df['DOD'].replace(np.nan,'rep') == 'rep'), 0, 1)

	# Changing dtype for DOD and DOB columns to datetime

	df['DOD'] = pd.to_datetime(df['DOD'])
	df['DOB'] = pd.to_datetime(df['DOB'])

	# Creating patient_age column

	df['Age'] = round(((df['DOD'] - df['DOB']).dt.days)/365)

	# Filling the age NA column with age calculated from the 
	# latest date from both datasets

	df['Age'] = df['Age'].fillna(((pd.to_datetime('2009-12-01',format ='%Y-%m-%d')\
													-df['DOB']).dt.days)/365)
	df['Age'] = df['Age'].astype(int)

	# Creating one column for reimbursement and deductible total amounts

	df['Tot_Reimbursed_Amt'] = df['IPAnnualReimbursementAmt'] + df['OPAnnualReimbursementAmt']	
	df['Tot_Deductible_Amt'] = df['IPAnnualDeductibleAmt'] + df['OPAnnualReimbursementAmt'] 

	# Breaking down date columns in to year, month, and year

	df['DOB_year'] = df['DOB'].dt.year
	df['DOB_month'] = df['DOB'].dt.month
	df['DOB_day'] = df['DOB'].dt.day














