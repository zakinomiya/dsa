class GroupAnagrams:
    """
    variables:
        n = the length of the list
        k = the length of the strings
    assumption:
        k is the same for all the str in the list
    time complexity:
        O(n * klogk)
    """
    def groupAnagrams(self, strs: list[str]):
        h = {}
        # n loops
        for s in strs:
            # sort: O(k ln k)
            ss = "".join(sorted(s))
            if ss not in h:
                # search O(1)
                h[ss] = [s]
            else:
                h[ss].append(s)
            
        return list(h.values())

if __name__ == "__main__":
    g = GroupAnagrams()
    print(g.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(g.groupAnagrams([""]))
    print(g.groupAnagrams(["a"]))
