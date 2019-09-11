#!/usr/bin/env python
# coding: utf-8

# In[41]:


####1. Merge String  
a = 'aaaaaaaa'
b = 'a'
m = len(a)
n = len(b)
ans = len(a) 
for i in range(m):
    for j in range(n):
        if a[i+j] != b[j]:
            break
        else:
            if i+j == m -1:
                ans = i
                break
       
    print(ans)
print(a[:ans] + b)


# In[454]:


###2.
#### Prefix/Non-prefix Search 
#### prefix search
import collections
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = {}
class Solution:
    def __init__(self):
        self.node = TrieNode()
    def insert(self, word):
        current = self.node
        for char in word:
            char = char.lower()
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
    def prefix_search(self, word):
        current = self.node
        for char in word:
            if char in current.children:
#                 return False
                current = current.children[char]
        return True
##test:
a = ["Burger King", "kdk dnsd Burgers", "sad Burger's", "asdd das a", "Walburgers"]
res = []
solution = Solution()
for word in a:
    for sub in word.split(' '):
#         print(sub)
        solution.insert(sub)
#         print(solution)
        if solution.prefix_search('bur'):
            res.append(word)
print(res)


# In[54]:


def strStr(haystack: str, needle: str):
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return True
        return False


# In[55]:


####3. substring search
a = ["Burger King", "kdk dnsd Burgers", "sad Burger's", "asdd das a", "Walburgers"]
res = []
for name in a:
    for char in name.split(' '):
        if strStr(char.lower(), 'bur'):
            res.append(name)
print(res)


# In[106]:


###4. love messgae
love_message = [{"sender":'a', "email":'1',"receiver":'b'},
                {"sender":'a', "email":'1',"receiver":'b'},
                {"sender":'c', "email":'3',"receiver":'a'},
                {"sender":'b', "email":'2',"receiver":'c'}]

class Item:
    def __init__(self,count,word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
import collections, heapq
def top_k(love_messgae, k):
    count_map = collections.defaultdict(int)
    heap = []
    res = []
    for item in love_message:
        count_map[item["receiver"]] += 1
    for name, count in count_map.items():
        item = Item(count, name)
        heapq.heappush(heap, (item))
        if len(heap)> k:
            heapq.heappop(heap)
    while heap:
        res.append(heapq.heappop(heap).word)
    return res[::-1]
top_k(love_message, 2)

###follow up: remove duplicates:
visited = []
for item in love_message:
    if item in visited:
        continue
    visited.append(item)


# In[ ]:


####5.Random Match Users
import random
def helper(a_list):
    res = []
    random.shuffle(a_list)
    for i in range(1, len(a_list),2):
        res.append((a_list[i-1], a_list[i]))
    return res

a_list = ['a','b','c','d','e','f']
helper(a_list)


# In[385]:


####Random Match Users follow up
b_list = [{'id': 'Alan', 'team': 'a'}, {'id': 'Da', 'team': 'a'},
          {'id': 'Same', 'team': 'd'}, {'id': 'TOM', 'team': 'c'} ]       
random.shuffle(b_list)
res = []
print(b_list)
for i in range(len(b_list)-1):
    if b_list[i]['team'] == b_list[i+1]['team']:
        continue
    if not b_list[i]['id']:
        continue
    res.append((b_list[i]['id'], b_list[i+1]['id']))
    b_list[i]['id'] = None
    b_list[i+1]['id'] = None
for i in range(len(b_list)-1):
    if not b_list[i]['id']:
        continue
    for j in range(i+1, len(b_list)):
        if b_list[i]['id'] and b_list[j]['id']:
            if b_list[i]['team'] != b_list[j]['team']:
                res.append((b_list[i]['id'], b_list[j]['id']))
            else:
                res.append((b_list[i]['id'], None))
                res.append((b_list[j]['id'], None))
            b_list[i]['id'] = None
            b_list[j]['id'] = None
if b_list[len(b_list)-1]['id']:
    res.append((b_list[len(b_list)-1]['id'], None))
print(res)


# In[331]:


####6. Waiting List
class Party:
    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.next = None    
class Table:
    def __init__(self,size):
        self.size = size
class Solution:
    def __init__(self):
        self.head = Party('head',0)
        self.tail = self.head
    def addParty(self, party):
        self.tail.next = party
        self.tail = self.tail.next     
    def chooseParty(self, table):
        start = self.head.next
        prev = self.head
        while start:
            if start.size <= table.size:
                prev.next = start.next
                return start.name
            else:
                prev = start
                start = start.next                


# In[344]:


solution = Solution()
p1 = Party('a',10)
p2 = Party('b',2)
p3 = Party('c',3)
solution.addParty(p1)
solution.addParty(p2)
solution.addParty(p3)


# In[347]:


t1 = Table(3)
print(solution.chooseParty(t1))


# In[505]:


from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
    def insert(self, word):
        node = self
        for w in word:
            node = node.children[w]
        node.isEnd = True
    def search(self, word):
        node = self
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return []
        # prefix match
        # traverse currnt node to all leaf nodes
        result = []
        self.traverse(node, list(word), result)
        print(node.children)
        return [''.join(r) for r in result]

    def traverse(self, root, prefix, result):
        if root.isEnd:
            result.append(prefix[:])
        
        for c,n in root.children.items():
            print(c)
            prefix.append(c)
            self.traverse(n, prefix, result)
            prefix.pop(-1)


# In[506]:


words = {'burger': 'Burger king',
        'king' : 'king',
         'burgg' : 'a',
        'buregrs': 'burder'}
root = TrieNode()
for w in words.keys():
    root.insert(w)
map_word = root.search('bur')
res = []
for item in map_word:
    res.append(words[item])
res


# In[ ]:




