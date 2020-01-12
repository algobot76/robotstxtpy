#!/usr/bin/env python3

import re
from argparse import ArgumentParser
# Check syntax

def readText(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        cnt = 1
        lines = []
        while line:
            lines.append(line.strip())
            line = f.readline()
            cnt += 1
    return lines

def checkLine(lines):
    s = ["User-Agent: ", "Crawl-delay: ", "Allow: ", "Disallow: "]
    allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -._~:/?#[]@!$&'()*+,;="
    # specialChars = allowedChars.split('-')[1]
    # validCombos = ['*.', '-*', '*?']
    # print(len(lines))
    for count, l in enumerate(lines):
        # print(count)
        # print(l)
        if re.search(r"([+._~:?#[]@!$&'*,;()=-])\1", l):
            return 0
        if not set(l) <= set(allowedChars):
            # print(set(l), "\n",  set(allowedChars))
            # print("a", count)
            return 0
        elif "#" in l or not l.strip():
            pass
        elif s[0] in l:
            if not l.startswith(s[0], 0):
                # print("b", count)
                return 0
        elif s[1] in l:
            if not l.startswith(s[1], 0) or not isinstance(int(l[len(s[1])]), int):
                # print("c", count)
                return 0
        elif s[2] in l:
            if not l.startswith(s[2], 0) or not l[len(s[2])]  == '/':
                # print("d", count)
                return 0
        elif s[3] in l:
            if not l.startswith(s[3], 0) or not l[len(s[3])] == '/':
                # print("e", count)
                return 0
        # else:                  
            # spliced = l.split("/", maxsplit=1)
            # print(spliced[0])
            # if not spliced[0] == any(s): return 0

def main(args):
    state = 1
    # change this as needed, can generalize to PATH/TO/FILE/robots.txt
    fn = args.filename
    lines = readText(fn)
    state = checkLine(lines)
    if state == 0:
        print("Syntax error. Please check syntax.")
    else:
        print("Error free!")
    return

def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("--filename", type=str, default="robots.txt")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parseArguments()
    main(args)
    
