from Questions import Question
question_prompt = [
    "Who was the Indian captain in ICC World Cup 1983? \n (a)Madan lal \n (b)Roger Binny \n(b)Sunil Gavaskar \n(d) Kapil Dev\n \n",
    "Which Indian player had scored highest run in One Day cricket in 2018? \n (a)Rohit Sharma \n (b)MS Dhoni \n (c)Virat Kohli \n (d)Shikhar Dhawan\n \n ",
    " Who was the highest run scorer in ICC Cricket World Cup 2003? \n (a)Sachin Tendulkar \n (b)Rahul Dravid \n (c)Sourav Ganguly \n (d)Virendra Sehwag\n \n ",
    "Sourav Ganguly was retired in which year?\n  (a)2005 \n (b)2006 \n (c) 2007 \n (d)2008\n \n ",
    "How many times have India won the World Cup? \n (a) 10 \n (b) 5 \n (c) 3 \n (d) 2\n \n ",
    "What was the highest total score of India in World Cup? \n (a) 399 \n (b) 423 \n (c)347 \n (d)413\n \n ",
    "At which World Cup did India first play in their famous light blue kit? \n (a)2003 \n (b)1996 \n (c)1993 \n (d)2000\n \n ",
    "Who is known as the father of Indian Cricket ? \n (a)Sachin Tendulkar \n (b)K.S.Renjith Singji \n (c)MS Dhoni \n (d)Virat Kohli\n \n ",
    "Sachin Tendulkar played his One-day debut against? \n (a)Australia \n (b)Pakistan \n (c) Sri Lanka \n (d) England\n \n ",
    "How many finals has Mahendra Singh Dhoni played in the IPL? \n (a) 5 \n (b) 8 \n (c) 3 \n (d)6\n \n ",
    "Which cricketer hit the winning runs for Rajasthan Royals in the 2008 IPL? \n (a) Shane Warne \n (b)Sohail Tanvir \n (c)Graeme Smith \n (d)Yusuf Pathan \n \n ",
    "Which cricketer has won the most number of IPL titles? \n (a)Gautam Gambhir \n (b)Virat Kohli \n (c)Dwayne Bravo \n (d)Rohit Sharma\n \n ",
    "How many foreign (overseas) captains have won IPL?\n (a)4 \n (b)3 \n (c)0 \n (d)1\n \n ",
    "Which team was going to take part in ipl 2022 for the first time? \n (a) Gujarat Titans \n (b) Chennai SuperKing \n (c) Pune Warrior \n (d) Rajasthan Royals\n \n ",
    "Who is the most expensive player in Ipl 2022 auction?\n  (a) Shreyas Iyer \n (b) Ishan Kishan \n (c) Liam Livingstone \n (d) David Warner\n \n "
]

questions = [
    Question(question_prompt[0], "d"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "a"),
    Question(question_prompt[3], "d"),
    Question(question_prompt[4], "d"),
    Question(question_prompt[5], "d"),
    Question(question_prompt[6], "b"),
    Question(question_prompt[7], "b"),
    Question(question_prompt[8], "b"),
    Question(question_prompt[9], "b"),
    Question(question_prompt[10], "b"),
    Question(question_prompt[11], "d"),
    Question(question_prompt[12], "b"),
    Question(question_prompt[13], "a"),
    Question(question_prompt[14], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(score)

run_test(questions)