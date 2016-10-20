from utilities import *

# test of caseInfo class definition 
# a = caseInfo('name', 'date', 'type') # new an instance
# print(a) # toStr() method



gDate = '' # global variable for date
            # change on different 'S&P 500 INDEX' section
with open('middleResult/one_record.txt', 'r') as inFile:
    with open('middleResult/dates.txt', 'w') as outFile:
        for line in inFile:
            if line.find('S&P 500 INDEX') != -1: # get announceDate from every INDEX line
                tLine = re.sub(' +',' ', line)  # remove redundant spaces in string
                dateLoc = tLine.find('- ') + 2
                tLine = tLine[dateLoc:]
                outFile.write(tLine)
                gDate = tLine # update date














