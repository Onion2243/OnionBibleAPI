from flask import jsonify

def Sarah_Questions(topic, question):
    Questions = [
        "1. Whose Daughter Was Sarah?",  # 0
        "1B. Whose Wife?",  # 1
        "1C. Half-Sister?",  # 2
        "2. What Of Her Appearance?",  # 3
        "3. What Near Tragedy Did This Cause ?",  # 4
        "4. What Affliction Did She Have?",  # 5
        "5. How Did She Try To Solve Her Problem",  # 6
        "6. How Did This Work Out",  # 7
        "7. When And Why Was Her Named Changed From SARA (Contentious) To SARAH (Princess)",  # 8
        "8. Why Did The Lord Rebuke Sarah In Genesis",  # 9
        "9. Who Was Her Illustrious Son?",  # 10
        "9B. Why Did She Name Him 'Laughter'?",  # 11
        "10. How Is Sarah Used To Teach A Lesson In Galatians?",  # 12
        "11. How Old Was Sarah At Her Death?",  # 13
        "12. How Did Her Passing Effect Abraham?",  # 14
        "13. Where Was She Buried?",  # 15
    ]
    question_map = {
        "Question1": 0,
        "Question1B": 1,
        "Question1C": 2,
        "Question2": 3,
        "Question3": 4,
        "Question4": 5,
        "Question5": 6,
        "Question6": 7,
        "Question7": 8,
        "Question8": 9,
        "Question9": 10,
        "Question9B": 11,
        "Question10": 12,
        "Question11": 13,
        "Question12": 14,
        "Question13": 15,
    }
    # Gets The Question And Its Index Out Of The Question Map
    question = question_map.get(question)

    # Only Runs If Question Is Not None And Is Smaller Than The Length Of The Questions
    if question is not None and question < len(Questions):
        return jsonify({f"{topic}, {question}": Questions[question]})