# block_text
Converts regular text to block letters
Read more about at http://codewrencher.com/modules/code_samples/code_samples.html

"""
Basic Implementation:
"""
from BlockText import BlockText
block_text = BlockText()
greeting = block_text.format('Hello There!') # format the string into block letters
print greeting
block_text.printLine()                       # prints a dividing horizontal line
block_text.printString('1234567890')         # shortcut for simply formatting and printing a string
block_text.printString('-------------', '')  # optionally specify a custom character spacing as the second parameter
