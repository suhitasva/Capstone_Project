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

	df['Deceased'] = np.where((df['DOD'].replace(np.nan,'rep') == 'rep'), 0, 1)

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

def show_values(axs, orient="v", space=.01):
	def _single(ax):
		if orient == "v":
			for p in ax.patches:
				_x = p.get_x() + p.get_width() / 2
				_y = p.get_y() + p.get_height() + (p.get_height()*0.01)
				value = '{:.2f}'.format(p.get_height())
				ax.text(_x, _y, value, ha="center") 
		elif orient == "h":
			for p in ax.patches:
				_x = p.get_x() + p.get_width() + float(space)
				_y = p.get_y() + p.get_height() - (p.get_height()*0.5)
				value = '{:.2f}'.format(p.get_width())
				ax.text(_x, _y, value, ha="left")

	if isinstance(axs, np.ndarray):
		for idx, ax in np.ndenumerate(axs):
			_single(ax)
	else:
		_single(axs)

def in_out_na_replace(df):

	# It was assumed that for missing deductible amounts, no deductible was paid

	df['DeductibleAmtPaid'] = df['DeductibleAmtPaid'].fillna(0)
  
	# Where no codes were listed, 0 was used

	col_list = ['ClmDiagnosisCode_1', 'ClmDiagnosisCode_2', 'ClmDiagnosisCode_3',
			   'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5', 'ClmDiagnosisCode_6',
			   'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8', 'ClmDiagnosisCode_9',
			   'ClmDiagnosisCode_10', 'ClmProcedureCode_1', 'ClmProcedureCode_2',
			   'ClmProcedureCode_3','ClmAdmitDiagnosisCode']

	for col in col_list:
		df[col] = df[col].fillna('None')

	# For missing doctor code values, None were added as there was no doctor listed for that category

	for col in ('AttendingPhysician','OperatingPhysician','OtherPhysician'):
		df[col] = df[col].fillna('None')    

def in_new_feats(df):

	# Changing dtype for claim start/end and admission/discharge date
	# columns to datetime

	df['ClaimStartDt'] = pd.to_datetime(df['ClaimStartDt'])
	df['ClaimEndDt'] = pd.to_datetime(df['ClaimEndDt'])
	df['AdmissionDt'] = pd.to_datetime(df['AdmissionDt'])
	df['DischargeDt'] = pd.to_datetime(df['DischargeDt'])

	# Creating Hospital_Stay and Claim_Duration features and changing
	# dtype to int

	df['Hospital_Stay'] = round(((df['DischargeDt'] - df['AdmissionDt']).dt.days))
	df['Claim_Duration'] = round(((df['ClaimEndDt'] - df['ClaimStartDt']).dt.days))
	df['Hospital_Stay'] = df['Hospital_Stay'].astype(int)
	df['Claim_Duration'] = df['Claim_Duration'].astype(int)


	# Breaking down claim made month and year

	df['Claim_Start_Year'] = df['ClaimStartDt'].dt.year
	df['Claim_Start_Month'] = df['ClaimStartDt'].dt.month

	# Insurance covered percentages

	df['Insurance_Covered_Per'] = round((df['InscClaimAmtReimbursed']/\
										(df['InscClaimAmtReimbursed']+\
										 df['DeductibleAmtPaid']))*100, 2)
	df['Insurance_Covered_Per'] = df['Insurance_Covered_Per'].fillna(0)

	# Total claim amount

	df['Total_Claim_Amt'] = (df['InscClaimAmtReimbursed']+df['DeductibleAmtPaid'])

	# Count of total number of physicians for each beneficiary

	phy_df = df[['BeneID','AttendingPhysician','OperatingPhysician','OtherPhysician']]\
			  .drop_duplicates()

	phy_df = phy_df.loc[phy_df.AttendingPhysician != 'None',:]\
               	   .loc[phy_df.OperatingPhysician != 'None',:]\
                   .loc[phy_df.OtherPhysician != 'None',:]	

	phy_df = phy_df[['BeneID','AttendingPhysician','OperatingPhysician','OtherPhysician']]\
			  .groupby('BeneID').agg(['count']).reset_index()

	phy_df.columns=['Bene_ID','Att_cnt', 'Op_cnt', 'Othr_cnt']

	df['Physician_Count'] = phy_df['Att_cnt'] + phy_df['Op_cnt'] + phy_df['Othr_cnt']
	df['Physician_Count'] = df['Physician_Count'].fillna(0)
	df['Physician_Count'] = df['Physician_Count'].astype(int)

	# Count of claims and hospitals associated with per beneficiary

	cl_df = df[['BeneID','ClaimID']].groupby('BeneID').agg(['count']).reset_index()
	cl_df.columns=['Bene_ID','Cl_cnt']

	df['Claim_Count'] = cl_df['Cl_cnt']
	df['Claim_Count'] = df['Claim_Count'].fillna(0)
	df['Claim_Count'] = df['Claim_Count'].astype(int)


	prv_df = df[['BeneID','Provider']].drop_duplicates()
	prv_df = prv_df[['BeneID','Provider']].groupby('BeneID')\
				 .agg(['count']).reset_index()

	prv_df.columns=['Bene_ID','Prov_cnt']

	df['Hospital_Count'] = prv_df['Prov_cnt']
	df['Hospital_Count'] = df['Hospital_Count'].fillna(0)
	df['Hospital_Count'] = df['Hospital_Count'].astype(int)

