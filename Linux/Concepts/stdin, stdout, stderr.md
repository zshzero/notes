- 0: Command accepts text as its input via `stdin` (standard input) stream 
- 1: Text output from the command to the shell is delivered via the `stdout` (standard out) stream. 
- 2: Error messages from the command are sent through the `stderr` (standard error) stream.

- Ex: `./error.sh > capture.txt`
	- `stdin` is what was inputted in the bash file 
	- Output from `stdin` was redirected to the file
	- Error message delivered via `stderr` is sent to the terminal window

- `>` redirection symbol
	- Redirecting `stderr`
		- `./error.sh 2> capture.txt`
	- Redirecting Both `stdout` and `stderr` 
		- `./error.sh 1> capture.txt 2> error.txt`
	- Redirecting `stdout` and `stderr` to the Same File
		- `./error.sh > capture.txt 2>&1`

Reference - https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/ 