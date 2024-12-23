from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import os
app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.urandom(24)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    scores = db.relationship('UserScore', backref='user', lazy=True)
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Question(id={self.id}, question={self.question_text})>"
class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question = db.relationship('Question', backref=db.backref('choices', lazy=True))

class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)


@app.route('/', methods=['GET','POST'])
def index():
    questions = Question.query.all()
    if request.method == "POST":
        score = 0
        user_name = request.form.get('user_name', '').strip()
        user = User.query.filter_by(name=user_name).first()
        if not user:
            user = User(name=user_name)
            db.session.add(user)
            db.session.commit()
        session['user_id'] = user.id
        answers = {}
        for question in questions:
            selected_choice = request.form.get(f'question_{question.id}')
            if selected_choice:
                answers[question.id] = selected_choice

                correct_choice = Choice.query.filter_by(question_id=question.id, is_correct=True).first()
                if correct_choice and correct_choice.choice_text == selected_choice:
                    score +=1
        percentage = score / len(questions) * 100
        user_score = UserScore(user_id=user.id, score=percentage)
        db.session.add(user_score)
        db.session.commit()
        highest_score = db.session.query(db.func.max(UserScore.score)).filter_by(user_id=user.id).scalar()

        
        result = {
            "name": user_name,
            "score": percentage,
            "total": len(questions),
            "answers": answers,
        }
        return render_template('result.html', result=result, highest_score=highest_score)
    else:
        highest_score = 0
        user_id = session.get('user_id')
        if user_id:
            highest_score = db.session.query(db.func.max(UserScore.score)).filter_by(user_id=user_id).scalar()
            
        return render_template('index.html',questions=questions, highest_score=highest_score)


if __name__ == "__main__":
    app.run(debug=True)