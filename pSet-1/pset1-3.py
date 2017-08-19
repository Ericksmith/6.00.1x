count = 0
longest = 0
numCount = 0

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > longest:
            longest = count
            numCount = char + 1
    else:
        count = 0
answer = numCount - longest
print('Longest substring in alphabetical order is:', s[answer:numCount + 1])
