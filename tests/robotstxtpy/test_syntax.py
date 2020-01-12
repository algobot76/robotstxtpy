#!/usr/bin/env python3
from robotstxtpy.syntax import checkLine

def test_checkLine():
    assert checkLine(["abc", "Allowed: /home/", "User-agent: hello",  "Allowed: abc", "Disallowed: /test/%%" ]) == 0
    
if __name__ == "__main__":
    test_checkLine()
    
