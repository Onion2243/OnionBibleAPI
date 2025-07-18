from flask import jsonify


# Returns The Questions For The Eve Part Of The Book
def Eve_Questions(topic, question):
    Questions= [
        "1. How Does Eve Differ From All Other Women?",  # 0
        "2. Why Was Eve Created?",  # 1
        "3. To Whom Was Eve Given As A Wife?",  # 2
        "4. What Position Was She To Have In The Relationship?",  # 3
        "5. What Did Jesus Say About This Union?",  # 4
        "6. What Home Was prepared For Eve?",  # 5
        "6B. Describe The Home Prepared For Eve.",  # 6
        "7. What Were her Duties?",  # 7
        "8. What Was Her Wardrobe?",  # 8
        "9. With What Was Eve Tempted?",  # 9
        "10. What Three Appeals Did This Offer?",  # 10
        "11. Whom Did She Tempt To Sin With Her?",  # 11
        "12. What Was Her Defense When Reproached?",  # 12
        "13. What Was Eve's Punishments?",  # 13
        "14. How Is Woman To Be Saved?",  # 14
        "15. Tell Of Eve's First Two Sons? (Cain And Abel)",  # 15
    ]
    question_map = {
        "Question1": 0,
        "Question2": 1,
        "Question3": 2,
        "Question4": 3,
        "Question5": 4,
        "Question6": 5,
        "Question6B": 6,
        "Question7": 7,
        "Question8": 8,
        "Question9": 9,
        "Question10": 10,
        "Question11": 11,
        "Question12": 12,
        "Question13": 13,
        "Question14": 14,
        "Question15": 15,
    }
    # Gets The Question And Its Index Out Of The Question Map
    question = question_map.get(question)

    # Only Runs If Question Is Not None And Is Smaller Than The Length Of The Questions
    if question is not None and question < len(Questions):
        return jsonify({f"{topic}, {question}": Questions[question]})

def Eve_Verses_NA(topic, question_verse):
    Verse = [
        "Genesis 2:21-22",  # 0
        "Genesis 2:20",  # 1
        "Genesis 2:22",  # 2
        "1 Corinthians 11:3, Ephesians 5:22",  # 3
        "Matthew 19:3-9",  # 4
        "Genesis 2:8-9",  # 5
        "Genesis 2:15, Genesis 2:20",  # 6
        "Genesis 2:25",  # 7
        "Genesis 3:1-6",  # 8
        "Genesis 3:6, 1 John 2:16",  # 9
        "Genesis 3:6",  # 10
        "Genesis 3:13",  # 11
        "Genesis 3:14-16",  # 12
        "1 Timothy 2:13-15",  # 13
        "Genesis 4:1-12",  # 14
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

    # Gets The Verse And Its Index Out Of The Verse Map
    question_verse = verse_map.get(question_verse)

    # Only Runs If Verse Is Not None And Is Smaller Than The Length Of The Verse
    if question_verse is not None and question_verse < len(Verse):
        return jsonify({f"{topic}, {question_verse}": Verse[question_verse]})

def Eve_Verses(topic, question_verse):
    Verse = [
        "Genesis 2:21-22",  # 0
        "Genesis 2:20",  # 1
        "Genesis 2:22",  # 2
        "1 Corinthians 11:3, Ephesians 5:22",  # 3
        "Matthew 19:3-9",  # 4
        "Genesis 2:8-9",  # 5
        "Genesis 2:15, Genesis 2:20",  # 6
        "Genesis 2:25",  # 7
        "Genesis 3:1-6",  # 8
        "Genesis 3:6, 1 John 2:16",  # 9
        "Genesis 3:6",  # 10
        "Genesis 3:13",  # 11
        "Genesis 3:14-16",  # 12
        "1 Timothy 2:13-15",  # 13
        "Genesis 4:1-12",  # 14
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