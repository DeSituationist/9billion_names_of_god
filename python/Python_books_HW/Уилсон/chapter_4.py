# Регулярные выражения
class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars
        self.rest = rest

    def match(self, text, start=0):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return False
        if self.rest:
            return self.rest.match(text, end)
        return end == len(text)
    
def  test_literal_match_entire_string():
    # /abc/ matches 'abc'
    assert Lit('abc').match('abc')

def test_literal_substring_alone_no_match():
    # /ab/ doesn't match 'abc'
    assert not Lit('ab').match('abc')

def test_literal_superstring_no_match():
    # /abc/ doesn't match 'ab'
    assert not Lit('abc').match('ab')

def test_literal_followed_by_literal_match():
    # /a/ + /b/ matches 'ab'
    assert Lit('a', Lit('b')).match('ab')

def test_literal_followed_by_literal_no_match():
    # /a/ + /b/ doesn't match 'ac'
    assert not Lit('a', Lit('b')).match('ac')

class Any:
    def __init__(self, rest=None):
        self.rest = rest
    
    def match(self, text, start=0):
        if self.rest is None:
            return True
        for i in range(start, len(text)):
            print(text[i])
            if self.rest.match(text, i):
                return True
        return False

def test_any_matches_empty():
    # /*/ matches ''
    assert Any().match('')

def test_any_matches_entire_string():
    # /*/ matches 'abc'
    assert Any().match('abc')

def test_any_matches_as_prefix():
    # /*def/ matches 'abcdef'
    assert Any(Lit('def')).match('abcdef')

def test_any_matches_as_suffix():
    # /abc*/ matches 'abcdef'
    assert Lit('abc', Any()).match('abcdef')

def test_any_matches_interior():
    # /a*c/ matches 'abc'
    assert Lit('a', Any(Lit('c'))).match('abc')

class Either:
    def __init__(self, left, right, rest=None):
        self.left = left
        self.right = right
        self.rest = rest
    
    def match(self, text, start=0):
        return self.left.match(text, start) or self.right.match(text, start)

def test_either_two_literals_first():
    # /{a, b}/ matches 'a'
    assert Either(Lit('a'), Lit('b')).match('a')

def test_either_two_literals_not_both():
    # /{a, b}/ doesn't match 'ab'
    assert not Either(Lit('a'), Lit('b')).match('ab')

#def test_either_followed_by_literal_match():   
    # /{a, b}c/ matches 'ac'
#    assert Either(Lit('a'), Lit('b'), Lit('c')).match('ac') 

#def test_either_followed_by_literal_no_match():
    # /{a, b}c/ doesn't match 'ax'
#    assert not Either(Lit('a'), Lit('b'), Lit('c')).match('ax')


# Рефакторинг через родительский класс match
class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()
    
    def match(self, text, start):
        result = self._match(text, start=0)
        print(text[: result])
        return result == len(text)
    
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
    
# HW   
class Plus(Match):
    def __init__(self, value, rest=None):
        super().__init__(rest)
        self.value = value

    def _match(self, text, start):
        if start >= len(text) or text[start] != self.value:
            return None
        end = start + 1
        while end < len(text) and text[end] == self.value:
            end += 1
        return end
        
class Charset(Match):
    def __init__(self, symbols, rest=None):
        super().__init__(rest)
        self.symbols = symbols
              
    def _match(self, text, start):
        if start >= len(text) or text[start] not in self.symbols:
            return None
        return start + 1

class Not(Match):
    def __init__(self, pattern, rest=None):
        super().__init__(rest)
        self.pattern = pattern
    
    def _match(self, text, start):
        if self.pattern._match(text, start) is not None:
            return None
        return self.rest._match(text, start)

class More_Either(Match):
    def __init__(self, *patterns, rest=None):
        super().__init__(rest)
        self.patterns = patterns
    
    def _match(self, text, start):
        for pat in self.patterns:
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None

text = "ac"
plus = Plus("a", Null())
print(plus._match(text, 0))

text = "aaacc"
chrs = Charset('ae', Null())
print(chrs.match(text, 0))

pattern = Not(Lit("abc"), rest=Any())
print(pattern._match('ab', 0))

pattern = More_Either(Lit("foo"), Lit("barrr"), Lit("baz"), rest=Any())
print(pattern._match('baz', 0))