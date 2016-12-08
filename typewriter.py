def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.
    
    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before
                 wrapping the next word.
    returns: a string, with newline characters inserted appropriately. 
    """ 
    typedText = ''
    
    i = 0
    while 0 <= i < len(text):
        j = text.find(' ', i+lineLength)
        if j == -1:
            break  # because find() returns -1 if ' ' not found
        typedText += text[i:j].lstrip() + '\n'
        i = j
    
    typedText += text[i:].lstrip()
    
    return typedText
