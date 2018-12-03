Automation for the People API
=====

Overview
-----

This repository contains application code to provision and run an application for the Automation for the People API. The REST api returns a json payload containing the current timestamp and a static message.

AWS Resources
-----

This application provisions two CloudFormation Stacks and configures the following AWS resources using CloudFormation Templates:

* S3 Bucket
* Api Gateway (Methods, Resources, Stages, Usage Plans, and Api Keys)
* Lambda Function
* IAM Roles

Prerequisites
-----

* An AWS account
* A Unix OS
* AWS Access Keys
  * To find/create your Access Keys, follow these [instructions](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) provided by AWS
* aws cli configured with your Access Keys
  * To configure the cli, follow these [instructions] (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
  * **NOTE:** The stack will be provisioned in the region of your choice, therefore, any region can be specified.
* python3
  * [Download Instructions](https://www.python.org/downloads/)
* boto3
* python3 unittest framework

#### OPTIONAL

You may change change the name of the S3 bucket in the paramaters.properties file. This will provision a bucket with the name that you specified. By default, it will provision a bucket with the name `automationforthepeoplepmartin` **NOTE:** The deploy will fail if the name is not unique. This is inteded as the destroy script **will** empty and destroy the bucket that is provisioned.

Deploying the API CloudFormation Stack
-----

To deploy the API Cloudformation Stack, run the ./deployStack.sh from within the deploy directory:

```bash
cd deploy
./deployStack.sh
```

This shell script performs the following:

1. Provisions a CloudFormation Stack (automation-for-the-people-storage) that includes an S3 Bucket for storing the compressed Lambda Function code.
2. Compresses awslambda/lambda_function.py to a .zip file and uploads it to the provisioned S3 Bucket
3. Provisions a CloudFormation Stack (automation-for-the-people) that includes an API Gateway Resource, API Gateway GET Method, API Gateway Usage Plan, an API Key, a Lambda function resource, and multiple roles to allow communication between the services.

Once the stack has finished provisioning, it will output the url api and the api key in the following format:

``` bash
ApiUrl: https://7temny3oci.execute-api.us-west-2.amazonaws.com/prod/api
ApiKey: cJPeQks72x2KsTidmbhKa7IwuNpQ2sVg3ysObLwL
```

Using the API
-----

To use the api, you can submit a GET request to the ApiUrl with the x-api-key header:

1. Use a a tool such as [Postman](https://www.getpostman.com/) to take the output ApiUrl and execute a GET request with the x-api-key header. 
2. Execute a curl command with the x-api-key header. Example: ```curl --header "x-api-key: cJPeQks72x2KsTidmbhKa7IwuNpQ2sVg3ysObLwL" https://7temny3oci.execute-api.us-west-2.amazonaws.com/prod/api ```

Testing
-----

To run all of the unit tests, from the root of the project directory, execute the command ```python -m unittest discover -v```

Cleanup
-----

To delete the API Cloudformation Stack, run ./deleteStack.sh from within the deploy directory:

```bash
cd deploy
./deleteStack.sh
```

This will cleanup the API stack, but **not** the S3 Storage Stack.

To delete the S3 Storage Stack, run ./deleteStorage.sh, with the name of the bucket as a command line argument, from within the deploy directory. This will empty the bucket, then delete the bucket, and finally delete the stack. This is to avoid accidental deletion of an s3 bucket or files.

```bash
cd deploy
./deleteStorage.sh automationforthepeoplepmartin
```

TODO
-----

Some future improvements for the project include:

* CloudWatch Metrics to monitor failed api requests and limitations
* Jenkins Pipeline to orchestrate testing following Cloudformation provisioning. 
