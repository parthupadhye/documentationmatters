def readFileAndSearchForKeyword ( filepath, searchString ):
    #open and read the file:
    f = open( filepath, "r" )
    contents = f.read()
    
    #searches the contents and assigns a True or False value to flag
    searchFlag = contents.find(searchString) >= 0
    
    #prints to the console
    if searchFlag :
        print ( "File '" + filepath + "' contains the string : '" + searchString + "'" )
        return True

    print ( "File '" + filepath + "' does not contain the string : '" + searchString + "'" )
    return False

#will output "File 'TextBlock.txt' contains the string : 'Linux':
readFileAndSearchForKeyword ( "TextBlock.txt", "Linux" )

#File 'TextBlock.txt' does not contain the string : 'Microsoft':
readFileAndSearchForKeyword ( "TextBlock.txt", "Microsoft" )
