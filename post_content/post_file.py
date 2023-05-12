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
    file_path = "/mnt/efs/test.txt"

    try:
        body = json.loads(event.get("body", "{}"))
        content = body.get("content", "")

        with open(file_path, "w") as file:
            file.write(content)

        response = {
            "statusCode": 200,
            "body": json.dumps({"message": f"Content {test()} saved to test.txt"}),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"message": "An error occurred: {}".format(str(e))}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    return response

