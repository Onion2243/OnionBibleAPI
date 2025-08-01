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

def Eve_Verses(topic, question_verse):
    Verse = [
        "Genesis 2:21-22",  # 0
        "Genesis 2:20",  # 1
        "Genesis 2:22",  # 2
        "1 Corinthians 11:3, Ephesians 5:22",  # 3
        "Matthew 19:3-9",  # 4
        "Genesis 2:8-9",  # 5
        "Genesis 2:8-9",  # 6
        "Genesis 2:15, Genesis 2:20",  # 7
        "Genesis 2:25",  # 8
        "Genesis 3:1-6",  # 9
        "Genesis 3:6, 1 John 2:16",  # 10
        "Genesis 3:6",  # 11
        "Genesis 3:13",  # 12
        "Genesis 3:14-16",  # 13
        "1 Timothy 2:13-15",  # 14
        "Genesis 4:1-12",  # 15
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



def Eve_Scripture(topic, scripture):
    TEMPLATE_FOR_SCRIPTURE = """<h2>Genesis 2:21-22</h2>
            <br>
            <b>21-</b><p></p>
            <b>22-</b><p></p>
            """,  # Question #

    Scripture = [
        """
        <br>
        <p><b>21-</b> So the Lord God caused the man to fall into a deep sleep; and while he was sleeping, he took one of the man’s ribs[a] and then closed up the place with flesh.</p>
        <p><b>22-</b> Then the Lord God made a woman from the rib[b] he had taken out of the man, and he brought her to the man.</p>
        """, # Question 1

        """
        <br>
        <p><b>20-</b> So the man gave names to all the livestock, the birds in the sky and all the wild animals.<br><br>But for Adam[a] no suitable helper was found.</p>
        """,  # Question 2

        """
        <br>
        <p><b>22-</b> Then the Lord God made a woman from the rib[b] he had taken out of the man, and he brought her to the man.</p>
        """,  # Question 3

        """<br>
        <h2>1 Corinthians 11:3</h2><br>
        <p><b>3-</b> But I want you to realize that the head of every man is Christ, and the head of the woman is man,[a] and the head of Christ is God.</p><br>
        <h2>Ephesians 5:22</h2><br>
        <p><b>22-</b> Wives, submit yourselves to your own husbands as you do to the Lord.</p>
        """,  # Question 4

        """<h2>Genesis Matthew 19:3-9</h2><br>
        <p><b>3-</b> Some Pharisees came to him to test him. They asked, “Is it lawful for a man to divorce his wife for any and every reason?”</p><br>
        <p><b>4-</b> [a]Haven’t you read,” he replied, “that at the beginning the Creator ‘made them male and female,’</p><br>
        <p><b>5-</b> and said, ‘For this reason a man will leave his father and mother and be united to his wife, and the two will become one flesh’[b]?</p><br>
        <p><b>6-</b> So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate.”</p><br>
        <p><b>7-</b> “Why then,” they asked, “did Moses command that a man give his wife a certificate of divorce and send her away?”</p><br>
        <p><b>8-</b> Jesus replied, “Moses permitted you to divorce your wives because your hearts were hard. But it was not this way from the beginning.</p><br>
        <p><b>9-</b> I tell you that anyone who divorces his wife, except for sexual immorality, and marries another woman commits adultery.”</p>
        """,  # Question 5

        """
        <br>
        <p><b>8-</b> Now the Lord God had planted a garden in the east, in Eden; and there he put the man he had formed.</p>
        <p><b>9-</b> The Lord God made all kinds of trees grow out of the ground—trees that were pleasing to the eye and good for food. In the middle of the garden were the tree of life and the tree of the knowledge of good and evil.</p>
        """,  # Question 6

        """
        <br>
        <p><b>8-</b> Now the Lord God had planted a garden in the east, in Eden; and there he put the man he had formed.</p>
        <p><b>9-</b> The Lord God made all kinds of trees grow out of the ground—trees that were pleasing to the eye and good for food. In the middle of the garden were the tree of life and the tree of the knowledge of good and evil.</p>
        """,  # Question 7

        """<h2>Genesis 2:15</h2><br>
        <p><b>15-</b> The Lord God took the man and put him in the Garden of Eden to work it and take care of it.</p><br>
        <h2>Genesis 2:20</h2><br>
        <p><b>20-</b> So the man gave names to all the livestock, the birds in the sky and all the wild animals.<br><br>But for Adam[a] no suitable helper was found.</p>
        """,  # Question 8

        """
        <br>
        <p><b>25-</b> Adam and his wife were both naked, and they felt no shame.</p>        
        """,  # Question 9

        """
        <p><b>1-</b> Now the serpent was more crafty than any of the wild animals the Lord God had made. He said to the woman, “Did God really say, ‘You must not eat from any tree in the garden’?”</p><br>
        <p><b>2-</b> The woman said to the serpent, “We may eat fruit from the trees in the garden,</p><br>
        <p><b>3-</b> but God did say, ‘You must not eat fruit from the tree that is in the middle of the garden, and you must not touch it, or you will die.’”</p><br>
        <p><b>4-</b> “You will not certainly die,” the serpent said to the woman.</p><br>
        <p><b>5-</b> “For God knows that when you eat from it your eyes will be opened, and you will be like God, knowing good and evil.”</p><br>
        <p><b>6-</b> When the woman saw that the fruit of the tree was good for food and pleasing to the eye, and also desirable for gaining wisdom, she took some and ate it. She also gave some to her husband, who was with her, and he ate it.</p>
        """,  # Question 9

        """ <br>
        <h2>Genesis 3:6</h2><br>
        <p><b>6-</b></p><br>
        <h2>1 John 2:16</h2><br>
        <p><b>16-</b> For everything in the world—the lust of the flesh, the lust of the eyes, and the pride of life—comes not from the Father but from the world.</p>
        """,  # Question 10

        """
        <br>
        <p><b>6-</b> When the woman saw that the fruit of the tree was good for food and pleasing to the eye, and also desirable for gaining wisdom, she took some and ate it. She also gave some to her husband, who was with her, and he ate it.</p>
        """,  # Question 11

        """
        <br>
        <p><b>13-</b> Then the Lord God said to the woman, “What is this you have done?”<br><br>The woman said, “The serpent deceived me, and I ate.”</p>
        """,  # Question 12

        """
        <br>
        <b>14-<p><b>14-</b> So the Lord God said to the serpent, “Because you have done this,<br>&nbsp;&nbsp;&nbsp;&nbsp;“Cursed are you above all livestock<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and all wild animals!<br>&nbsp;&nbsp;&nbsp;&nbsp;You will crawl on your belly<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and you will eat dust<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all the days of your life.</p>
        <p><b>15-</b> &nbsp;&nbsp;&nbsp;&nbsp;And I will put enmity<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;between you and the woman,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and between your offspring[a] and hers;<br>&nbsp;&nbsp;&nbsp;&nbsp;he will crush[b] your head,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and you will strike his heel.”</p><br>
        <p><b>16-</b> To the woman he said,<br>&nbsp;&nbsp;&nbsp;&nbsp;“I will make your pains in childbearing very severe;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with painful labor you will give birth to children.<br>&nbsp;&nbsp;&nbsp;&nbsp;Your desire will be for your husband,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and he will rule over you.”</p>
        """,  # Question 13

        """
        <p><b>13-</b> For Adam was formed first, then Eve.</p><br>
        <p><b>14-</b> And Adam was not the one deceived; it was the woman who was deceived and became a sinner.</p><br>
        <p><b>15-</b> But women[a] will be saved through childbearing—if they continue in faith, love and holiness with propriety.</p>
        """,  # Question 14

        """
        <p><b>1-</b> Adam[a] made love to his wife Eve, and she became pregnant and gave birth to Cain.[b] She said, “With the help of the Lord I have brought forth[c] a man.”</p><br>
        <p><b>2-</b> Later she gave birth to his brother Abel. Now Abel kept flocks, and Cain worked the soil.</p><br>
        <p><b>3-</b> In the course of time Cain brought some of the fruits of the soil as an offering to the Lord.</p><br>
        <p><b>4-</b> And Abel also brought an offering—fat portions from some of the firstborn of his flock. The Lord looked with favor on Abel and his offering,</p><br>
        <p><b>5-</b> but on Cain and his offering he did not look with favor. So Cain was very angry, and his face was downcast.</p><br>
        <p><b>6-</b> Then the Lord said to Cain, “Why are you angry? Why is your face downcast?</p><br>
        <p><b>7-</b> If you do what is right, will you not be accepted? But if you do not do what is right, sin is crouching at your door; it desires to have you, but you must rule over it.”</p><br>
        <p><b>8-</b> Now Cain said to his brother Abel, “Let’s go out to the field.”[d] While they were in the field, Cain attacked his brother Abel and killed him.</p><br>
        <p><b>9-</b> Then the Lord said to Cain, “Where is your brother Abel?” “I don’t know,” he replied. “Am I my brother’s keeper?”</p><br>
        <p><b>10-</b> The Lord said, “What have you done? Listen! Your brother’s blood cries out to me from the ground.</p><br>
        <p><b>11-</b> Now you are under a curse and driven from the ground, which opened its mouth to receive your brother’s blood from your hand.</p><br>
        <p><b>12-</b> When you work the ground, it will no longer yield its crops for you. You will be a restless wanderer on the earth.”</p>
        """,  # Question 15
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

