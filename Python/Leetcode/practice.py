def valid_parantheses(s):

    pairs = {"{": "}",
            "(": ")",
            "[": "]"}

    stack = list()

    for c in s:
        if c in pairs:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                if c != pairs[stack.pop()]:
                    return False

        return not stack



