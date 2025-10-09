from openai import OpenAI

client = OpenAI(
    api_key="ZbopIErY4JTTbyi2qMSA17bZxjLje3gI",
    base_url="https://api.mistral.ai/v1"  
)

def generate_report(data_summary: str) -> str:
    prompt = f"Generate an English analytical report summarizing TikTok trends:\n{data_summary}"

    try:
        response = client.chat.completions.create(
            model="mistral-large-latest", 
            messages=[{"role": "user", "content": prompt}],
            timeout=30
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI report could not be generated due to error: {e}"