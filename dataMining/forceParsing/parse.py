import utilities

resultList = []
temp500 = []
state500 = 0 
with open('middleResult/middle_3.txt', 'r') as inFile:
    for line in inFile:
        if line.find('S&P 500 INDEX') != -1:
            if state500 == 0:
                state500 = 1
                temp500.append(line)
            else:
                if len(temp500) > 0:
                    resultList += utilities.parseRecord(temp500)
                    temp500 = []
                    temp500.append(line)
        else:
            temp500.append(line)
    # after for loop
    resultList += utilities.parseRecord(temp500)
del inFile

# for debugging
# print('\n'.join(map(utilities.caseInfo.__str__, resultList)))

result = '\n'.join(map(utilities.caseInfo.__str__, resultList))
# print final result
with open('finalResult/final.txt', 'w') as resultFile:
    resultFile.write(result)