arr = [-1] * 26
s = input()
for i in range(len(s)):
    if arr[ord(s[i]) - ord('a')] == -1:
        arr[ord(s[i]) - ord('a')] = i

for i in range(26):
    print(arr[i], end=' ')