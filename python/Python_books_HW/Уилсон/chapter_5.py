#chpater_4
class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()
    
    def match(self, text, start):
        result = self._match(text, start=0)
        print(text[: result])
        return result == len(text)
    
    def __eq__(self, other):
        return (other is not None and self.__class__ == other.__class__
                and self.rest == other.rest)
    
class Null(Match):
    def __init__(self):
        self.rest = None
    
    def _match(self, text, start):
        return start
    
class Lit(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars
    
    def _match(self, text, start):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
    
    def __eq__(self, other):
        return super().__eq__(other) and (self.chars == other.chars)

class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)
    
    def _match(self, text, start):
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None

class Either(Match):
    def __init__(self, left, right, rest=None):
        super().__init__(rest)
        self.left = left
        self.right = right
    
    def _match(self, text, start):
        for pat in [self.left, self.right]:
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
#токенизатор
import string

CHARS = set(string.ascii_letters + string.digits)

class Tokenizer:
    def __init__(self):
        self._setup()
    def _setup(self):
        self.result = []
        self.current = ''

    def tok(self, text):
        self._setup()
        for ch in text:
            if ch == '*':
                self._add('Any')
            elif ch == '{':
                self._add('EitherStart')
            elif ch == ',':
                self._add(None)
            elif ch == '}':
                self._add('EitherEnd')
            elif ch in CHARS:
                self.current += ch
            else:
                raise NotImplementedError(f'what is {ch}')
        self._add(None)
        return self.result

    def _add(self, thing):
        if len(self.current) > 0:
            self.result.append(['Lit', self.current])
            self.current = ''
        if thing is not None:
            self.result.append([thing])

def test_tok_empty_string():
    assert Tokenizer().tok('') == []

def test_tok_any_either():
    assert Tokenizer().tok('*{abc,def}') == [
        ['Any'],
        ['EitherStart'],
        ['Lit', 'abc'],
        ['Lit', 'def'],
        ['EitherEnd'],
    ]
test_tok_empty_string()
test_tok_any_either()

#Парсер
class Parser:
    def _parse(self, tokens):
        if not tokens:
            return Null()
        front, back = tokens[0], tokens[1:]
        if front[0] == 'Any': handler = self._parse_Any
        elif front[0] == 'EitherStart': handler = self._parse_EitherStart
        elif front[0] == 'Lit': handler = self._parse_Lit
        elif (front[0] == '/' or front[0] == '\\'): handler = self._parseSpecial_1
        else:
            assert False, f'Unknown token type {front}'
        return handler(front[1:], back)

    def _parse_Any(self, rest, back):
        return Any(self._parse(back))

    def _parse_Lit(self, rest, back):
        return Lit(rest[0], self._parse(back))

    def _parseEitherStart(self, rest, back):
        if (
            len(back) < 3
            or (back[0][0] != 'Lit')
            or (back[1][0] != 'Lit')
            or (back[2][0] != 'EitherEnd')
        ):
            raise ValueError('badly formatted Either')
        left = Lit(back[0][1])
        right = Lit(back[1][1])
        return Either([left, right], self._parse(back[3:]))
    #HW
    #Task-1
    def _parseSpecial_1(self, rest, back):
        print(rest, back)
        return Lit(rest[1], self._parse(back))

print(Parser().parse())