def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    StrOrFile=input()
    if StrOrFile[0] == 'F':
        file_name = './tests/06'
        #sys.path[0]+ "/tests/" + 
        with open(file_name, "r") as f:
            pattern = f.readline()
            text=f.readline()
    elif StrOrFile[0] == 'I':
        print()
        pattern = input()
        text = (input())
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    patternLen = len(pattern)
    textLen = len(text)
    patternHash=hash(pattern)
    HashText=hash(text[:patternLen])
    occurrences = []
    for i in range(textLen-patternLen+1):
        if HashText == patternHash:
            if text[i:i+patternLen] == pattern:
                occurrences.append(i)
        if i < textLen-patternLen:
            HashText = hash(text[i+1:i+patternLen+1])
        
    return occurrences
    # this function should find the occurances using Rabin Karp alghoritm 
    


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
