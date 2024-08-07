#NEA - TASK 2

import random


#function for login system to authorise users
def login():
    username = input("Enter your name: ")
    password = len(username)
    print("The password is the length (number of characters) of your username in digits.")
    login = False #using a flag
    while login == False: #while loop asks the user to try again until the correct password has been inputted
        pass1 = int(input("Enter password: "))
        if pass1 == password:
            print("Correct password - authorised access.")
            login = True
        else:
            print("Incorrect password, try again.")
    return username

#function to roll the dice and return the value rolled
def rolldice():
    input("Please enter to roll the dice.")
    roll = random.randint(1,6)
    print(roll)
    return(roll)

#function to calculate the score the player gets
def rollplayer(username,numrolls):
    global pscore #making the variable global so that it can be used outside the function
    pscore = 0
    print(username)
    rollone = rolldice()
    pscore = rollone
    if numrolls == 2:
        rolltwo = rolldice()
        pscore += rolltwo
        if rollone == rolltwo:
            rollthree = rolldice()#rolling a 3rd dice in the case of a double
            pscore += rollthree
    if (pscore%2) == 0:
        pscore = (pscore+10) #adding 10 points if the value is even
    elif (pscore%2) != 0:
        pscore = (pscore-5) #subtracting 5 points if the value is odd
        if pscore < 0:
            pscore = 0 #ensuring the score does not go below 0
    print("Your score for this round is: ",pscore,)
    return pscore
    
print("Player 1,")
username1 = login()
print()
print("Player 2,")
username2 = login()

print("\n"+"Here are the rules of the game:")
print(" •The points rolled on each player’s dice are added to their score.")
print(" •If the total is an even number, an additional 10 points are added to their score.")
print(" •If the total is an odd number, 5 points are subtracted from their score.")
print(" •If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.")
print(" •The score of a player cannot go below 0 at any point.")
print(" •The person with the highest score at the end of the 5 rounds wins.")
print(" •If  both  players  have  the  same  score  at  the  end  of  the  5  rounds,  they  each  roll  1  die  and  whoever gets the highest score wins (this repeats until someone wins).")
print()


roundnum = 1 #using a variable for the round number so that it can be changed and displayed in every round
p1totalscore = 0
p2totalscore = 0
scores_equal = False

while roundnum < 6: #using a while loop for all the rounds (roundnum does not get incremented if the scores are equal at the end of the game)
    if scores_equal == False:
        print("\n"+"ROUND ", roundnum, "\n"+"\n")

        rollplayer(username1,2)
        p1totalscore += pscore #adding the score from thr most recent round to the total score
        print("Your total score is: ",p1totalscore, "\n"+"\n")

        rollplayer(username2,2)
        p2totalscore += pscore#adding the score from thr most recent round to the total score
        print("Your total score is: ",p2totalscore, "\n"+"\n")
    else:
        print("\n"+"ADDITIONAL ROUND"+"\n")

        rollplayer(username1,1) #rolling only one dice for the additional rounds
        p1totalscore += pscore #adding the score from the most recent round to the total score
        print("Your total score is: ",p1totalscore, "\n"+"\n")

        rollplayer(username2,1) #rolling only one dice for the additional rounds
        p2totalscore += pscore #adding the score from the most recent round to the total score
        print("Your total score is: ",p2totalscore, "\n"+"\n")


    if roundnum < 5:
        print("At the end of Round "+str(roundnum)+",",username1,"has a total of",p1totalscore, "and", username2,"has a total score of", p2totalscore,)
        if p1totalscore > p2totalscore: #using an if loop to determine which player has the higher score and how much they are winning by
            print(username1, "is winning by", (p1totalscore - p2totalscore), "points.")
        elif p2totalscore > p1totalscore:
            print(username2, "is winning by", (p2totalscore - p1totalscore), "points.")
        elif p1totalscore == p2totalscore:
            print("At the end of Round "+str(roundnum)+",", username1, "and", username2, "have the same score.")
        print()

    else:
        if p1totalscore > p2totalscore: #using an if loop to determine which player has the higher score and how much they are winning by
            print("At the end of the game",username1,"has a total score of",p1totalscore,"and",username2,"has a total score of",p2totalscore,)
            print(username1, "won by", (p1totalscore - p2totalscore), "points.")
            print("Congratulations "+username1+"!")
            scores_equal = False
        elif p2totalscore > p1totalscore: #using an if loop to determine which player has the higher score and how much they are winning by
            print("At the end of the game",username1,"has a total score of",p1totalscore,"and",username2,"has a total score of",p2totalscore,)
            print(username2, "won by", (p2totalscore - p1totalscore), "points.")
            print("Congratulations "+username2+"!")
            scores_equal = False
        elif p1totalscore == p2totalscore:
            print("At the end of this round,", username1, "and", username2, "have the same score.")
            print("As the scores are the same, there will be another orund to decide who he winner is.")
            print()
            scores_equal = True #setting the flag to indicate that the scores are equal

    if scores_equal == False: #if scores are not equal, increment roundnum
        roundnum += 1

print()



leaderboard = open("Leaderboard.txt", "a") #appending to text file for leaderboard

if p1totalscore > p2totalscore:
    leaderboard.write(str(p1totalscore)) #inputting player score first, so values are sorted by score, for leaderboard
    leaderboard.write(" - "+username1+"\n") #inputting player name for leaderboard
elif p2totalscore > p1totalscore:
    leaderboard.write(str(p2totalscore)) #inputting player score first, so values are sorted by score, for leaderboard
    leaderboard.write(" - "+username2+"\n") #inputting player name for leaderboard
leaderboard.close()

leaderboard = open("Leaderboard.txt", "r").readlines()
leaderboard.sort(reverse = True)
elements =(len(leaderboard)) #elements indicate the number of scores in the leaderboard
print("LEADERBOARD: ")
print()
if elements > 5: #if there are more than 5 scores in the leaderboard, only the top 5 will be printed
    elements = 5
    
for i in range (0,elements):
    print(leaderboard[i]) #printing the top 5 scores and usernames from the leaderboard
