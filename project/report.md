**Ingest Live Streaming Data/Replicating Database using Logs**

fa19-516-171, Jagadeesh Kandimalla

**Objective:**

We will be ingesting data in real-time using AWS Services and Parse the data and load it in to database in abstract format/detailed(depending on the log which we are ingesting) for future processing.
CloudMesh will have a API which will subscribe to any realtime data and publish in the database by parsing.The Streaming may happen from On-premises to Cloud or in Cloud to Cloud , 
The steaming data can be anything if we choose photos as an example whenever the user uploads a photo in S3, 
and S3 events will trigger a message to send the photo to Queue the Queue will transfer it to the Database .

**Technologies:**

AWS Kinesis,
AWS Lambda,
OpenAPI 3.0.2,
REST,
Aurora/DynamoDB
