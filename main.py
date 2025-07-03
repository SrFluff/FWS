import os
import sys
from sys import argv
import random

argv.pop(0)

if len(argv) == 0:
    print("No file given")
    sys.exit()

if not argv[0] == "-v":
    if os.path.exists(argv[0]):
        f = open(argv[0], "r")
        doc = []
        for line in f:
            doc.append(line)
        f.close()
else:
    print("1.2.0")
    sys.exit()

if os.path.exists("log.eff"):
    os.remove("log.eff")
f = open("log.eff", "w")

i = 0
stack = []
while i < len(doc):
    if len(doc[i].split()) == 0:
        pass
    else:
        if doc[i].split()[0] == "psh":
            if doc[i].split()[1] == "$":
                f.write("a2\n")
                stack.append(doc[i][6:-1])
            elif doc[i].split()[1] == "&":
                f.write("a3\n")
                stack.append(random.randint(int(doc[i].split()[2]), int(doc[i].split()[3])))
            elif doc[i].split()[1] == "*":
                f.write("a4\n")
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
                f.write("a1\n")
                stack.append(int(doc[i].split()[2]))
        elif doc[i].split()[0] == "get":
            f.write("b0\n")
            print(stack[int(doc[i].split()[1])])
        elif doc[i].split()[0] == "jmp":
            if doc[i].split()[2] == "==":
                f.write("c1\n")
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one == num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        sys.exit()
            elif doc[i].split()[2] == "!=":
                f.write("c2\n")
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one != num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        sys.exit()
            elif doc[i].split()[2] == "<":
                f.write("c3\n")
                num_one = stack[int(doc[i].split()[1])]
                num_two = stack[int(doc[i].split()[3])]
                if num_one < num_two:
                    if doc[i].split()[4] == "jmp":
                        i = int(doc[i].split()[5]) - 1
                    elif doc[i].split()[2] == "ext":
                        sys.exit()
        elif doc[i].split()[0] == "ext":
            f.write("d0\n")
            sys.exit()
        elif doc[i].split()[0] == "pop":
            f.write("e0\n")
            stack.pop(int(doc[i].split()[1]))
        elif doc[i].split()[0] == "swp":
            f.write("f0\n")
            num_one = stack[int(doc[i].split()[1])]
            num_two = stack[int(doc[i].split()[2])]
            temp = num_one
            stack[int(doc[i].split()[1])] = num_two
            stack[int(doc[i].split()[2])] = temp
    i += 1
f.close()
