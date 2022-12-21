import  collections


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word=False
        self.children={}

class Trie:

    def __init__(self):
        self.root=TrieNode()


    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node=self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter]=TrieNode()
            node=node.children[letter]
        node.word=True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return  False
            node = node.children[letter]
        return  node.word


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return  False
            node = node.children[letter]
        return True




trie =  Trie();
trie.insert("apple");
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app");
print(trie.search("app"))   # return True