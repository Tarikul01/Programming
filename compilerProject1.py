# Lexical Analysis
import re

# Regular expressions for C tokens
token_patterns = [
    (r'\bint\b', 'INT_KEYWORD'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),
    (r'\d+', 'INTEGER'),
    (r'[=;\+\-*/]', 'OPERATOR'),
    (r'\s+', None),  # Ignore whitespace
]


def tokenize(code):
    tokens = []
    code = code.strip()

    while code:
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                if token_type:
                    tokens.append((token_type, match.group()))
                code = code[match.end():]
                break
        else:
            raise ValueError("Invalid character: " + code[0])

    return tokens


# Syntax Analysis
def parse(tokens):
    code = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == 'INT_KEYWORD':
            i += 1
            if tokens[i][0] != 'IDENTIFIER':
                raise SyntaxError("Expected identifier after 'int'")
            var_name = tokens[i][1]
            i += 1
            if tokens[i][0] == 'OPERATOR' and tokens[i][1] == '=':
                i += 1
                if tokens[i][0] != 'INTEGER':
                    raise SyntaxError("Expected integer value after '='")
                var_value = tokens[i][1]
                code.append(f'{var_name} = {var_value}')
                i += 1
            code.append(f'print({var_name})')
            if tokens[i][0] == 'OPERATOR' and tokens[i][1] == ';':
                i += 1
            else:
                raise SyntaxError("Expected ';' at the end of the statement")
        else:
            raise SyntaxError("Invalid statement")
    return '\n'.join(code)


# Main function
def c_to_python(c_code):
    tokens = tokenize(c_code)
    python_code = parse(tokens)
    return python_code


if __name__ == "__main__":
    c_code = """
    int a = 5;
    int b = 10;
    int c = a + b;
    """
    python_code = c_to_python(c_code)
    print(python_code)
