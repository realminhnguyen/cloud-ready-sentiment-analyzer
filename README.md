# Cloud-Ready Sentiment Analyzer

This project is a web application that performs sentiment analysis on user-input text using machine learning techniques. It's designed to be cloud-ready and showcases skills in web development, Natural Language Processing (NLP), and cloud technologies.

## Features

- Web-based interface for text input
- Sentiment analysis using TextBlob
- AWS S3 integration (and tutorial) for result storage

## Technologies Used

- Python 3.11.9
- Flask for web application framework
- TextBlob for NLP and sentiment analysis
- Boto3 for AWS S3 interaction

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/realminhnguyen/cloud-ready-sentiment-analyzer.git
   cd cloud-ready-sentiment-analyzer
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   conda create -n sentiment-analysis-app python=3.11.9
   conda activate sentiment-analysis-app
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file and use your credentials (keep the single quotes):
    ```
    AWS_ACCESS_KEY_ID='YOUR_KEY'
    AWS_SECRET_ACCESS_KEY='YOUR_SECRET_KEY'
    AWS_REGION='your-region'
    AWS_BUCKET_NAME='your-bucket-name'
    ```
### AWS Setup Help (Extensive)

1. Create AWS Account, set up billing, etc.

2. Create an IAM User:
   - Go to the AWS IAM console
   
   ![Go to AWS IAM Console](Images/0.1-navtoIAMconsole.png)

   - Click "Users" in the left sidebar

   ![Click Users](Images/0.2-navtoUsers.png)
   
   - Click "Create User" 

   ![Click create User](Images/0.3-navtoCreateuser.png)

   - Name the user

   ![Name the user](Images/0.4-nameUser.png)

   - Set permissions and create a policy

   ![Set permissions](Images/0.5-setPermissions.png)

   - Make a new tab and search for s3 in AWS

   ![Search for S3 on AWS](Images/0.7-navtoS3.png)
   - Create a bucket in S3 so we can actually store data

   ![Create a Bucket](Images/0.8-createBucket.png)
   - Name the Bucket

   ![Name the Bucket](Images/0.9-nameBucket.png)
   - Back to creating a policy. Create policy using JSON format and use the created bucket name

   ![Create Policy](Images/1.0-createPolicy.png)
   - Review policy

   ![Review Policy](Images/1.1-reviewPolicy.png)
   - Attach policy to created user

   ![Attach Policy to User](Images/1.2-attachPolicy.png)
   - Navigate to created user's keys

   ![Nav to User Key](Images/1.3-navtoKey.png)
   - Select key

   ![Select Key type](Images/1.4-keySelect.png)
   - Create and copy keys to add into .env file

   ![Create Key](Images/1.5-keyCreated.png)
   

## Run the Application

1. Run the application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

### Results

- Landing page with user input (pos, neut, neg):

![Positive Sentiment](Images/SentimentPositive.png)
![Neutral Sentiment](Images/SentimentNeutral.png)
![Negative Sentiment](Images/SentimentNegative.png)

- "Analyze" button pressed. Successful upload:

![Successful Upload](Images/s3uploadSuccess.png)

- NOTE: If you don't have an S3 Bucket created, you will encounter an error:

![S3 Error](Images/s3error-nobucketoruser.png)

- We can verify it was uploaded to the S3 bucket:

![Checking results in bucket](Images/sentimentresultPage.png)

- Open the file:

![Opened result file](Images/sentimentResult.png)

And that conludes the project. Thank you for following along!

## Future Enhancements

- Add more advanced NLP techniques
- Implement user authentication and result history
- Implement Docker containerization for easy deployment


## License

This project is open source and available under the [MIT License](LICENSE).