# Function to output something on the console
def consout(out, tabulations, f):
    stream = f"printf(\"{out}\");"
    print(tabulations + stream, file=f)

# Function to generate the main block of code

def ekans_go(file):
    with open(file, 'w') as f:

        # Print the headers
        print("#include <stdio.h>\n", file=f)

        # Print the body
        print("int main(void) {", file=f)

        # Test
        consout("This is my very first test for generating C code in python...", "\t", f)

        # Close
        print("}", file=f)

if __name__ == "__main__":
    ekans_go("main.c")

# TODO: Tabulation handling
# TODO: Interactivness
# TODO: Syntax