def out_new_feats(df):

	# Changing dtype for claim start/end and admission/discharge date
	# columns to datetime

	df['ClaimStartDt'] = pd.to_datetime(df['ClaimStartDt'])
	df['ClaimEndDt'] = pd.to_datetime(df['ClaimEndDt'])

	# Creating Hospital_Stay and Claim_Duration features and changing
	# dtype to int

	df['Claim_Duration'] = round(((df['ClaimEndDt'] - df['ClaimStartDt']).dt.days))
	df['Claim_Duration'] = df['Claim_Duration'].astype(int)

	# Breaking down claim made month and year

	df['Claim_Start_Year'] = df['ClaimStartDt'].dt.year
	df['Claim_Start_Month'] = df['ClaimStartDt'].dt.month

	# Insurance covered percentages

	df['Insurance_Covered_Per'] = round((df['InscClaimAmtReimbursed']/\
										(df['InscClaimAmtReimbursed']+\
										 df['DeductibleAmtPaid']))*100, 2)

	df['Insurance_Covered_Per'] = df['Insurance_Covered_Per'].fillna(0)

	# Total claim amount

	df['Total_Claim_Amt'] = (df['InscClaimAmtReimbursed']+df['DeductibleAmtPaid'])

	# Count of total number of physicians for each beneficiary

	phy_df = df[['BeneID','AttendingPhysician','OperatingPhysician','OtherPhysician']]\
			  .drop_duplicates()

	phy_df = phy_df.loc[phy_df.AttendingPhysician != 'None',:]\
               	   .loc[phy_df.OperatingPhysician != 'None',:]\
                   .loc[phy_df.OtherPhysician != 'None',:]

	phy_df = phy_df[['BeneID','AttendingPhysician','OperatingPhysician','OtherPhysician']]\
			  .groupby('BeneID').agg(['count']).reset_index()

	phy_df.columns=['Bene_ID','Att_cnt', 'Op_cnt', 'Othr_cnt']

	df['Physician_Count'] = phy_df['Att_cnt'] + phy_df['Op_cnt'] + phy_df['Othr_cnt']
	df['Physician_Count'] = df['Physician_Count'].fillna(0)
	df['Physician_Count'] = df['Physician_Count'].astype(int)

	# Count of claims and hospitals associated with per beneficiary

	cl_df = df[['BeneID','ClaimID']].groupby('BeneID').agg(['count']).reset_index()
	cl_df.columns=['Bene_ID','Cl_cnt']

	df['Claim_Count'] = cl_df['Cl_cnt']
	df['Claim_Count'] = df['Claim_Count'].fillna(0)
	df['Claim_Count'] = df['Claim_Count'].astype(int)


	prv_df = df[['BeneID','Provider']].drop_duplicates()
	prv_df = prv_df[['BeneID','Provider']].groupby('BeneID')\
				 .agg(['count']).reset_index()

	prv_df.columns=['Bene_ID','Prov_cnt']

	df['Hospital_Count'] = prv_df['Prov_cnt']
	df['Hospital_Count'] = df['Hospital_Count'].fillna(0)
	df['Hospital_Count'] = df['Hospital_Count'].astype(int)

def inout_label_encode(df):

	# Updating data type to strings for certain columns (listed below):

	df['ClmProcedureCode_1'] = df['ClmProcedureCode_1'].astype(str)
	df['ClmProcedureCode_2'] = df['ClmProcedureCode_2'].astype(str)
	df['ClmProcedureCode_3'] = df['ClmProcedureCode_3'].astype(str)

	# List of columns for label encoding 

	col_list1 = ['AttendingPhysician', 'OperatingPhysician', 'OtherPhysician',
				'ClmAdmitDiagnosisCode', 'DiagnosisGroupCode','ClmDiagnosisCode_1',
				'ClmDiagnosisCode_2', 'ClmDiagnosisCode_3','ClmDiagnosisCode_4',
				'ClmDiagnosisCode_5', 'ClmDiagnosisCode_6','ClmDiagnosisCode_7',
				'ClmDiagnosisCode_8', 'ClmDiagnosisCode_9','ClmDiagnosisCode_10',
				'ClmProcedureCode_1', 'ClmProcedureCode_2','ClmProcedureCode_3']

	# Label Encoding each column one by one

	for col in col_list1:
		label_encoder = preprocessing.LabelEncoder()
		df[col] = label_encoder.fit_transform(df[col])

