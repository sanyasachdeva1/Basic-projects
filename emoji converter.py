emoji = {
    ":)": "😀",
    ";)": "😉",
    ":(": "☹",
    ":-*": "😘",
    ":-$": "🤫",
    ":P": "😛",
    "=((": "💔",
    ":-O": "😮",
    "B-)": "😎",
    ":((": "😭"}
# output = " "
mood = input("Enter your mood :")
# for item in mood:
#     output += convert.get(item)
# print(output)
words = mood.split(" ")
#print(words)
for word in words:
    print(emoji.get(word, word), end=" ")

