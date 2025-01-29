import requests
import json

# Конфигурация API Qwen
BASE_URL = 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions'
API_KEY = 'sk-03d336e812894c5e9a6669e34ca2f535'  # Твой ключ

def get_qwen_response(user_input):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        "model": "qwen",  # Указываем модель Qwen
        "input": user_input,
        "parameters": {
            "max_tokens": 100  # Максимальное количество токенов в ответе
        }
    }
    response = requests.post(BASE_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json().get('response', 'Не удалось получить ответ')
    else:
        return f'Ошибка при обращении к API: {response.status_code}'

# Пример использования функции
user_input = "Какой сегодня день?"
response = get_qwen_response(user_input)
print(response)
