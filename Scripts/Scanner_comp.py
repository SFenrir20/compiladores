import codecs

class Scanner:
    def __init__(self,filename):
        self.line = 1
        self.column = 0
        try:
            with codecs.open(filename,'r', encoding='utf-8') as file:
                txt_content = file.read()
            self.content = list(txt_content)
            self.pos = 0
        except Exception as ex:
            print(ex)


    def next_token(self):
        pass

    def is_digt(self, c):
        return '0' <= c <= '9'
    
    def is_char(self, c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'
    

    def is_operator(self, c):
        return c in ['>','<','=','!','+','-','*','/']
    
    def is_space(self, c):
        return c in [' ','\t','\n','\r']
    
    def next_char(self):
        if self.is_eof():
            return '$'
        self.pos = self.pos + 1
        return self.content[self.pos - 1]
    
    def is_eof(self):  
        return self.pos >= len(self.content)
    

    def back(self):
        self.pos -= 1
        self.column -=1
    
    def is_eof_char(self, c):
        return c == "\8"