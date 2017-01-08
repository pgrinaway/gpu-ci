import boto


def lambda_handler(event, context):
    # TODO implement
    message_result = event['Records'][0]['Sns']['Message']
    print(message_result)

    return 'Hello from Lambda'