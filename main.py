# Critical Import Statements, Python And Flask
try:
    from flask import Flask, request, jsonify
    import random
    import time
    import schedule
    import threading
    import logging
except ModuleNotFoundError:
    import subprocess
    import sys
    ask = input("It Would Appear You Do Not Have All Of The Packages Needed To Run The API Installed, Would You Like To Install Them [y/n]: ")

    if ask.lower() == "yes" or ask.lower() == "y":
        try:
            print("Installing Dependencies Flask And Scheduling...")
            subprocess.run([sys.executable, "-m", "pip", "install", "flask"], check=True)
            subprocess.run([sys.executable, "-m", "pip", "install", "schedule"], check=True)
        except subprocess.CalledProcessError:
            try:
                print("Regular Install Failed, It Would Appear You Are Using MacOS, Switching Install Commands")
                subprocess.run([sys.executable, "-m", "pip3", "install", "flask"], check=True)
                subprocess.run([sys.executable, "-m", "pip3", "install", "schedule"], check=True)
            except subprocess.CalledProcessError:
                print("Both Installations Failed, Which Means You Are Using Python Through An Unsupported Method, Or Pip Is Not Working, If So, Please Fix The Issue And Attempt To Run The Program Again, Or Install Flask And Schedule Manually")
        print("Package Instllation Complete.")
    elif ask.lower() == "no" or ask.lower() == "n":
        print("Packages Not Installed, Quitting Program")
    else:
        print("Invalid Input, Closing Program")

# Imports Questions For The 'Books'
from Books.WomenOfBibleVol1.Sarah.sarah import Sarah_Questions, Sarah_Verses, Sarah_Scripture
from Books.WomenOfBibleVol1.Eve.eve import Eve_Questions, Eve_Verses, Eve_Scripture
from Books.WomenOfBibleVol1.LotsWife.lotswife import LotWife_Questions, LotWife_Verses, LotWife_Scripture
from Books.WomenOfBibleVol1.Rebekah.rebekah import Rebekah_Questions, Rebekah_Verses, Rebekah_Scripture

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
        if topic == "Eve, Mother Of All Living":
            return Eve_Questions(topic, question)
        if topic == "Sarah, Mother Of Nations":
            return Sarah_Questions(topic, question)
        if topic == "Lot's Wife":
            return LotWife_Questions(topic, question)
        if topic == "Rebekah, A Lovely Maiden":
            return Rebekah_Questions(topic, question)

# Verses For The 'Books'
@app.route('/Books/<book>/<topic>/Verse/<verse>', methods=['GET'])
def Books_Verses(book, topic, verse):
    if book == "WomenOfBibleVol1":
        if topic == "Eve, Mother Of All Living":
            return Eve_Verses(topic, verse)
        if topic == "Sarah, Mother Of Nations":
            return Sarah_Verses(topic, verse)
        if topic == "Lot's Wife":
            return LotWife_Verses(topic, verse)
        if topic == "Rebekah, A Lovely Maiden":
            return Rebekah_Verses(topic, verse)

# Scripture For The 'Books'
@app.route('/Books/<book>/<topic>/Scripture/<scripture>', methods=['GET'])
def Books_Scriptures(book, topic, scripture):
    if book == "WomenOfBibleVol1":
        if topic == "Eve, Mother Of All Living":
            return Eve_Scripture(topic, scripture)
        if topic == "Sarah, Mother Of Nations":
            return Sarah_Scripture(topic, scripture)
        if topic == "Lot's Wife":
            return LotWife_Scripture(topic, scripture)
        if topic == "Rebekah, A Lovely Maiden":
            return Rebekah_Scripture(topic, scripture)


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


# Runs The Flask Application,
if __name__ == '__main__':
    app.run(debug=True)

