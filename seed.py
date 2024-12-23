from app import db, Question, Choice


def seed_database():

    question1 = Question(question_text='What Python library is primarily used for building machine learning models?')
    db.session.add(question1)
    db.session.commit()

    choice1_q1 = Choice(question_id=question1.id, choice_text='Flask', is_correct=False)
    choice2_q1 = Choice(question_id=question1.id, choice_text='NumPy', is_correct=False)
    choice3_q1 = Choice(question_id=question1.id, choice_text='TensorFlow', is_correct=True)
    choice4_q1 = Choice(question_id=question1.id, choice_text='Django', is_correct=False)
    db.session.add(choice1_q1)
    db.session.add(choice2_q1)
    db.session.add(choice3_q1)
    db.session.add(choice4_q1)
    db.session.commit()

    question2 = Question( question_text='Which of the following Python libraries is used for data manipulation and analysis, especially in AI development?')
    db.session.add(question2)
    db.session.commit()

    choice1_q2 = Choice(question_id=question2.id, choice_text='Matplotlib', is_correct=False)
    choice2_q2 = Choice(question_id=question2.id, choice_text='Pandas', is_correct=True)
    choice3_q2 = Choice(question_id=question2.id, choice_text='PyTorch', is_correct=False)
    choice4_q2 = Choice(question_id=question2.id, choice_text='Scikit-learn', is_correct=False)
    db.session.add(choice1_q2)
    db.session.add(choice2_q2)
    db.session.add(choice3_q2)
    db.session.add(choice4_q2)
    db.session.commit()
    
    # Question 3: What is the primary purpose of the scikit-learn library in Python?
    question3 = Question(question_text='What is the primary purpose of the `scikit-learn` library in Python?')
    db.session.add(question3)
    db.session.commit()

    choice1_q3 = Choice(question_id=question3.id, choice_text='Image processing', is_correct=False)
    choice2_q3 = Choice(question_id=question3.id, choice_text='Data visualization', is_correct=False)
    choice3_q3 = Choice(question_id=question3.id, choice_text='Machine learning algorithms', is_correct=True)
    choice4_q3 = Choice(question_id=question3.id, choice_text='Natural Language Processing (NLP)', is_correct=False)
    db.session.add(choice1_q3)
    db.session.add(choice2_q3)
    db.session.add(choice3_q3)
    db.session.add(choice4_q3)
    db.session.commit()
    
    # Question 4: Which Python library is most commonly used for creating neural networks in AI?
    question4 = Question( question_text='Which Python library is most commonly used for creating neural networks in AI?')
    db.session.add(question4)
    db.session.commit()

    choice1_q4 = Choice(question_id=question4.id, choice_text='Keras', is_correct=True)
    choice2_q4 = Choice(question_id=question4.id, choice_text='OpenCV', is_correct=False)
    choice3_q4 = Choice(question_id=question4.id, choice_text='Flask', is_correct=False)
    choice4_q4 = Choice(question_id=question4.id, choice_text='Pillow', is_correct=False)
    db.session.add(choice1_q4)
    db.session.add(choice2_q4)
    db.session.add(choice3_q4)
    db.session.add(choice4_q4)
    db.session.commit()

    # Question 5: Which function in Python is used to split a dataset into training and testing sets for machine learning?
    question5 = Question( question_text='Which function in Python is used to split a dataset into training and testing sets for machine learning?')
    db.session.add(question5)
    db.session.commit()

    choice1_q5 = Choice(question_id=question5.id, choice_text='train_test_split()', is_correct=True)
    choice2_q5 = Choice(question_id=question5.id, choice_text='fit_predict()', is_correct=False)
    choice3_q5 = Choice(question_id=question5.id, choice_text='split_data()', is_correct=False)
    choice4_q5 = Choice(question_id=question5.id, choice_text='cross_validate()', is_correct=False)
    db.session.add(choice1_q5)
    db.session.add(choice2_q5)
    db.session.add(choice3_q5)
    db.session.add(choice4_q5)
    db.session.commit()


if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_database()