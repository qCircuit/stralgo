tests = [
    {"input": {"cards": [13, 11, 9, 8, 5, 2, 1, 0], "query": 5}, "output": 4},
    {"input": {"cards": [13, 11, 9, 8, 5, 2, 1, 0], "query": 0}, "output": 7},
    {"input": {"cards": [10, 7, 2, 1, 0], "query": 10}, "output": 0},
    {"input": {"cards": [0, -7, -15, -22], "query": -15}, "output": 2},
    {"input": {"cards": [8], "query": 8}, "output": 0},
    {"input": {"cards": [23, 19, 11, 1], "query": 8}, "output": -1},
    {"input": {"cards": [], "query": 1}, "output": -1},
    {"input": {"cards": [10, 7, 2, 2, 1, 0], "query": 2}, "output": 2},
    {"input": {"cards": [9, 9, 5, 5, 5, 5, 5, 5, 2, 2, 2, 1, 1, 1], "query": 5}, "output": 2},
]

def locate_card(cards, query): # linear
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

def locate_card(cards, query): # binary search
    le, ri = 0, len(cards) - 1

    while le <= ri:
        mi = (le + ri) // 2
        if False:
            print(le, ri, mi, cards[mi])
        if cards[mi] == query:
            return mi
        if cards[mi] < query:
            ri = mi - 1
        elif cards[mi] > query:
            le = mi + 1

    return -1

def test_location(cards, query, mi):
    if cards[mi] == query:
        if all([(mi-1 >= 0), (cards[mi-1] == query)]):
            return "left"
        else:
            return "found"
    elif cards[mi] < query:
        return "left"
    else:
        return "right"

def locate_card(cards, query): # binary search conditioned
    le, ri = 0, len(cards) - 1

    while le <= ri:
        mi = (le + ri) // 2
        result = test_location(cards, query, mi)
        if result == "found":
            return mi
        if result == "left":
            ri = mi - 1
        elif result == "right":
            le = mi + 1

    return -1

if __name__=="__main__":
    for n, test in enumerate(tests):
        print(locate_card(**test["input"]))
        try: 
            assert locate_card(**test["input"]) == test["output"], "incorrect output"
            print(f"test {n+1} passed")
        except Exception as e:
            print(f"test {n+1} failed, error: {e}")
            continue
