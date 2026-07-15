import os
import boto3
from rembg import remove

os.environ['U2NET_HOME'] = '/tmp'
s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        record = event["Records"][0]
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        
        # DEBUG LINE
        print(f"DEBUG: Searching for Bucket: {bucket}, Key: {key}")

        input_obj = s3.get_object(Bucket=bucket, Key=key)
        input_bytes = input_obj["Body"].read()

        output_bytes = remove(input_bytes, session=None, post_process_mask=True, alpha_matting=False)
        
        output_key = f"final/{os.path.basename(key)}"
        s3.put_object(Bucket=bucket, Key=output_key, Body=output_bytes, ContentType="image/png")

        return {"statusCode": 200, "body": "Success"}
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise
