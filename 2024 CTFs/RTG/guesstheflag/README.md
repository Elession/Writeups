## Guess The Flag

Connect to the TCP Port to guess the flag.

The service interacts and does the following conditional checks in order:
1. Checks for correct length of flag
2. Compares the content of the flag based on the index (basically checks if each character is correct, before moving on to the next)

If the character is wrong, it will print `too high` or `too low`, based on the ascii character table.

I already figured the length of the flag is 29 characters long by manually testing.

So I just crafted the script to do the following:
1. print the flag format + placement holder with length of 29 characters
2. brute force each index until i get a output of `correct` for the following index
