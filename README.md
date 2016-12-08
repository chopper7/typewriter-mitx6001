# typewriter-mitx6001
Given some text and a specified line length, wrap the text output.

_From:_  
MITx 6.001x - "Introduction to Computer Science with Python"  
Problem Set 6, Problem 5

"Typewriter"
- As long as i is less than len(text)-(1*lineLength)...
  * assign i to the index of the 1st whitespace after lineLength characters
  * concat the slice[i to whitespace], and a '\n', to newText
  * reassign i to that whitespace location
- Finally, concat remainder of text.

####TO DO:
- How to deal with text that already has newline characters in it?
