"""
  _____          _   __          __                  _
 / ____|        | |  \ \        / /                 | |
| |     ___   __| | __\ \  /\  / / __ ___ _ __   ___| |__   ___ _ __
| |    / _ \ / _` |/ _ \ \/  \/ / '__/ _ \ '_ \ / __| '_ \ / _ \ '__|
| |___| (_) | (_| |  __/\  /\  /| | |  __/ | | | (__| | | |  __/ |
 \_____\___/ \__,_|\___| \/  \/ |_|  \___|_| |_|\___|_| |_|\___|_|

Copyright: None

This code is free for anyone to use, share, copy, modify, and distribute.
You may do what you want with it for any reason, except for try to claim the right to it, change this license
to a more restrictive one, and then try to get me to pay you for it.
"""


class BlockText(object):
    """
    Convert any text string to ASCII Art block letters
    Supports upper and lower case letters, numbers, and basic punctuation
    Block characters are grouped by type into their own initialization methods found at the end of the class
    Blank blocks are inserted for characters which are not defined here
    """

                            # Special characters
    blank = ''
    space = ''
    line_separator = ''
    hyphen = ''
    underscore = ''
    plus = ''
    equals = ''
    star = ''
    front_slash = ''
    left_bracket = ''
    right_bracket = ''
    left_parentheses = ''
    right_parentheses = ''
    left_curly_brace = ''
    right_curly_brace = ''
    hash_tag = ''
    less_than = ''
    greater_than = ''
    pipe = ''
    back_slash = ''
    tilde = ''
    back_tick = ''
                            # Punctuation
    period = ''
    comma = ''
    exclamation_point = ''
    exclamation_point_2 = ''
    question_mark = ''
    colon = ''
    semi_colon = ''
    single_quote = ''
    double_quote = ''
                            # Letters
    a = ''
    A = ''
    b = ''
    B = ''
    c = ''
    C = ''
    d = ''
    D = ''
    e = ''
    E = ''
    f = ''
    F = ''
    g = ''
    G = ''
    h = ''
    H = ''
    i = ''
    I = ''
    j = ''
    J = ''
    k = ''
    K = ''
    l = ''
    L = ''
    m = ''
    M = ''
    n = ''
    N = ''
    o = ''
    O = ''
    P = ''
    p = ''
    q = ''
    Q = ''
    r = ''
    R = ''
    s = ''
    S = ''
    t = ''
    T = ''
    u = ''
    U = ''
    v = ''
    V = ''
    w = ''
    W = ''
    x = ''
    X = ''
    y = ''
    Y = ''
    z = ''
    Z = ''
                            # Numbers
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    zero = ''

    def __init__(self):
        """
        Constructor: Initialize all characters
        """
        self.initSpecialChars()
        self.initPunctuation()
        self.initLetters()
        self.initNumbers()

    # Core Logic

    def format(self, string, char_spacing=' ', char_type='normal'):
        """
        Converts all regular string characters to ascii art block letters
        :param string: The message you want to conver
        :param char_type: Optional -  used to set alternate characters
        :param char_spacing: Optional - used to set character spacing
        :return: <String>: Formatted block letter string
        """
        if string is None:
            print "Encountered None string"
            return

        block_string = ''
        block_list = self.getBlockList(string, char_type)            # get a list of block chars representing the input
        max_block_height = self.getMaxBlockStringHeight(block_list)  # get the maximum height of the block string

        for line_position in range(max_block_height):                # build the block string line by line

            for block in block_list:

                max_block_width = 0
                block_lines = block.split('\n')

                # figure out the max width of the block character first
                for block_line in block_lines:

                    if len(block_line) > max_block_width:
                        max_block_width = len(block_line)

                line_spacer = ''
                for index in range(max_block_width):
                    line_spacer += ' '
                # fill in the line with block characters and fill in the rest of the width with spaces
                for char_position in range(max_block_width):
                    if line_position < len(block_lines):

                        block_line = block_lines[line_position]
                        if char_position < len(block_line):
                            block_string += block_line[char_position]
                        else:
                            block_string += ' '
                    else:
                        block_string += line_spacer

                block_string += char_spacing

            block_string += '\n'

        return block_string

    def getBlockList(self, string, char_type='normal'):
        """
        Creates a list of class variables corresponding to the characters in the passed string
        :param string:
        :param char_type:
        :return: List[class var]: A list of class variables corresponding to the characters in the passed string
        """
        block_list = []

        for char in string:
            if char == '!':
                if char_type == 'special':
                    char = 'exclamation_point_2'
                else:
                    char = 'exclamation_point'
                block_list.append(getattr(self, char))
            elif char == '?':
                block_list.append(self.question_mark)
            elif char == '.':
                block_list.append(self.period)
            elif char == ',':
                block_list.append(self.comma)
            elif char == ':':
                block_list.append(self.colon)
            elif char == ';':
                block_list.append(self.semi_colon)
            elif char == "'":
                block_list.append(self.single_quote)
            elif char == '"':
                block_list.append(self.double_quote)
            elif char == '-':
                block_list.append(self.hyphen)
            elif char == '_':
                block_list.append(self.underscore)
            elif char == '+':
                block_list.append(self.plus)
            elif char == '=':
                block_list.append(self.equals)
            elif char == '*':
                block_list.append(self.star)
            elif char == '/':
                block_list.append(self.front_slash)
            elif char == '[':
                block_list.append(self.left_bracket)
            elif char == ']':
                block_list.append(self.right_bracket)
            elif char == '(':
                block_list.append(self.left_parentheses)
            elif char == ')':
                block_list.append(self.right_parentheses)
            elif char == '{':
                block_list.append(self.left_curly_brace)
            elif char == '}':
                block_list.append(self.right_curly_brace)
            elif char == '#':
                block_list.append(self.hash_tag)
            elif char == '<':
                block_list.append(self.less_than)
            elif char == '>':
                block_list.append(self.greater_than)
            elif char == '|':
                block_list.append(self.pipe)
            elif char == '\\':
                block_list.append(self.back_slash)
            elif char == '~':
                block_list.append(self.tilde)
            elif char == '`':
                block_list.append(self.back_tick)
            elif char == ' ':
                block_list.append(self.space)
            elif char == '0':
                block_list.append(self.zero)
            elif char == '1':
                block_list.append(self.one)
            elif char == '2':
                block_list.append(self.two)
            elif char == '3':
                block_list.append(self.three)
            elif char == '4':
                block_list.append(self.four)
            elif char == '5':
                block_list.append(self.five)
            elif char == '6':
                block_list.append(self.six)
            elif char == '7':
                block_list.append(self.seven)
            elif char == '8':
                block_list.append(self.eight)
            elif char == '9':
                block_list.append(self.nine)
            elif hasattr(self, char):
                block_list.append(getattr(self, char))

            else:
                block_list.append(self.blank)

        return block_list

    def getMaxBlockStringHeight(self, block_list):
        """
        Calculate the max height of the block string, which will be the max number of new lines out of any character
        string contained in block_list
        :param block_list: List[String]:List of character string representing the input string
        :return: int: max_block_height: the maximum height of the highest character in block_list
        """
        max_block_height = 0

        for block in block_list:
            block_lines = block.split('\n')

            if len(block_lines) > max_block_height:
                max_block_height = len(block_lines)

        return max_block_height

    # Printing

    def printString(self, string, char_spacing=' '):
        """
        Simply print the input string in block format
        :param char_spacing: The spacing between characters, set to one space by default
        :param string: The string to print
        """
        print self.format(string, char_spacing)

    def printLine(self):
        """
        Prints a line to separate code
        """
        print self.line_separator

    # Initialization of Characters

    def initSpecialChars(self):
        """
        Assign string values to all special characters
        """
        self.blank = """\
 ___________
| character |
| missing   |
| from      |
| block     |
| library   |
|___________|"""
        self.space = """\






        """
        self.line_separator = """\
 ___________________________________________________________________________________________________________________
|___________________________________________________________________________________________________________________|"""

        self.hyphen = """\



 _______
|_______|

         """
        self.underscore = """\





 ___________
|___________|"""
        self.plus = """\


    __
 __|  |__
|__    __|
   |__|
"""
        self.equals = """\


 _________
|_________|
 _________
|_________|
"""
        self.star = """\

    /\\
___/  \___
\        /
 /  /\  \\
| /    \ |
"""
        self.front_slash = """\
      __
     /  /
    /  /
   /  /
  /  /
 /  /
/__/"""
        self.left_bracket = """\
 ____
|  __|
| |
| |
| |
| |__
|____|"""
        self.right_bracket = """\
 ____
|__  |
   | |
   | |
   | |
 __| |
|____|"""
        self.left_parentheses = """\
    _
  / /
 / /
| |
| |
 \ \\
  \_\\"""
        self.right_parentheses = """\
_
\ \\
 \ \\
  | |
  | |
 / /
/_/"""
        self.left_curly_brace = """\
    _
  / _|
 | |
/ /
\ \
 | |_
  \ _|"""
        self.right_curly_brace = """\
 _
|_ \
  | |
   \ \
   / /
 _| |
|_ /"""
        self.hash_tag = """\
       __  __
   ___/ /_/ /__
  /__  __  ___/
 ___/ /_/ /__
/_   __  ___/
 /_/  /_/
"""
        self.less_than = """\

    __
  /  /
/  /
\  \\
  \__\\
"""
        self.greater_than = """\

__
\  \\
  \  \\
  /  /
/__/
"""
        self.pipe = """\
 _
| |
| |
| |
| |
| |
|_| """
        self.back_slash = """\
__
\  \\
 \  \\
  \  \\
   \  \\
    \  \\
     \__\\"""
        self.tilde = """\


   __      _
 /  _  \__/ |
|_/   \ __ /

"""
        self.back_tick = """\
__
\ |
 \|



"""

    def initPunctuation(self):
        """
        Assign string values to all punctuation characters
        """
        self.period = """\





 __
|__|"""
        self.comma = """\




  __
/_  |
 /_/"""
        self.exclamation_point = """\
 __
|  |
|  |
|  |
|__|
 __
|__|"""
        self.exclamation_point_2 = """\
________
\      /
 \    /
  \  /
  |__|
   __
  |__|  """
        self.question_mark = """\
   _____
 /   _   \\
|_ /   \  \\
       /  /
     /_ /
     __
    |__|  """
        self.colon = """\

  __
 |__|

  __
 |__|
"""
        self.semi_colon = """\

  __
 |__|

  __
/_  |
 /_/"""
        self.single_quote = """\
     _
   / /
 /__/



"""
        self.double_quote = """\
     _   _
   / / / /
 /__//__/



"""

    def initLetters(self):
        """
        Assign string values to all letter characters
        """
        self.a = """\



  __ _
 / _` |
| (_| |
 \__,_|"""
        self.A = """\
     __
    /   \\
   /     \\
  /  / \  \\
 /  /___\  \\
|   _____   |
|__|     |__|"""
        self.b = """\


 _
| |__
| '_ \\
| |_) |
|_.__/"""
        self.B = """\
 ______
|   __  \\
|  |__|  |
|   __   /
|  /  \  \\
|  \__/   |
|________/ """
        self.c = """\



  ___
 / __|
| (__
 \___|"""
        self.C = """\
    ____
  /  __  \\
 /  /  \__\\
|  |
|  |    ___
 \  \__/  /
  \ ____ /  """
        self.d = """\


     _
  __| |
 / _` |
| (_| |
 \__,_|"""
        self.D = """\
 ______
|   __  \\
|  |  \  \\
|  |   |  |
|  |   |  |
|  |__/  /
|_______/  """
        self.e = """\



   _
 / _ \\
|  __/
 \___|"""
        self.E = """\
 _________
|   ______|
|  |____
|   ____|
|  |
|  |_____
|________|"""
        self.f = """\


  __
 / _|
| |_
|  _|
|_|"""
        self.F = """\
 _________
|   ______|
|  |____
|   ____|
|  |
|  |
|__|"""
        self.g = """\


  __ _
 / _` |
| (_| |
 \__, |
 |___/"""
        self.G = """\
    _____
  /  ___  \\
 /  /   \__|
|  |   ____
|  |  |_   |
 \  \__/  /
  \______/  """
        self.h = """\


 _
| |_
| '_ \\
| | | |
|_| |_|"""
        self.H = """\
 __     __
|  |   |  |
|  |___|  |
|   ___   |
|  |   |  |
|  |   |  |
|__|   |__|"""
        self.i = """\


 _
(_)
| |
| |
|_|"""
        self.I = """\
 ________
|__    __|
   |  |
   |  |
   |  |
 __|  |__
|________|"""
        self.j = """\

   _
  (_)
  | |
  | |
 _/ |
|__/ """
        self.J = """\
   ________
  |__    __|
     |  |
     |  |
__   |  |
\  \_|  |
 \______/"""
        self.k = """\


 _
| | __
| |/ /
|   \\
|_|\_\\"""
        self.K = """\
 __    ___
|  |  /  /
|  |_/  /
|      /
|  |\  \\
|  | \  \\
|__|  \__\\"""
        self.l = """\


 _
| |
| |
| |
|_|
"""
        self.L = """\
 __
|  |
|  |
|  |
|  |
|  |_____
|________|
"""
        self.m = """\



 _ __ __
| '_ ` _ \\
| | | | | |
|_| |_| |_|"""
        self.M = """\
 __        __
|   \    /   |
|    \  /    |
|  |\ \/ /|  |
|  | \  / |  |
|  |  \/  |  |
|__|      |__|"""
        self.n = """\



 _ _
| '_ \\
| | | |
|_| |_|"""
        self.N = """\
 ___     __
|   \   |  |
|    \  |  |
|  |\ \ |  |
|  | \ \|  |
|  |  \    |
|__|   \___|"""
        self.o = """\



   _
 / _ \\
| (_) |
 \___/ """
        self.O = """\
    ____
  /  __  \\
 /  /  \  \\
|  |    |  |
|  |    |  |
 \  \__/  /
  \______/  """
        self.p = """\


 _ _
| '_ \\
| |_) |
| .__/
|_|"""
        self.P = """\
 _____
|   _  \\
|  | \  |
|  |_/ /
|   _ /
|  |
|__|"""
        self.q = """\


  __ _
 / _` |
| (_| |
 \__, |
    |_|"""
        self.Q = """\
    ____
  /  __  \\
 /  /  \  \\
|  |    |  |
|  |    |  |
 \  \__/   \\
   \___/\ __\\ """
        self.r = """\



 _ __
| '__|
| |
|_|"""
        self.R = """\
 _____
|   _  \\
|  | \  |
|  |_/ /
|   _  \\
|  | \  \\
|__|  \__\\ """
        self.s = """\



 ___
/ __|
\__ \\
|___/"""
        self.S = """\
  _______
/   ___   \\
\   \   \__\\
   \  \\
__   \  \\
\  \__ \  \\
 \_______ /"""
        self.t = """\


 _
| |_
| __|
| |_
 \__|"""
        self.T = """\
 __________
|___    ___|
    |  |
    |  |
    |  |
    |  |
    |__|
"""
        self.u = """\



 _   _
| | | |
| |_| |
 \__,_|"""
        self.U = """\
 __      __
|  |    |  |
|  |    |  |
|  |    |  |
|  |    |  |
\  \____/  /
 \________/  """
        self.v = """\



__   __
\ \ / /
 \ V /
  \_/"""
        self.V = """\
 __        __
|  |      |  |
 \  \    /  /
  \  \  /  /
   \  \/  /
    \    /
     \__/"""
        self.w = """\



__      __
\ \ /\ / /
 \ V  V /
  \_/\_/"""
        self.W = """\
 __        __
|  |      |  |
|  |      |  |
\  \  /\  /  /
 \  \/  \/  /
  \   /\   /
   \_/  \_/"""
        self.x = """\



__  __
\ \/ /
 /  \\
/_/\_\\"""
        self.X = """\
  ___     ___
  \  \   /  /
   \  \ /  /
    |     |
    /  /\  \\
   /  /  \  \\
  /__/    \__\\"""
        self.y = """\


 _   _
| | | |
| |_| |
 \__, |
 |___/ """
        self.Y = """\
  ___    ___
  \  \  /  /
   \  \/  /
    \    /
     |  |
     |  |
     |__|"""
        self.z = """\



  ____
 |_  /
  / /
 /___|"""
        self.Z = """\
 _________
|______   |
      /  /
    /  /
   /  /
 /  /_____
|_________|"""

    def initNumbers(self):
        """
        Assign string values to all number characters
        """
        self.one = """\
   __
  /  |
/_   |
  |  |
  |  |
 _|  |_
|______|
"""
        self.two = """\
  ______
 /  ___  \\
|__/   \  |
  _____/  /
 /  _____/
|  |______
|_________|
"""
        self.three = """\
  ______
 /  ___  \\
|__/  _\  \\
     |_   /
 __    \  \\
|  \___/  /
 \_______/  """
        self.four = """\
 __     __
|  |   |  |
|  |   |  |
|  |___|  |
|______   |
       |  |
       |__| """
        self.five = """\
 _________
|   ______|
|  |____
|_____   \\
 __    \  \\
|  \___/  /
 \_______/  """
        self.six = """\
    ______
  /  _____|
 /  /___
|   ___  \\
|  /   \  \\
\  \___/  /
 \_______/  """
        self.seven = """\
 _________
|______   |
       |  |
      /  /
     /  /
    /  /
   /__/  """
        self.eight = """\
   _____
 /  ___  \\
|  |___|  |
\   ___   /
/  /   \  \\
|  \___/  |
 \_______/ """
        self.nine = """\
   _____
 /  ___  \\
|  |___|  |
\______   |
 __    |  |
|  \___/  |
 \_______/ """
        self.zero = """\
   _____
 /  ___  \\
|  |   |  |
|  |   |  |
|  |   |  |
|  |___|  |
 \_______/ """
