import os
from openai import OpenAI
from dotenv import load_dotenv
from difflib import SequenceMatcher
from prompts import SYSTEM_PROMPT_EN, USER_PROMPT_TEMPLATE_EN
from config import CLIENTS, ACTIVITIES, PROJECTS, LANGUAGE

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def transcribe_audio(file_path: str, language=LANGUAGE) -> str:
    with open(file_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language
        )
    return transcript.text


def transform_to_timesheet(text: str, clients=CLIENTS,
                           activities=ACTIVITIES,
                           projects=PROJECTS) -> list:
    user_prompt = USER_PROMPT_TEMPLATE_EN.format(
        clients=clients,
        activities=activities,
        projects=projects,
        transcribed_text=text
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_EN},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
        max_tokens=150
    )
    content = response.choices[0].message.content
    return [x.strip() for x in content.split(";")]


def similarity_score(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def evaluate(predicted: list, expected: list) -> dict:
    scores = [similarity_score(p, e) for p, e in zip(predicted, expected)]
    overall = sum(scores) / len(scores)
    return {
        "field_scores": {
            "Client": scores[0],
            "Activity": scores[1],
            "Project": scores[2],
            "Time Spent": scores[3],
            "Description": scores[4]
        },
        "overall_score": overall
    }
