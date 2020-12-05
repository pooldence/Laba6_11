f=open('text.txt')
text=f.read()
key=3;
code_text=""
text=text.replace(' ', '')
text=text.replace('\n', '')
for i in range(key):
    code_text+=text[i]
    n=i
    while(n+key<len(text)):
        n+=key
        code_text+=text[n]
print(code_text)
d=open("code.txt","w")
d.write(code_text)
f.close()
d.close()
