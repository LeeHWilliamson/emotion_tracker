#This module will analyze user thoughts and label them according to the 27 emotions included on Google's goemotion research dataset
#I will utilize the tutorial here https://github.com/tensorflow/models/blob/master/research/seq_flow_lite/demo/colab/emotion_colab.ipynb to build the model
#I will use files and data from the google-research goemotion respository https://github.com/google-research/google-research/tree/master/goemotions

from transformers import DistilBertTokenizer, TFDistilBertModel
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = TFDistilBertModel.from_pretrained("distilbert-base-uncased")
text = "I am happy."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
print(output)