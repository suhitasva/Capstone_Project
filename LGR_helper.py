import pandas as pd
import numpy as np
from math import sqrt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler,RobustScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import average_precision_score

def std_num_cols(df):

	# Creating a scalar object

	scaler = StandardScaler()

	# Standardizind the dataframe
	
	df = scaler.fit_transform(df)

def rb_scale_cols(df):

	# Creating a scalar object

	scaler = RobustScaler()

	# Standardizind the dataframe
	
	df = scaler.fit_transform(df)

def get_confusion_matrix(bi_clf, X, y, thres=0.5):
	
	return confusion_matrix(
		y,
		bi_clf.predict_proba(X)[:,1] > thres
	)

def model_results(X_train, y_train, X_test, y_test, model, show = True):

	model.fit(X_train, y_train)

	train_accr = model.score(X_train, y_train)
	test_accr = model.score(X_test, y_test)
	y_pred = model.predict(X_test)
	precision = precision_score(y_test, y_pred)
	avg_precision = average_precision_score(y_test, y_pred)
	recall = recall_score(y_test, y_pred)
	f1 = f1_score(y_test, y_pred)
	roc_auc = roc_auc_score(y_test, y_pred)
	tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
	corr_cls = tp+tn
	incorr_cls = fp+fn

	if show:
		print('The Model Results for ', model)
		print("*"*60)
		print('Train Accuracy is equal to %.3f' %round(train_accr,3))
		print('Test Accuracy is equal to %.3f' %round(test_accr,3))
		print('The Precision score is %.3f' %round(precision,3))
		print('The Average Precision score is %.3f' %round(avg_precision,3))
		print('The Recall score is %.3f' %round(recall,3))
		print('The F1 score is %.3f' %round(f1,3))
		print('The AUC/ROC score is %.3f' %round(roc_auc,3))
		print("True-Positive: %.3f" %tp)
		print("True-Negative: %.3f" %tn)
		print("False-Positive: %.3f" %fp)
		print("False-Negative: %.3f" %fn)
		print("Correctly Classified: %.3f" %corr_cls)
		print("Incorrectly Classified: %.3f" %incorr_cls)

	return [train_accr, test_accr, precision, recall]