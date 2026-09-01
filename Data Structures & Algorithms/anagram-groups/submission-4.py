class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            code = [0] * 26
            for c in s:
                code[ord('a') - ord(c)] += 1
            hashmap[tuple(code)].append(s)
        output = []
        for code in hashmap:
            output.append(hashmap[code])
        return output