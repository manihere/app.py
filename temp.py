
def count_anagrams(s):
    words = s.split()  # Split the string into words on the basis of whitespaces
    anagram_count = 0  # Initialize the count of anagrams
    # Iterate through each word
    for i in range(len(words)):
        # Skip words consisting of repeated characters only
        if len(set(words[i])) == 1: #set() function returns only unique values in array
            continue
        
        for j in range(i + 1, len(words)):
            # Check if the words are anagrams and not the same word
            if (sorted(words[i]) == sorted(words[j])) and (words[i] != words[j]):
                anagram_count += 1
                # if len(words[i]) == 1 and len(words[j]) == 1:
                #     anagram_count += 1
                # # elif words[i] != words[j]:
                #     anagram_count += 1
    return anagram_count
# Test cases
print(count_anagrams("aa aa odg dog gdo"))  # Output: 2
print(count_anagrams("a c b c run urn urn"))  # Output: 1