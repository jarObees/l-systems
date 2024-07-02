from typing import List, Dict
class L_sysA:
    def __init__(self, name, vars, const, axiom, rules):
        self.name = name
        self.vars: List[str] = vars
        self.consts: List[str] = const
        self.axiom: str = axiom
        self.rules: Dict[str] = rules
        self.string: str = self.axiom
        self.gen: int = 0

    def crawl(self):
        for key, value in self.rules.items():
            if self.string[-1] == key:
                self.string += value
        self.gen += 1

    def reset(self):
        self.string = self.axiom
        self.gen = 0

class L_sysB(L_sysA):
    def crawl(self):
        new_string = []
        for char in self.string:
            if char in self.consts:
                new_string.append(char)
                continue
            else:
                new_string.append(self.rules[char])
        new_string = "".join(new_string)
        self.string = new_string
        self.gen += 1