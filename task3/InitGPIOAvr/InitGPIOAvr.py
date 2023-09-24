bit = ""

for i in range(8):
    print(f"Please enter Bit {i} mode : ", end = "")
    ans = input()

    if(ans == "in"):
        bit += "0"
    elif(ans == "out"):
        bit += "1"

bit += "b0"
bit = bit[::-1]

code = f'''#include <avr/io.h>\n
void Init_PORTA_DIR(void)
{{\nDDRA={bit}\n}}\n
int main()\n{{\n
return 0;\n}}'''

file_path = "/home/zeyad/Desktop/embeddedlinuxtasks/task3/InitGPIOAvr.c"
file = open(file_path, "w")
file.write(code)