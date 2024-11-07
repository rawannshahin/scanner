import re


def scanner(code):
    # التعبيرات النظامية
    keyword_pattern = r'\b(int|float|if|else|return|while|for)\b'
    identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
    operator_pattern = r'[+\-*/=<>!&|]'
    numeric_pattern = r'\b\d+\b'
    char_constant_pattern = r"'[^']'"
    special_char_pattern = r'[;(){}[\],.]'
    comment_pattern = r'//.*|/\*.*?\*/'
    whitespace_pattern = r'\s+'
    newline_pattern = r'\n'

    # التحليل وعرض النتائج
    print("Keywords:")
    for match in re.finditer(keyword_pattern, code):
        print(match.group())

    print("\nIdentifiers:")
    for match in re.finditer(identifier_pattern, code):
        print(match.group())

    print("\nOperators:")
    for match in re.finditer(operator_pattern, code):
        print(match.group())

    print("\nNumeric Constants:")
    for match in re.finditer(numeric_pattern, code):
        print(match.group())

    print("\nCharacter Constants:")
    for match in re.finditer(char_constant_pattern, code):
        print(match.group())

    print("\nSpecial Characters:")
    for match in re.finditer(special_char_pattern, code):
        print(match.group())

    print("\nComments:")
    for match in re.finditer(comment_pattern, code):
        print(match.group())

    print("\nWhite Space:")
    for match in re.finditer(whitespace_pattern, code):
        print(match.group())

    print("\nNewlines:")
    for match in re.finditer(newline_pattern, code):
        print(match.group())


# نص الاختبار
code = """int x = 5; // this is a comment
float y = 3.14;
if (x > y) { 
    cout << 'Hello'; 
}
"""

scanner(code)
