Repository to help train the creation of terraform resources.

Requirements: Start localstack with docker

## Commands
#### Install local terraform
```
pip install terraform-local
```

#### Init Local terraform
```
tflocal init -upgrade
```

#### Plan Local terraform
```
tflocal apply
```

#### Apply Local terraform
```
tflocal apply
```

#### Start Localstack
```
docker-compose up
```

# Validate created resources
Inside  your docker localstack cli, run a command to see if your resource was created:

https://github.com/liniribeiro/terraform-localstack/assets/10133177/b6306b44-1e70-427a-9523-1b190365d19e

Commands: 
```
 awslocal s3 ls
 awslocal dynamodb list-tables
 etc..
 ```

# Useful Links

- [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [terraform-local](https://github.com/localstack/terraform-local)
- [Localstack](https://docs.localstack.cloud/overview/)
