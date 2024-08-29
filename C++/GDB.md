- Create executable that can be debugged using GDB   
`$ gcc -­g program.c -o program // -g includes debugging info`

- Start debugging program with command-line arguments  
`$ gdb --­­args program args`

- Breakpoint
  - Sets a breakpoint on either function, line number, or memory address   
  `(gdb) [b]reak​ <function name or filename:line# or *memory address>`
  - List breakpoints   
  `(gdb) [i]nfo [b]reak​​`
  - Removes breakpoint   
  `(gdb) [d]elete​ <breakpoint #>`

- Info - Lists information about argument (lists possible args if none are provided)   
`(gdb) [i]nfo​ (about)`
  - `[f]rame` – info about current stack frame, including address of current frame, address of previous frame, locations of saved registers, function arguments, and local variables
  - `[s]tack`|`[b]ack[t]race`|`[where]` – lists stack backtrace, showing what function calls have been made, and their arguments
  - `[r]egisters` – lists contents of each register. 
    - `[all-r]egisters`​ - lists even more registers
  - `[b]reak` – lists number and address of each breakpoint, and what function breakpoints are in
  - `[fu]nctions` - lists all of the function signatures, if the program was compiled with the gcc​ flag -g​

- Runs loaded executable program with program arguments arg1...argn   
`(gdb) [r]un​ (arg1 arg2 ... argn)`

- Resumes execution of a stopped program, stopping again at the next breakpoint   
`(gdb) [c]ontinue`

- Steps through single line of code. Steps into function calls   
`(gdb) [s]tep`
- Steps through a single x86 instruction. Steps into calls   
`(gdb) [s]tep[i]`

- Steps through a single line of code. Steps over function calls   
`(gdb) [n]ext`
- Steps through a single x86 instruction. Steps over calls   
`(gdb) [n]ext[i]`

- Kills the current debugging session   
`(gdb) [k]ill`

- Quits gdb   
`(gdb) [q]uit`

Reference: 
- https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf
- https://gabriellesc.github.io/teaching/resources/GDB-cheat-sheet.pdf
- https://github.com/reveng007/GDB-Cheat-Sheet