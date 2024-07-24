## Ctrl+B Cheat Sheet for tmux

### Session Commands

- S: List sessions.
- $: Rename current session.
- D: Detach current session.
- Ctrl+B, and then ?: Display Help page in tmux.

### Window Commands

- C: Create a new window.
- ,: Rename the current window.
- W: List the windows.
- N: Move to the next window.
- P: Move to the previous window.
- 0 to 9: Move to the window number specified.

### Pane Commands

- %: Create a horizontal split.
- “: Create a vertical split.
- H or Left Arrow: Move to the pane on the left.
- I or Right Arrow: Move to the pane on the right.
- J or Down Arrow: Move to the pane below.
- K or Up Arrow: Move to the pane above.
- Q: Briefly show pane numbers.
- O: Move through panes in order. Each press takes you to the next, until you loop through all of them.
- }: Swap the position of the current pane with the next.
- {: Swap the position of the current pane with the previous.
- X: Close the current pane.
 
 
- tmux kill-server => to cleanly and gracefully kill all tmux open sessions (and server).
- tmux kill-session -a to close all other sessions when you are inside a tmux session you would like to keep
- tmux kill-session -t targetSession to kill that specific session.
