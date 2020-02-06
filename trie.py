class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root.children

        for char in word[:-1]:
            if char not in node:
                node[char] = {'world_end': False}
            node = node[char]
        node[word[-1]] = {'world_end': True}

    def exists(self, word):
        node = self.root.children
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node['world_end']


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'appe', 'goo', 'good', 'goos']
for w in test_words:
    if word_trie.exists(w):
        print('"{}" is a word.'.format(w))
    else:
        print('"{}" is not a word.'.format(w))
