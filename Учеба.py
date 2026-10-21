p1 = input()
s1 = "Barcelona"
length1 = len(s1)

print("Футбольная команда" + p1 + "имеет длину" + s1 + "символов")

distance = abs(p1 - q1) + abs(p2 - q2)
print(distance)

str1 = "1"
str2 = str1 + "2" + str1
str3 = str2 + "3" + str2
str4 = str3 + "4" + str3
print(str4)

print(
    '''"Python is a great language!"', said Fred. '"I don't ever remember having this much fun before."'''
)

s = input()

if "@" in s or "." in s:
    print("YES")
else:
    print("NO")

for i in range(1, 10, 3):
    print(i)

m = int(input())
n = int(input())

for i in range(m, n - 1):
    print(i)

s = "01234567891011121314151617"
for i in range(0, len(s), 5):
    print(s[i], end="")
