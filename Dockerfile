# Use latest TensorFlow image (make sure to update to version that supports AMD GPU)
FROM tensorflow/tensorflow:latest

# Set the working directory
WORKDIR /app

#Copy files into container. I guess . . means source = this directory and dest = this directory
COPY . . 

#Install additional python packages
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y git

#Install curl and gnupg (verifies signatures)
# RUN apt-get update && apt-get install -y curl gnupg software-properties-common \ 
#     #downloads bazel's public key for package verification, converts it to .gpg format that can be stored
#     && curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor -o /usr/share/keyrings/bazel-archive-keyring.gpg \
#     && curl -LO https://github.com/bazelbuild/bazelisk/releases/download/v1.15.0/bazelisk-linux-amd64 \
#     && chmod +x bazelisk-linux-amd64 \
#     && mv bazelisk-linux-amd64 /usr/local/bin/bazel
#note, docker does come with a web browser
#CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
CMD ["python", "emotion_classifier.py"]
