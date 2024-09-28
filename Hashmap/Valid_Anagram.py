class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1, map2 = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1

        return dict(sorted(map1.items(), key=lambda item: item[1])) == dict(sorted(map2.items(), key=lambda item: item[1]))
