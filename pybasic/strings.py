string = "don't you know \"python\"?"
print(string)
a = "a"
b = "b"
print(a + " " + b)
print(a*3)
print(string[2:7])  # 2부터 7전까지

# a[0] = b 불가능


# slice 표현식 [::] (string도 list 인거 잊지말기)
# [start:stop:step]
inputString = "hello"
reverseString = inputString[::-1]
print(reverseString)


text = "hello"
# 9 = fix the width, fill "*" with the empty spaces
centered_text = text.center(9, "*")
print(centered_text)  # **hello**

text = "123.456.789"
segments = text.split('.')
print(segments)  # segments는 list이다


char = "a"
char.isalpha()  # check if char is english letter or not

''.join(["a", "b"])  # change char list to string

ord(char)  # char의 ascii값
chr(21)  # ASCII 21값의 char 반환
