def lengthOfLastWord(self, s: str) -> int:
    return len(s.rstrip(' ').split(' ')[-1])


s = "here is a string         "
srstripped = s.rstrip(' ')
srstrippedSplit = srstripped.split(' ')[-1]
quick = s.rstrip(' ').split(' ')[-1]


txt = "welcome to the jungle"

x = txt.split()

print(x)

