#Count the occurrence of each vowel in the sentence given as input by the user

vowel={"a":0,"e":0,"i":0,"o":0,"u":0}

occurrence=input("sentance ").lower()
for c in occurrence:
    print(c)
    if c in vowel:
        vowel[c]=vowel[c]+1

print(vowel)

#Count the occurrence of each alphabet that occurs in the sentence given as input by the user.

alphabet={}
occor=input("sentance ").upper()
for ch in occor:
    print(ch)
    if ch.isalpha():
        if ch not in alphabet:
            alphabet[ch]=1
        else:
            alphabet[ch]=alphabet[ch]+1
print(alphabet)        
