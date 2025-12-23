from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs
from modules.intent_parser import extract_project_type


def main():
    print("\n🤖 === Conversational GenAI Code Assistant ===")
    print("Describe the project you want to build (in natural language).\n")

    user_input = input("🧑 You: ")

    project_key = extract_project_type(user_input)

    if not project_key:
        print("\n❌ AI: Sorry, I couldn't identify the project type.")
        print("Try describing it using different keywords.")
        return

    print(f"\n🤖 AI: Detected project → '{project_key.replace('_', ' ')}'")
    print("Generating boilerplate code, tests, and documentation...\n")

    print("📌 ----- Generated Code -----\n")
    print(generate_code(project_key))

    print("\n🧪 ----- Generated Tests -----\n")
    print(generate_tests(project_key))

    print("\n📄 ----- Generated Documentation -----\n")
    print(generate_docs(project_key))

    print("\n✅ AI: Generation completed successfully!")


if __name__ == "__main__":
    main()
