def longestWord(lst):
    length=0
    longWord=""
    for word in lst:
        if len(word) >=length:
            length = len(word)
            longWord = word
    return longWord

print (longestWord(["Hello","I","am","Goutama","Sarma","and","I","am","printing","longest","word"]))