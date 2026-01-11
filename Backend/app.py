import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_wikipedia
from quiz_generator import generate_quiz
from database import db
from models import WikiQuiz
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/api/generate", methods=["POST"])
def generate():
    try:
        url = request.json.get("url")
        print("URL RECEIVED:", url)

        # 1️⃣ CHECK IF URL ALREADY EXISTS
        existing = WikiQuiz.query.filter_by(url=url).first()
        if existing:
            return jsonify(existing.to_dict())

        # 2️⃣ SCRAPE & GENERATE
        scraped = scrape_wikipedia(url)
        quiz_data = generate_quiz(scraped["text"])

        record = WikiQuiz(
            url=url,
            title=scraped["title"],
            summary=scraped["text"][:500],
            quiz=quiz_data["quiz"],
            related_topics=quiz_data["related_topics"]
        )

        db.session.add(record)
        db.session.commit()

        return jsonify(record.to_dict())

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Quiz already exists for this URL"}), 409

    except Exception as e:
        print("ERROR IN /api/generate:", str(e))
        return jsonify({"error": str(e)}), 400




@app.route("/api/history", methods=["GET"])
def history():
    quizzes = WikiQuiz.query.all()
    return jsonify([
        {
            "id": q.id,
            "url": q.url,
            "title": q.title,
            "summary": q.summary,
            "quiz": q.quiz,
            "related_topics": q.related_topics
        }
        for q in quizzes
    ])


if __name__ == "__main__":
    app.run(debug=True)
