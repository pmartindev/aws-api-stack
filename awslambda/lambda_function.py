import json
import time

def lambda_handler(event, context):
    return {'message': "Automation for the people", 'timestamp': int(round(time.time()))}