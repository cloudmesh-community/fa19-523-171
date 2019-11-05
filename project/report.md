# Abstract Streaming interfaces for the NIST Big data Architecture

Jagadeesh Kandimalla, fa19-516-171 :o2:

:o2: Original title proposal was "Ingest Live Streaming Data/Replicating Database using Logs" whcih is too limited and does not showcase applicability on multiple clouds. However, this is easy to fix by developing a "register" like specification in OpenAPI just as we did for databases in the NIST document. YOu will have to look at 2 cloud providers to derive some common features. You could even describe how to much such dat between clouds. There are APIs and services that doe this. Provide a survey.

:o2: I like the idea of the queue, but you need to move forward, with an architecture diagram and code as well as potential tests to do this

The streaming service initial architecure is when a Object gets added to S3 ,An AWS Lambda function will get triggered and will call the Google cloud endpoint which inturn will call the APP engine where we write the data to Google cloud Storage


# Objective

The streaming service initial architecure is when a Object gets added to S3 and S3 event will trigger AWS Lambda function and the lambda will call the Google cloud endpoint which inturn will call the APP engine where we write the data to Google cloud Storage.This way the streaming is automated ,anytime a object gets detected in S3 it is loaded to Google Storage and all the components are loosely coupled so that anytime we can replace the destination like Google Big query by just switching the app name in Google App Engine.


# Technologies

AWS S3,
AWS Lambda,
OpenAPI 3.0.2,
GCP Cloudendpoint,
GCP App Engine,
GCP Coud Storage

# Architecture

![architecture](images/architecuture-171.png)

# Progress
1.) Create a AWS account

