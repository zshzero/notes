- Make is not a compiler itself - Its just a utility to compile coder easier
	- clang is a C compiler
	- `clang hello.c` - Outputs a file called `a.out` (assembler output)
	- `clang -o hello hello.c -lcs50` - args to specify output file name instead of a.out and link cs50 header file
- Steps undergone to convert Source code from C to Zeros and Ones
	- Pre-processing 
		- Pre-processor directives written on the top of the file (starts with '#')- header files contains prototypes of the functions
	- Compiling
		- Converts c code to assembly lang - low level lang just before Zeros and Ones
	- Assembling
		- Converts assembly lang to Zeros and Ones
	- Linking
		- Stitches all the Zeros and Ones. Ex: `hello.c, cs50.cs, stdio.cs`
- Debugging using printf
- Debugging using Debugger Tool
- Debugging using Rubber Duck
- Array - sequential collection of elements of the same datatype 
	- Declaring one variable to store multiple values
	- Stores data contiguously
- Implicit type Conversion
- `\0` (nul character) demarcates the end of the string
	- Ex: "Hi!\n" takes 5 bytes - 3 for char, 1 for \n and 1 for \0
- Convert string to uppercase
```C
for (int i = O, n = strlen(s); i < n; i++)  
{  
	if (s[i] >= 'a' && s[i] <= 'z') // compares ascii values  
	{  
		printf("%c", s[i] - 32); // maps to uppercase letter
	}
	else
	{
		printf("%c", s[i]);
	}
}
```
- Cmd line args
```C
int main(int argc, string argsv[])
{
	// argument count and argument vectors
}
```
- Exit status