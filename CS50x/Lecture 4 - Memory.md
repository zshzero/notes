- Hexadecimal 
	- Ex: 255 decimal in hex is FF and FF in binary is 1111 1111
	- Represented as '0x' - Ex: 0xFF
- Pointer - variable that stores address
	- Ex: `int *p = &n;` `printf("%p\n", p)`
	- Deference operator - Ex:  `printf("%p\n", *p)`
```c
string s = "HI!";  
char *p = &s[0];
printf("%p\n", p); \\ prints address of first letter  
printf("%p\n", s); \\ prints the same as string represented the address of first letter till null char 
```
- `string` in `cs50.h` is just `char *`
- pointer arithmetic - adding 1 to point to next address of a char in string
	- Ex: `printf("%c\n", *(s+1))`
	- Adding 1 here means adding bytes taken by that particular datatype
		- Ex: Adding 1 here means adding 1 byte as char takes 1 byte
			- Adding 1 for int means adding 4 bytes as int takes 4 bytes
	 - Array can be treated as the address of the first element in that array
- Comparing 2 strings will actually compare 2 address of the 1st char 
- malloc and free
	- Sometimes, malloc doesn't get enough memory to allocate - should handle that fail manually
- valgrind - designed to find memory related bugs in code
	- garbage values
- pass by value and pass by reference 
- When you run a exe, It Loads machine code first, then global vars, then heap and stack