from git import Repo
from os import path
parentPath = "D:/kudu/"
cSharpCode = ".cs"
from xmlFormat import helper
if __name__ == "__main__":
    repo = Repo(parentPath)
    hcommit = repo.head.commit
    # print(hcommit)
    diffObjects = hcommit.diff() # of type diffIndex
    for diff in diffObjects.iter_change_type('M'):
        relativePath = diff.a_path
        if relativePath[-3:] != cSharpCode:
            fPath = parentPath+relativePath
            helper(fPath)
