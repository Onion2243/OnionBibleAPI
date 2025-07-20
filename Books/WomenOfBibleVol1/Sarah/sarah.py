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
        "Genesis 21:1-5",  # 10
        "Genesis 21:6" # 11
        "Galatians 4:24-26",  # 12
        "Genesis 23:1",  # 13
        "Genesis 23:2",  # 14
        "Genesis 23:17-20",  # 15
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

def Sarah_Scripture(topic, scripture):
    TEMPLATE_FOR_SCRIPTURE = """<h2>Genesis 2:21-22</h2><br>
        <p><b>21-</b></p>
        <p><b>22-</b></p>
        """,  # Question #

    Scripture = [
        """
        <br><h2>Genesis 11:27</h2><br>
        <p><b>27-</b> This is the account of Terah’s family line.<br><br>Terah became the father of Abram, Nahor and Haran. And Haran became the father of Lot.</p><br>
        <h2>Genesis 20:12</h2><br>
        <p><b>12-</b> Besides, she really is my sister, the daughter of my father though not of my mother; and she became my wife.</p>
        """,  # Question 1

        """
        <br><p><b>29-</b> Abram and Nahor both married. The name of Abram’s wife was Sarai, and the name of Nahor’s wife was Milkah; she was the daughter of Haran, the father of both Milkah and Iskah.</p>
        """,  # Question 1B

        """
        <br><p><b>12-</b> Besides, she really is my sister, the daughter of my father though not of my mother; and she became my wife.</p>
        """,  # Question 1C

        """
        <br><h2>Genesis 12:11</h2><br>
        <p><b>11-</b>As he was about to enter Egypt, he said to his wife Sarai, “I know what a beautiful woman you are.</p>
        <br><h2>Genesis 12:14</h2><br>
        <p><b>14-</b>When Abram came to Egypt, the Egyptians saw that Sarai was a very beautiful woman. </p>
        """,  # Question 2

        """<br><h2>Genesis 12:11-15</h2><br>
        <p><b>11-</b>As he was about to enter Egypt, he said to his wife Sarai, “I know what a beautiful woman you are.</p><br>
        <p><b>12-</b>When the Egyptians see you, they will say, ‘This is his wife.’ Then they will kill me but will let you live.</p><br>
        <p><b>13-</b>Say you are my sister, so that I will be treated well for your sake and my life will be spared because of you.”</p><br>
        <p><b>14-</b>When Abram came to Egypt, the Egyptians saw that Sarai was a very beautiful woman.</p><br>
        <p><b>15-</b>And when Pharaoh’s officials saw her, they praised her to Pharaoh, and she was taken into his palace.</p>
        <br><h2>Genesis 20:1-2</h2><br>
        <p><b>1-</b>Now Abraham moved on from there into the region of the Negev and lived between Kadesh and Shur. For a while he stayed in Gerar,</p><br>
        <p><b>2-</b>and there Abraham said of his wife Sarah, “She is my sister.” Then Abimelek king of Gerar sent for Sarah and took her.</p><br>
        """,  # Question 3

        """
        <br><p><b>30-</b>Now Sarai was childless because she was not able to conceive.</p>
        """,  # Question 4

        """
        <br><p><b>1-</b>Now Sarai, Abram’s wife, had borne him no children. But she had an Egyptian slave named Hagar;</p><br>
        <p><b>2-</b>so she said to Abram, “The Lord has kept me from having children. Go, sleep with my slave; perhaps I can build a family through her.”<br><br>Abram agreed to what Sarai said.</p><br>
        <p><b>3-</b>So after Abram had been living in Canaan ten years, Sarai his wife took her Egyptian slave Hagar and gave her to her husband to be his wife.</p>
        """,  # Question 5

        """
        <br><p><b>4-</b>He slept with Hagar, and she conceived.<br><br>When she knew she was pregnant, she began to despise her mistress.</p><br>
        <p><b>5-</b>Then Sarai said to Abram, “You are responsible for the wrong I am suffering. I put my slave in your arms, and now that she knows she is pregnant, she despises me. May the Lord judge between you and me.”</p><br>
        <p><b>6-</b>“Your slave is in your hands,” Abram said. “Do with her whatever you think best.” Then Sarai mistreated Hagar; so she fled from her.</p><br>
        <p><b>7-</b>The angel of the Lord found Hagar near a spring in the desert; it was the spring that is beside the road to Shur.</p><br>
        <p><b>8-</b>And he said, “Hagar, slave of Sarai, where have you come from, and where are you going?”<br><br>“I’m running away from my mistress Sarai,” she answered.</p><br>
        <p><b>9-</b>Then the angel of the Lord told her, “Go back to your mistress and submit to her.”</p><br>
        <p><b>10-</b>The angel added, “I will increase your descendants so much that they will be too numerous to count.”</p><br>
        <p><b>11-</b>The angel of the Lord also said to her:

        “You are now pregnant
            and you will give birth to a son.
        You shall name him Ishmael,[a]
            for the Lord has heard of your misery.</p><br>
        <p><b>12-</b>
        He will be a wild donkey of a man;
            his hand will be against everyone
            and everyone’s hand against him,
        and he will live in hostility
            toward[b] all his brothers.”</p><br>
        <p><b>13-</b>She gave this name to the Lord who spoke to her: “You are the God who sees me,” for she said, “I have now seen[c] the One who sees me.”</p><br>
        <p><b>14-</b>That is why the well was called Beer Lahai Roi[d]; it is still there, between Kadesh and Bered.</p><br>
        <p><b>15-</b>So Hagar bore Abram a son, and Abram gave the name Ishmael to the son she had borne. </p><br>
        <p><b>16-</b>Abram was eighty-six years old when Hagar bore him Ishmael.</p>
        """,  # Question 6

        """
        <br><p><b>15-</b>God also said to Abraham, “As for Sarai your wife, you are no longer to call her Sarai; her name will be Sarah.</p><br>
        <p><b>16-</b>I will bless her and will surely give you a son by her. I will bless her so that she will be the mother of nations; kings of peoples will come from her.”</p><br>
        <p><b>17-</b>Abraham fell facedown; he laughed and said to himself, “Will a son be born to a man a hundred years old? Will Sarah bear a child at the age of ninety?”</p>
        """,  # Question 7

        """
        <br><p><b>9-</b></p>“Where is your wife Sarah?” they asked him.<br><br>“There, in the tent,” he said.<br>
        <p><b>10-</b>Then one of them said, “I will surely return to you about this time next year, and Sarah your wife will have a son. Now Sarah was listening at the entrance to the tent, which was behind him.”</p><br>
        <p><b>11-</b> Abraham and Sarah were already very old, and Sarah was past the age of childbearing.</p><br>
        <p><b>12-</b>So Sarah laughed to herself as she thought, “After I am worn out and my lord is old, will I now have this pleasure?”</p><br>
        <p><b>13-</b>Then the Lord said to Abraham, “Why did Sarah laugh and say, ‘Will I really have a child, now that I am old?’</p><br>
        <p><b>14-</b> Is anything too hard for the Lord? I will return to you at the appointed time next year, and Sarah will have a son.”</p><br>
        <p><b>15-</b>Sarah was afraid, so she lied and said, “I did not laugh.”<br><br>But he said, “Yes, you did laugh.”</p>
        """,  # Question 8

        """
        <br><p><b>1-</b>Now the Lord was gracious to Sarah as he had said, and the Lord did for Sarah what he had promised.</p><br>
        <p><b>2-</b>Sarah became pregnant and bore a son to Abraham in his old age, at the very time God had promised him.</p><br>
        <p><b>3-</b>Abraham gave the name Isaac[a] to the son Sarah bore him.</p><br>
        <p><b>4-</b>When his son Isaac was eight days old, Abraham circumcised him, as God commanded him.</p><br>
        <p><b>5-</b>Abraham was a hundred years old when his son Isaac was born to him.</p>
        """,  # Question 9

        """
        <br><p><b>6-</b>Sarah said, “God has brought me laughter, and everyone who hears about this will laugh with me.”</p>
        """,  # Question 9B

        """
        <br><p><b>24-</b>These things are being taken figuratively: The women represent two covenants. One covenant is from Mount Sinai and bears children who are to be slaves: This is Hagar.</p><br>
        <p><b>25-</b>Now Hagar stands for Mount Sinai in Arabia and corresponds to the present city of Jerusalem, because she is in slavery with her children.</p><br>
        <p><b>26-</b>But the Jerusalem that is above is free, and she is our mother.</p>
        """,  # Question 10

        """
        <br><p><b>1-</b>Sarah lived to be a hundred and twenty-seven years old.</p>
        """,  # Question 11

        """
        <br><p><b>2-</b>She died at Kiriath Arba (that is, Hebron) in the land of Canaan, and Abraham went to mourn for Sarah and to weep over her.</p>
        """,  # Question 12

        """
        <br><p><b>17-</b>So Ephron’s field in Machpelah near Mamre—both the field and the cave in it, and all the trees within the borders of the field—was deeded</p><br>
        <p><b>18-</b>to Abraham as his property in the presence of all the Hittites who had come to the gate of the city.</p><br>
        <p><b>19-</b>Afterward Abraham buried his wife Sarah in the cave in the field of Machpelah near Mamre (which is at Hebron) in the land of Canaan.</p><br>
        <p><b>20-</b>So the field and the cave in it were deeded to Abraham by the Hittites as a burial site.</p>
        """,  # Question 13
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
        return jsonify({f"{topic}, {scripture}": Scripture[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404