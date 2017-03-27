from git import Repo
from os import path
from xmlFormat import helper
parentPath = "D:/kudu/"
cSharpCode = ".cs"
repo = Repo(parentPath)

def diffIndexAgainstCommit(id):
    index = repo.index
    diff = index.diff(id)
    # return modified, and does not end with ".cs"
    return [parentPath + d.a_path for d in diff.iter_change_type('M') if d.a_path[-3:] != cSharpCode] #TODO yield

if __name__ == "__main__":
    for fPath in diffIndexAgainstCommit('e8fce7a78a7ff261f44c9ddf60d57186efa4a2b1'):
        print(fPath)
        if helper(fPath):
            print("above lines are modified")
