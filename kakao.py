import os
import json
import requests

def sendToMeMessage(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

text = "Hello, This is KaKao Message Test!!("+os.path.basename(__file__).replace(".py", ")")

#KAKAO_TOKEN = "48e8ad8538596d181d4dfaee1c49218f"
KAKAO_TOKEN = "OOm7Z9NfgFwI4_CzBSqxvHKuV_q0CLQISRrY0go9dJcAAAF5l9OLiw"

print(sendToMeMessage(text).text)
