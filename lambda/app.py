import json

# import requests
####


def lambda_handler(event, context):
    textInput = event['input']
    print(textInput)

    return {
        "statusCode": 200,
        "headers": {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": textInput
        }