def code_count(df):

	diag_cnt_df = df[['Provider','ClmDiagnosisCode_1','ClmDiagnosisCode_2',\
					  'ClmDiagnosisCode_3','ClmDiagnosisCode_4','ClmDiagnosisCode_5',\
					  'ClmDiagnosisCode_6','ClmDiagnosisCode_7','ClmDiagnosisCode_8',\
					  'ClmDiagnosisCode_9','ClmDiagnosisCode_10']].drop_duplicates()

	diag_cnt_df = diag_cnt_df.loc[diag_cnt_df.ClmDiagnosisCode_1 != 'None',:]\
               	   			 .loc[diag_cnt_df.ClmDiagnosisCode_2 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_3 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_4 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_5 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_6 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_7 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_8 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_9 != 'None',:]\
                   			 .loc[diag_cnt_df.ClmDiagnosisCode_10 != 'None',:]


	diag_cnt_df = diag_cnt_df[['Provider','ClmDiagnosisCode_1','ClmDiagnosisCode_2',\
					  'ClmDiagnosisCode_3','ClmDiagnosisCode_4','ClmDiagnosisCode_5',\
					  'ClmDiagnosisCode_6','ClmDiagnosisCode_7','ClmDiagnosisCode_8',\
					  'ClmDiagnosisCode_9','ClmDiagnosisCode_10']].\
					   groupby('Provider').agg(['count']).reset_index()

	diag_cnt_df.columns=['Provider','CD1','CD2', 'CD3', 'CD4',\
						 'CD5','CD6','CD7', 'CD8', 'CD9','CD10']

	df['Diag_Code_Cnt'] = diag_cnt_df['CD1'] + diag_cnt_df['CD2'] + diag_cnt_df['CD3'] +\
						  diag_cnt_df['CD4'] + diag_cnt_df['CD5'] + diag_cnt_df['CD6'] +\
						  diag_cnt_df['CD7'] + diag_cnt_df['CD8'] + diag_cnt_df['CD9'] +\
						  diag_cnt_df['CD10']

	df['Diag_Code_Cnt'] = df['Diag_Code_Cnt'].fillna(0)
	df['Diag_Code_Cnt'] = df['Diag_Code_Cnt'].astype(int)
					  

	proc_cnt_df = df[['Provider','ClmProcedureCode_1', 'ClmProcedureCode_2','ClmProcedureCode_3']].\
					   drop_duplicates()
					   
	proc_cnt_df = proc_cnt_df.loc[proc_cnt_df.ClmProcedureCode_1 != 'None',:]\
               	   			 .loc[proc_cnt_df.ClmProcedureCode_2 != 'None',:]\
                   			 .loc[proc_cnt_df.ClmProcedureCode_3 != 'None',:]\
    	
	proc_cnt_df = proc_cnt_df[['Provider','ClmProcedureCode_1', 'ClmProcedureCode_2','ClmProcedureCode_3']].\
					   groupby('Provider').agg(['count']).reset_index()

	proc_cnt_df.columns=['Provider','CD1','CD2','CD3']

	df['Proc_Code_Cnt'] = proc_cnt_df['CD1'] + proc_cnt_df['CD2'] + proc_cnt_df['CD3']

	df['Proc_Code_Cnt'] = df['Proc_Code_Cnt'].fillna(0)
	df['Proc_Code_Cnt'] = df['Proc_Code_Cnt'].astype(int)

def chr_cond_cnt(df):

	# Counting all chronic conditions per claim

	df['Chr_Cond_Count'] = df['RenalDiseaseIndicator'] + df['ChronicCond_Heartfailure'] + df['ChronicCond_KidneyDisease'] +\
	df['ChronicCond_Cancer'] + df['ChronicCond_ObstrPulmonary'] + df['ChronicCond_Alzheimer'] +\
	df['ChronicCond_Depression'] + df['ChronicCond_Diabetes'] + df['ChronicCond_IschemicHeart'] +\
	df['ChronicCond_Osteoporasis'] + df['ChronicCond_rheumatoidarthritis'] + df['ChronicCond_stroke']	















