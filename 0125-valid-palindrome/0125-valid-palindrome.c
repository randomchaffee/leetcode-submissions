// Aug 11, 2026 08:18
// two pointer approach

bool isPalindrome(char* s) {
    int length = strlen(s);

    // we create two pointers, one starting at the start of the string
    // and one starting at the end of the string
    int left = 0;
    int right = length - 1;

    while (left < right) {
        // we check if either of the current characters are 
        // part of the alphabet. if they aren't, we skip them
        if (!isalnum(s[left])) {
            left++;
        }
        else if (!isalnum(s[right])) {
            right--;
        }
        else {
            // we convert the characters to lowercase
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }
    }

    return true;
}
