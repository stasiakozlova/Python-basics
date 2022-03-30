from nltk.tokenize import word_tokenize
import os

class FileReader():
    
    def __init__(self, file):
        self.file = file

    def read(self):
        try:
            with open(self.file) as f:
                return f.read()
        except FileNotFoundError:
            return ''

    def write(self, data):
        self.write('data')

    def count(self):
        with open(self.file) as f:
            line_count = 0
            words = []
            for line in f:
                line_count += 1
                for word in word_tokenize(line):
                    words.append(word)
            word_count = len(words)
            return line_count, word_count

    def __add__(self, other):
        new_file = self.read() + other.read()
        with open('new_file.txt', 'w') as file:
            file.write(new_file)
        new_file = FileReader(new_file)
        return new_file

    def __repr__(self):
        p = os.path.abspath(self.file)
        return p
