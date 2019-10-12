fin = open('words.txt')

def avoid(word,letters):
    #this function takes a word and a string of forbidden letters, 
    #and that returns True if the word doesn’t use any of the forbidden letters.
    for chr in word:
        if chr in letters:
            return False
    else:
        return True
    
def avoid_costom():
    #prompt the user to enter a string of forbidden letters 
    letters = raw_input('Enter the forbidden letters: ')
    return letters

def count(fin, letters):
    #print the persent of words that don’t contain any of forbidden letters.
    count2 = 0
    count1 = 0
    for line in fin:
       if avoid(line,letters) == True:
            print line
            count2 += 1
       else:
            count1 += 1
    percent = count2*1.0/(count1+count2)*100
    return percent
        
if __name__ == "__main__":
    print str(count(fin,avoid_costom())) + "% of the forbidden words"
