import ais_decoder
import re

try:
    fileIn = open("../ingest", "r")
    regex = re.compile('!AIVDM,[0-9],[0-9],[0-9]{0,1},[0-3A-B],[0-9\\:\\;\\<\\=\\>\\?\\@A-W\\`a-w]+,[0-9]\*[A-F0-9]{2}')
    matchList = regex.findall(fileIn.read())
    print(len(matchList))
    for i in matchList:
        m1 = i+"\n"
        ais_decoder.pushAisSentence(m1, len(m1))
        #msg = ais_decoder.popAisMessage().asdict()
        print(i)
        msg = ais_decoder.popAisMessage().asdict()
        print(msg)
    
        #ais_decoder.pushAisChunk(str, len(str))

        #n = ais_decoder.numAisMessages()
        #print("num messages = ", n)
        

        #while True:
            #if ais_decoder.numAisMessages() == 0:
                #break
            
            #msg = ais_decoder.popAisMessage().asdict()
            #print(msg)


except RuntimeError as err:
    print("Runtime error. ", err)
#except:
 #   print("Error.")
