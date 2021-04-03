# aws-sam-test
A small repo to test creating a Lambda function with the SAM CLI.

The `lambda_handler.py` file contains the lambda function.   
The `template.yml` fle is the SAM template file used to create the lambda function.   
The `requirements.txt` file is an empty Python requirements file that allows for local building and testing.


## Prerequisites
Before you can run this package you must have the associated IAM permissions and a S3 bucket to read and write to.  
In the following commands replace `<bucket>` with your S3 bucket name and a unique `<stack-name>`.

## Automated Build, Local Test, Deploy & Remote Test
Executing the following command will build, locally test, deploy and remotely test the lambda function.  
```bash
bash deploy.bsh <bucket> <stack-name>
```
Please read the [deploy.bsh](deploy.bsh) file to see all of the individual commands.


## Manual Package, Deploy & Test
### Build
This command builds the CloudFormation package `.aws-sam` to be tested locally.
```bash
sam build
```

### Local Test (FAILS, SEE ABOVE)
This command tests the Lambda function locally.
```bash
sam local invoke
```

### Deploy (FAILS, SEE ABOVE)
This command deploys the CloudFormation template in `.aws-sam`, which creates the lambda function.  
```bash
sam deploy --stack-name <stack-name> --s3-bucket <bucket> 
```
