# SAM - Lambda with Layer sample

Sample SAM CloudFormation Template with Lambda using Layer

## Package
```bash
sam package --template-file template.yaml --s3-bucket <S3-BUCKET-NAME> \
--output-template-file packaged.yaml --region <AWS_REGION>
```

## Deploy
```bash
sam deploy --template-file ./packaged.yaml \
--stack-name <CFN-STACK-NAME> --capabilities CAPABILITY_IAM 
```