from genericpath import samefile
import heapq
from itertools import count
from multiprocessing import heap
from operator import le
from platform import node
from re import L
from tkinter import NO

class Node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.right=right
        self.left=left
        self.huff=''
        
    def __lt__(self,nxt):
        return self.freq<nxt.freq
my_prefix_table={}
def print_nodes(node,val=''):
    newVal=val+str(node.huff)
    if node.left:
        print_nodes(node.left,newVal)
    if node.right:
        print_nodes(node.right,newVal)
    if not node.left and not node.right:

        print(f'{node.symbol} -> {newVal}')
        my_prefix_table[node.symbol]=newVal

my_input = input('Insert filename\n')
lines = ""
with open(f'{my_input}.txt','r',encoding='utf-8') as file:
    lines =" ".join(file.readlines())
# print(lines.count('t'))
my_set=list(set(lines))
nodes = []
for x in range(len(my_set)):
    heapq.heappush(nodes,Node(lines.count(my_set[x]),my_set[x]))
print_nodes(nodes[0])
print('printed no')
while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    left.huff=0
    right.huff=1
    newNode=Node(left.freq+right.freq,left.symbol+right.symbol,left,right)
    heapq.heappush(nodes,newNode)
print_nodes(nodes[0])


def convert_to_compress(lines):
    stringy = ""
    for char in lines:
        stringy += my_prefix_table[char]
    return stringy


def _to_bytes(data):
    b=bytearray()
    for i in range(0,len(data),8):
        b.append(int(data[i:i+8], 2))
    return bytes(b)


compressed_data=convert_to_compress(lines)
converted_to_bytes=_to_bytes(compressed_data)
with open('test.bin','wb') as file:
    file.write(converted_to_bytes)


def decode_file(root, s):
    ans = ""
    curr = root
    n = len(s)
    for i in range(n):
        if s[i] == '0':
            curr = curr.left
        else:
            curr = curr.right
        # reached leaf node
        if curr.left is None and curr.right is None:
            ans += curr.symbol
            curr = root
    return ans + '\0'


print(compressed_data)
decodedstring=decode_file(nodes[0],compressed_data)
print(decodedstring)