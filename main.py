# Critical Import Statements, Python And Flask
from flask import Flask, request, jsonify
import random
import time
import schedule
import threading
import logging

# Imports Questions For The 'Books'
from Books.WomenOfBibleVol1.Sarah.sarah import Sarah_Questions
from Books.WomenOfBibleVol1.Eve.eve import Eve_Questions, Eve_Verses

# Imports Verse Of The Day
from VersesOfTheDayList.ListOfVerses import ListOfVerses

# Import Statements For Each Bible
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

# Questions For The 'Books'
@app.route('/Books/<book>/<topic>/Question/<question>', methods=['GET'])
def Books_Questions(book, topic, question):
    if book == "WomenOfBibleVol1":
        if topic == "Eve":
            return Eve_Questions(topic, question)
        if topic == "Sarah":
            return Sarah_Questions(topic, question)

# Verses For The 'Books'
@app.route('/Books/<book>/<topic>/Verse/<verse>', methods=['GET'])
def Books_Verses(book, topic, verse):
    if book == "WomenOfBibleVol1":
        if topic == "Eve":
            return Eve_Verses(topic, verse)
        if topic == "Sarah":
            return Sarah_Questions(topic, verse)


@app.route('/<Version>/Chapters/<Chapter>')
def Bible(Version, Chapter):
    if Version == "NIV":
        if Chapter.startswith("Genesis "):
            try:
                chapter_num = int(Chapter.split(" ")[1])
                attr_name = f"genesis_{chapter_num}"
                scripture = getattr(NIV, attr_name).get_scripture()
                return jsonify({"Scripture": scripture})
            except (AttributeError, IndexError, ValueError):
                pass  # Handle error if chapter is out of range or invalid


# Runs The Flask Application
if __name__ == '__main__':
    app.run(debug=True)

