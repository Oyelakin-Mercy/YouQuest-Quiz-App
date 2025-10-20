from flask import Flask, render_template, request, redirect, url_for, session
import requests, html

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

@app.route('/')
def index():
    # Fetch available categories from API
    category_url = "https://opentdb.com/api_category.php"
    categories = requests.get(category_url).json().get("trivia_categories", [])

    difficulties = ["easy", "medium", "hard"]
    types = ["multiple", "boolean"]

    return render_template("index.html", categories=categories, difficulties=difficulties, types=types)

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    category = request.form.get("category", "")
    difficulty = request.form.get("difficulty", "")
    q_type = request.form.get("type", "")
    amount = request.form.get("amount", "5")

    url = f"https://opentdb.com/api.php?amount={amount}"
    if category:
        url += f"&category={category}"
    if difficulty:
        url += f"&difficulty={difficulty}"
    if q_type:
        url += f"&type={q_type}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
    except Exception as e:
        print("Error fetching API:", e)
        return "Error fetching quiz questions. Please try again later."

    if data.get("response_code") != 0:
        print("API returned non-zero response:", data)
        return "Error fetching quiz questions. Please try again."

    questions = []
    for item in data["results"]:
        all_answers = item["incorrect_answers"] + [item["correct_answer"]]
        all_answers = sorted(all_answers)
        questions.append({
            "question": html.unescape(item["question"]),
            "answers": [html.unescape(a) for a in all_answers],
            "correct": html.unescape(item["correct_answer"])
        })

    session["quiz"] = questions
    return render_template("quiz.html", quiz={"questions": questions})

# RESULT PAGE
@app.route('/result')
def result_page():
    score = session.get("score", 0)
    quiz = session.get("quiz", [])
    total = len(quiz)
    return render_template("results.html", score=score, total=total)


# REVIEW PAGE
@app.route('/review')
def review_page():
    results = session.get("results", [])
    score = session.get("score", 0)
    total = len(session.get("quiz", []))
    return render_template("review.html", results=results, score=score, total=total)


# RESTART QUIZ
@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))

# SUBMIT QUIZ
@app.route('/submit', methods=['POST'])
def submit():
    quiz = session.get("quiz", [])
    score = 0
    results = []

    for i, q in enumerate(quiz):
        user_answer = request.form.get(f"answer_{i}")
        correct_answer = q["correct"]
        if user_answer == correct_answer:
            score += 1

        results.append({
            "question": q["question"],
            "answers": q["answers"],
            "correct": correct_answer,
            "user_answer": user_answer
        })

    session["results"] = results
    session["score"] = score

    return redirect(url_for("result_page"))


if __name__ == '__main__':
    app.run(debug=True)

