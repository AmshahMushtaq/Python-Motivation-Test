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
    file.close()
    exit()

main()

