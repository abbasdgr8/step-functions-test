# Test Step Function Service
A Proof of Concept that tries implementing an API and orchestrations using AWS Step Functions.


## Pre-Requisites
- You must have Python 2.7.1 installed and setup on your machine
- You must have an AWS Account with a Lambda subscription
- You must have Serverless 1.15.3 installed and setup on your machine - https://serverless.com/framework/docs/providers/aws/guide/installation/

## Deploy
In order to deploy, change your present working directory to the project directory and then simply run

```bash
serverless deploy
```

## States Language Reference
https://states-language.net/spec.html

## PoC Requirements
- Build an orchestration and expose it as an API endpoint using a State Machine
- The API must be synchronous in nature
- The orchestration must be resilient in nature
- The orchestration must be transactional and atomic
- The solution should provide great debugging, monitoring and logging functionalities

## Findings/Result
- Built a simple API chaining 3 lambdas in an orchestration call
- High level orchestrations can be specified in the serverless.yml file
- AWS Step Functions exposes the endpoint as a long-lived/asynchronous process. Currently, there is no way to build synchronous API calls using AWS Step Functions.
- High level business logic needs to be specified in the serverless.yml file. There might be limitations on doing complex business rules in the serverless.yml file
- Increased cost compared to Lambdas
- Not the ideal framework for building APIs. Good only for building long-lived processes, jobs, etc.