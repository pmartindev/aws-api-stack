#!/bin/sh -x

aws cloudformation deploy \
    --stack-name automation-for-the-people-storage  \
    --template-file storage.template \
    --parameter-overrides $(cat params.properties) \
    --capabilities CAPABILITY_IAM

python deployLambda.py

aws cloudformation deploy \
    --stack-name automation-for-the-people  \
    --template-file automationforthepeople.template \
    --parameter-overrides $(cat params.properties) \
    --capabilities CAPABILITY_IAM

python getApiKey.py