import boto3


def get_user(user_id):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("luftdaten-skill-users")

    result = table.get_item(
        Key={
            "user_id": user_id
        }
    )

    return result.get("Item")


def add_user(user_id):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("luftdaten-skill-users")

    table.put_item(
        Item={
            "user_id": user_id
        }
    )


def set_sensor_id(user_id, sensor_id):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("luftdaten-skill-users")

    table.update_item(
        Key={
            "user_id": user_id
        },
        UpdateExpression="set sensor_id=:s",
        ExpressionAttributeValues={
            ":s": sensor_id
        },
        ReturnValues="UPDATED_NEW"
    )
