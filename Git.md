# Git Notes
- Total Number of commands: 145
  - Porcelain (82)
    - 44 main commands (add, commit, push, pull, ...)
    - 11 manipulators (config, reflog, replace, ...)
    - 47 interrogators (blame, fsck, rerere, ...)
    - 10 main commands (send-mail, p4,svn, ...)

  - Plumbing (63)
    - 19 manipulators (apply, commit-tree, update-ref, ...)
    - 47 interrogators (cat-file, for-each-ref, ...)
    - 10 main commands (fetch-pack, send-pack, ...)
    - 10 main commands (check-attr, sh-i18n, ...)

### Customize Merging Standards
```
git config --global pull.rebase true // Configure to use rebase by default for pull
git config --global pull.ff only // Configure to use squash merging for pull requests
```

### Search string
```
git grep 'search string'
```

### Autocorrect commands
```
git config --global help.autocorrect 20 // value 20 is time taken before it runs autocorrected command
```

### Efficient Pull Request Handling with Heads
```
git fetch origin pull/ID/head:BRANCHNAME // fetch directly from PR refs
```

## [Oldies but Goodies](https://blog.gitbutler.com/git-tips-1-theres-a-git-config-for-that)

### Conditional Configs
```
[includeIf "gitdir:~/projects/work"]
  path = ~/.gitconfig-work
[includeIf "gitdir:~/projects/oss"]
  path = ~/.gitconfig-oss
```

### Line Ranges for Blame & Log
```
git blame -L 28,43 path/to/file // line range option
git blame -L :'class LocalFile' path/to/file // : to specify pattern
git log -L 28,43:path/to/file
git log -L :'class LocalFile':path/to/file
```

### Subsequent Following of Blame
```
git blame -w // ignore whitespace changes
git blame -w -C // and detect lines moved or copied in same file
git blame -w -C -C // or commit that created the file
git blame -w -C -C -C // or any commit at all
```

### Grep commits
```
git log -S varName -p path/to/file // S to specify pattern and p to path
```

### Reference logs
```
git reflog 
```

### Word Diff
```
git diff --word-diff rev1..rev2 // Default, line based diff
git diff --color-words rev1..rev2 // gives expected colored output 
git log --word-diff
```

### Reuse Recorded Resolution
```
git config --global rerere.enabled true // Git memorizes conflicts, resolutions and automatically resolves it next time
git config --global rerere.autoUpdate true // automatically stage it
```

## [Some Subtle New Things](https://blog.gitbutler.com/git-tips-2-new-stuff-in-git)

### Sort Branches
```
git config --global branch.sort -committerdate // sort by last commit date
git config --global column.ui auto // list branches as columns
```

### Safe Force Pushing
```
git push --force-with-lease // check if your last push is still latest on server before it forces
```

### Setting up Aliases
```
git config --global alias.br branch
git config --global alias.bb !run-script.sh
```

### Sign Commit with SSH
```
git config gpg.format ssh
git config user.signingKey ~/.ssh/id_rsa.pub
git commit -S -am "message"
```

### way to add cronjobs, Maintenance
```
git maintenance start // turn on maintenace taks. Strategy = incremental means:
  gc: disabled, commit-graph: hourly, prefetch: hourly, loose-objects: daily, incremental-repack: daily, pack-refs: none
```

## [Really Large Repositories and Monorepos](https://blog.gitbutler.com/git-tips-3-really-large-repositories)

### Garbage Collection
- Repositories accumulate garbage like orphaned or inaccessible commits when performing history altering commands like reset or rebase. In effort to preserve history and avoid data loss, detached commits are not deleted (detached commit can still be checked out, cherry picked, and examined through the git log)
- GC also performs compression on stored Git Objects, freeing up precious disk space. When it identifies a group of similar objects, it will compress them into a 'pack' which are like zip files of Git objects and live in `./git/objects/pack` inside repository
- It is automatically invoked through frequently used commands when needed. Invoked manually by running : `git gc`

### Prefetching
- A cronjob called "prefetching" is added, which will essentially run fetch command every hour automatically for you
- It does not update your remote references and instead, it populates special refs/prefetch area of your references which makes manual fetches fast

### Commit Graph
- Instead of opening up one commit object at a time to see what it's parent is, commit graph is basically an index of all that information that can be quickly read in one go
- This makes walking your commit history faster and things like git log --graph or git branch --contains 

### Filesystem Monitor
- One thing that VFS for Git needed was a filesystem monitor, which could detect when virtual file contents were being requested and fetch them from central server if needed
- This monitor speeds up git status command by updating index based on filesystem modification events rather than running stat on every file
- This became unnecessary when virtualization layer was abandoned and integrated into Git core
<br/> <br/>
- Set config settings: `git config core.fsmonitor true`
- git status command will see when it runs, indicating that it should use fsmonitor-daemon. (If daemon is not running, it will start it)
- First git status run after setting it won't be much faster. But every time after that, it will be massively faster

### Partial Cloning
- By default, Git fetchs everything 
- Git has shallow clones, `git clone --depth=1` to get only last commit and objects it needs. Then `git fetch --unshallow` to get remanining history later if needed. But it did break things like blame, you can't log, etc
<br/> <br/>
- Now, Blobless and treeless clones gets the whole history, but doesn't have actual content locally (treeless clones are not recommended generally)
- Pass `--filter=blob:none` for blobless clones (`--no-checkout` to skip the initial checkout)
- By default, It does two fetches: one for commits and tree data and a second for files it needs for my local checkout.
- Downsides to this is, if you run a command which needs data that is not there, Git needs to reach server and request those objects. But, this happens on-demand and make something like blame do a bunch of roundtrips

### Sparse Checkouts
- Monorepos may contain multiple projects as subdirectories and could be annoying to manage those
- Sparse checkouts filters the checkouts to just specified directories : `git sparse-checkout set [dir1] [dir2]`
- It will still have top level files, but only subdirectories that we specified. This is called "cone mode" and tends to be pretty fast. It also makes status and related commands faster because there are fewer files to care about 
- You can also however, set patterns rather than subdirectories, but it's more complicated.

## [DevWorld Git](https://blog.gitbutler.com/devworld-git-slides)

### Change Branch
```
git switch branch
git switch --create branch // Create new branch starting at <start-point> (default HEAD) before switching to branch
git switch --detach // detach working tree (HEAD refers to a specific commit, as opposed to referring a named branch)
```

### Restore Branch
```
git restore file
git restore --staged file // restore content in index
git restore --patch file // Interactively select hunks in the diff between the restore source and restore location
git restore --source master~2 file //  restores file two revisions back
```

### Hooks

### Attributes
```
echo '*.png diff=exif' >> .gitattributes // pre-process files based on extensions 
dif config diff.exif.textconv exiftool // strategy to run on specified files
```

### Smudge and Clean : RCS Keywords, LFS

### Fixup commits
```
git commit --fixup=hash-of-commit-to-be-added-to // Adds commit to squash and rebase it later
git rebase --autosquash <target-branch> // Update commit and rebase the commit series
```

### Rebasing Stacks
```
git config --global rebase.updateRefs true // Update refs after rebase
```

### Worktrees