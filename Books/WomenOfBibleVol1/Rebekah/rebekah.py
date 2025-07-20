from flask import jsonify

# Returns The Questions For The Eve Part Of The Book
def Rebekah_Questions(topic, question):
    Questions= [
        "1. Who Was Her Father?",  # 0
        "1B. Her Brother?",  # 1
        "1C. Her Grandparents?",  # 2
        "2. Who Was Her Husband?",  # 3
        "3. How Was She Chosen For A Wife?",  # 4
        "4. Describe Her Meeting With Her Husband.",  # 5
        "5. How Old Was Her Groom?",  # 6
        "6. Was Was Her Affliction?",  # 7
        "6B. How Long Did It Last?",  # 8
        "7. Who Was Born Of This Union?",  # 9
        "8. Describe The Children?",  # 10
        "9. How Were Parental Affections Divided?",  # 11
        "10. What Fault Did Her Husband Inherit?",  # 12
        "11. Tell Of Her Scheme Against Issac For Jacob.",  # 13
        "12. Under What Pretense Did She Induce Issac To Send Jacob Away?",  # 14
        "13. Who Was Rebekah's Trusted Nurse?",  # 15
        "14. Where Was Rebekah Buried?",  # 16
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
        "Question17": 16,
    }
    # Gets The Question And Its Index Out Of The Question Map
    question = question_map.get(question)

    # Only Runs If Question Is Not None And Is Smaller Than The Length Of The Questions
    if question is not None and question < len(Questions):
        return jsonify({f"{topic}, {question}": Questions[question]})

