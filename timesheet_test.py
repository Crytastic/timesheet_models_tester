import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv
from difflib import SequenceMatcher

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT_EN = """You are a skilled text transformer that understands work descriptions in English and produces data records for a structured database."""

USER_PROMPT_TEMPLATE_EN = """
Transform the text given below into a CSV row semicolon separated in this exact format: "CLIENT;ACTIVITY;PROJECT;TIME SPENT;WORK DESCRIPTION"

Instructions:
* Always try to fill all attributes. If not possible, use a generic option or "N/A"
* CLIENT options: {clients}
* ACTIVITY options: {activities}
* PROJECT options: {projects}
* TIME SPENT format: HH:MM
* WORK DESCRIPTION: max 5 words

Text to process: {transcribed_text}
"""


def transcribe_audio(file_path: str, language='en') -> str:
    with open(file_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language
        )
    return transcript.text


def transform_to_timesheet(text: str, language='en',
                           clients="ACME Inc,Globex",
                           activities="Development,Meeting",
                           projects="Alpha,Beta") -> list:
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
