from flask import Flask, render_template, request, session
from ai_generator import generate_questions

app = Flask(__name__)
app.secret_key = "secret123"


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# FORM PAGE
# =========================
@app.route("/form")
def form():
    return render_template("form.html")


# =========================
# GENERATE TEST
# =========================
@app.route("/generate", methods=["POST"])
def generate():

    session["name"] = request.form["name"]
    session["stream"] = request.form["stream"]
    session["course"] = request.form["course"]
    session["specialization"] = request.form["specialization"]
    session["year"] = request.form["year"]
    session["difficulty"] = request.form["difficulty"]

    # ✅ FIX IS HERE (5 PARAMETERS)
    questions = generate_questions(
        session["stream"],
        session["course"],
        session["specialization"],
        session["year"],
        session["difficulty"]
    )

    session["questions"] = questions

    return render_template("test.html", questions=questions)
# ===============================
# 🧠 SKILL ANALYSIS ENGINE
# ===============================
def analyze_skills(questions, answers):

    strength = []
    weakness = []
    gained = []

    for i, q in enumerate(questions):

        selected = answers.get(f"q{i}")
        topic = q.get("topic", "General")
        correct = q.get("correct_answer_index", 0)

        try:
            if selected is not None and int(selected) == correct:
                gained.append(topic)

                if topic not in strength:
                    strength.append(topic)
            else:
                if topic not in weakness:
                    weakness.append(topic)

        except:
            # safety fallback
            if topic not in weakness:
                weakness.append(topic)

    return strength, weakness, gained


# ===============================
# 📊 IMPROVEMENT PLAN
# ===============================
def improvement_plan(weakness):

    if not weakness:
        return ["Keep practicing advanced problems"]

    plan = []

    for w in weakness:
        plan.append(f"Revise {w} fundamentals and practice 5–10 problems daily")

    plan.append("Take mixed difficulty mock tests")
    plan.append("Focus on accuracy before speed")

    return plan


# ===============================
# 📊 LEVEL CALCULATION
# ===============================
def performance_level(score_percent):

    if score_percent >= 80:
        return "Advanced"
    elif score_percent >= 50:
        return "Intermediate"
    else:
        return "Beginner"


# ===============================
# SUBMIT + REPORT
# ===============================
@app.route("/submit", methods=["POST"])
def submit():

    questions = session.get("questions", [])
    answers = request.form

    if not questions:
        return "No questions found. Please generate test again."

    score = 0

    for i, q in enumerate(questions):

        selected = answers.get(f"q{i}")

        try:
            if selected is not None and int(selected) == q.get("correct_answer_index", 0):
                score += 1
        except:
            pass

    total = len(questions)
    percent = int((score / total) * 100) if total > 0 else 0

    # Skill analysis
    strength, weakness, gained = analyze_skills(questions, answers)
    plan = improvement_plan(weakness)
    level = performance_level(percent)

    return render_template(
        "skill_report.html",
        name=session.get("name"),
        stream=session.get("stream"),
        course=session.get("course"),
        specialization=session.get("specialization"),  # ✅ added
        score=percent,
        total=total,
        level=level,
        strength=strength,
        weakness=weakness,
        gained=gained,
        plan=plan
    )


# ===============================
# RUN APP
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)