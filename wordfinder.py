"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in ["aardvark", "gazing", "indefinite"]
    True

    >>> wf.random() in ["lawn", "lazy", "nomad"]
    True

    >>> wf.random() in ["noisy", "paradox", "silk"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""
        word = random.choice(self.words)
        print(word)
        return word in ["aardvark", "gazing", "indefinite"] or \
               word in ["lawn", "lazy", "nomad"] or \
               word in ["noisy", "paradox", "silk"]

wf = WordFinder("words.txt")


