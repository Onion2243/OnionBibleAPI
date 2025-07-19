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

def Sarah_Verses(topic, question_verse):
    Verse = [
        "Genesis 11:27, Genesis 20:12",  # 0
        "Genesis 11:29",  # 1
        "Genesis 20:12",  # 2
        "Genesis 12:11, Genesis 12:14",  # 3
        "Genesis 12:11-15, Genesis 20:1-2",  # 4
        "Genesis 11:30",  # 5
        "Genesis 16:1-3",  # 6
        "Genesis 16:4-16",  # 7
        "Genesis 17:15-17",  # 8
        "Genesis 18:9-15",  # 9
        "Genesis 21:1-6",  # 10
        "Galatians 4:24-26",  # 11
        "Genesis 23:1",  # 12
        "Genesis 23:2",  # 13
        "Genesis 23:17-20",  # 14
    ]

    verse_map = {
        "Verse1": 0,
        "Verse2": 1,
        "Verse3": 2,
        "Verse4": 3,
        "Verse5": 4,
        "Verse6": 5,
        "Verse7": 6,
        "Verse8": 7,
        "Verse9": 8,
        "Verse10": 9,
        "Verse11": 10,
        "Verse12": 11,
        "Verse13": 12,
        "Verse14": 13,
        "Verse15": 14,
    }

    index = verse_map.get(question_verse)

    if index is not None and index < len(Verse):
        return jsonify({"verse": Verse[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404

def Sarah_Scripture(topic, scripture):
    TEMPLATE_FOR_SCRIPTURE = """<h2>Genesis 2:21-22</h2>
        <br>
        <b>21-</b><p></p>
        <b>22-</b><p></p>
        """,  # Question #

    scripture = [
        """<h2>Genesis 11:27</h2>
        <br>
        <b>27-</b><p>This is the account of Terah’s family line.
        <br>
        Terah became the father of Abram, Nahor and Haran. And Haran became the father of Lot.</p>
        <br>
        <h2>Genesis 20:12</h2>
        <br>
        <b>12-</b><p>Besides, she really is my sister, the daughter of my father though not of my mother; and she became my wife.</p>
        """,  # Question 1
    ]

    scripture_map = {
        "Scripture1": 0,
        "Scripture2": 1,
        "Scripture3": 2,
        "Scripture4": 3,
        "Scripture5": 4,
        "Scripture6": 5,
        "Scripture7": 6,
        "Scripture8": 7,
        "Scripture9": 8,
        "Scripture10": 9,
        "Scripture11": 10,
        "Scripture12": 11,
        "Scripture13": 12,
        "Scripture14": 13,
        "Scripture15": 14,
    }

    index = scripture_map.get(scripture)

    if index is not None and index < len(scripture):
        return jsonify({"verse": scripture[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404