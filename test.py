from bauhaus import Encoding, proposition, constraint

e = Encoding()

@proposition(e)
class A(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"A({self.val})"

if __name__ == "__main__":
    objects = [A(val) for val in range(1,4)]
    constraint.add_exactly_one(e, objects[0], objects[1])
    theory = e.compile()
    print(f"Theory: {theory}\n")
    print(theory.solve())

