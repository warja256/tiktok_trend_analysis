import os
from openai import OpenAI

# Используем переменную окружения для API-ключа
client = OpenAI(api_key="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")
def generate_report(data_summary: str) -> str:
    """
    Генерация аналитического отчёта через ChatGPT.
    data_summary: строка с описанием данных (небольшой объём!)
    """
    prompt = f"Generate an English analytical report summarizing TikTok trends:\n{data_summary}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            timeout=30  # максимум 30 секунд на выполнение запроса
        )
        return response.choices[0].message.content
    except Exception as e:
        # Если возникла ошибка (таймаут, сеть и т.д.), возвращаем сообщение
        return f"AI report could not be generated due to error: {e}"
