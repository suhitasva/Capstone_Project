# Healthcare Fraud Detection

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link" href="" target="_blank" rel="noreferrer noopener">LinkedIn</a></div>
<!-- /wp:button -->

<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link" href="" target="_blank" rel="noreferrer noopener">GitHub</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:heading {"level":1} -->
<h1>Introduction</h1>
<!-- /wp:heading -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>In recent years the rate at which doctors, and hospitals have conducted fraudulent activities, scams, and schemes have troubled authorities.  The Department of Justice&nbsp;(DOJ) <a href="https://www.justice.gov/opa/pr/justice-department-recovers-over-3-billion-false-claims-act-cases-fiscal-year-2019" target="_blank" rel="noreferrer noopener">recovered</a>&nbsp;over $3 billion from False Claims cases in the 2019 fiscal year, with $2.6 billion coming from healthcare fraud schemes.&nbsp;DOJ also reported that&nbsp;the billions of dollars stemming from healthcare fraud cases involved a wide range of stakeholders, including drug and medical device manufacturers. The stakeholders also included care providers, hospitals, pharmacies, hospice organizations, laboratories, and physicians.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86501,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-215777-vyDUyUsd.png" alt="fraud" class="wp-image-86501"/><figcaption>Fraud Investigation</figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Healthcare/Medicare fraud is more prevalent among medical providers and usually results in higher health care costs, insurance premiums, and taxes for the general population. Medical Providers try to maximize reimbursement received from Medicare which they are not entitled to via illegitimate activities such as submitting false claims. This capstone project will focus on fraud committed by doctors and hospitals. Using real-life Medicare claims data, I have attempted to identify key healthcare fraud indicators and fraudulent provider characteristics which could be used in Medicare fraud investigation via supervised machine learning. Machine learning classification algorithms will be used in an attempt to classify providers as fraud or non-fraud.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Healthcare Fraud Overview</h2>
<!-- /wp:heading -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:image {"align":"center","id":86510,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/617658c02228c7cf8c8251726c98d5c5e29ad4c2-620x350-437529-hxQnxqWg.jpg" alt="fraud" class="wp-image-86510"/></figure></div>
<!-- /wp:image -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>As per the <a href="https://www.fbi.gov/scams-and-safety/common-scams-and-crimes/health-care-fraud" target="_blank" rel="noreferrer noopener" title="FBI">FBI</a>, health care fraud can be committed by medical providers, patients, and others who intentionally deceive the health care system to receive unlawful benefits or payments.  Some of the common ways that medical providers deceive patients/insurance providers through claims procedures are listed below:</p>
<!-- /wp:paragraph -->

<!-- wp:media-text {"mediaId":86523,"mediaLink":"https://nycdatascience.com/blog/?attachment_id=86523","mediaType":"image","mediaWidth":43} -->
<div class="wp-block-media-text alignwide is-stacked-on-mobile" style="grid-template-columns:43% auto"><figure class="wp-block-media-text__media"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/download-130347-u0Jum9K5.jpg" alt="Fraud" class="wp-image-86523 size-full"/></figure><div class="wp-block-media-text__content"><!-- wp:list -->
<ul><li>Billing for care not rendered. </li><li>Submitting duplicate claims. </li><li>Falsifying claim/patient info. </li><li>Disguising non-covered services as covered services. </li><li>Using incorrect diagnosis/procedure codes. </li><li>Stealing a Medicare number or card and using it to submit fraudulent claims.</li></ul>
<!-- /wp:list --></div></div>
<!-- /wp:media-text -->

<!-- wp:paragraph -->
<p>Let us also look at some of the common terminology associated with healthcare, which includes some of the offences described above. As per a Medicare Advantage <a href="https://www.medicareadvantage.com/enrollment/medicare-fraud" target="_blank" rel="noreferrer noopener" title="article">article</a>, some of the common ways in which illegitimate Medicare spending may be carried out are as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Double Billing: <ul><li>This type of Medicare fraud involves deliberately charging twice for a service or product that was only performed or supplied once.</li></ul></li><li>Phantom Billing: <ul><li>This involves billing for a test or procedure or other medical service that was never actually performed. This is one of the most common forms of Medicare fraud</li></ul></li><li>Upcoding: <ul><li>Upcoding is altering the codes assigned to specific billable services to reflect a higher-level service than what was actually performed. This type of scam is carried out to receive a fraudulently higher Medicare reimbursement than what is required.</li></ul></li><li>Unbundling: <ul><li>This involves taking a comprehensive service and separating it into several specific services in order to bill for each one independently. This leads to a higher reimbursement total.</li></ul></li><li>Kickbacks: <ul><li>Kickbacks occur when a provider accepts payment on behalf of a pharmaceutical company or medical device supplier. This is done in exchange of recommending or prescribing patients to use the product.</li></ul></li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Medicare Claims Dataset</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Medicare claims data used in this project comes from data uploaded to Kaggle - <a href="https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis" target="_blank" rel="noreferrer noopener" title="Healthcare Provider Fraud Detection Analysis">Healthcare Provider Fraud Detection Analysis</a> by Rohit Anand Gupta. The data is comprised of three sub-datasets; their details are listed below.</p>
<!-- /wp:paragraph -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:image {"align":"center","id":86529,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-015578-LGMbKnsy.png" alt="" class="wp-image-86529"/></figure></div>
<!-- /wp:image -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>In the Beneficiary dataset, we get patient-level information such as their age, race, gender, geographical conditions, chronic conditions, deductible paid, reimbursement received, etc. The Inpatient and Outpatient dataset comprises of claim-level information for those patients. These datasets include information such as associated hospital, associated physicians, claim start/end date, discharge start/end date, and diagnosis/procedure codes associated with the claim.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Another key piece of information that is included in this dataset is the fraud labels. In this data, the fraud labels are placed upon the medical providers/hospitals. The fraud labels indicate if the hospitals are possibly fraud or non-fraud. Based on the initial review, we can see that the labels provided are highly imbalanced; almost all the doctors are labeled as non-fraud. Such kind of imbalance is detrimental while data modeling, especially for classification tasks as we run into the risk of labeling all our providers as non-fraud. The data was balanced using up sampling techniques, which are discussed further in the blog.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86533,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-918017-S4mKzrAL.png" alt="" class="wp-image-86533"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Fraud Data Preprocessing</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Before getting into some details about the extensive data analysis done on the claims data, I would like to discuss how the data was preprocessed. First off, the missingness in the data was handled. The data included a lot of missing values, such as missing date of death if the patient is alive and missing operating physician if no surgical operation was performed. Missing information was imputed accordingly. Also, for uniform and efficient preprocessing, all categorical data was label encoded.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I also decided to keep outliers in the data, as the outliers could provide key fraud indicator information. These outliers could very well be transactions where actual fraud is being committed. This was also the reason why the data was robust scaled before modeling. Another important preprocessing step done was up sampling the data to reduce the imbalance and fraud label ratio to 1:1. The data was processed via two up sampling techniques; SMOTE (creates data randomly between two data points) and BorderlineSMOTE (creates data along the decision boundary between the two classes) and performances were compared between both.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86541,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-901834-bXyXJtbs.png" alt="" class="wp-image-86541"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Next, I also created new features and dropped some redundant ones. New features that give information on whether the patient was deceased or not, duration of the hospital stay/claim, number of associated doctors/claims, number of chronic conditions the patient has, etc. were created. Also, some other features with high null values or ones from which other features were created were dropped. After all of the preprocessing all the three datasets were combined into one to create one training and testing dataset.</p>
<!-- /wp:paragraph -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:image {"align":"center","id":86546,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img5-062651-sbAl5jSz.png" alt="" class="wp-image-86546"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Beneficiary Information Analysis</h2>
<!-- /wp:heading -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86558,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img6-782413-GHEKnxoC.png" alt="" class="wp-image-86558"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86557,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img7-242637-UPPNnDY9.png" alt="" class="wp-image-86557"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>Before we proceed, let us look at who our patients are. If we look at the graphs above, we see that majority of our patients belong to race encoded as 0 and gender encoded as 1. Most of the patients fall between the ages of 68 through 82 years old; however, we have some outliers as well. Almost all our patients are alive. I also studied the top beneficiaries that paid the highest deductible and for whom the highest total reimbursements were received. There are several beneficiaries that are common in both groups as we can see from the two graphs below.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86664,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img8-961323-q85ZmcQu.png" alt="" class="wp-image-86664"/></figure></div>
<!-- /wp:image -->

<!-- wp:image {"align":"center","id":86665,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img9-119892-CD0lOdDa.png" alt="" class="wp-image-86665"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Fraud vs Non-Fraud Providers Study:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To understand what the key fraud provider characteristics are, I extensively studied the inpatient/outpatient data based on the fraud labels provided. I attempted to uncover what sets some of these fraud providers apart from the non-fraud providers. Following, are some of the findings that were uncovered through the study (comparison done between inpatient/outpatient datasets and fraud/non-fraud providers):</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Maximum Reimbursement Amounts</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>These graphs below detail the distribution of the maximum total reimbursement amount received for fraud and non-fraud providers between the inpatient and outpatient claims. There is a difference in the average maximum reimbursement amounts received for both types of providers in the inpatient dataset. A similar difference is not seen between the outpatient fraud and non-fraud providers; however, we can see that fraud providers claimed some of the highest reimbursements.</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86675,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-646504-5r04gPJs.png" alt="" class="wp-image-86675"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86674,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-799769-DmUXLmoG.png" alt="" class="wp-image-86674"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>The bar graphs below show the top providers with high maximum reimbursement amounts (both inpatient and outpatient datasets) and how many of those were fraud vs non-fraud. In the top inpatient providers, all except one of the providers are labeled as fraud. In the top outpatient providers, there is a 50:50 division; however, the highest reimbursements were claimed by fraud providers. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86676,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-926144-7wmdyOdM.png" alt="" class="wp-image-86676"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86677,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-196356-facUvj5q.png" alt="" class="wp-image-86677"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Number of Claims</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>These graphs below detail the distribution of the total number of claims submitted for fraud and non-fraud providers between the inpatient and outpatient claims. For both inpatient and outpatient datasets, fraud providers had an extremely high number of claims submitted than the non-fraud providers.</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86683,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-897688-t3WQ5atM.png" alt="" class="wp-image-86683"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86682,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-342732-2YOFvtKq.png" alt="" class="wp-image-86682"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>The bar graphs below show the top providers with the high total number of claims submitted (both inpatient and outpatient datasets) and how many of those were fraud vs non-fraud. All the top providers for both datasets are labeled as fraud.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86685,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-150555-gKWsmunF.png" alt="" class="wp-image-86685"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86686,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-537635-NOMLxPVI.png" alt="" class="wp-image-86686"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Diagnosis Code Counts</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>These graphs below detail the distribution of the total number diagnosis codes listed on claims for fraud and non-fraud providers between the inpatient and outpatient claims. In Inpatient providers, the average code counts are higher for non-fraud providers than the fraud providers; however, exactly opposite is true for the outpatient providers.</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86692,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-000557-ldUNeIiF.png" alt="" class="wp-image-86692"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86693,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-527415-SoIU89Qd.png" alt="" class="wp-image-86693"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>The bar graphs below show the top providers with the high total number of diagnosis codes listed on claims (both inpatient and outpatient datasets) and how many of those were fraud vs non-fraud. For the top inpatient providers, all except one of the providers is labeled as fraud; whereas, in the top outpatient providers few providers have the fraud label associated with them.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86694,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-509277-jB39izZw.png" alt="" class="wp-image-86694"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86695,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-216421-BgeO5KG4.png" alt="" class="wp-image-86695"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Average Patient Age/Chronic Condition Counts</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Next, I also looked at average patient age and chronic condition counts between inpatient and outpatient providers for both types of providers. It seems like from the graphs below that for both inpatient and outpatient providers, the range of patient age is narrower for the fraud providers than the non-fraud providers. Likewise, the range of patient chronic condition counts is also narrower for the fraud providers than the non-fraud providers.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86700,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img5-907926-o2X3hYWE-1024x330.png" alt="" class="wp-image-86700"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86699,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img6-038797-Zn2pjBmy-1024x344.png" alt="" class="wp-image-86699"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Patients per state - Fraud Providers</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The last avenue that I explored as a part of this study was, to look at where the majority of the patients are residing for fraud providers in the inpatient and outpatient datasets. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86704,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img7-892608-7k0sCrnM.png" alt="" class="wp-image-86704"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>From these graphs, it looks like most of the patients for the fraud providers in both inpatient and outpatient datasets are coming from few common states. States that encoded as 5, 30 and 33 have the highest number of patients who are associated with a fraud labeled medical provider.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86705,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdatascience.com/blog/wp-content/uploads/2022/06/suhita-acharya/img8-470303-SQJFikhp.png" alt="" class="wp-image-86705"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Classification Task - Data Modeling</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>After all the in-depth data analysis, I moved on to the data modeling part using python and machine learning classification algorithms. For modeling, I used the training dataset; did a 70:30 train-test split and evaluated the results for SMOTE and BorderlineSMOTE unsampled data. The model performances were evaluated based on the F1 score, which achieves a harmonious balance between precision and recall. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86709,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img9-672178-LcZeqjnl.png" alt="" class="wp-image-86709"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Based, on these graphs we can see that there is not much difference in performance between data up sampled via two different up sampling techniques. The Linear SVC model performs the worst in this case and completely misclassifies the majority of the providers. However, the XGBoost and the LightGBM models (final features selected via Recursive Feature Selection) perform much better in terms of classifying between both classes. In the next section we will look at performance evaluation of our better performing LightGBM model.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86710,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img10-538624-YKhXS1ig.png" alt="" class="wp-image-86710"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>LightGBM Performance Evaluation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One of the best-performing models out of all the model types attempted was the LightGBM model. We can see the reason why it performed well through some of the classification model performance metrics. First off, we will look at the confusion matrix. This confusion matrix shows us correct vs misclassifications as predicted by the model. We can see that this model does a good job of classifying non-frauds as non-frauds and possibly frauds as such. I was also able to achieve better possibly-fraud detections by adjusting the model classification threshold a bit.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Confusion matrix</h3>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":86772,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img11-123868-Mpx5EKGC.png" alt="" class="wp-image-86772"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>AUC/ROC and Precision-Recall Curve:</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Next, we will look at the ROC and Precision-Recall Curve for the LightGBM classifier. The AUCROC curves allow us to visualize the tradeoff between a model's sensitivity and specificity.&nbsp;Ideally, the true-positive rate should be closer to one and the false positive rate should be closer to zero. Additionally, the higher the area under the curve (computation of the relationship between false positives and true positives) the better the model is. Our LightGBM model seems to do well in this regard; it has a high and steep ROC curve with an AUC score of 0.94. </p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86789,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img1-978922-LlzPYpDV.png" alt="" class="wp-image-86789"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86773,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdatascience.com/blog/wp-content/uploads/2022/07/suhita-acharya/img13-223426-yoPhBDx7.png" alt="" class="wp-image-86773"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>Next, we will look at the precision-recall curve for this model. Precision-Recall curve shows the tradeoff between result relevancy and completeness. The goal always would be to maximize both precision and recall and have a high area under the curve. Also, having a high average precision is also highly desirable. The LightGBM model achieves both in this case.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Class Prediction Error</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Lastly, we will also look at the Class Prediction Error plot for the LightGBM model. This Class Prediction Error plot allows us to see how efficient our classifier is at predicting correct classes. For our model, this plot shows us that our model does a good job predicting the majority of the classes correctly and the misclassification rate is relatively low.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86775,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img14-000623-pdE9nuO2.png" alt="" class="wp-image-86775"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Model Feature Importances</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One way we can understand what factors are important while trying to distinguish between fraud and non-fraud providers is to look at model feature importances. This feature allows us to examine which attributes contribute to the model's classifying capability. In this section we will look at feature importances for three models: XGBoost, LightGBM, and Random Forest.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86833,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img2-952940-nIP2Oel0.png" alt="" class="wp-image-86833"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If we look at the results from the XGBoost and the LightGBM model, we can see the same top four features contribute the most in terms of decision-making. These are the attending physician or the primary doctor, the county, the state the patient is from, and other physicians listed on the claim. If we look at top features by weight for the Random Forest model, we again see the attending physician or the primary doctor, county, and the state the patient is from.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86834,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img3-770111-YYcQ2zuk.png" alt="" class="wp-image-86834"/></figure></div>
<!-- /wp:image -->

<!-- wp:image {"id":86835,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdatascience.com/blog/wp-content/uploads/2022/07/suhita-acharya/img4-953562-CXiUo2kT-1024x526.png" alt="" class="wp-image-86835"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>SHAP Value Analysis</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The last thing that I looked at in terms of feature evaluation was the SHAP values of the important features in the model. SHAP values are calculated based on the game-theory approach where weightage is assigned to different features based on how much they contribute to the model's prediction capability. The first graph which is shown below, tells us about the top features based on the SHAP values and their overall effect on the model. We will look at the results for the XGBoost and the LightGBM model.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86839,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img5-369939-zvvteH3F.png" alt="" class="wp-image-86839"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Both the models, share the top five features themselves. These features are the patient's birth year, age, state/county they belong to, and their primary physician listed on the submitted claim. The x-axis on the graph below all the SHAP values plotted for the feature and whether they positively or negatively impact the model and the colors (from red to blue) tell us whether the feature value is high or low.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86840,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img6-499565-GE4kBx5x.png" alt="" class="wp-image-86840"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>We will also look at top features ordered by total mean SHAP values for the linear models. These linear models tell us a different story. For these models the total claim amount, the insurance claim amount reimbursed, and the deductible paid by the patient were the top influencers in the prediction decision-making.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86841,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/07/suhita-acharya/img7-103022-jTxilb9s-1024x364.png" alt="" class="wp-image-86841"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Conclusions:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>When I first started looking at this data, I looked at the beneficiaries/patients first. Some key insights that I gathered through this exploration were:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Certain beneficiaries listed below could be actively experiencing fraud or could be more susceptible to fraud.<ul><li>Patients for whom high reimbursements were received.</li><li>Patients who have paid high deductibles.</li><li>Some of the aforementioned patients that have high chronic condition counts.</li></ul></li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Next, I studied the fraud and the non-fraud providers from the inpatient and the outpatient dataset and came up with following distinguishing characteristics between the two:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":87191,"width":835,"height":181,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://nycdatascience.com/blog/wp-content/uploads/2022/07/suhita-acharya/img8-945308-mf4XaR68-1024x222.png" alt="" class="wp-image-87191" width="835" height="181"/></figure>
<!-- /wp:image -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>One other thing to note is that possibly fraud providers could be more active in certain states and counties. A patient’s age being in a certain range, which state/county they are from, their total claim amount, and who their primary doctor is could in certain cases make them more vulnerable to fraud. These features could also help investigators differentiate between fraud and non-fraud providers.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Future work:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>When I started working on this project, I came to realize that I am only just scratching the surface in terms of deciphering the black box of healthcare fraud detection. The possibilities are limitless in the type of work we can do or the areas we can focus on to zero in on fraud providers. Given more time some things that I would love to try are:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Duplicate claim investigation.</li><li>Doctor-Hospital Network Analysis.</li><li>Studying patterns in beneficiaries.</li><li>Conducting a market basket analysis.</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>References:</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>The US Department of Justice. 2022.&nbsp;<em>Justice Department Recovers over $3 Billion from False Claims Act Cases in Fiscal Year 2019</em>. [online] Available at: &lt;https://www.justice.gov/opa/pr/justice-department-recovers-over-3-billion-false-claims-act-cases-fiscal-year-2019&gt; [Accessed 28 June 2022].</li><li>Federal Bureau of Investigation. 2022.&nbsp;<em>Health Care Fraud | Federal Bureau of Investigation</em>. [online] Available at: &lt;https://www.fbi.gov/scams-and-safety/common-scams-and-crimes/health-care-fraud&gt; [Accessed 28 June 2022].</li><li>Medicareadvantage.com. 2022.&nbsp;<em>What Are the Most Common Types of Medicare Fraud?</em> [online] Available at: &lt;https://www.medicareadvantage.com/enrollment/medicare-fraud&gt; [Accessed 28 June 2022].</li><li>Gupta, R., 2022.&nbsp;<em>HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS</em>. [online] Kaggle.com. Available at: &lt;https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis&gt; [Accessed 28 June 2022].</li></ul>
<!-- /wp:list -->
