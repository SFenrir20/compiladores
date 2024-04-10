
class Token:
    TK_IDENTIFIER = 0
    TK_NUMBER = 1
    TK_OPERATOR = 2
    TK_PUNCTUATION = 3
    TK_ASSIGN = 4


    def __init__(self, type = None, text=""):
        self.type = type
        self.text = text
        self.line = None
        self.column = None

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text

    def get_line(self):
        return self.line

    def set_line(self, line):
        self.line = line

    def get_column(self):
        return self.column
    
    def set_column(self, column):
        self.column = column