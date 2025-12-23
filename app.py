from flask import Flask, render_template, request
from modules.intent_parser import extract_project_type, extract_language
from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form.get("project_type")

        project_key = extract_project_type(user_input)
        language = extract_language(user_input)

        if project_key:
            result = {
                "project_type": project_key.replace("_", " ").title(),
                "language": language,
                "code": generate_code(project_key, language),
                "tests": generate_tests(project_key, language),
                "docs": generate_docs(project_key, language),
            }
        else:
            result = {
                "project_type": "Unknown Project",
                "language": "",
                "code": "❌ Could not detect project type from input.",
                "tests": "",
                "docs": "",
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
