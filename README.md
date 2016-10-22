# block_text
Converts regular text to block letters

Read more about at http://codewrencher.com/modules/code_samples/code_samples.html


Basic Implementation:

from BlockText import BlockText

block_text = BlockText()

# format the string into block letters
greeting = block_text.format('Hello There!') 
print greeting

# prints a dividing horizontal line
block_text.printLine()                 

# shortcut for simply formatting and printing a string
block_text.printString('1234567890')         
block_text.printString('-------------', '')  # optionally specify a custom character spacing as the second parameter
