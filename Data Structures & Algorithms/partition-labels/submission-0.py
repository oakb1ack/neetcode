class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}

        for i in range(len(s)):
            store[s[i]] = i
        
        output = []
        size = 0
        end = store[s[0]]

        for i in range(len(s)):
            end = max(end, store[s[i]], end)
            size += 1
            if i == end:
                output.append(size)
                size = 0

        return output