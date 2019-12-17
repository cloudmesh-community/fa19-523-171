# Abstract Streaming interfaces for the NIST Big data Architecture/Now Changed to Cloudmesh Storage execution of AwsS3 to Local and Local to AwsS3.

Jagadeesh Kandimalla, fa19-516-171 

The streaming service initial architecure is when a Object gets added to
S3. An AWS Lambda function will get triggered and will call the Google
cloud endpoint which inturn will call the APP engine where we write the
data to Google cloud Storage

* Documentation: <https://cloudmesh.github.io/cloudmesh-manual/storage/storage.html>
* API: <https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.storage.provider.awss3.html>
* Manual: <https://cloudmesh.github.io/cloudmesh-manual/manual/storage/storage.html>
* Code: <https://github.com/cloudmesh/cloudmesh-storage/tree/master/cloudmesh/storage>

## Objective

The streaming service initial architecure is when a Object gets added to
S3 and S3 event will trigger AWS Lambda function and the lambda will
call the Google cloud endpoint which inturn will call the APP engine
where we write the data to Google cloud Storage.This way the streaming
is automated, anytime a object gets detected in S3 it is loaded to
Google Storage and all the components are loosely coupled so that
anytime we can replace the destination like Google Big query by just
switching the app name in Google App Engine.

## Technologies

AWS S3,
AWS Lambda,
OpenAPI 3.0.2,
GCP Cloudendpoint,
GCP App Engine,
GCP Coud Storage.

## Architecture

![architecture](images/architecuture-171.png)

## Progress

1. Created a AWS account/S3 bucket - Done.
1. Updated the .cloudmesh.yaml file with awss3 key pair - Done .
1. Debugged the Cloudmesh-Storage awss3.provdier.py and StorageABC.py 
   and got the put and list commands working for AWS S3- Done .
1. Uploded the files to S3 files using Cloudmesh commands(PUT and LIST) 
   -- Done . 
1. Created the GCP account and set up gsutil on the mac - Done .
1. Created the project and bucket and created the google application 
   credentials - Done 
1. Download the Google app credentials and set the authentication in 
   the environment variables - Done . 
1. Developed a flask application to read the data and load the data to 
   google cloud storage -Done 
1. Debugged the flask application in the local using POSTMAN - Done . 
1. Extend the flask application to read from the URL and get 
   the data downloaded from URL and load in to Google cloud storage 
   - In Progress.
1. Development of AWS Lambda application - Not Started . 

# Project Scope changed from streaming to AwsS3 to Local and Local to AwsS3

Professor wants to fix the AwsS3 Provider and add some new functionality
and test and benchmark the new chages. Now AwsS3 provider has been fixed
and and the new functionality(checking bucket exists, if not create
code) has been implemented in the provider. Pytests have been updated to
print out benchamarks and the code has been tested using Pytests and CMD
commands. All the code has been checked to Cloudmesh-Storage transfer
bucket and has been merged with master. Pytest have been changes again
to remove the hardcording for storage and process them as variables.

The documentation of cloud storage has been updated and ordered properly
and checked into cloudmesh-manual storage.md file

* <https://github.com/cloudmesh/cloudmesh-manual/blob/master/docs-source/source/storage/storage.md>

The code is available in 

* <https://github.com/cloudmesh/cloudmesh-storage/tree/master/cloudmesh/storage>

and there is also a working directory for this code

* <https://github.com/cloudmesh/cloudmesh-storage/tree/transfer/cloudmesh/storage/provider>

## Pytest Benchmark Results

* [Pytest test_storage_py benchmark results](../project/awss3storagebenchmarks.txt)
* [Pytest test_storage_local.py results](../project/localtest9.txt)
* [Pytest put and get benchmarks for 1.5GB file](../project/cloud-awss3-fa19-171.txt)
* [Pytest put and get benchmarks for 750MB file](../project/cloud-awss3-fa19-171-750MB.txt)
* [Benchmarks file using newly written test_storage_size.py](../project/storage-aws-fa19-516-171.txt)






