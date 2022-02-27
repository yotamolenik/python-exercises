
class Node(object):
        def __init__(self, c=None):
            if c:
                self.__char = c
            self.__is_word = False
            self._children = [None] * 26
        
        def setchar(self, c):
            self.__char = c
        
        def getchar(self):
            return self.__char

        def isword(self):
            return self.__is_word

        def set_isword(self, isword):
            self.__is_word = isword

        @property
        def children(self):
            return self._children


class Trie(object):
    """ a Trie data structure for the letters a-z"""
    def __init__(self):
        self._root = Node()

    def insert(self, word):
        curr = self._root
        for c in word:
            index = ord(str(c)) - 97  # a -> 0
            if curr.children[index] is None:
                curr.children[index] = Node(c)
            curr = curr.children[index] # move down the tree
        curr.set_isword(True)

    def search(self, word):
        curr = self._root
        for c in word:
            for index, child in enumerate(curr.children):
                if child is not None:
                    if child.getchar() == c:
                        curr = curr.children[index]
        return curr.isword()

    def starts_with(self, prefix):
        curr = self._root
        down = False
        for c in prefix:
            for index, child in enumerate(curr.children):
                if child is not None:
                    if child.getchar() == c:
                        curr = curr.children[index]
                        down = True
            if not down:
                return False
        return True


if __name__ == "__main__":
    t = Trie()
    t.insert('cats')
    t.insert('cape')
    print(('the word cat is in the trie: {}'.format(t.search('cat'))))
    print(('the word cape is in the trie: {}'.format(t.search('cape'))))
    print(('the trie contains a word that starts with cat: {}'.format(t.starts_with('cat'))))
    print(('the trie contains a word that starts with banana: {}'.format(t.starts_with('banana'))))
