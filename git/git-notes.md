# git notes

#### Get commit date of all files in a repo
```bash
git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _
```

#### Get commit date of single file
```bash
git log -1 --format=%ci <filename>
```