class Node:
    def __init__(self):
        self.child={}
        self.end=False
root=Node()
def insert(word):
    p=root
    for ch in word:
        if ch not in p.child:
            p.child[ch]=Node()
        p=p.child[ch]
    p.end=True
def search(word):
    p=root
    for ch in word:
        if ch not in p.child:
            return 0
        p=p.child[ch]
    return 1 if p.end else 0
n=int(input())
words=input().split(",")
s=input()
for word in words:
    insert(word)
print(search(s))
