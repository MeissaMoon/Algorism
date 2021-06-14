[Input]  strs = ["eat","tea","tan","ate","nat","bat"]
[Output]  [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdic(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()