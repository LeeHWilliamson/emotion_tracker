# Use latest TensorFlow image (make sure to update to version that supports AMD GPU)
FROM tensorflow/tensorflow:latest

# Set the working directory
WORKDIR /app

#Copy files into container. I guess . . means source = this directory and dest = this directory
COPY . . 

#Install additional python packages
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]