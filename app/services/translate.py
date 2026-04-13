import os
import requests

from fastapi import HTTPException

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/mbart-large-50-many-to-many-mmt"
headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}

def query(payload):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        except:
            raise HTTPException(status_code=404, detail='Server error')

def translate(request):
    output = query(request)[0]
    return output

if __name__ == "__main__":
    request_dict = {
        "inputs": "Меня зовут Вольфганг и я живу в Берлине",
        "parameters": {
            "src_lang": "ru_RU",
            "tgt_lang": "en_XX"
        }
    }
    output = translate(request_dict)
    print(output)