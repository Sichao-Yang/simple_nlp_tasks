class RecursiveDescentParser:
    """
    E -> T E'
    E' -> + T E' | ε
    T -> F T'
    T' -> * F T' | ε
    F -> ( E ) | id
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.position = -1
        self.next_token()

    def next_token(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def parse(self):
        if self.E():
            if self.current_token is None:
                return True
            else:
                return False
        return False

    def E(self):
        if self.T():
            if self.E_prime():
                return True
        return False

    def E_prime(self):
        if self.current_token == '+':
            self.next_token()
            if self.T():
                if self.E_prime():
                    return True
            return False
        return True  # ε production

    def T(self):
        if self.F():
            if self.T_prime():
                return True
        return False

    def T_prime(self):
        if self.current_token == '*':
            self.next_token()
            if self.F():
                if self.T_prime():
                    return True
            return False
        return True  # ε production

    def F(self):
        if self.current_token == 'id':
            self.next_token()
            return True
        elif self.current_token == '(':
            self.next_token()
            if self.E():
                if self.current_token == ')':
                    self.next_token()
                    return True
            return False
        return False

if __name__ == "__main__":
    tokens = "id + id * id".split()
    
    parser = RecursiveDescentParser(tokens)
    
    if parser.parse():
        print("Parsing successful")
    else:
        print("Parsing failed")
