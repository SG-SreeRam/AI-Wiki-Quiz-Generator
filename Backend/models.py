from database import db
from sqlalchemy.dialects.postgresql import JSON

class WikiQuiz(db.Model):

    __tablename__="wiki_quiz"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), unique=True)
    title = db.Column(db.String(200))
    summary = db.Column(db.Text)
    quiz = db.Column(JSON)
    related_topics = db.Column(JSON)


    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "summary": self.summary,
            "quiz": self.quiz,
            "related_topics": self.related_topics
        }
