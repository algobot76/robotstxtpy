#!/usr/bin/env python3
from robotstxtpy.syntax import check
from robotstxtpy import RobotsTxt

def test_check():
    rbtxt = RobotsTxt()
    rbtxt.add_user_agent("Chrome")
    rbtxt.add_endpoint("Chrome", "Allow", "test")
    assert check(rbtxt) == 1

if __name__ == "__main__":
    test_check()
    
