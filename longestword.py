# String Challenge
# Have the function StringChallenge (sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123
# 567"
# Py
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Once your function is working, take the final output string and combine it with your ChallengeToken, both in reverse order and separated by a colon.
# Your ChallengeToken: j894gbvad3
# ?
# Examples
# Input: "fun&!! time"
# Output: time
# Final Output: emit: 3davbg498j
# Input: "I love dogs"
# Output: love
# Final Output: evol: 3davbg498j

#==============Code1 without RE library============================================
 
# def remove_punctuation(s):
#     """
#     Helper function to remove punctuation from a string.
#     """
#     punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     s_without_punct = ""
#     for char in s:
#         if char not in punctuation:
#             s_without_punct += char
#     return s_without_punct

# def StringChallenge(sen):
#     # Remove punctuation and split the string into words
#     sen = remove_punctuation(sen)
#     words = sen.split()
    
#     # Find the longest word
#     longest_word = max(words, key=len)
    
#     return longest_word

# # Test cases
# print(StringChallenge("fun&!! time"))
# print(StringChallenge("I love dogs"))
#===============================================

# ======================Code2=======================
import re

def StringChallenge(sen):
    # Remove punctuation and split the string into words
    words = re.findall(r'\w+', sen)
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    return longest_word

# Test cases
print(StringChallenge("fun&!! time"))
print(StringChallenge("I love dogs"))

challenge_token = "j894gbvad3"
output = StringChallenge("fun&!! time")
final_output = f"{output[::-1]}:{challenge_token[::-1]}"
print("Final Output:", final_output)
