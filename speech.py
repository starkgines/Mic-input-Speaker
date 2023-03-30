import speech_recognition
import pyttsx3
import openai

print(speech_recognition.Microphone.list_microphone_names())

recognizer = speech_recognition.Recognizer()
openai.api_key = open("keys.txt", "r").read().strip("\n")

message_history = [
    {
        "role": "user",
        "content": "Eres un asistente  y haces lo que te dice tu dueño, responde OK si entiendes."
    },
    {
        "role": "assistant",
        "content": "OK"
    }
]


def predict(user_input):
    """"
    Predict next answer using chatgpt API
    :arg
        user_input (string): input of the user
    :return
        response: string with the last response of chatGPT
    """

    message_history.append({
        "role": "user",
        "content": f"{user_input}"
    })

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    # Just the reply text
    reply_content = completion.choices[0].message.content

    message_history.append({
        "role": "assistant",
        "content": f"{reply_content}"
    })

    return reply_content


def text_to_speech(input_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # set speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # set volume (float between 0 and 1)
    engine.say(input_text)
    engine.runAndWait()


while True:
    try:
        with speech_recognition.Microphone(device_index=1) as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language='es-ES')
            text = text.lower()
            chat_response = predict(text)
            print(f'speech recognized: {text}')
            print(f'chat response: {chat_response}')
            text_to_speech(chat_response)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
