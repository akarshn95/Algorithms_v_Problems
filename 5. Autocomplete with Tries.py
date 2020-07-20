# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word=False
        self.children={}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char]=TrieNode()
    
    def suffixes(self,suffix=''):
        words=[]
        
        for i in self.children:
            if self.children[i].is_word:
            #the suffix is from the previous iteration/recursion   
                words.append(suffix+i)
            words+=self.children[i].suffixes(suffix+i)
        return words
        
        
## The Trie itself containing the root node and insert/find functions
class Trie(object):

    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        node=self.root
        for char in word:
            node.insert(char)
            node=node.children[char]
        node.is_word=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node=self.root
        
        for char in prefix:
            if char in node.children:
                node=node.children[char]
            else:
                return None
        return node


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",""
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\t','\n \t'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# # TEST CASE 2
# MyTrie = Trie()
# wordList = [
#     "zzz"
# ]
# for word in wordList:
#     MyTrie.insert(word)
# #interact(f,prefix='');

# # TEST CASE 3
# MyTrie = Trie()
# wordList = [ ]
# for word in wordList:
#     MyTrie.insert(word)
# #interact(f,prefix='');


