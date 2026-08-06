// Aug 06, 2026 15:45
// trying this problem again, but in C
// why? I don't want to get cooked for this semester's C 
// lab courses using C as the langauge medium
// hashmap frequency approach (via an array with the index representing the letter)

char findTheDifference(char* s, char* t) {
    // we use a frequency array of size 26 for the lowercase letters as a hashmap
    int counts[26] = {0};

    // we count the frequencies of characters in s
    for (int i = 0; s[i] != '\0'; i++) {
        counts[s[i] - 'a']++;
    }

    // after that, we decrement the frequencies
    // for each chracter in t
    for (int i = 0; t[i] != '\0'; i++) {
        counts[t[i] - 'a']--;
    }

    // then we find the character with a non-zero count
    for (int i = 0; i < 26; i++) {
        if (counts[i] != 0) {
            // typecast the ASCII value back to a char
            // since that is what we need to return
            return (char)(i + 'a');
        }
    }

    // if the loop finishes without returning a char
    // we return null (not NULL, since that represents a null pointer)
    return '\0';
}