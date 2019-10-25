# Abstract Streaming interfaces for the NIST Big data Architecture

Jagadeesh Kandimalla, fa19-516-171 :o2:

:o2: Original title proposal was "Ingest Live Streaming Data/Replicating Database using Logs" whcih is too limited and does not showcase applicability on multiple clouds. However, this is easy to fix by developing a "register" like specification in OpenAPI just as we did for databases in the NIST document. YOu will have to look at 2 cloud providers to derive some common features. You could even describe how to much such dat between clouds. There are APIs and services that doe this. Provide a survey.

:o2: I like the idea of the queue, but you need to move forward, with an architecture diagram and code as well as potential tests to do this

The streaming service initial architecure is when a Object gets added to S3 ,An AWS Lambda function will get triggered and will call the Google cloud endpoint which inturn will call the APP engine where we write the data to Google cloud Storage

# Objective

We will be ingesting data in real-time using AWS Services and Parse the data and load it in to database in abstract format/detailed(depending on the log which we are ingesting) for future processing.
CloudMesh will have a API which will subscribe to any realtime data and publish in the database by parsing.The Streaming may happen from On-premises to Cloud or in Cloud to Cloud , 
The steaming data can be anything if we choose photos as an example whenever the user uploads a photo in S3, 
and S3 events will trigger a message to send the photo to Queue the Queue will transfer it to the Database .

# Technologies

AWS S3,
AWS Lambda,
OpenAPI 3.0.2,
GCP Cloudendpoint,
GCP App Engine,
GCP Coud Storage

# Architecture

project/Project.pptx


