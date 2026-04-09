# Create a single lambda expression that takes a list of strings and
# returns the longest string whose length is a prime number, using only
# filter and max (no separate prime-check function)

longest_prime = lambda lst: max(
    filter(
        lambda s: len(s) > 1 and not any(len(s) % i == 0 for i in range(2, len(s))),
        lst
    ),
    key=len,
    default=None
)

words = ["hi", "hello", "world", "python", "AI"]
print(longest_prime(words))