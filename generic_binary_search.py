# generic binary search

cards = [18, 10, 9, 8, 7, 6, 4, 2]
querry = 10
def condition():
    pass
def binary_search():
    pass

# the condition function
def locate_card(cards, querry):
    def condition(mid):
        if cards[mid] == querry:
            if mid > 0 and cards[mid -1] == querry:
                return "left"
            else:
                return "found"
        elif cards[mid] < querry:
            return "left"
        else:
            return "right"
    return binary_search(0, len(cards) - 1, condition)

def binary_search(lo, hi, condition):
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

print(locate_card(cards, querry))