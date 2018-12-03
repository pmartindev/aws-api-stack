#!/bin/sh -x

aws s3 rm s3://$1 --recursive
aws s3 rb s3://$1 --force

aws cloudformation delete-stack \
    --stack-name automation-for-the-people-storage