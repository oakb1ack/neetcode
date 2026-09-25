class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for card in hand:
            if card in freq:
                freq[card] += 1
            else: 
                freq[card] = 1

        hand.sort()

        for i in range(len(hand)):
            if freq[hand[i]] <= 0:
                continue
            else: 
                freq[hand[i]] -= 1
                for j in range(hand[i] + 1, hand[i] + groupSize):
                    if j in freq and freq[j] > 0:
                        freq[j] -= 1
                    else:
                        return False

        return True