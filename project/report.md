# Abstract Streaming interfaces for the NIST Big data Architecture/Now Changed to Cloudmesh Storage execution of AwsS3 to Local and Local to AwsS3.

Jagadeesh Kandimalla, fa19-516-171 

The streaming service initial architecure is when a Object gets added to S3 ,An AWS Lambda function will get triggered and will call the Google cloud endpoint which inturn will call the APP engine where we write the data to Google cloud Storage


# Objective

The streaming service initial architecure is when a Object gets added to S3 and S3 event will trigger AWS Lambda function and the lambda will call the Google cloud endpoint which inturn will call the APP engine where we write the data to Google cloud Storage.This way the streaming is automated ,anytime a object gets detected in S3 it is loaded to Google Storage and all the components are loosely coupled so that anytime we can replace the destination like Google Big query by just switching the app name in Google App Engine.


# Technologies

AWS S3,<br/>
AWS Lambda,<br/>
OpenAPI 3.0.2,<br/>
GCP Cloudendpoint,<br/>
GCP App Engine,<br/>
GCP Coud Storage

# Architecture

![architecture](images/architecuture-171.png)

# Progress
1.) Created a AWS account/S3 bucket - Done.  
2.) Updated the .cloudmesh.yaml file with awss3 key pair - Done   .  
3.) Debugged the Cloudmesh-Storage awss3.provdier.py and StorageABC.py and got the put and list commands working for AWS S3- Done .    
4.) Uploded the files to S3 files using Cloudmesh commands(PUT and LIST) -- Done .     
5.) Created the GCP account and set up gsutil on the mac - Done .  
6.) Created the project and bucket and created the google application credentials - Done   
7.) Download the Google app credentials and set the authentication in the environment variables - Done .   
8.) Developed a flask application to read the data and load the data to google cloud storage -Done       
9.) Debugged the flask application in the local using POSTMAN - Done .   
10.) Extend the flask application to read from the URL and get the data downloaded from URL and load in to Google cloud storage - In Progress.<br/>
11.) Development of AWS Lambda application - Not Started . 

# Project Scope changed from streaming to AwsS3 to Local and Local to AwsS3

Professor wants to fix the AwsS3 Provider and add some new functionality and test and benchmark the new chages.
Now AwsS3 provider has been fixed and and the new functionality(checking bucket exists ,if not create code) has been implemented in the provider.
Pytests have been updated to print out benchamarks and the code has been tested using Pytests and CMD commands.
All the code has been checked to Cloudmesh-Storage transfer bucket and has been merged with master.



