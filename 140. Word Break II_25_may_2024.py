"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

## first think and easy way to generate more words with one word just adding spacces

string = ""
for i in s:
    string += i

print(string)

