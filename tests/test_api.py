import requests

BASE_URL = "http://127.0.0.1:8000" # modify if your server runs on a different host/port


def print_separator(title: str):
    print("\n" + "=" * 20 + f" {title} " + "=" * 20)


def print_success(case, src, tgt, text, translated):
    print(f"[{case}] SUCCESS")
    print(f"  Input text      : {text}")
    print(f"  Source language : {src}")
    print(f"  Target language : {tgt}")
    print(f"  Translated text : {translated}")


def print_error(case, res):
    print(f"[{case}] ERROR")
    print(f"  Status code: {res.status_code}")
    try:
        detail = res.json()
    except Exception:
        detail = res.text
    print(f"  Detail     : {detail}")


# 1. Health check
def test_health():
    print_separator("HEALTH CHECK")
    res = requests.get(f"{BASE_URL}/health")

    if res.status_code == 200:
        print("[Health] SUCCESS:", res.json())
    else:
        print_error("Health", res)


# 2. Root
def test_root():
    print_separator("ROOT")
    res = requests.get(f"{BASE_URL}/")

    if res.status_code == 200:
        print("[Root] SUCCESS:", res.json())
    else:
        print_error("Root", res)


# 3. Valid translation (Vietnamese -> English)
def test_vi_to_en():
    print_separator("VI -> EN")

    text = "Xin chào, tôi là sinh viên"
    payload = {
        "inputs": text,
        "parameters": {
            "src_lang": "vietnamese",
            "tgt_lang": "english"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)

    if res.status_code == 200:
        data = res.json()
        print_success("VI->EN", "vietnamese", "english", text, data["translation_text"])
    else:
        print_error("VI->EN", res)


# 4. Valid translation (English -> Vietnamese)
def test_en_to_vi():
    print_separator("EN -> VI")

    text = "Machine learning is interesting"
    payload = {
        "inputs": text,
        "parameters": {
            "src_lang": "english",
            "tgt_lang": "vietnamese"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)

    if res.status_code == 200:
        data = res.json()
        print_success("EN->VI", "english", "vietnamese", text, data["translation_text"])
    else:
        print_error("EN->VI", res)


# 5. Valid translation (Russian -> English)
def test_ru_to_en():
    print_separator("RU -> EN")

    text = "Меня зовут Иван"
    payload = {
        "inputs": text,
        "parameters": {
            "src_lang": "russian",
            "tgt_lang": "english"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)

    if res.status_code == 200:
        data = res.json()
        print_success("RU->EN", "russian", "english", text, data["translation_text"])
    else:
        print_error("RU->EN", res)


# 6. Invalid language
def test_invalid_language():
    print_separator("INVALID LANGUAGE")

    payload = {
        "inputs": "Hello",
        "parameters": {
            "src_lang": "abcxyz",
            "tgt_lang": "english"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)
    print_error("Invalid Language", res)


# 7. Missing field
def test_missing_field():
    print_separator("MISSING FIELD")

    payload = {
        "parameters": {
            "src_lang": "english",
            "tgt_lang": "vietnamese"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)
    print_error("Missing Field", res)


# 8. Empty text
def test_empty_text():
    print_separator("EMPTY TEXT")

    payload = {
        "inputs": "",
        "parameters": {
            "src_lang": "english",
            "tgt_lang": "vietnamese"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)
    print_error("Empty Text", res)


# 9. Extra field (should be rejected due to extra='forbid')
def test_extra_field():
    print_separator("EXTRA FIELD")

    payload = {
        "inputs": "Hello",
        "parameters": {
            "src_lang": "english",
            "tgt_lang": "vietnamese"
        },
        "extra_field": "not allowed"
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)
    print_error("Extra Field", res)


# 10. Long text
def test_long_text():
    print_separator("LONG TEXT")

    text = "This is a long sentence. " * 20

    payload = {
        "inputs": text,
        "parameters": {
            "src_lang": "english",
            "tgt_lang": "vietnamese"
        }
    }

    res = requests.post(f"{BASE_URL}/translate/generate", json=payload)

    if res.status_code == 200:
        data = res.json()
        print_success("Long Text", "english", "vietnamese", text[:50] + "...", data["translation_text"][:50] + "...")
    else:
        print_error("Long Text", res)


if __name__ == "__main__":
    print("🚀 RUNNING API TESTS 🚀")

    test_health()
    test_root()

    test_vi_to_en()
    test_en_to_vi()
    test_ru_to_en()

    test_invalid_language()
    test_missing_field()
    test_empty_text()
    test_extra_field()

    test_long_text()