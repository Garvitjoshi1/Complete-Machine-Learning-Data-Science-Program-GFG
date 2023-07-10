from os import *
from sys import *
from collections import *
from math import *


from sys import stdin

n = 1
def countWords(string) :
    l = string.split()
    return len(l)
	



#main
string = stdin.readline().strip()


print(countWords(string))

