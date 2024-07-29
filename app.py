from flask import Flask, request, jsonify, render_template 
'''
Flask is used to create the web application. Request is used to handle incoming requests. 
jsonify is used to return JSON responses. render_template is used to render HTML templates.
'''
from textblob import TextBlob # Textblob is used to perform sentiment analysis on the text
import boto3 # boto3 is used to interact with AWS services using python
from botocore.exceptions import ClientError # ClientError is used to handle exceptions
import os # os is used to access environment variables
from dotenv import load_dotenv # load_dotenv is used to load environment variables from .env file

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize AWS S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                  region_name=os.getenv('AWS_REGION'))  # Getting the AWS credentials from the environment variables

@app.route('/')
def home(): 
    return render_template('index.html') # Render the HTML template

@app.route('/analyze', methods=['POST']) # This route is used to analyze the sentiment of the text
def analyze_sentiment():
    data = request.json # Get the JSON data from the request
    text = data['text'] # Extract the text from the JSON data
    
    # Perform sentiment analysis
    analysis = TextBlob(text) # Calling the TextBlob function to analyze the sentiment of the text
    sentiment = analysis.sentiment.polarity # Getting the sentiment polarity from the analysis. sentiment.polarity returns a value between -1 and 1
    
    # Determine sentiment category
    if sentiment > 0:
        category = "Positive"
    elif sentiment < 0:
        category = "Negative"
    else:
        category = "Neutral"
    
    # Store result in S3
    bucket_name = os.getenv('AWS_BUCKET_NAME')  # Getting the bucket name from the environment variables
    if bucket_name: # Checking if the bucket name is set
        try:
            s3.put_object(Bucket=bucket_name,   # Storing the result in the S3 bucket using put_object method
                          Key=f'result_{data["id"]}.txt',   # Setting the key of the object
                          Body=str(sentiment))  # Setting the body of the object
            print(f"Successfully stored result in S3 bucket: {bucket_name}")    # Printing the success message
        except ClientError as e:    # Handling the exception
            print(f"Error storing result in S3: {str(e)}")  # Printing the error message
    else:
        print("AWS_BUCKET_NAME not set. Skipping S3 storage.")  # Printing the message if the bucket name is not set
    
    return jsonify({
        'sentiment': sentiment,
        'category': category
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # Running the application in debug mode on host