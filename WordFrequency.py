
infile = open("sometext.txt", "r")
  

freqDict = dict()
  

for w in infile:
    
    w = w.replace(',',' ')
    w = w.replace('.', ' ')
    w = w.lower()
    
    words = w.split(" ")
                             
    for word in words:
        
        if word in freqDict:
            
            freqDict[word] = freqDict[word] + 1
        else:
            
            freqDict[word] = 1

for key in list(freqDict.keys()):
    print(key, ":", freqDict[key])