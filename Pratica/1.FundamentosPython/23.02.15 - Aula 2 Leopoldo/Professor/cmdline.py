import getopt, argparse
import sys
first = ""
last = ""
argv = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, "f:l:", ["first =", "last ="])
    print(options)
    print(args)
except:
    print("alguma mensagem de erro")

for name, value in options:
    if name in ['-f', '--first']:
        first = value
    elif name in ['-l', '--last']:
        last = value

print("First:", first)
print("Last:", last)