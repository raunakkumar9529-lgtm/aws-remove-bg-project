from flask import Flask, request, send_file, render_template, jsonify
import boto3
import io, os, time, uuid
from botocore.exceptions import ClientError

app = Flask(__name__)
s3 = boto3.client("s3")
BUCKET_NAME = "remove-bg-project-adarsh"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    try:
        if "image" not in request.files:
            return jsonify({"error":"No image uploaded"}),400
        file=request.files["image"]
        if file.filename=="":
            return jsonify({"error":"Empty file"}),400
        ext=os.path.splitext(file.filename)[1] or ".png"
        name=f"{uuid.uuid4().hex}{ext}"
        ok=f"original/{name}"
        fk=f"final/{name}"
        s3.put_object(Bucket=BUCKET_NAME,Key=ok,Body=file.read(),ContentType=file.mimetype or "application/octet-stream")
        end=time.time()+180
        while time.time()<end:
            try:
                s3.head_object(Bucket=BUCKET_NAME,Key=fk)
                break
            except ClientError as e:
                if e.response["Error"]["Code"] not in ("404","NoSuchKey","NotFound"):
                    raise
                time.sleep(2)
        else:
            return jsonify({"error":"Timed out waiting for Lambda output"}),504
        obj=s3.get_object(Bucket=BUCKET_NAME,Key=fk)
        b=io.BytesIO(obj["Body"].read()); b.seek(0)
        return send_file(b,mimetype="image/png",as_attachment=True,download_name="no-bg.png")
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
