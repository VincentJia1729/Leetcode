class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range (len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for key, value in count.items():
            frequency[value].append(key)

        result = []

        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result