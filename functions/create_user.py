import json

def handle(event, context):
    return {
        "statusCode": 201,
        "body": json.dumps({"foo": "bar"})
    }