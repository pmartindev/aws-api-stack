#!/usr/bin/env python3

import boto3 

def getCloudFormationResponse(stackName):
    cfClient = boto3.client('cloudformation')

    cftResponse = cfClient.describe_stacks(
        StackName = stackName
    )
    return cftResponse

def getApiIdFromCloudFormationResponse(cftResponse):
    outputs = cftResponse.get('Stacks')[0].get('Outputs')
    for output in outputs:
        outputKey = output.get('OutputKey')
        if outputKey == 'ApiId':
            apiId = output.get('OutputValue')
    return apiId

def getApiUrlFromCLoudFormationResponse(cftResponse):
    outputs = cftResponse.get('Stacks')[0].get('Outputs')
    for output in outputs:
        outputKey = output.get('OutputKey')
        if outputKey == 'ApiGatewayUrl':
            apiGatewayUrl = output.get('OutputValue')
    return apiGatewayUrl
    
def getApiKeyFromApiId(apiId):
    apiClient = boto3.client('apigateway')

    apiResponse = apiClient.get_api_key(
        apiKey=apiId, 
        includeValue=True
    )
    return apiResponse.get('value')

if __name__ == "__main__":
    response = getCloudFormationResponse('automation-for-the-people')
    apiId = getApiIdFromCloudFormationResponse(response)
    apiUrl =  getApiUrlFromCLoudFormationResponse(response)
    print('ApiUrl: ' + apiUrl + '/prod/api')
    print('ApiKey: ' + getApiKeyFromApiId(apiId))

