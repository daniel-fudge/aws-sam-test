def lambda_handler(event, context):
    print(event)
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
    print(message)
    return {'message': message}
