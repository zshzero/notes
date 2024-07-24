## Keys to move (multiples accepted)
```
	k
    h       l
	j
```

## Exit Vim
- :q to quit
- :q! to quit without saving
- :wq to save and quit
- Shitf+z+z

## Normal Mode
- i for normal mode to insert mode
- shift+i for going to non blank char in insert mode
- a append to the line
- A append to the end of the line
- s deleted the char anf enters insert mode
- S deletes entire line and enters insert mode
- o adds a newline and enters insert mode
- O adds a newline preceeding to cursor and inserts a new line
- v for normal mode to visual mode
- gg to jump to the first line
- shift+g to jump to the last line
- g+[nav-key] to to get into visual line
- 0 to get to the first char to line
- [num]+shift+g to move to specfic line
- x to delete char
- u to undo 
- ctrl+r to redo
- [num]+x to delete num chars
- d+w to delete word (--||--)
- d+d to delete line (--||--)
- d$ deletes from cursor to end of line
- D deletes from cursor to end of line
- w to move forward first chars (multiples accepted)
- e to move forward with end chars (--||--) 
- b to move backward with first chars (--||--)
- p to put or paste one line after
- r to replace char
- c to change which puts to insert mode [ex: c+e deletes till end of the word and to i mode. c+$ from cursor to change entierly line]
- C to delete from cursor to end of line
- W,E,B navigates by ignoring the punctuation
- f[char] puts us to char that it encounter first
- F[char] puts us to char that it encounter first in backward
- t[char] puts us to one letter behind the char that it encounter first
- T[char] puts us to one letter behind char that it encounter first in backward
- yw yanking a word(copying)
- yy yanks a entire line
- y$ yanks from cursor to end of line
- / to search a word and n to go forward instance and N for back instance
- ctrl+o for undo cursor position
- ctrl+i for redo cursor position

- Ctrl+W, S for horizontal splitting
- Ctrl+W, v lower case) for vertical splitting
- Ctrl+W, Q to close one
- Ctrl+W, Ctrl+W to switch between windows
- Ctrl+W, J (xor K, H, L) to switch to adjacent window (intuitively up, down, left, right)


## Cmd Mode
- :s/oldstring/newstring/g search and replace in entire doc
- :3,9s/oldstring/newstring/g search and replace in between lines 3 and 9
- :%s/oldstring/newstring/gc search and replace in entire doc with interactive mode
- :!cmd to run terminal commands
- ctrl+d as tab in terminal
