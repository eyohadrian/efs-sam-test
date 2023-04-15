import json
import os

def test():
    file_path = "/mnt/efs/test.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            return content
    else:
        return "File does not exist."

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        "body": json.dumps({"content": test()}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
