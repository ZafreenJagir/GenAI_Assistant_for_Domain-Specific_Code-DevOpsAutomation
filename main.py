from modules.intent_parser import extract_project_type, extract_language
from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs


def main():
    print("\n🤖 === Conversational GenAI Code Assistant ===\n")
    user_input = input("🧑 You: ")

    project_key = extract_project_type(user_input)
    language = extract_language(user_input)

    if not project_key:
        print("\n❌ Could not identify project type.")
        return

    print(f"\n🤖 Detected Project: {project_key}")
    print(f"💻 Language: {language}\n")

    print(generate_code(project_key, language))
    print(generate_tests(project_key, language))
    print(generate_docs(project_key, language))


if __name__ == "__main__":
    main()
