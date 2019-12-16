import Stack
stack = Stack.myStack()


def BracketCheck(string):
    """Parameters 
  --------
  sting:
      String 

  Return
  -------
    Boolean if input string follows the following rules:
      - Every opening bracket has a corresponding closing bracket.
      - The opening bracket is always before its corresponding closing bracket.
      - Between a opening bracket and its corresponding closing bracket, their
        can be sets of opening and corresponding closing brackets, but no loose
        opening or closing brackets.
    """

    left = "<{(["
    right = ">})]"
    for char in string:
        if char in left:
            stack.push(char)
        elif char in right and left[right.find(char)] == stack.peek():
          # check if right bracket has containing left bracket on stack, if so remove it from stack
            stack.pop()
        elif char in right:
            return False
    return True


print(BracketCheck("[{<<[]>>}]{}[[]]"))
print(BracketCheck("<<<[]]]{][]{]()))[[]]{}][}[[]]"))
print(BracketCheck(""))
