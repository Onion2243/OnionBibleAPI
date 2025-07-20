from flask import jsonify

# Returns The Questions For The Eve Part Of The Book
def LotWife_Questions(topic, question):
    Questions= [
        "",  # 0
        "",  # 1
        "",  # 2
        "",  # 3
        "",  # 4
        "",  # 5
        "",  # 6
        "",  # 7
        "",  # 8
        "",  # 9
        "",  # 10
        "",  # 11
        "",  # 12
        "",  # 13
        "",  # 14
        "",  # 15
    ]
    question_map = {
        "Question1": 0,
        "Question2": 1,
        "Question3": 2,
        "Question4": 3,
        "Question5": 4,
        "Question6": 5,
        "Question7": 6,
        "Question8": 7,
        "Question9": 8,
        "Question10": 9,
        "Question11": 10,
        "Question12": 11,
        "Question13": 12,
        "Question14": 13,
        "Question15": 14,
        "Question16": 15,
    }
    # Gets The Question And Its Index Out Of The Question Map
    question = question_map.get(question)

    # Only Runs If Question Is Not None And Is Smaller Than The Length Of The Questions
    if question is not None and question < len(Questions):
        return jsonify({f"{topic}, {question}": Questions[question]})

def LotWife_Verses(topic, question_verse):
    Verse = [
        "",  # 0
        "",  # 1
        "",  # 2
        "",  # 3
        "",  # 4
        "",  # 5
        "",  # 6
        "",  # 7
        "",  # 8
        "",  # 9
        "",  # 10
        "",  # 11
        "",  # 12
        "",  # 13
        "",  # 14
        "",  # 15
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
        "Verse16": 15,
    }

    index = verse_map.get(question_verse)

    if index is not None and index < len(Verse):
        return jsonify({f"{topic}, {question_verse}": Verse[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404



def LotWife_Scripture(topic, scripture):
    TEMPLATE_FOR_SCRIPTURE = """
            <h2>Genesis 2:21-22</h2><br>
            <b>21-</b><p></p>
            <b>22-</b><p></p>
            """,  # Question #

    Scripture = [
        """
        """
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
        "Scripture16": 15,
    }

    index = scripture_map.get(scripture)

    if index is not None and index < len(Scripture):
        return jsonify({f"{topic}, {scripture}": Scripture[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404

