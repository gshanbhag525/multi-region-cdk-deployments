import json
def handler(event, context):    
    body = {
        'message': "lambda created"
    }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }


