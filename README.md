![icon](https://github.com/user-attachments/assets/54d22a47-19af-470c-bb17-35fc7d88e3a9)

# The FWS Programming Language
## Instructions
```
psh - Pushes an item onto the stack
swp - Swaps two stack items
get - Prints a specified stack item
pop - Removes a specified stack item
jmp - Jumps to a certain line if criteria is met
ask - Takes user input, and pushes it to the top of the stack
ext - Exits
```
## PSH
|symbol|push type|
|-|-|
|$|String |
|&|Random number (psh min max) |
|*|Mathematical operation (+, -, *, /, % , ^) |
|!|Integer |

## JMP
|symbol|operation|
|-|-|
|==|Equal |
|!=|Not equal |
|<|Less than |

|Follow up operations|example|
|-|-|
|jmp|jmp 0 == 1 jmp 0|
|ext|jmp 0 == 1 ext|

*(JMP CAN ONLY COMPARE STACK ITEMS)*

## ASK

|symbol|ask type|
|------|--------|
|$     |String  |
|!     |Integer |

# Others
You can use `-v` to get the interpreter version

# Releases
You can run the raw python file followed up by a file with the .fws extension, or you can download the precompiled executable (No MacOS anytime soon). Thanks to the Pyinstaller team for making this possible.

*1.2.0*
