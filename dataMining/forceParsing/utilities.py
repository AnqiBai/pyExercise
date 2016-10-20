import re # for regular expression

class caseInfo(object):

    def __init__(self, companyName, announceDate, actionType):
        self.companyName = companyName
        self.announceDate = announceDate
        self.actionType = actionType

    def __str__(self):
        return (self.announceDate + '|' + self.companyName + '|' + self.actionType)


def wordCenter(word):
    wordLen = len(word)
    if wordLen % 2 == 0 :
        result = wordLen/2
    else:
        result = (wordLen + 1)/2
    return result

def parseRecord(record): # record : array of stirngs
    caseList = []
    numLines = len(record)
    # parse INDEX line
    line = record[0]
    tLine = re.sub(' +',' ', line)  # remove redundant spaces in string
    dateLoc = tLine.find('- ') + 2
    tLine = tLine[dateLoc:]
    gDate = tLine.strip()
    # parse table head line, get locations
    line = record[1]
    companyLoc = line.find('COMPANY') + 4 # center of first column
    gicsLoc = line.find('GICS ECONOMIC') + 11 # center of second column
    indusLoc = line.find('GICS SUB') + 9 # center of third column
    ind_currentLine = 2
    caseState = 0 # turn off case state
    companyName = []
    actionType = 'error'
    while ind_currentLine < numLines:
        ind_currentLine += 1
        tLine = record[ind_currentLine - 1]
        deleteFlag = tLine.find('DELETED')
        addFlag = tLine.find('ADDED')
        if deleteFlag != -1 or addFlag != -1:
            companyNameStr = ' '.join(companyName)
            caseList.append(caseInfo(companyNameStr, gDate, actionType))
            companyName = []
            if deleteFlag != -1:
                actionType = 'DELETED'
            else:
                actionType = 'ADDED'
            tList = re.sub(' +', ' ', tLine).strip().split(' ')
            tList.pop(0)
            for word in tList:
                tLoc = tLine.find(word) + wordCenter(word) # potential bug using find here, for the same word may appear at different locations
                dist1 = abs(tLoc - companyLoc)
                dist2 = abs(tLoc - gicsLoc)
                dist3 = abs(tLoc - indusLoc)
                if dist1 < dist2 and dist1 < dist3:
                    companyName.append(word)
                else:
                    break # stop examing when confront the first word which is too far
        else:
            tList = re.sub(' +', ' ', tLine).strip().split(' ')
            for word in tList:
                tLoc = tLine.find(word) + wordCenter(word)
                dist1 = abs(tLoc - companyLoc)
                dist2 = abs(tLoc - gicsLoc)
                dist3 = abs(tLoc - indusLoc)
                if dist1 < dist2 and dist1 < dist3:
                    companyName.append(word)
    companyNameStr = ' '.join(companyName)
    caseList.append(caseInfo(companyNameStr, gDate, actionType))
    caseList.pop(0)
    return caseList
