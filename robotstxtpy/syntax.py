#!/usr/bin/env python3
from robotstxtpy import RobotsTxt
import re
# Check syntax

def check(robottxt):
    s = ["Allow", "Disallow"]
    allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -._~:/?#[]@!$&'()*+,;="
    user_agent = robottxt.user_agents()
    print(user_agent)
    for agent in user_agent:
        print(agent)
        cntnt = robottxt.rules(agent)
        print("cntnt", cntnt)
        for tup in cntnt:
            print("in cntnt", tup)
            permission, endpoint = tup[0], tup[1]
            print(permission, endpoint)
            if permission not in s:
                return 0
            elif set(allowedChars) <= set(endpoint):
                return 0
            elif re.search(r"([+._~:?#[]@!$&'*,;()=-])\1", endpoint):
                return 0
            else:
                return 1
        
def main():
    state = 1
    rbtxt = RobotsTxt()    
    state = check(rbtxt)
    if state == 0:
        print("Syntax error. Please check syntax.")
    else:
        print("Error free!")
    return

if __name__ == "__main__":
    main()
    
