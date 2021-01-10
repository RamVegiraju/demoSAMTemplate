import json

# import requests
####


def lambda_handler(event, context):
    textInput = event['input']
    print(textInput)

    return {
        "statusCode": 200,
        "body": textInput
    }

