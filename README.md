# Mic-input-Speaker

This is a project to talk directly to ChatGPT with input mic and voice output 

to used the respositroy install all dependency with 

```pip install -r requirements.txt```


# API 
To used the api you need a apikey from openAI create a key.txt and copy and paste inside the key

You can list all microphone with and then select the index of the selected mic: 

```
# list all available microphones
print(sr.Microphone.list_microphone_names())  

# search and change this part of the code with the correct index in this case mi main mic is in the index 1

speech_recognition.Microphone(device_index=1)

```

If you have you own key file replace this 

```
openai.api_key = open("path_of_youkeys.txt", "r").read().strip("\n")

```

# todo
* Implement a more eficiently way to make the speech to text
* Implement the way to change the output voice
