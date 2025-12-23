"""
Module: intent_parser.py
Purpose: Extract project intent and programming language
         strictly aligned with dataset.json keys.
"""

PROJECT_KEYWORDS = {
    "calculator": ["calculator", "add", "subtract", "multiply", "divide"],
    "rest_api": ["api", "rest", "backend", "flask", "endpoint"],
    "todo_app": ["todo", "to-do", "task", "tasks"],
    "weather_app": ["weather", "forecast", "temperature"],
    "contact_manager": ["contact", "contacts", "phonebook"],
    "file_manager": ["file", "files", "directory", "folder"],
    "simple_chatbot": ["chatbot", "chat", "bot"],
    "banking_app": ["bank", "banking", "account", "deposit", "withdraw"],
    "blog_app": ["blog", "post", "article"],
    "quiz_app": ["quiz", "question", "answer"],
    "currency_converter": ["currency", "convert", "converter"],
    "text_editor": ["text editor", "editor", "write text"],
    "note_app": ["note", "notes", "notepad"],
    "simple_game": ["game", "guess"],
    "inventory_system": ["inventory", "stock", "items"],
    "password_checker": ["password", "password check"],
    "email_sender": ["email", "mail", "send email"],
    "number_guess_game": ["number guess", "guess number"],
    "simple_counter": ["counter", "increment", "decrement"]
}

# ✅ NEW (language support)
LANGUAGE_KEYWORDS = {
    "python": ["python", "py"],
    "c": ["c language", "c"],
    "java": ["java"],
    "javascript": ["javascript", "js", "node"]
}


def extract_project_type(user_input: str):
    user_input = user_input.lower()
    for project_key, keywords in PROJECT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in user_input:
                return project_key
    return None


# ✅ NEW FUNCTION
def extract_language(user_input: str):
    user_input = user_input.lower()
    for lang, keywords in LANGUAGE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in user_input:
                return lang
    return "python"  # default language
