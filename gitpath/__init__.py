from subprocess import check_output
from functools import lru_cache
import os.path


@lru_cache(maxsize=1)
def root():
    ''' returns the absolute path of the repository root '''
    base = check_output('git rev-parse --show-toplevel', shell=True)
    return base.decode('utf-8').strip()


def abspath(relpath):
    ''' returns the absolute path for a path given relative to the root of
    the git repository
    '''
    return os.path.join(root(), relpath)
