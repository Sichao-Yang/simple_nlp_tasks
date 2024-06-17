class ShiftReduceParser:
    def __init__(self, grammar):
        self._parse_g(grammar)
        self.stack = []
        self.input = []

    def _parse_g(self, grammar_list):
        self.grammar = []
        for p in grammar_list:
            head, body = p.split("->")
            self.grammar.append((head.strip(), body.strip().split()))

    def _get_production_str(self, head, body):
        return f"{head} -> {' '.join(body)}"

    def parse(self, tokens):
        self.input = tokens + ["$"]  # End of input marker
        self.stack = ["$"]

        while True:
            print("Stack:", self.stack)
            print("Input:", self.input)
            action = self.get_action()
            if action == "SHIFT":
                self.shift()
            elif action.startswith("REDUCE"):
                self.reduce(action)
            elif action == "ACCEPT":
                print("Input accepted")
                return True
            else:
                print("Error in parsing")
                return False

    def get_action(self):
        for head, body in self.grammar:
            if self.stack[-len(body) :] == body:
                return f"REDUCE {self._get_production_str(head,body)}"

        if self.input[0] != "$":
            return "SHIFT"
        elif self.stack == ["$", "E"]:
            return "ACCEPT"
        else:
            return "ERROR"

    def shift(self):
        token = self.input.pop(0)
        self.stack.append(token)

    def reduce(self, action):
        _, production = action.split(" ", 1)
        head, body = production.split("->")
        head = head.strip()
        body = body.strip().split()

        for _ in body:
            self.stack.pop()

        self.stack.append(head)


if __name__ == "__main__":
    grammar = ["E -> E + E", "E -> E * E", "E -> ( E )", "E -> id"]

    parser = ShiftReduceParser(grammar)

    tokens = "id + id * id".split()

    if parser.parse(tokens):
        print("Parsing successful")
    else:
        print("Parsing failed")
    ########################################################
    grammar = [
        "E -> 2 E 2",
        "E -> 3 E 3",
        "E -> 4",
    ]

    parser = ShiftReduceParser(grammar)

    tokens = "3 2 4 2 3".split()

    if parser.parse(tokens):
        print("Parsing successful")
    else:
        print("Parsing failed")
    ########################################################
    grammar = [
        "S -> ( E )",
        "S -> a",
        "E -> E , S",
        "E -> S",
    ]

    parser = ShiftReduceParser(grammar)

    tokens = "( a , ( a , a ) )".split()

    if parser.parse(tokens):
        print("Parsing successful")
    else:
        print("Parsing failed")
