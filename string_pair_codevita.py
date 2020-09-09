n=int(input("enter no of integer to be added in the list "))
a=input(f"enter {n} no's seprated by space ").split()
digits=[int(i) for i in a]
print(digits)
def textual(n):
    tup=tuple(str(n))
    digit=[i for i in range(10)]
    spell=["zero","one","two","three","four","five","six","seven","eight","nine"]
    combo=dict(zip(digit,spell))
    text=""
    if n==100:
        return "hundred"
    else:
        for _ in tup:
            text+=combo.get(int(_))
        return text
new_digit=[textual(i) for i in digits]
print(new_digit)
vowel_count=[]
for i in new_digit:
    count=0
    for j in i:
        if j in "aeiou":
            count+=1
    vowel_count.append(count)
print(vowel_count)
sum_vowel_count=sum(vowel_count)
if sum_vowel_count>100:
    print("greater 100")
else:#require pair
    pair_count=0
    for i in range(len(digits)):
        for j in range(1,len(digits)):
            if (digits[i]+digits[j])==sum_vowel_count:
                pair_count+=1
    print(textual(pair_count))

