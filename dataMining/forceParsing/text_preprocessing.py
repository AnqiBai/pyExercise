# get the summary of changes part from each file (actually, the file contains all the files)
index_state = 0
n = 0 
with open('sourceData/Factiva_2007_2008.txt', 'r') as sourceFile:
    with open('middleResult/middleResult.txt', 'w') as middleFile:
        for line in sourceFile:
            # n = n+1
            if index_state == 1 :
                if line.find('Additions to and deletions from an S&P equity') != -1:
                    index_state = 0 # turn off the state machine
                else:
                    middleFile.write(line)
            else: # index_state == 0
                if line.find('Following is a summary of the changes:') != -1:
                    index_state = 1 # turn on the state machine
                    n = n + 1
                    print(n) # maintain a record for turnning on the state machine, for debugging


# remove empty lines in the middle result
with open('middleResult/middleResult.txt','r') as inFile:
    with open('middleResult/middle_2.txt', 'w') as outFile:
        for line in inFile:
            if line.strip() != '':
                outFile.write(line)

# release the variable to avoid possible conflicting
del inFile
del outFile

# get only the "S&P 500 INDEX" part
state500 = 0 
with open('middleResult/middle_2.txt', 'r') as inFile:
    with open('middleResult/middle_3.txt', 'w') as outFile:
        for line in inFile: 
            if line.find('INDEX') != -1 : # index line, time for state change
                if line.find('S&P 500 INDEX') != -1 :
                    state500 = 1 # turn on the state machine
                    outFile.write(line)
                else:
                    state500 = 0
            else: # not an index line
                if state500 == 1: # if state machine is on
                    outFile.write(line)

del inFile
del outFile




