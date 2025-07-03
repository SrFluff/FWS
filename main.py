import os
from sys import argv
import random

argv.pop(0)

if len(argv) == 0:
    print("No file given")
    exit()
if os.path.exists(argv[0]):
    f = open(argv[0], "r")
    doc = []
    for line in f:
        doc.append(line)
    f.close()

i = 0
stack = []
while i < len(doc):
    if len(doc[i].split()) == 0:
        pass
    else:
        if doc[i].split()[0] == "psh":
            if doc[i].split()[1] == "$":
                stack.append(doc[i][6:-1])
            elif doc[i].split()[1] == "&":
                stack.append(random.randint(int(doc[i].split()[2]), int(doc[i].split()[3])))
            elif doc[i].split()[1] == "*":
                num_one = stack[int(doc[i].split()[2])]
                num_two = stack[int(doc[i].split()[4])]
                if doc[i].split()[3] == "+":
                    stack.append(num_one + num_two)
                elif doc[i].split()[3] == "-":
                    stack.append(num_one - num_two)
                elif doc[i].split()[3] == "*":
                    stack.append(num_one * num_two)
                elif doc[i].split()[3] == "/":
                    stack.append(num_one / num_two)
                elif doc[i].split()[3] == "%":
                    stack.append(num_one % num_two)
                elif doc[i].split()[3] == "^":
                    stack.append(num_one ** num_two)
            elif doc[i].split()[1] == "!":
                stack.append(int(doc[i].split()[2]))
        elif doc[i].split()[0] == "get":
            print(stack[int(doc[i].split()[1])])
        elif doc[i].split()[0] == "jmp":
            if doc[i].split()[2] == "==":
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one == num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        exit()
            elif doc[i].split()[2] == "!=":
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one != num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        exit()
            elif doc[i].split()[2] == "<":
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one < num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        exit()
        elif doc[i].split()[0] == "ext":
            exit()
        elif doc[i].split()[0] == "pop":
            stack.pop(int(doc[i].split()[1]))
        elif doc[i].split()[0] == "swp":
            num_one = stack[int(doc[i].split()[1])]
            num_two = stack[int(doc[i].split()[2])]
            temp = num_one
            stack[int(doc[i].split()[1])] = num_two
            stack[int(doc[i].split()[2])] = temp
    i += 1