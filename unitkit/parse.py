from .base import BaseUnit, all_base_units, Custom

special_chars = ["/", "*", "(", ")", "^"]

def parse_units(tokens, in_numerator = True, group = False):
    if isinstance(tokens, BaseUnit):
        return str(tokens), [tokens]
    elif tokens is None or tokens == "":
        return "", []
    elif isinstance(tokens, str):
        # tokens = tokens.replace(" ", "")
        
        # In Python, "**" is used for exponentiation so change "**" to "^"
        tokens = tokens.replace("**", "^")

        for special in special_chars:
            tokens = tokens.replace(special, f" {special} ")
        tokens = tokens.strip().split()

    base_units = []
    last_added = []
    i = 0
    flip = lambda x: x
    while i < len(tokens):
        token = tokens[i]

        if token in special_chars:
            if token == "/":
                flip = lambda x: not x
            elif token == "*":
                flip = lambda x: x
            elif token == "(":
                match, num = parse_units(tokens[i + 1:], flip(in_numerator), group = True)
                base_units.extend(match)
                last_added = match
                i += num
            elif token == ")":
                if not group:
                    raise Exception("Found unmatched ')' token")
                return base_units, i + 1
            elif token == "^":
                exp, num = parse_exp(tokens[i + 1:])
                for base_unit in last_added:
                    base_unit.update_exp(exp)
                i += num               

        elif token != "1":
            match = None
            for u in all_base_units:
                match = BaseUnit.try_match(u, token)
                if match:
                    break
            if not match:
                raise Exception(f"Unable to parse token: {token}")
            
            if not flip(in_numerator):
                match.exp *= -1
            base_units.append(match)
            last_added = [match]

        i += 1

    return "".join(tokens), base_units
    

def parse_exp(tokens: str):
    i = 0
    string = ""
    num_open = 0
    num_close = 0
    while i < len(tokens) and (tokens[i] in special_chars or is_number(tokens[i])):
        if tokens[i] in special_chars:
            if tokens[i] == "(":
                num_open += 1
            elif tokens[i] == ")":
                num_close += 1
                if num_close > num_open:
                    break
                
        string += tokens[i]
        i += 1
    return eval(string), i


def is_number(string: str):
    if string.isdigit():
        return True
    return string.strip().lstrip("-").replace(".", "", 1).isdigit()


def add_base_unit(name, base, dimension, base_modifier):
    global all_base_units
    new_unit = Custom(base, dimension, name, base_modifier)
    all_base_units = [new_unit] + all_base_units