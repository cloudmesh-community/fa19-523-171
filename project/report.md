# Cloudmesh Storage Provider for AwsS3

Jagadeesh Kandimalla, fa19-516-171 

<https://github.com/cloudmesh-community/fa19-516-171>

[Contributors](https://github.com/cloudmesh-community/fa19-516-171/graphs/contributors)

The AWSS3 Storage Provider interacts with Cloudmesh Shell and The Storage functions
of the provider are available through Cloudmesh command line. The documentation
related the the Storage provider can be been in the below documentation link.

* Documentation: <https://cloudmesh.github.io/cloudmesh-manual/storage/storage.html>

The functions and the arguments given to the functions are explained in this API documentation.

* API: <https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.storage.provider.awss3.html>

The code should always be referred on the cloudmesh-storage module in the master branch

* Code: <https://github.com/cloudmesh/cloudmesh-storage/tree/master/cloudmesh/storage>

## Objective

The Objective was to completely fix the AWSS3 provider and create new functions wherever
needed(like Bucket exists and Bucket Create) and fix/create Pytests for storage and file sizes.
Size Pytests are used for benchmarking the functions with different size input files.

## Technologies


AWS S3(Amazon Simple Storage Service (Amazon S3) is an object storage service that
that offers industry-leading scalability, data availability, security, and performance.)

OpenAPI 3.0.2(An OPENAPI is an publicly available API that provides developers with 
Programmatic access to proprietary software application or web service)


## Architecture

![architecture](images/architecuture-171.png)


## AWSS3 to Local and Local to AWSS3  Storage Provider

AWSS3 Storage provider has implemented with the below functions.

Here is the Usage.

   Usage:
   
     storage [--storage=SERVICE] create dir DIRECTORY
     storage [--storage=SERVICE] get SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] put SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] list [SOURCE] [--recursive] [--output=OUTPUT]
     storage [--storage=SERVICE] delete SOURCE
     storage [--storage=SERVICE] search  DIRECTORY FILENAME [--recursive] [--output=OUTPUT]
     storage config list [--output=OUTPUT]
     
     
   This command does some useful things.
   
   Arguments:
   
     SOURCE        SOURCE can be a directory or file
     DESTINATION   DESTINATION can be a directory or file
     DIRECTORY     DIRECTORY refers to a folder on the cloud service


   Options:
   
     --storage=SERVICE  specify the cloud service name like aws or
                        azure or box or google

   Description:
   
     commands used to upload, download, list files on different
     cloud storage services.

     storage put [options..]
       Uploads the file specified in the filename to specified
       cloud from the SOURCEDIR.

     storage get [options..]
       Downloads the file specified in the filename from the
       specified cloud to the DESTDIR.

     storage delete [options..]
        Deletes the file specified in the filename from the
        specified cloud.

     storage list [options..]
       lists all the files from the container name specified on
       the specified cloud.

     storage create dir [options..]
       creates a folder with the directory name specified on the
       specified cloud.

     storage search [options..]
       searches for the source in all the folders on the specified
       cloud.

    
There are some additional functions available for other Storage Providers
 which can be found in the below link.


* <https://github.com/cloudmesh/cloudmesh-manual/blob/master/docs-source/source/manual/storage.rst>


The code is available in 

* <https://github.com/cloudmesh/cloudmesh-storage/tree/master/cloudmesh/storage>

In the Storage Provider directory both  for awss3 and local provider new code have been changed 
and existing code is modified.


The AWS Account creation has been provided in 

* <https://cloudmesh.github.io/cloudmesh-manual/accounts/aws.html>

The complete documentation and YAML file update we should do is in

* <https://cloudmesh.github.io/cloudmesh-manual/storage/storage.html>

The Pytests related to Awss3 and local are in 

* <https://github.com/cloudmesh/cloudmesh-storage/tree/master/tests>

The Pytests which should be run in the code are

test_storage.py
test_storage_local.py
test_storage_size.py




## Pytest Benchmark Results

* [Pytest test_storage_py benchmark results](../project/awss3storagebenchmarks.txt)
* [Pytest test_storage_local.py results](../project/localtest9.txt)
* [Pytest put and get benchmarks for 1.5GB file](../project/cloud-awss3-fa19-171.txt)
* [Pytest put and get benchmarks for 750MB file](../project/cloud-awss3-fa19-171-750MB.txt)
* [Benchmarks file using newly written test_storage_size.py](../project/storage-aws-fa19-516-171.txt)






