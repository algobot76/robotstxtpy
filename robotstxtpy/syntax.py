#!/usr/bin/env python3
from robotstxtpy import RobotsTxt
import re
# Check syntax

def check(robottxt):
    s = ["Allow", "Disallow"]
    allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -._~:/?#[]@!$&'()*+,;="
    user_agent = robottxt.user_agents()
    for agent in user_agent:
        cntnt = robottxt.rules(agent)
        for tup in cntnt:
            permission, endpoint = tup[0], tup[1]
            if permission not in s:
                return False
            elif set(allowedChars) <= set(endpoint):
                return False
            elif re.search(r"([+._~:?#[]@!$&'*,;()=-])\1", endpoint):
                return False
            else:
                return True
        
def main():
    state = True
    rbtxt = RobotsTxt()    
    state = check(rbtxt)
    if not state:
        print("Syntax error. Please check syntax.")
    else:
        print("Error free!")
    return

    
