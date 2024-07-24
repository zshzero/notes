## Stream editor parses and performs basic text transformations on an input stream

- `$ sed 's/unix/linux/' filename -> replaces the first occurrence of the pattern in each line i.e unix word with linux in filename`
- `$ sed 's/unix/linux/2' filename -> Use the /1, /2 etc flags to replace the first, second occurrence of a pattern in a line`
- `$ sed 's/unix/linux/g' filename -> flag /g(global) specifies in command replaces all the occurrences of the string in the line`
- `$ sed 's/unix/linux/3g' filename -> replaces nth occurrence of a pattern in a line. Here, n is 3`
- `$ sed '3 s/unix/linux/' filename -> Replacing string on a specific line number`
- `$ sed 's/unix/linux/p' filename -> Duplicating the replaced line with /p flag`
- `$ sed -n 's/unix/linux/p' filename -> Printing only the replaced lines`
- `$ sed '1,3 s/unix/linux/' filename -> Replacing string on a range of lines (inclusive of 1 and 3)`
- `$ sed '5d' filename -> Deletes the 5th line`
- `$ sed '$d' filename -> Deletes the last line`
- `$ sed '3,6d' filename -> Deletes range of lines`
- `$ sed '/abc/d' filename -> Deletes pattern matching line`
