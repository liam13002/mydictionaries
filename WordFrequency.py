
infile = open("sometext.txt", "r")
  

freqDict = dict()
  

for line in infile:
    
    line = line.replace(',',' ')
    line = line.replace('.', ' ')
    line = line.lower()
    
    words = line.split(" ")
                             
    for word in words:
        
        if word in freqDict:
            
            freqDict[word] = freqDict[word] + 1
        else:
            
            freqDict[word] = 1

for key in list(freqDict.keys()):
    print(key, ":", freqDict[key])