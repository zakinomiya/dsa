

# return index of first non-repeating character in a string.
# if there is no such character, return -1
def firstUniqChar(s: str) -> int:
    uniqChar = {}
    
    for i, c in enumerate(s):
        if c not in uniqChar:
            uniqChar[c] = i
        else:
            uniqChar[c] = len(s)
    
    m = min(uniqChar.values())
    return m if m != len(s) else -1


# erase dots and plus sign from localname string
def eraseDotsAndPlus(localname: str) -> str:
    l = localname
    if "+" in l:
        l = l[:l.index("+")] 

    return l.replace(".", "")

# return the number of distinctive emails.
# localname is compared after dots and plus erased
def numUniqueEmails(emails: list[str]) -> int:
    uniqueEmails = {}
    i = 0
    for e in emails:
        (localname, _, domainname) = e.partition("@")
        l = eraseDotsAndPlus(localname)

        if domainname not in uniqueEmails:
            uniqueEmails[domainname] = [l]
            i+= 1
        else:
            if l not in uniqueEmails[domainname]:
                uniqueEmails[domainname].append(l)
                i+= 1

    return i
        

# return intersection of two arrays
def intersectionOfArrays(n1: list[int], n2: list[int]) -> list:
    intersection = []
    for n in n1: 
        if n in n2 and n not in intersection:
            intersection.append(n)

    return intersection



if __name__ == "__main__":
    r = intersectionOfArrays([4,9,5], [9,4,9,8,4])
    assert(r == [4,9] or r == [9,4])

    r = numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    assert(r == 2)

    r = firstUniqChar("loveleetcode")
    assert(r == 2)
