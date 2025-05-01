# --- System Prompts ---
SYSTEM_PROMPT_EN = (
    "You are a skilled text transformer that understands work descriptions in English "
    "and produces data records for a structured database."
)

SYSTEM_PROMPT_CS = (
    "Jsi zkušený textový transformátor, který rozumí popisu práce v češtině "
    "a převádí je do strukturované databázové podoby."
)

# --- User Prompt Templates ---
USER_PROMPT_TEMPLATE_EN = """
Transform the text given below into a CSV row semicolon separated in this exact format: CLIENT;ACTIVITY;PROJECT;TIME SPENT;WORK DESCRIPTION

Instructions for the transformation:
* Always try to fill out all attributes. If it is not possible to extract from the text, use a generic option if available. If not, use "N/A"
* Use only following values in the CLIENT field: {clients}
* Use only following values in the ACTIVITY field: {activities}
* Use only following values in the PROJECT field: {projects}
* Convert the described work duration into hours and minutes
* The time format for TIME SPENT field is HH:MM (HOURS:MINUTES)
* Summarize the task into a WORK DESCRIPTION field, maximum 5 words. Make sure the description makes sense and is grammatically correct.
* Do not include any additional explanations or text in the output

Text to process: {transcribed_text}
"""

USER_PROMPT_TEMPLATE_CS = """
Převeď následující text do jednoho řádku CSV, odděleného středníkem, ve formátu: KLIENT;AKTIVITA;PROJEKT;STRÁVENÝ ČAS;POPIS PRÁCE

Instrukce:
* Vždy se snaž vyplnit všechna pole. Pokud to není možné, použij obecnou možnost, nebo "N/A".
* Povolené hodnoty pro KLIENT: {clients}
* Povolené hodnoty pro AKTIVITA: {activities}
* Povolené hodnoty pro PROJEKT: {projects}
* Čas zpracuj ve formátu HH:MM
* Popis práce shrň do max. 5 slov

Text ke zpracování: {transcribed_text}
"""
