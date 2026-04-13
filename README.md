# Report Homework 1: APPLICATION PROGRAMMING INTERFACE

- Name: Võ Lân Tuấn
- ID: 24120240  
- Class: 24CTT3

## Models
- Name: mbart-50
- URL: [Model link](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)

**Why this model?**
1. It is a many-to-many language model that supports 50 languages, including Vietnamese and English.
2. It has only 0.6B parameters, so inference is relatively fast.
3. It has HF Inference Provider.


## System
This system is for multilingual translation.

Supported languages:
- The model supports 50 languages from mBART-50.
- This API accepts language aliases such as `vietnamese`, `english`, `russian`, `japanese`, and many others.
- The full supported language map is defined in `app/schemas/translate.py`.

Main functionality:
- Translate text between supported languages (for example, Vietnamese to English).
- Test endpoints directly in Swagger UI.

## Installation
**Requirements**
- Python >= 3.11
- uv (recommended) or pip

Current package versions in this project:
- fastapi==0.135.3
- pydantic==2.12.5
- uvicorn==0.44.0
- And other dependencies in `requirements.txt`/`pyproject.toml`

**Step 1:** Clone this project, then `cd translator`.
**Step 2:**
- Option 1 (recommended, with `uv`):
  1. Make sure `uv` is installed and available.
  2. Run `uv sync --frozen` to install exactly what is defined in `uv.lock`.
  3. Activate the virtual environment: `source .venv/bin/activate`.
- Option 2 (with `pip`):
  1. Create a virtual environment: `python -m venv .venv`.
  2. Activate it: `source .venv/bin/activate`.
  3. Install dependencies: `pip install -r requirements.txt`.

## How to run
**Step 1:** Create your Hugging Face token: [Generate token](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained)

**Step 2:** Export the token to your environment:
`export HF_TOKEN=YOUR_HF_TOKEN_HERE`

Check the HF_TOKEN:
`echo $HF_TOKEN`

**Step 3:** Stay in `translator/` and run:
`uvicorn app.main:app --reload`

The default port is `8000`, and `--reload` enables auto-reload.

## How to call API? Examples request/response
**Step 1:** Open your browser and go to https://localhost:8000/docs to access Swagger UI.
**Step 2:** Test the available APIs:

- `/`: root endpoint
- `/health`: health check
- `/translate/generate`: translation endpoint

**Example 1:** Vietnamese -> English
Request:
```
{
  "inputs": "Xin chào, tôi là sinh viên",
  "parameters": {
    "src_lang": "vietnamese",
    "tgt_lang": "english"
  }
}
```
Response (200):
```
{
  "translation_text": "Hello, I am a student"
}
```

**Example 2:** English -> Vietnamese
Request:
```
{
  "inputs": "Machine learning is interesting",
  "parameters": {
    "src_lang": "english",
    "tgt_lang": "vietnamese"
  }
}
```
Response (200):
```
{
  "translation_text": "Học máy rất thú vị"
}
```

**Example 3:** Russian -> English
Request:
```
{
  "inputs": "Меня зовут Иван",
  "parameters": {
    "src_lang": "russian",
    "tgt_lang": "english"
  }
}
```
Response (200):
```
{
  "translation_text": "My name is Ivan"
}
```

More examples are in `tests/test_api.py`.

## Demo
- [Youtube](https://www.youtube.com/watch?v=gmQ_VnoySZU)