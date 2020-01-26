word = input()
if(len(word) == 1):
    if(word.isupper()):    
        answer = word.lower()
    else:
        answer = word.upper()
else:
    if( "".join(word[:len(word)]).isupper() ):
        answer = str(word).lower()
    elif( "".join(word[1:len(word)]).isupper() and word[0].islower()):
        answer = str(word).capitalize()
    else:
        answer = word
print(answer)