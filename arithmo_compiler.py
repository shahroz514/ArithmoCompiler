import re

class ArithmoCompiler:
    def __init__(self):
        self.variables = {}

    def tokenize(self, expression):
        token_specification = [
            ('NUMBER', r'\d+'),
            ('IDENT', r'[a-zA-Z_]\w*'),
            ('ASSIGN', r'='),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MUL', r'\*'),
            ('DIV', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        tokens = []
        for match in re.finditer(token_regex, expression):
            token_type = match.lastgroup
            token_value = match.group()
            if token_type == 'NUMBER':
                tokens.append(('NUMBER', int(token_value)))
            elif token_type == 'IDENT':
                tokens.append(('IDENT', token_value))
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {token_value}')
            else:
                tokens.append((token_type, token_value))
        return tokens

    def parse_and_evaluate(self, tokens):
        def parse_expression(index):
            left_value, index = parse_term(index)
            while index < len(tokens) and tokens[index][0] in ('PLUS', 'MINUS'):
                op = tokens[index][0]
                index += 1
                right_value, index = parse_term(index)
                if op == 'PLUS':
                    left_value += right_value
                elif op == 'MINUS':
                    left_value -= right_value
            return left_value, index

        def parse_term(index):
            left_value, index = parse_factor(index)
            while index < len(tokens) and tokens[index][0] in ('MUL', 'DIV'):
                op = tokens[index][0]
                index += 1
                right_value, index = parse_factor(index)
                if op == 'MUL':
                    left_value *= right_value
                elif op == 'DIV':
                    left_value /= right_value
            return left_value, index

        def parse_factor(index):
            token_type, token_value = tokens[index]
            if token_type == 'NUMBER':
                return token_value, index + 1
            elif token_type == 'IDENT':
                if token_value in self.variables:
                    return self.variables[token_value], index + 1
                else:
                    raise NameError(f"Variable '{token_value}' is not defined")
            elif token_type == 'LPAREN':
                index += 1
                value, index = parse_expression(index)
                if tokens[index][0] != 'RPAREN':
                    raise SyntaxError('Expected closing parenthesis')
                return value, index + 1
            else:
                raise SyntaxError(f'Unexpected token: {token_type}')

        result, index = parse_expression(0)
        if index != len(tokens):
            raise SyntaxError('Unexpected token at the end')
        return result

    def process_input(self, input_str):
        if '=' in input_str:  # Assignment operation
            var_name, expr = map(str.strip, input_str.split('=', 1))
            if not re.match(r'^[a-zA-Z_]\w*$', var_name):
                raise SyntaxError(f"Invalid variable name: '{var_name}'")
            tokens = self.tokenize(expr)
            self.variables[var_name] = self.parse_and_evaluate(tokens)
            return f"{var_name} = {self.variables[var_name]}"
        else:  # Evaluation operation
            tokens = self.tokenize(input_str)
            return self.parse_and_evaluate(tokens)
