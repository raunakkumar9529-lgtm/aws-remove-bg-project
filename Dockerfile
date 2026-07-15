FROM public.ecr.aws/lambda/python:3.11

# Libraries install karo aur cache saaf karo
RUN yum update -y && \
    yum install -y gcc gcc-c++ zlib-devel libjpeg-devel libpng-devel && \
    yum clean all && \
    rm -rf /var/cache/yum

COPY lambda_function.py .
COPY requirements.txt .

# 🔥 Yahan dekho: Saari libraries ek saath aur --no-cache-dir ke saath
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.26.4 pillow opencv-python-headless==4.9.0.80 onnxruntime scipy==1.13.1 rembg==2.0.50 pymatting boto3

CMD ["lambda_function.lambda_handler"]
