'''Amshah Mushtaq and Emily Burda
Computer 150 Motivation Test Final Project
This project is a Motivation Test. It asks the user 35 question and determines
their motivation level. Then, it requests user-specific responses and creates
a personalized message for the user, which includes tips and advice to
increase motivation. A graphic at the end is also incorporated to provide the
user a closing statement. No one helped either of us, and we did not help any other group.'''

name = input("Hi there! Please enter your name: ")
print("Dear " + name + ", please read the following instructions carefully.")

inFile = open('instructions.txt','r')
contents = inFile.read()
print(contents)

ready = input("Are you ready to start? Please enter Yes or No: ")
def readyMain():
    if ready == "Yes":
        print("Great! We hope you enoy!")
    else:
        print("Please read the instructions again before moving on.")
readyMain()

print()

print("Starting below you will see statements. Evaluate each on a scale of 1 to 5 based on your personal experiences and opinions.")

print()

Q1 = int(input("I look forward to waking up everyday: "))
Q2 = int(input("I have big aspirations and goals for my future: "))
Q3 = int(input("I am interested in the majority of my current classes: "))
Q4 = int(input("I have supportive people in my life: "))
Q5 = int(input("I would rather work hard than cheat to succeed: "))

Q6 = int(input("I believe that my mistakes and flaws don't hinder my ability to succeed in the future: "))
Q7 = int(input("I workout/exercise three or more times a week: "))
Q8 = int(input("I feel like I am where I am currently for a reason: "))
Q9 = int(input("I would rather get ahead on studying than sleep all day: "))
Q10 = int(input("When I get a chance, I enjoy meditating: "))

Q11 = int(input("Taking risks can be fun!: "))
Q12 = int(input("I feel good in my body, and I like who I am: "))
Q13 = int(input("I would rather make a positive impact on someone’s life than have 1 million dollars: "))
Q14 = int(input("I am not in college in just to get a job that will pay my bills: "))
Q15 = int(input("I would rather make an impact than an income: "))

Q16 = int(input("If I need help, I know there are people that I can reach out to: "))
Q17 = int(input("The easiest way is not the best way: "))
Q18 = int(input("Procrastination stresses me out: "))
Q19 = int(input("Instead of spending my time scrolling through social media, I like to meet up with friends in person: "))
Q20 = int(input("I would sacrifice a weekend of fun to get ahead on studying for finals: "))

Q21 = int(input("I want my potential future children to have a better life than me: "))
Q22 = int(input("When I have a few extra dollars, I donate it to those less fortunate than myself: "))
Q23 = int(input("I have a general idea of where I want to be in 10 years: "))
Q24 = int(input("There are some topics that I am passionate about, enough that I am willing to debate my viewpoint: "))
Q25 = int(input("During this time of online learning, I am able to be productive everyday: "))

Q26 = int(input("Challenge and change are good: "))
Q27 = int(input("I tend to be an optimist, even if I’m not always down to earth: "))
Q28 = int(input("No one can truly motivate me until I motivate myself: "))
Q29 = int(input("I move on from my past regrets: "))
Q30 = int(input("I often set goals of what I want to accomplish: "))

Q31 = int(input("I know my strengths and weaknesses: "))
Q32 = int(input("I try not to allow stress, negativity, and uncertainty bother my peace of mind: "))
Q33 = int(input("I like to stand out, whether by my fashion, style, or personality: "))
Q34 = int(input("I believe that my education is more than just a means to an end: "))
Q35 = int(input("I wake up every day, happy and ready to take on the world: "))

TotalScore = Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8 + Q9 + Q10 + Q11 + Q12 + Q13 + Q14 + Q15 + Q16 + Q17 + Q18 + Q19 + Q20 + Q21 + Q22 + Q23 + Q24 + Q25 + Q26 + Q27 + Q28 + Q29 + Q30 + Q31 + Q32 + Q33 + Q34 + Q35
print()

print()

def MotivationLevel():
    if TotalScore >= 141 and TotalScore <= 175:
        inFile = open('HighMotivation.txt','r')
        contents = inFile.read()
        print(contents)
        
    elif TotalScore >= 106:
        inFile = open('AverageMotivation.txt','r')
        contents = inFile.read()
        print(contents)
        
    elif TotalScore >= 71: 
        inFile = open('MediumMotivation.txt','r')
        contents = inFile.read()
        print(contents)
        
    elif TotalScore >= 35:
        inFile = open('BelowAverageMotivation.txt','r')
        contents = inFile.read()
        print(contents)
        
    else:
        print("Each question must be answered on a scale of 1 to 5. Please repeat the questionnaire and make sure you answer every question.")
MotivationLevel()
print()

print("Thank you for rating the statements above. Now, please take some time to enter some specific information about yourself.")

print()

def getKeys(formatString):

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) 

    return set(keyList) 

def addPick(cue, dictionary): 
    
    promptFormat = "Enter your {answer}: "
    prompt = promptFormat.format(answer=cue)
    response = input(prompt)
    dictionary[cue] = response


def getUserPicks(cues):
    
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks   

def tellStory(storyFormat):
    
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():

    storyFormat = ''
    file = open('personalizedMessage.txt', 'r')
    for line in file:
        storyFormat = storyFormat + line.strip()

    tellStory(storyFormat)
    
main()

print()
print()

scoreResponse = input("Would you like to know your numerical motivation level? Enter Yes or No: ")
def scoreReport():
    if scoreResponse == "Yes":
        TotScore = TotalScore
        percentileScore = TotScore/1.75
        print('Your total score out of 175 points is {TotScore} points, which is a Motivation Level of {percentileScore:.2f}%.'
          .format(**locals()))
    else:
        print("That's alright too!")
    
scoreReport()

print()
print()
print()

from graphics import *
import random, time

def closingGraphic():
    win = GraphWin("Thank You for Taking Assessment", 400, 400)
    circle = Circle(Point(200,200), 150)
    circle.setFill('light blue')
    circle.draw(win)
    message1 = Text(Point(win.getWidth()/2, 200), 'Thank you for taking our Motivation Test!')
    message1.setStyle("bold")
    message1.setSize(15)
    message1.draw(win)
    time.sleep(3)
    for i in range(80):
        r = random.randrange(5)
        b = random.randrange(256)
        g = random.randrange(5)
        color = color_rgb(r, g, b)
        
        radius = random.randrange(3, 40)
        x = random.randrange(5, 395)
        y = random.randrange(5, 395)
        
        circle = Circle(Point(x,y), radius)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(0.09)

    message = message = Text(Point(win.getWidth()/2, 380), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()    

closingGraphic()