def Rebekah_Verses(topic, question_verse):
    Verse = [
        "Genesis 22:23",  # 0
        "Genesis 24:29",  # 1
        "Genesis 22:20, Genesis 24:15",  # 2
        "Genesis 24:67",  # 3
        "Genesis 24:1-14",  # 4
        "Genesis 24:61-67",  # 5
        "Genesis 25:50",  # 6
        "Genesis 25:21",  # 7
        "Genesis 25:26",  # 8
        "Genesis 25:24-26",  # 9
        "Genesis 25:24-27",  # 10
        "Genesis 25:28",  # 11
        "Genesis 26:7, Genesis 12:13",  # 12
        "Genesis 27:5-17",  # 13
        "Genesis 27:46",  # 14
        "Genesis 24:59, Genesis 35:8",  # 15
        "Genesis 49:30-31",  # 16
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
        "Verse17": 16,
    }

    index = verse_map.get(question_verse)

    if index is not None and index < len(Verse):
        return jsonify({f"{topic}, {question_verse}": Verse[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404



def Rebekah_Scripture(topic, scripture):
    TEMPLATE_FOR_SCRIPTURE = """
            <h2>Genesis 2:21-22</h2><br>
            <b>21-</b><p></p>
            <b>22-</b><p></p>
            """,  # Question #

    Scripture = [
        """
        <br><p><b>23-</b> Bethuel became the father of Rebekah. Milkah bore these eight sons to Abraham’s brother Nahor.</p>
        """,  # Question 1

        """
        <br><p><b>29-</b>Now Rebekah had a brother named Laban, and he hurried out to the man at the spring.</p>
        """,  # Question 1B

        """
        <br><h2>Genesis 22:20</h2><br>
        <p><b>20-</b>Some time later Abraham was told, “Milkah is also a mother; she has borne sons to your brother Nahor:</p>
        <br><h2>Genesis 24:15</h2><br>
        <p><b>15-</b>Before he had finished praying, Rebekah came out with her jar on her shoulder. She was the daughter of Bethuel son of Milkah, who was the wife of Abraham’s brother Nahor.</p>
        """,  # Question 1C

        """
        <br><p><b>67-</b>Isaac brought her into the tent of his mother Sarah, and he married Rebekah. So she became his wife, and he loved her; and Isaac was comforted after his mother’s death.</p>
        """,  # Question 2

        """
        <br><p><b>1-</b>Abraham was now very old, and the Lord had blessed him in every way.</p><br>
        <p><b>2-</b>He said to the senior servant in his household, the one in charge of all that he had, “Put your hand under my thigh.</p><br>
        <p><b>3-</b> I want you to swear by the Lord, the God of heaven and the God of earth, that you will not get a wife for my son from the daughters of the Canaanites, among whom I am living,</p><br>
        <p><b>4-</b>but will go to my country and my own relatives and get a wife for my son Isaac.”</p><br>
        <p><b>5-</b>The servant asked him, “What if the woman is unwilling to come back with me to this land? Shall I then take your son back to the country you came from?”</p><br>
        <p><b>6-</b>“Make sure that you do not take my son back there,” Abraham said. </p><br>
        <p><b>7-</b> “The Lord, the God of heaven, who brought me out of my father’s household and my native land and who spoke to me and promised me on oath, saying, ‘To your offspring[a] I will give this land’—he will send his angel before you so that you can get a wife for my son from there.</p><br>
        <p><b>8-</b> If the woman is unwilling to come back with you, then you will be released from this oath of mine. Only do not take my son back there.”</p><br>
        <p><b>9-</b> So the servant put his hand under the thigh of his master Abraham and swore an oath to him concerning this matter.</p><br>
        <p><b>10-</b> Then the servant left, taking with him ten of his master’s camels loaded with all kinds of good things from his master. He set out for Aram Naharaim[b] and made his way to the town of Nahor. </p><br>
        <p><b>11-</b>He had the camels kneel down near the well outside the town; it was toward evening, the time the women go out to draw water.</p><br>
        <p><b>12-</b> Then he prayed, “Lord, God of my master Abraham, make me successful today, and show kindness to my master Abraham.</p><br>
        <p><b>13-</b>See, I am standing beside this spring, and the daughters of the townspeople are coming out to draw water.</p><br>
        <p><b>14-</b>May it be that when I say to a young woman, ‘Please let down your jar that I may have a drink,’ and she says, ‘Drink, and I’ll water your camels too’—let her be the one you have chosen for your servant Isaac. By this I will know that you have shown kindness to my master.”</p>
        """,  # Question 3

        """
        <br><p><b>61-</b>Then Rebekah and her attendants got ready and mounted the camels and went back with the man. So the servant took Rebekah and left.</p><br>
        <br><p><b>62-</b>Now Isaac had come from Beer Lahai Roi, for he was living in the Negev.</p><br>
        <br><p><b>63-</b>He went out to the field one evening to meditate,[a] and as he looked up, he saw camels approaching.</p><br>
        <br><p><b>64-</b>Rebekah also looked up and saw Isaac. She got down from her camel</p><br>
        <br><p><b>65-</b>and asked the servant, “Who is that man in the field coming to meet us?”<br><br>“He is my master,” the servant answered. So she took her veil and covered herself.</p><br>
        <br><p><b>66-</b>Then the servant told Isaac all he had done.</p><br>
        <br><p><b>67-</b>Isaac brought her into the tent of his mother Sarah, and he married Rebekah. So she became his wife, and he loved her; and Isaac was comforted after his mother’s death.</p><br>
        """,  # Question 4

        """
        <br><p><b>20-</b>and Isaac was forty years old when he married Rebekah daughter of Bethuel the Aramean from Paddan Aram[a] and sister of Laban the Aramean.</p>
        """,  # Question 5

        """
        <br><p><b>21-</b>Isaac prayed to the Lord on behalf of his wife, because she was childless. The Lord answered his prayer, and his wife Rebekah became pregnant.</p>
        """,  # Question 6

        """
        <br><p><b>26-</b>After this, his brother came out, with his hand grasping Esau’s heel; so he was named Jacob.[a] Isaac was sixty years old when Rebekah gave birth to them.</p>
        """,  # Question 6B

        """
        <br><p><b>24-</b></p>When the time came for her to give birth, there were twin boys in her womb.<br>
        <p><b>25-</b>The first to come out was red, and his whole body was like a hairy garment; so they named him Esau.[a]</p><br>
        <p><b>26-</b>After this, his brother came out, with his hand grasping Esau’s heel; so he was named Jacob.[b] Isaac was sixty years old when Rebekah gave birth to them.</p>
        """,  # Question 7

        """
        <br><p><b>24-</b>When the time came for her to give birth, there were twin boys in her womb.</p><br>
        <p><b>25-</b>The first to come out was red, and his whole body was like a hairy garment; so they named him Esau.[a]</p><br>
        <p><b>26-</b>After this, his brother came out, with his hand grasping Esau’s heel; so he was named Jacob.[b] Isaac was sixty years old when Rebekah gave birth to them.</p><br>
        <p><b>27-</b>The boys grew up, and Esau became a skillful hunter, a man of the open country, while Jacob was content to stay at home among the tents.</p>
        """,  # Question 8

        """
        <br><p><b>28-</b>Isaac, who had a taste for wild game, loved Esau, but Rebekah loved Jacob.</p>
        """,  # Question 9

        """
        <br><h2>Genesis 26:7</h2><br>
        <p><b>7-</b>When the men of that place asked him about his wife, he said, “She is my sister,” because he was afraid to say, “She is my wife.” He thought, “The men of this place might kill me on account of Rebekah, because she is beautiful.”</p>
        <br><h2>Genesis 12:13</h2><br>
        <p><b>13-</b>Say you are my sister, so that I will be treated well for your sake and my life will be spared because of you.”</p>
        """,  # Question 10

        """
        <br><p><b>5-</b>Now Rebekah was listening as Isaac spoke to his son Esau. When Esau left for the open country to hunt game and bring it back,</p><br>
        <p><b>6-</b>Rebekah said to her son Jacob, “Look, I overheard your father say to your brother Esau,</p><br>
        <p><b>7-</b>‘Bring me some game and prepare me some tasty food to eat, so that I may give you my blessing in the presence of the Lord before I die.’</p><br>
        <p><b>8-</b>Now, my son, listen carefully and do what I tell you:</p><br>
        <p><b>9-</b>Go out to the flock and bring me two choice young goats, so I can prepare some tasty food for your father, just the way he likes it.</p><br>
        <p><b>10-</b>Then take it to your father to eat, so that he may give you his blessing before he dies.”</p><br>
        <p><b>11-</b>Jacob said to Rebekah his mother, “But my brother Esau is a hairy man while I have smooth skin.</p><br>
        <p><b>12-</b>What if my father touches me? I would appear to be tricking him and would bring down a curse on myself rather than a blessing.”</p><br>
        <p><b>13-</b>His mother said to him, “My son, let the curse fall on me. Just do what I say; go and get them for me.”</p><br>
        <p><b>14-</b>So he went and got them and brought them to his mother, and she prepared some tasty food, just the way his father liked it.</p><br>
        <p><b>15-</b>Then Rebekah took the best clothes of Esau her older son, which she had in the house, and put them on her younger son Jacob.</p><br>
        <p><b>16-</b>She also covered his hands and the smooth part of his neck with the goatskins.</p><br>
        <p><b>17-</b>Then she handed to her son Jacob the tasty food and the bread she had made.</p><br>
        """,  # Question 11

        """
        <br><p><b>46-</b>Then Rebekah said to Isaac, “I’m disgusted with living because of these Hittite women. If Jacob takes a wife from among the women of this land, from Hittite women like these, my life will not be worth living.”</p>
        """,  # Question 12

        """
        <br><h2>Genesis 24:59</h2><br>
        <p><b>59-</b>So they sent their sister Rebekah on her way, along with her nurse and Abraham’s servant and his men.</p>
        <br><h2>Genesis 35:8</h2><br>
        <p><b>8-</b>Now Deborah, Rebekah’s nurse, died and was buried under the oak outside Bethel. So it was named Allon Bakuth.[a]</p>
        """,  # Question 13

        """
        <br><p><b>30-</b>the cave in the field of Machpelah, near Mamre in Canaan, which Abraham bought along with the field as a burial place from Ephron the Hittite.</p><br>
        <p><b>31-</b>There Abraham and his wife Sarah were buried, there Isaac and his wife Rebekah were buried, and there I buried Leah.</p>
        """,  # Question 14

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
        "Scripture17": 16,
    }

    index = scripture_map.get(scripture)

    if index is not None and index < len(Scripture):
        return jsonify({f"{topic}, {scripture}": Scripture[index]})
    else:
        return jsonify({"error": "Invalid verse reference"}), 404

