import re
for x in range(1, 101):
    nameOfDoc =""
    transcriptsDontExist = [3,6,9,10,13,15,17,18,26,32,40,45,49,62,66,68,73,78,79,80,83,89,91,92,93]
    if (transcriptsDontExist.__contains__(x) == False):
        if (x<10):
            nameOfDoc = "00"+str(x)+"-transcript.txt"
        elif(50<x<76):
            nameOfDoc = "0" + str(x) + "-script.txt"
        elif (x<=99):
            nameOfDoc = "0" + str(x) + "-transcript.txt"
        else:
            nameOfDoc = str(x) + "-transcript.txt"
        with open(nameOfDoc, "r") as f:
            preprocessed = ""
            for line in f:
                cleanedLine = line.strip()
                if cleanedLine: # is not empty
                    preprocessed += " "+cleanedLine
        preprocessed=re.sub(r" ?\([^)]+\)", "", preprocessed)

        preprocessed = re.sub(r" ?\([^)]+\)", "", preprocessed)
        preprocessed = re.sub("<[^>]+>", "", preprocessed)
        preprocessed = re.sub("([$@*&#]).*?\1(.*)", "", preprocessed)
        preprocessed = re.sub("\.\.\.", "", preprocessed)
        preprocessed = preprocessed.replace("-", "")
        re.sub(' +',' ',preprocessed)
        if (50 < x < 76):
            nameOfDoc = "0" + str(x) + "-transcript.txt"
        OutFile = "P"+nameOfDoc
        text_file = open(nameOfDoc, "w")
        text_file.write("%s" % preprocessed)
        text_file.close()
