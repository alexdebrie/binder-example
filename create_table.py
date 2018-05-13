import boto3

client = boto3.client('dynamodb')

try:
    resp = client.create_table(
        TableName="Test",
        AttributeDefinitions=[
            {
                "AttributeName": "Name",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "Name",
                "KeyType": "HASH"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)
