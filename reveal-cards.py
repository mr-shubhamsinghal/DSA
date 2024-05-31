
from collections import deque
from typing import List


def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    
    n = len(deck)
    deck.sort()
    ans = [0] * n
    index_queue = deque(range(n))
    i = 0
    while index_queue:
        x = index_queue.popleft()
        ans[x] = deck[i]
        # print(in)
        if index_queue:
            y = index_queue.popleft()
            index_queue.append(y)
        i += 1
    
    return ans

if __name__ == "__main__":
    arr = [17,13,11,2,3,5,7]
    print(deckRevealedIncreasing(arr))