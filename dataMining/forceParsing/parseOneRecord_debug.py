import utilities

# design and define test case:
testRecord = []
testRecord.append('                          S&P 500 INDEX   - November 12, 2008')
testRecord.append('                  COMPANY         GICS ECONOMIC SECTOR      GICS SUB-INDUSTRY')
testRecord.append('     DELETED General Growth            Financials             Retail REITs')
testRecord.append('                Properties')

result1 = utilities.parseRecord(testRecord)
print(map(utilities.caseInfo.__str__, result1))


testRecord_2 = []
testRecord_2.append('                             S&P 500 INDEX - TBA')
testRecord_2.append('             COMPANY            GICS ECONOMIC SECTOR         GICS SUB-INDUSTRY')
testRecord_2.append('    ADDED    CF Industries      Materials                    Fertilizers &')
testRecord_2.append('                                                             Agricultural')
testRecord_2.append('                                                             Chemicals')
testRecord_2.append('    DELETED  Electronic Data    Information Technology       Data Processing &')
testRecord_2.append('             Systems                                         Outsourced')
testRecord_2.append('                                                             Services')

result2 = utilities.parseRecord(testRecord_2)
print(map(utilities.caseInfo.__str__, result2))






