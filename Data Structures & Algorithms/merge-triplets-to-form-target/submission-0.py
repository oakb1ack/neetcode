class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = False, False, False 

        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                t1 = True
            if triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2]:
                t2 = True
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2]:
                t3 = True

        return t1 == t2 == t3 == True