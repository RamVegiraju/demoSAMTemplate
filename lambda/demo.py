import json

# import requests
####


def lambda_handler(event, context):
    print("This is a test function with CFN")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
