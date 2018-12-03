#!/usr/bin/env python3

import boto3
import zipfile
import os

def zipLambdaFunction(file):
    # ziph is zipfile handle
    zipName = 'lambda_function.zip'
    zipf = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
    zipf.write(file, os.path.basename(file))
    relativeZipPath = zipf.filename
    zipf.close()
    return relativeZipPath

def uploadToS3(path, s3Bucket):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(path, s3Bucket, os.path.basename(path))

def deleteZip(zipPath):
    os.remove(zipPath)

def paramsFileToList(paramFile):
    with open(paramFile) as f:
        paramLines = f.readlines()
    return paramLines

def getS3BucketFromParamsList(paramLines):
    for param in paramLines:
        param = param.split('=')
        if param[0] == 'S3Bucket':
            return param[1]

if __name__ == "__main__":   
    s3Bucket = getS3BucketFromParamsList(paramsFileToList('params.properties'))
    zipPath = zipLambdaFunction('../awslambda/lambda_function.py')
    uploadToS3(zipPath, s3Bucket)
    deleteZip(zipPath)