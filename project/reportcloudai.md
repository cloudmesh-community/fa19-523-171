# AI services comparision between Amazon and Google

Jagadeesh Kandimalla, fa19-516-171 

<https://github.com/cloudmesh-community/fa19-516-171>

[Contributors](https://github.com/cloudmesh-community/fa19-516-171/graphs/contributors)

Update: Feb 3 2020

Analysis of the Cloud ML/AI offerings has been completed between AMAZON and GOOGLE.

Amazon offers ML/AI offering through the service called SageMaker.

Amazon SageMaker Processing to analyze data and evaluate models on the Amazon SageMaker machine learning platform. 
Amazon SageMaker is a fully managed service that covers the entire machine learning workflow, from preparing your data,
to training and deploying the model to make predictions, and monitoring model performance when in production. 
Data processing tasks such as feature engineering, data validation, model evaluation, and model interpretation are 
essential steps performed by engineers and data scientists in this machine learning workflow. With Processing you 
can leverage a simplified, managed experience to run your data processing workloads on the Amazon SageMaker 
platform or by using the Amazon SageMaker APIs, in the experimentation phase and after code is deployed in production

SageMaker can be accessed as low-level client through boto3.The SageMaker API has lot 
of methods which can be used to built a ML algorithm from scratch.
The methods are available in below link

<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html>

The  below link is the example of SageMaker processing using SciKit_learm

<https://github.com/awslabs/amazon-sagemaker-examples/blob/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.ipynb>


Feature	                             Amazon           	Google
Notebook environment	             Yes	            Yes
Train custom learning algorithms	 Yes	            Yes
Deploy custom learning algorithms	 Yes	            No
Automatic hyperparameter tuning	     Yes	            Only for TensorFlow models
Distributed training	             Yes	            Only for TensorFlow models
