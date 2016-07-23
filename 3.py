#!/usr/bin/python


def loadFile(fileName):
       InputFile = open(fileName)
       fileInputText = InputFile.read().splitlines() 
       return fileInputText

def main():

    try:
        File = '/tmp/input'
        string = loadFile(File)
        MaxWidth = string[0]
    
    	tokenstring = string[1].split()
    	counter = int(MaxWidth)
    	line=''
    	i=0

    	for token in tokenstring:
        	i+=1
		wordsize = len(token)+1
	        counter = counter - wordsize
		line = line + token + ' ' 
		if (counter <= 0) or (i == len(tokenstring)): 
	            counter = int(MaxWidth)
	            print line
	            line=''
          
     	return 0

    except IOError:
		print "Error : Input file not found"
		return 1          
  
if __name__ == "__main__":
    main()

