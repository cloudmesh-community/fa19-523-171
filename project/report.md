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

storage
=======

.. parsed-literal::

   Usage:
     storage [--storage=SERVICE] create dir DIRECTORY
     storage [--storage=SERVICE] get SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] put SOURCE DESTINATION [--recursive]
     storage [--storage=SERVICE] list [SOURCE] [--recursive] [--output=OUTPUT]
     storage [--storage=SERVICE] delete SOURCE
     storage [--storage=SERVICE] search  DIRECTORY FILENAME [--recursive] [--output=OUTPUT]
     storage [--storage=SERVICE] sync SOURCE DESTINATION [--name=NAME] [--async]
     storage [--storage=SERVICE] sync status [--name=NAME]
     storage config list [--output=OUTPUT]
     storage copy SOURCE DESTINATION [--recursive]


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

     sync SOURCE DESTINATION
       puts the content of source to the destination.
        If --recursive is specified this is done recursively from
           the source
        If --async is specified, this is done asynchronously
        If a name is specified, the process can also be monitored
           with the status command by name.
        If the name is not specified all date is monitored.

     sync status
       The status for the asynchronous sync can be seen with this
       command

     config list
       Lists the configures storage services in the yaml file

     storage copy SOURCE DESTINATION
       Copies files from source storage to destination storage.
       The syntax of SOURCE and DESTINATION is:
       SOURCE - awss3:source.txt
       DESTINATION - azure:target.txt

   Example:
      set storage=azureblob
      storage put SOURCE DESTINATION --recursive

      is the same as
      storage --storage=azureblob put SOURCE DESTINATION --recursive

      storage copy azure:source.txt oracle:target.txt


Here is the overview of functions.

1.) Create dir

2.)





*<https://github.com/cloudmesh/cloudmesh-manual/blob/master/docs-source/source/manual/storage.rst>

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

:o2: has account cereation and registering in the yaml file been discussed and tested/implemented. lots was done by a previous student

## Pytest Benchmark Results

* [Pytest test_storage_py benchmark results](../project/awss3storagebenchmarks.txt)
* [Pytest test_storage_local.py results](../project/localtest9.txt)
* [Pytest put and get benchmarks for 1.5GB file](../project/cloud-awss3-fa19-171.txt)
* [Pytest put and get benchmarks for 750MB file](../project/cloud-awss3-fa19-171-750MB.txt)
* [Benchmarks file using newly written test_storage_size.py](../project/storage-aws-fa19-516-171.txt)






