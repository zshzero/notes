- sync your forked repository with the original repository and push the changes to your Github repository

```
$ git remote add upstream https://github.com/[Original Owner Username]/[Original Repository].git
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
$ git push
```

- Update other branch with master branch
```
$ git checkout <branch>
$ git rebase master
```
