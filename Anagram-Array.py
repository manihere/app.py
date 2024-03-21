# Array Challenge
# Have the function ArrayChallenge (str) take the str parameter and determine how many anagrams exist in the string.
#  An anagram is a new word that is produced from rearranging the characters in a different word,
# for example: cars and arcs are anagrams. Your program should determine how many anagrams exist in a given string
#and return the total number. For example: if str is "aa aa odg dog gdo" then your program should return 2 because 
#"dog" and "gdo" are anagrams of "odg". The word "aa" occurs twice in the string but it isn't an anagram because it is the same
# word just repeated. The string will contain only spaces and lowercase letters, no punctuation, numbers, or uppercase letters.
# Examples
# Input: "aa aa odg dog gdo"
# Output: 2
# Input: "a c b c run urn urn"
# Output: 1

def count_anagrams(s):
    words = s.split()  # Split the string into words
    anagram_count = 0  # Initialize the count of anagrams

    # Iterate through each word
    for i in range(len(words)):
        # Skip words consisting of repeated characters only
        if len(set(words[i])) == 1:
            continue
        
        for j in range(i + 1, len(words)):
            # Check if the words are anagrams and not the same word
            if sorted(words[i]) == sorted(words[j]):
                if len(words[i]) == 1 and len(words[j]) == 1:
                    anagram_count += 1
                elif words[i] != words[j]:
                    anagram_count += 1

    return anagram_count

# Test cases
print(count_anagrams("aa aa odg dog gdo"))  # Output: 2
print(count_anagrams("a c b c run urn urn"))  # Output: 1
