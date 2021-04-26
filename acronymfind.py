file = open('thesis.txt', 'r', encoding = 'UTF-8' )
filestring = file.read()

def isCAP(letter):
    ''' string --> boolean
    checks if a letter is in caps, if it is returns True'''
    if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D' or letter == 'E' or letter == 'F' or letter == 'G' or letter == 'H' or letter == 'I' or letter == 'J' or letter == 'K' or letter == 'L' or letter == 'M' or letter == 'N' or letter == 'O' or letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S' or letter == 'T' or letter == 'U' or letter == 'V' or letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
        return True
    else:
        return False

print (isCAP('Z'))

def makeAcrolist (filestring):
    '''string -> list
    takes a string and makes a list of all the acronyms present, that is words that are made up of 2 or more capitalized letters'''
    acrolist = []
    acro = []
    acrostringlist = []
    noreplist = []
    
    for letter in (filestring):
        if isCAP(letter) == True:
            acro.append(letter)
        elif len(acro) > 1 and isCAP(letter) == False:
            acrolist.append (acro)
            acro = []
        else:
            acro = []
    
    for acro in acrolist:
        acro = ''.join(acro)
        #print (acro)
        acrostringlist.append(acro)
        
    for acro in acrostringlist:
        if acro in noreplist:
            continue
        else:
            noreplist.append(acro)
    return noreplist
            
print ('start here')     
for acro in (makeAcrolist(filestring)):
    print (acro)
#print (filestring)
#print (makeAcrolist(filestring))