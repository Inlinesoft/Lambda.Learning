Copy all the libraries required to run the Lambda function (which you might find it in virtual environment folder)

'aws sqs send-message --region eu-west-1 --endpoint-url https://sqs.eu-west-1.amazonaws.com/ --queue-url https://sqs.eu-west-1.amazonaws.com/019179091045/lambda-queue --message-body "Hello from Amazon SQS 3."'
