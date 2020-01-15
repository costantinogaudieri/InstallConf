import os
from git import Repo
from xmlReader import XmlReader

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with

repo = 0

def configureGit(path):
     rw_dir = path
     global repo
     repo = Repo(rw_dir)

def checkoutDev():
     git = repo.git
     git.checkout('develop')

def executeRelease(release,path):

     git = repo.git
     XmlReader.removeSNAPSHOT(path, release)

     # relPath = "release/"+release
     # git.checkout('HEAD', b=relPath)
     # git.checkout(relPath)


     # git.add('-u')
     # git.commit(message=release+' version')

    # git.push('origin', relPath)
    # git.checkout('master')

    # master = repo.branches['master']
    # b_rel = repo.branches[relPath]
    # base = repo.merge_base(master, b_rel)
    # repo.index.merge_tree(b_rel, base=base)
    # repo.index.commit('Finish ' + release, parent_commits=(b_rel.commit, master.commit))
    # git.push('origin', master)
    # b_rel.checkout(force=True)
    # git.checkout('develop')
    # relPathOrigin = "origin/release/" + release

    # remote = repo.remote('origin')
    # for repo_branch in repo.references:
         # print(repo_branch)
         # if relPathOrigin in repo_branch.name:
              # print("deleting remote branch: %s" % repo_branch.remote_head)
              # remote.push(refspec=(
                            #  ":%s" % repo_branch.remote_head))


#def upgradeRelease():

