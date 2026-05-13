class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for word in strs:
            sortedWord = " ".join(sorted(word))
            groups[sortedWord].append(word)
        return list(groups.values())