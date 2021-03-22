class CheckParentheses(object):

    valid_pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def check_validity(self, s):

        stack = list()

        # If the length of string is not an even number then there is no way the pairs will match
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in CheckParentheses.valid_pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if c != CheckParentheses.valid_pairs[stack.pop()]:
                        return False

        return not stack


if __name__ == "__main__":
    check_parantheses = CheckParentheses()
    print(check_parantheses.check_validity("([)]"))
