# prompts.py

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
