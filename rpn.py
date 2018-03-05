#!/usr/bin/env python3
import readline
import sys

class bcolors:
    PROMPT = '\033[94m'
    POS = '\033[92m'
    INPUT = '\033[93m'
    NEG = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			arg1 = stack.pop()
			arg2 = stack.pop()
			if token == "+":
				return arg1 + arg2
			elif token == "^":
				return arg2**arg1
			elif token == "*":
				return arg1*arg2
			elif token == "-":
				return arg2-arg1

def main():
	while True:
		try:
			val = calculate(input(bcolors.PROMPT + "rpn calc> " + bcolors.INPUT))
			if val >= 0:
				print(bcolors.POS + str(val))
			elif val < 0:
				print(bcolors.NEG + str(val))
		except KeyboardInterrupt:
			sys.exit()
		except:
			pass
if __name__ == '__main__':
	main()
