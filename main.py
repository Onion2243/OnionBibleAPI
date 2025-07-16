# Import Statements
from flask import Flask, request, jsonify
import random
import time
import schedule
import threading
import logging
from VersesOfTheDayList.ListOfVerses import ListOfVerses
import Bibles.NIV as NIV

# Enables Logging For Gunicorn WSGI
logging.basicConfig(level=logging.INFO)

# Creates A New Flask Application
app = Flask(__name__)

# region VerseOfTheDayRefresh

# Initially Makes A New Verse When The Program Is Run
current_verse = random.choice(ListOfVerses)

# Function to update the verse
def update_verse():
    # Makes Current Verse A Global Variable
    global current_verse

    # Gets A New Verse Randomly
    current_verse = random.choice(ListOfVerses)
    logging.info("New Verse:", current_verse)

def schedule_daily_updates():
    # Schedule the update at 6:00 AM daily
    schedule.every().day.at("05:59").do(update_verse)

    # Schedular Which Checks What Time It Is Every Minute.
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    # Creates A New Background Thread, Which Will Run The Time Checker In The Background
    threading.Thread(target=run_scheduler, daemon=True).start()

# Runs The Schedule Daily Updates Function
schedule_daily_updates()

# endregion

# A GET Method, Which Gets The Verse Of The Day When The API Path /VerseOfTheDay Is Called
@app.route('/VerseOfTheDay/', methods=['GET'])
def getVerseOfTheDay():
    # Returns A JSON Of The Current Verse When This API Route Is Called
    return jsonify({"verse": current_verse})

@app.route('/Books/<book>/<topic>/<question>', methods=['GET'])
def Books(book, topic, question):
    if book == "WomenOfBibleVol1":
        # region EveChapter
        if topic == "Eve":
            Questions = [
                "1. How Does Eve Differ From All Other Women?", # 0
                "2. Why Was Eve Created?", # 1
                "3. To Whom Was Eve Given As A Wife?",# 2
                "4. What Position Was She To Have In The Relationship?", # 3
                "5. What Did Jesus Say About This Union?", # 4
                "6. What Home Was prepared For Eve?", # 5
                "6B. Describe The Home Prepared For Eve.", # 6
                "7. What Were her Duties?", # 7
                "8. What Was Her Wardrobe?", # 8
                "9. With What Was Eve Tempted?", # 9
                "10. What Three Appeals Did This Offer?", # 10
                "11. Whom Did She Tempt To Sin With Her?", # 11
                "12. What Was Her Defense When Reproached?", # 12
                "13. What Was Eve's Punishments?", # 13
                "14. How Is Woman To Be Saved?", # 14
                "15. Tell Of Eve's First Two Sons? (Cain And Abel)", # 15
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
        # endregion
        # region SarahChapter
        if topic == "Sarah":
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
        # endregion

@app.route('/<Version>/Chapters/<Chapter>')
def Bible(Version, Chapter):
    if Version == "NIV":
        if Chapter == "Genesis 1":
            return jsonify({"Scripture": NIV.genesis_1.get_scripture()})
        if Chapter == "Genesis 2":
            return jsonify({"Scripture": NIV.genesis_2.get_scripture()})
        if Chapter == "Genesis 3":
            return jsonify({"Scripture": NIV.genesis_3.get_scripture()})
        if Chapter == "Genesis 4":
            return jsonify({"Scripture": NIV.genesis_4.get_scripture()})
        if Chapter == "Genesis 5":
            return jsonify({"Scripture": NIV.genesis_5.get_scripture()})
        if Chapter == "Genesis 6":
            return jsonify({"Scripture": NIV.genesis_6.get_scripture()})
        if Chapter == "Genesis 7":
            return jsonify({"Scripture": NIV.genesis_7.get_scripture()})
        if Chapter == "Genesis 8":
            return jsonify({"Scripture": NIV.genesis_8.get_scripture()})
        if Chapter == "Genesis 9":
            return jsonify({"Scripture": NIV.genesis_9.get_scripture()})
        if Chapter == "Genesis 10":
            return jsonify({"Scripture": NIV.genesis_10.get_scripture()})


# Runs The Flask Application
if __name__ == '__main__':
    app.run(debug=True)

