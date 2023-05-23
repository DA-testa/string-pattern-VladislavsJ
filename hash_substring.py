B = 256
Q = 13

def read_input():
    StrOrFile = input()
    if StrOrFile[0] == 'F':
        file_name = './tests/06'
        with open(file_name, "r") as f:
            pattern = f.readline()
            text = f.readline()
    elif StrOrFile[0] == 'I':
        pattern = input()
        text = input()

    return pattern.rstrip(), text.rstrip()

def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0   
    for i in range(m):
        result = (result * B + ord(pattern[i])) % Q
    return result

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    patternLen = len(pattern)
    textLen = len(text)
    patternHash = get_hash(pattern)
    HashText = get_hash(text[:patternLen])
    occurrences = []
    multiplier = 1
    for i in range(1,patternLen):
        multiplier = (multiplier * B) % Q

    for i in range(textLen - patternLen + 1):
        if HashText == patternHash:
            if text[i:i+patternLen] == pattern:
                occurrences.append(i)
        if i < textLen - patternLen:
            HashText = (B * (HashText - ord(text[i]) * multiplier) + ord(text[i + patternLen])) % Q
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
