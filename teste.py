num = input()
num = str(num)

separa = str.split(num, '.')
if 'separa[1]' in locals():
    print("separou")

print(separa[0])