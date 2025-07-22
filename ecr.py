import boto3            ## i got it from here, you can also leearn  more from here https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr/client/create_repository.html

ecr_client = boto3.client('ecr')

repository_name = "my-cloud-app-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

# I just attempted to do a little with it, and have an idea of how it works, i still prefer my terraform approach, as this requires a lot of API calls, which may delay or throw me off the plan.