import boto3
import os
from botocore.exceptions import ClientError

class DynamoDBRepository:
    def __init__(self):
        self.table_name = os.environ.get("TABLE_NAME", "LawyerTasks")
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)

    def save(self, task_data: dict):
        try:
            self.table.put_item(Item=task_data)
            return True
        except ClientError as e:
            print(f"Erro ao salvar no DynamoDB: {e.response['Error']['Message']}")
            raise e
            
    def get_by_id(self, task_id: str):
        response = self.table.get_item(Key={"id": task_id})
        return response.get("Item")
    
    def list_all(self):
        response = self.table.scan()
        return response.get("Items", [])

    def update(self, task_id: str, update_data: dict):
        update_expr = "SET " + ", ".join([f"#{k} = :{k}" for k in update_data.keys()])
        attr_names = {f"#{k}": k for k in update_data.keys()}
        attr_values = {f":{k}": v for k, v in update_data.items()}

        self.table.update_item(
            Key={"id": task_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=attr_names,
            ExpressionAttributeValues=attr_values,
            ConditionExpression="attribute_exists(id)"
        )

    def delete(self, task_id: str):
        self.table.delete_item(Key={"id": task_id})