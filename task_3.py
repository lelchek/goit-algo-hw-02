opened_set = ["(", "{", "["]
closed_set = [")", "}", "]"]


def is_symmetric(string: str):
    stack = []

    for s in string:
        if s in opened_set:
            stack.append(s)
        elif s in closed_set:
            if not stack:
                return False

            opened = stack.pop()
            opened_index = opened_set.index(opened)
            closed_index = closed_set.index(s)

            if opened_index != closed_index:
                return False
        else:
            continue

    return len(stack) == 0
