import boto3
import json

SETTINGS = {
    "AWS_DEFAULT_REGION": "ap-northeast-2",
    "ENV": "prod"
}
def main():
    lambda_client = boto3.client('lambda', region_name=SETTINGS['AWS_DEFAULT_REGION'])

    payload = {
        "image_url": "https://picsum.photos/200/300"
    }

    ret = lambda_client.invoke(
        FunctionName="SampleApp",
        InvocationType="DryRun" if SETTINGS['ENV'] == "test" else "Event",
        Payload=json.dumps(payload)
    )
    print(ret)


if __name__ == "__main__":
    main()
