# lexer.py

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def error(self):
        raise Exception('Ungültiges Zeichen')

    def advance(self):
        """Bewege die Position nach rechts und aktualisiere das aktuelle Zeichen."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Ende des Textes erreicht
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Überspringe Whitespace."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        """Gibt den nächsten Token zurück."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == ';':
                self.advance()
                return Token('SEMICOLON', ';')

            if self.current_char.isdigit():
                value = self.integer()
                return Token('INTEGER', value)

            if self.current_char == 'r':
                self.advance()
                if self.current_char == 'e':
                    self.advance()
                    if self.current_char == 't':
                        self.advance()
                        if self.current_char == 'u':
                            self.advance()
                            if self.current_char == 'r':
                                self.advance()
                                if self.current_char == 'n':
                                    self.advance()
                                    return Token('RETURN', 'return')
                self.error()

            self.error()

        return Token('EOF', None)

    def integer(self):
        """Liest eine ganze Zahl aus dem Text."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
