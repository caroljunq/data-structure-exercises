# https://www.hackerrank.com/challenges/contacts/problem
# https://tutorialedge.net/compsci/data-structures/getting-started-with-tries-in-python/
class Trie():
    def __init__(self):
        self._end = '*'
        self.trie = dict()

    def find_word(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False

        if self._end in sub_trie:
            return True
        else:
            return False

    def add_word(self, word):
        if self.find_word(word):
            print("Word already inserted!")
            return self.trie

        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})

        temp_trie[self._end] = self._end
        return temp_trie

    def find_prefix(self, trie, prefix):
        n_words = 0
        sub_trie = trie

        for letter in prefix:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return 0
        for key in sub_trie.keys():
            if key == self._end:
                n_words += 1
            else:
                n_words += self.find_prefix(sub_trie, key)
        return n_words



my_trie = Trie()
my_trie.add_word('hack')
my_trie.add_word('hackerrank')
my_trie.add_word('hackathon')
print(my_trie.find_prefix(my_trie.trie, 'hack'))
print(my_trie.find_prefix(my_trie.trie,'he'))

print(my_trie.find_prefix(my_trie.trie,'hak'))
