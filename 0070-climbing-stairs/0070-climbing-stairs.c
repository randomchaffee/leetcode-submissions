// Aug 06, 2026 19:09
// this feels more like a combinatorics than a programming problem
// used dynamic programming 
// same solution I used in python, just in C (for practice)


int climbStairs(int n) {
    // these two will represent the number of ways to reach the
    // current step from the two previous steps
    int one = 1;
    int two = 1;

    // basically, we iteratively build up the number of ways
    // from the base steps up to the n-th step
    for (int i = 0; i < n-1; i++) {
        int temp = one;
        one += two;
        two = temp;
    }

    return one;
}