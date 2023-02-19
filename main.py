# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            top_bracket = opening_brackets_stack.pop()
            if not are_matching(top_bracket.char, next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return None

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch is None:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()

