from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """ Special word finder that skips blank spaces and comments.
    
    >>> swf = SpecialWordFinder('specialwords.txt')
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    """
    def __init__(self, path):
        """Get information from dictionary while using the orginal word finder code."""
        super().__init__(path)

    def parse(self, dict_file):
        """Returns words, but skips the blank spaces and comments"""
        
        return [word.strip() for word in dict_file
                if word.strip() and not word.startswith("#")]