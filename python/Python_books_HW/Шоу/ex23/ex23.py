'''
import sys
script, encoding, error = sys.argv
bite_languages = open('byte_languages', 'wb')
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    bite_languages.write(raw_bytes)
    bite_languages.write(b'\n')
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    print(raw_bytes, "<==>", cooked_string)
languages = open('languages.txt', encoding='utf-8')
main(languages, encoding, error)
#Byte_languages to utf-8
import sys
script, encoding, error = sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.decode(encoding, errors = errors)
    raw_bytes = cooked_string.encode(encoding, errors = errors)
    print(raw_bytes, "<==>", cooked_string)
languages = open('byte_languages', encoding='utf-8')
main(languages, encoding, error)
'''
import sys
script, encoding, error = sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.decode(encoding, errors = errors)
    raw_bytes = cooked_string.encode(encoding, errors = errors)
    print(raw_bytes, "<==>", cooked_string)
languages = open('byte_languages.txt', 'rb')
main(languages, encoding, error)