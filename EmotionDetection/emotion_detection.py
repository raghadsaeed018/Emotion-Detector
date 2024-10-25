import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text":text_to_analyse} }

    response = requests.post(url, json=myobj, headers=header)

    fresponse = json.loads(response.text)


    if response.status_code == 200:
        emotions = {
            'anger': fresponse['emotionPredictions'][0]['emotion']['anger'],
            'disgust': fresponse['emotionPredictions'][0]['emotion']['disgust'],
            'fear': fresponse['emotionPredictions'][0]['emotion']['fear'],
            'joy': fresponse['emotionPredictions'][0]['emotion']['joy'],
            'sadness': fresponse['emotionPredictions'][0]['emotion']['sadness']
        }

        emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    elif response.status_code == 400 or response.status_code == 500:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions
