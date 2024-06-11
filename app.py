import boto3
import botocore.config
import json

from datetime import datetime

def blog_generate_using_bedrock(blogtopic:str)-> str:
    prompt=f"""User: Write a 1000 words blog on the topic {blogtopic}\n
    Bot:
    """

    body={
        "inputText":prompt,
        "textGenerationConfig": {
            "maxTokenCount":3072,
            "stopSequences":[],
            "temperature":0.5,
            "topP":0.9
    }
    }

    try:
        bedrock=boto3.client("bedrock-runtime",region_name="<region_name>",
                             config=botocore.config.Config(read_timeout=3000,retries={'max_attempts':3}))
        response=bedrock.invoke_model(body=json.dumps(body),modelId="<model_id>")
        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        blog_details=response_data['results'][0]['outputText']
        
        return blog_details
    except Exception as e:
        print(f"Error generating the blog:{e}")
        return ""

def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body =generate_blog )
        print("Code saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")



def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    blogtopic=event['blog_topic']

    generate_blog=blog_generate_using_bedrock(blogtopic=blogtopic)

    if generate_blog:
        current_time=datetime.now().strftime('%H%M%S')
        s3_key=f"blog-output/{current_time}.txt"
        s3_bucket='<s3_bucket_name>'
        save_blog_details_s3(s3_key,s3_bucket,generate_blog)


    else:
        print("No blog was generated")

    return{
        'statusCode':200,
        'body':json.dumps('Blog Generation is completed')
    }

    



