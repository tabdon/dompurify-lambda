import boto3
import json


def dom_purify(dirty_dom,
               region='us-west-2', lambda_name='DOMPurify'):

    client = boto3.client(
        'lambda',
        region_name=region,
        aws_access_key_id='',
        aws_secret_access_key=''
    )

    ready_json = {"dirty": dirty_dom}

    payload3=json.dumps(ready_json)

    response = client.invoke(
        FunctionName=lambda_name,
        InvocationType="RequestResponse",
        Payload=payload3
    )

    return json.loads(response['Payload'].read())