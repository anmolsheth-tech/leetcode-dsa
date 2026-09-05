#String is immuttable in Python, You'll need to convert it to a list first
class Solution:
    def reverseVowels(self, s: str) -> str:
        newList = list(s)
        left = 0
        right = len(newList) - 1
        vowels = ["a", "e", "i", "o", "u",
                  "A", "E", "I", "O", "U"]
        while left < right:
            if newList[left] not in vowels:
                left += 1
            if newList[right] not in vowels:
                right -= 1
            if newList[left] in vowels and newList[right] in vowels:
                newList[left], newList[right] = newList[right], newList[left]
                left += 1
                right -= 1
        
        return "".join(newList) #convert back

