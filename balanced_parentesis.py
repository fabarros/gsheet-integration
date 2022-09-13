
class BalanceParentesis:
    def __init__(self, chain):
        self.chain = self.validate_chain(chain)
        self.is_balanced = self.evaluate_balance(chain)

    @staticmethod
    def validate_chain(chain):
        if not isinstance(chain, str):
            raise Exception("Invalid type on input")
        if len(chain) == 0:
            raise Exception("Input is a empty string")
        return chain

    @staticmethod
    def evaluate_balance(chain):
        # chian is odd
        if len(chain) % 2 != 0 or len(chain) == 0:
            return False
        else:
            unclosed_opens = 0
            for literal in chain:
                if literal in "()":
                    if literal == "(":
                        unclosed_opens += 1
                    else:
                        unclosed_opens -= 1
                    if unclosed_opens < 0:
                        return False
                else:
                    raise Exception("Invalid literal in chain")
            if unclosed_opens == 0:
                return True
            else:
                return False
        
patentesis_error1 = BalanceParentesis("")
# patentesis_error2 = BalanceParentesis(None)
# patentesis_error3 = BalanceParentesis(777)
# patentesis_error4 = BalanceParentesis("(())[]")
patentesis_test1 = BalanceParentesis("(((((()))))()())")
patentesis_test2 = BalanceParentesis("((()))(()))")
patentesis_test3 = BalanceParentesis("((((())")

print(patentesis_test1.is_balanced)
print(patentesis_test2.is_balanced)
print(patentesis_test3.is_balanced)