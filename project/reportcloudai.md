# AI services comparision between Amazon and Google

Jagadeesh Kandimalla, fa19-516-171 

<https://github.com/cloudmesh-community/fa19-516-171>

[Contributors](https://github.com/cloudmesh-community/fa19-516-171/graphs/contributors)

Update: Feb 3 2020

Analysis of the Cloud ML/AI offerings has been completed between AMAZON and GOOGLE.

# Amazon SageMaker

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

The  below link is the example of SageMaker processing using SciKit_learn

<https://github.com/awslabs/amazon-sagemaker-examples/blob/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.ipynb>

![AWS SageMaker](images/sagemaker.png)



# Google Cloud AI Hub

Cloud AutoML makes the power of machine learning available to you even if you have limited knowledge of 
machine learning. You can use AutoML to build on Google's machine learning capabilities to create your own custom 
machine learning models that are tailored to your business needs, and then integrate those models into your
applications and web sites.

pip install google-cloud-automl

Service: automl.googleapis.com

We recommend that you call this service using Google-provided client libraries. If your application needs to
call this service using your own libraries, you should use the following information when making the API requests.


Google API 

<https://googleapis.dev/python/automl/latest/gapic/v1beta1/tables.html>

Here is the github link for Python version of CloudAutoml.

<https://github.com/googleapis/python-automl>



# Comparision between Amazon and Google features.

| Feature                            |  Amazon      | Google     |
| :----------------------------------| :----------: | -----------: |
| Notebook environment               | Yes          |       Yes    |
| Train custom learning algorithms   | Yes          |       Yes    |
| Deploy custom learning algorithms  | Yes          |       No     |
| Automatic hyperparameter tuning    | Yes          | Only for TensorFlow models|
| Distributed training	             | Yes          | Only for TensorFlow models|
