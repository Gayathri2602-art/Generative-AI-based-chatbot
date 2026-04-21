# app.py

from flask import Flask, render_template, request
from src.chatbot import get_qa_chain
import re

app = Flask(__name__)

# ✅ Initialize RAG QA chain (same as notebook)
qa = get_qa_chain(k=2)

# ----------------------------
# Home Route
# ----------------------------
@app.route("/")
def index():
    return render_template("chat.html")


# ----------------------------
# Chat Route
# ----------------------------
@app.route("/get", methods=["POST"])
def chat():
    try:
        msg = request.form.get("msg")

        if not msg:
            return "No input received!"

        # 🧹 Clean timestamps like 18:19
        msg = re.sub(r'\d{1,2}:\d{2}', '', msg).strip()

        print("User Query:", msg)

        # ✅ Invoke RAG
        result = qa.invoke({"query": msg})

        answer = result.get("result", "")

        # ✅ Safety fallback
        if not answer.strip():
            return "I don't know"

        return answer

    except Exception as e:
        print("❌ Error:", str(e))
        return "Something went wrong. Please try again."


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)