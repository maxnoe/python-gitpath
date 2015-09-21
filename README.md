# gitpath

A few functions to make working with python
inside git repos easier.

## path handling

`repository_root` returns the absolute path of the repository root
directory

`abspath` returns an absolute path for a path given relative to the
root directory,
so assuming, this repo resites in `/home/maxnoe/python-gitpath`:

```{python}
import gitpath

print(gitpath.abspath('setup.py'))
```

Will give you:
`/home/maxnoe/python-gitpath/setup.py`
