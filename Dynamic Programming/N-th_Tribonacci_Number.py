class Solution:
    def tribonacci(self, n: int) -> int:
        trib = []
        trib.append(0)
        trib.append(1)
        trib.append(1)

        for i in range(3, n+1):
            trib.append(trib[i-3] + trib[i-2] + trib[i-1])

        return trib[n]