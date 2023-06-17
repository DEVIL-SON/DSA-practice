# CREATED A BIT LENGTHY CODE FOR GETTING BETTER OPERATION
from Questions import Question # CREATED EXTRENAL CLASS FOR QUESTION, ANSWER AND SCORE
f = open("Instrutions.txt", "r") # INSTRUCTION SET FOR PLAYER IMPORTED FROM TEXT FILE
instructions = f.read()
question_prompt = [
    "1. Who was the Indian captain in ICC World Cup 1983? \n (a)Madan lal \n (b)Roger Binny \n(b)Sunil Gavaskar \n(d) Kapil Dev\n \n",
    "2. Which Indian player had scored highest run in One Day cricket in 2018? \n (a)Rohit Sharma \n (b)MS Dhoni \n (c)Virat Kohli \n (d)Shikhar Dhawan\n \n ",
    "3. Who was the highest run scorer in ICC Cricket World Cup 2003? \n (a)Sachin Tendulkar \n (b)Rahul Dravid \n (c)Sourav Ganguly \n (d)Virendra Sehwag\n \n ",
    "4. Sourav Ganguly was retired in which year?\n  (a)2005 \n (b)2006 \n (c) 2007 \n (d)2008\n \n ",
    "5. How many times have India won the World Cup? \n (a) 10 \n (b) 5 \n (c) 3 \n (d) 2\n \n ",
    "6. What was the highest total score of India in World Cup? \n (a) 399 \n (b) 423 \n (c)347 \n (d)413\n \n ",
    "7. At which World Cup did India first play in their famous light blue kit? \n (a)2003 \n (b)1996 \n (c)1993 \n (d)2000\n \n ",
    "8. Who is known as the father of Indian Cricket ? \n (a)Sachin Tendulkar \n (b)K.S.Renjith Singji \n (c)MS Dhoni \n (d)Virat Kohli\n \n ",
    "9. Sachin Tendulkar played his One-day debut against? \n (a)Australia \n (b)Pakistan \n (c) Sri Lanka \n (d) England\n \n ",
    "10. How many finals has Mahendra Singh Dhoni played in the IPL? \n (a) 5 \n (b) 8 \n (c) 3 \n (d)6\n \n ",
    "11. Which cricketer hit the winning runs for Rajasthan Royals in the 2008 IPL? \n (a) Shane Warne \n (b)Sohail Tanvir \n (c)Graeme Smith \n (d)Yusuf Pathan \n \n ",
    "12. Which cricketer has won the most number of IPL titles? \n (a)Gautam Gambhir \n (b)Virat Kohli \n (c)Dwayne Bravo \n (d)Rohit Sharma\n \n ",
    "13. How many foreign (overseas) captains have won IPL?\n (a)4 \n (b)3 \n (c)0 \n (d)1\n \n ",
    "14. Which team was going to take part in ipl 2022 for the first time? \n (a) Gujarat Titans \n (b) Chennai SuperKing \n (c) Pune Warrior \n (d) Rajasthan Royals\n \n ",
    "15. Who is the most expensive player in Ipl 2022 auction?\n  (a) Shreyas Iyer \n (b) Ishan Kishan \n (c) Liam Livingstone \n (d) David Warner\n \n "
]   # SET OF 15 QUESTIONS ACCORDING TO DIFFERENT FIELDS AND GK

questions = [
    Question(question_prompt[0], "d" ,  3.5), 
    Question(question_prompt[1], "c" , 2),
    Question(question_prompt[2], "a" , 3.5 ),
    Question(question_prompt[3], "d" ,  2),
    Question(question_prompt[4], "d" , 2 ),
    Question(question_prompt[5], "d" , 4 ),
    Question(question_prompt[6], "b" ,  3.5),
    Question(question_prompt[7], "b" , 4 ),
    Question(question_prompt[8], "b" , 4 ),
    Question(question_prompt[9], "b" , 3.5),
    Question(question_prompt[11], "d", 4 ),
    Question(question_prompt[12], "b", 4 ),
    Question(question_prompt[13], "a", 2 ),
    Question(question_prompt[10], "b",  3.5),
    Question(question_prompt[14], "b",  2),
] # CREATED ARRAY FOR QUESTION ANSWER AND SCORE TO STORE AND USE IT IN run_test FUNCTION
def run_test(questions): # FUNCTION USED FOR GAME 
    score1 = 0
    score2 = 0
    for question in questions:
        print("-->>Select who will Answer: A for " + player_1 + "and L for " + player_2 + " and X for quiting")
        player = input("****>>Enter the player: ")
        if player == "A" or player == "a":
            answer = input(question.prompt)
            print("^_^ Correct Answer is:  ", question.answer)
            if answer == question.answer:
                score1 += question.per_score
        elif player == "L" or player == "l":
            answer = input(question.prompt)
            print("^_^ Correct Answer is:  ", question.answer)
            if answer == question.answer:
                score2 += question.per_score
        elif player == "x" or player == "X":
            break
        total = score1 + score2
        score_1 = (score1/total)*100
        score_2 = (score2/total)*100

    print(player_1 + " Got "  +  str("{:.2f}".format(score_1)) + "%")
    print(player_2 + " Got " +  str( "{:.2f}".format(score_2)) + "%")

# CALLING FUNCTION HERE TO START
print("________________WELCOME TO THE CRICKET 2 PLAYER QUIZ______________")
print(instructions)
f.close
print("{Click p to start or q to quit}")
wanna_play = input("<>Enter here: ")
if wanna_play == "p" or wanna_play == "P":
    player_1 = input(">>>>Enter the Player Name 1: ")
    player_2 = input(">>>>Enter the Player Name 2: ")
    run_test(questions)
elif wanna_play == "q" or wanna_play == "Q":
    print("------->Thanks, To Play game Run the Program again<---------")