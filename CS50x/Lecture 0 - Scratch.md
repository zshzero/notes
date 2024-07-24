- Computer just speaks only 0s and 1s
	- It counts further more by adding more bits. Ex - 010
	- Simply store or don't store electricity (ON or OFF of switches)
- But this only crunches only number, so we built standards to represent alphabets and number 
	- ASCII Standard - Uses 8 bits = 1 Byte to represent a character
- Unicode - Modern standard of mapping many more possibilities - uses both 16 and 32 bits - 8 bits for backward compatibility 
	- Unicode has Standardized the description of what these things are, but not on how they look - emojis look different in ios and android 
- Colors - Represented by mixing RGB - 8 bits for each - They added extra bit for ASCII and calling it extended ASCII
	- 8 bits for a Black and White image and 24 bits - one byte each for Red, Green, and Blue
- Video is just a sequence of photos (24 frames per second)
	- Storing multimedia data in raw format is not feasible as they are huge 
	- Modern formats compresses the data by representing same data with shorter pattern of zeros and ones
		- Lossless and lossy compression
	- Containers that can combine different formats of audio and video

- Input -> Algorithm -> Output
	- Step by step instruction to solve a problem
- Ex: Finding a name on a telephone directory
	- Starting in the middle -> check if its on left or right -> Go in that direction and discard the other side -> Repeat the same until you reach or don't find the name at all
- Size of problem v/s time to solve
	- Looking every page from start - n
	- Looking 2 pages at a time from start - n/2
	- Looking according to the above example algorithm - logn
- Pseudo Code
	1 Pick up phone book  
	2 Open to middle of phone book  
	3 Look at page  
	4 If person is on page  
		5 Call person  
	6 Else if person is earlier in book  
		7 Open to middle of left half of back  
		8 Go back to line 3  
	9 Else if person is later in book  
		10 Open to middle of right half of back  
		11 Go back to line 3  
	12 Else  
		13 Quit

- Scratch - implemented by MIT for visual and abstracted coding 