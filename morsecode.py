morsedata = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', 
              '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-'}
choice=input("1.Morse Code encoder\n2.Morse code decoder\nPress 1 or 2 to move further\n")
choice=int(choice)
#Text to Morse conversion
if(choice==1):
    text_input=input("Enter text to be converted to Morse code\n")
    text_input=text_input.upper()
    for i in list(text_input):
        if(i==" "):
            print("    ",end="")
        elif(i==list(text_input[-1])):
            print(morsedata.get(i),end="")
        else:
            print(morsedata.get(i),end="  ")
#Morse to text conversion
elif(choice==2):
    word=list()
    print("RULES:\n1. No space between dots and dashes expressing letter\n2. Double space between two letter's morse code\n3. 6 spaces between letters")
    morse_input=input("Enter morse code to be converted to text\n")
    word=morse_input.split("  ")
    i=0
    while (i<=(len(word)-2)):
        if(word[i]==word[i+1]):
            word.pop(i)
        else:
            i+=1
    for j in word:
        if(j==''):
            print(" ",end="")
        for key,value in morsedata.items():
            if(value==j):
                print(key,end="")
