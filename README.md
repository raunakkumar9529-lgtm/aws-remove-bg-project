Remove Background Web Application (AWS Powered)

Yeh ek Flask-based web application hai jo images ka background remove karne ke liye AWS S3 (Storage) aur AWS Lambda (Processing) ka use karti hai.


🚀 Deployment Instructions (End-to-End)

Is project ko live karne ke liye niche diye gaye steps ko sequence mein follow karein:-

### 1. AWS S3 Setup (Storage)

1. S3 Bucket Banayein:- AWS Console mein jaakar S3 service kholein aur 'Create bucket' par click karein.

2. Naming:- Bucket ko ek unique naam dein (e.g., my-bg-remover-bucket-2026).

3. Permissions:- Bucket settings mein jaakar "Block all public access" ko uncheck karein (taaki images upload ho sakein).

4. Bucket Policy:- Bucket ke 'Permissions' tab mein jaakar bucket policy set karein taaki Lambda isse access kar sake.


### 2. AWS Lambda Setup (Processing)

1. Function Create Karein: Lambda service mein jayein aur 'Create function' par click karein.

2. Runtime:- Python 3.x select karein.
   
3. Code Upload:- Apna lambda_function.py wahan upload karein.

4. Environment Variables:- Lambda ke 'Configuration' tab mein S3_BUCKET_NAME aur AWS_ACCESS_KEY/SECRET_KEY set karein.

5. Timeout:- 'General configuration' mein jaakar timeout ko 30 seconds ya usse zyada set karein (taaki badi image process ho sake).


### 3. Local Development Setup

Aapke system mein Python aur Git installed hona chahiye.

# 1. Clone the repository
git clone https://github.com/raunakkumar9529-lgtm/aws-remove-bg-project.git
cd aws-remove-bg-project

# 2. Virtual Environment Setup
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt


4. Application Configuration

1. Credentials:- Project folder mein ek .env file banayein aur apne AWS credentials yahan save karein:-

AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here
S3_BUCKET_NAME=your_bucket_name


2. Run Application:-

```
python app.py
```


3. Access:- Browser mein [http://127.0.0.1:5000] kholein.


🛠 Tech Stack

* **Backend:-** Python, Flask
* **Cloud Storage:-** AWS S3
* **Serverless:-** AWS Lambda
* **Version Control:-** Git & GitHub


### ⚠️ Important Note

Apne AWS IAM user ko S3FullAccess aur LambdaFullAccess ki policies zaroor attach karein.
.env file ko kabhi bhi public repository par push na karein (.gitignore zaroor set karein).
