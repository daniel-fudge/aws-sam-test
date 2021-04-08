# aws-sam-test
A small repo to test creating a Lambda function with the SAM CLI.

The `lambda_handler.py` file contains the lambda function.   
The `template.yml` fle is the SAM template file used to create the lambda function.
You will need to update this file with the arn of your Lambda function role.   
The `requirements.txt` file is an empty Python requirements file that allows for local building and testing.

## Prerequisites
Before you can run this package you must have the associated IAM permissions and a S3 bucket to read and write to.  
In the following commands replace `<bucket>` with your S3 bucket name and a unique `<stack-name>`.   
You also need a Lambda role as created in [this](https://github.com/daniel-fudge/aws-s3-trigger) repo 
and update the `template.yml` file with this arn.

## Automated Build, Deploy & Remote Test
Executing the following command will build, deploy and remotely test the lambda function.  
```shell
bash deploy.bsh <bucket> <stack-name>
```
If successful you should see `Test successful` at end of script output
Please read the [deploy.bsh](deploy.bsh) file to see all of the individual commands.

## Manual Build, Deploy & Test
Note that all of these operations occur in the `package` folder so only these contents are deployed to AWS.
### Build
This command builds the CloudFormation package `.aws-sam` to be tested locally and deployed.
```shell
cd package
sam build
```

### Local Test
First start a local Lambda endpoint with this command.
```shell
sam local start-lambda
```
Then in a new terminal invoke the local lambda with this command.
```shell
rm response.json
aws lambda invoke \
  --function-name demo-sam-lambda \
  --endpoint-url "http://127.0.0.1:3001" \
  --payload '{"first_name": "Dan", "last_name": "the man"}' \
  --cli-binary-format raw-in-base64-out \
  --no-verify-ssl response.json
```
You should see a `200` status code and the `response.json` file should contain `{"message": "Hello Dan the man!"}`. 

### Deploy
This command deploys the CloudFormation template in `.aws-sam`, which creates the lambda function.  
```bash
sam deploy --stack-name <stack-name> --s3-bucket <bucket> --capabilities CAPABILITY_IAM
```

### Test deployed function
```shell
rm response.json
aws lambda invoke \
  --function-name demo-sam-lambda \
  --payload '{"first_name": "Dangerous", "last_name": "Dan"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```
You should see a `200` status code and the `response.json` file should contain `{"message": "Hello Dangerous Dan!"}`. 


## References
- [S3 Trigger Repo](https://github.com/daniel-fudge/aws-s3-trigger)
- [C++ Lambda Function with Python Handler](https://github.com/daniel-fudge/aws-lambda-cpp-python#make-iam-role-for-the-lambda-function)
- [Cloud9 C++ Lambda Repo](https://github.com/daniel-fudge/aws-lambda-cpp-cloud9)
- [AWS CLI - Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
- [AWS CLI - Add permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html)
- [AWS CLI - Invoke Lambda](https://docs.aws.amazon.com/cli/latest/reference/lambda/invoke.html#examples)
- [AWS CLI - Payload Error](https://stackoverflow.com/questions/60310607/amazon-aws-cli-not-allowing-valid-json-in-payload-parameter)
- [AWS S3 API](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification-configuration.html)
- [AWS Lambda Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
