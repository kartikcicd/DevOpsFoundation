# How Git Works
# Git is a distributed version control system that allows multiple developers to work on a project simultaneously. 
# It tracks changes to files and enables collaboration through branching and merging. Here's a brief overview of how Git works:

# Git Concepts:
# 1. Snapshots: Git takes snapshots of your files at different points in time, allowing you to track changes and revert 
#    to previous versions if needed.
# - Unchanged files are linked to the previous snapshot, while changed files are stored as new snapshots.
# - This makes Git efficient in terms of storage and performance (Space efficient, Fast, and Reliable).

# Three Main States of Files in Git:
# 1. Modified: Changes have been made to the file but not yet staged for commit. 
#    (git add <file-name> that's missing) [Working Directory]
# 2. Staged: Changes have been added to the staging area and are ready to be committed. 
#    (git add <file-name> is done) [Working Directory -> Staging Area]
# 3. Committed: Changes have been committed to the local repository. 
#    (git commit -m "commit message") [Staging -> Local Repository]

# Git's Architecture:
# 1. Working Directory: The directory where you make changes to your files.
# 2. Staging Area (Index): A temporary area where you prepare changes before committing them to the local repository.
# 3. Repository (Local Repository): The database where Git stores the history of your project, including all commits and branches.
# 4. Repository (Remote Repository): A version of your repository hosted on a remote server, allowing collaboration with other developers. 

# Git's Internal Data Structures:

# 1. Blob: 
#   - Represents the content of a file in Git.
#   - Identified by a SHA-1 hash of its content.
#   - Same content produces the same blob, regardless of file name or location.
#   - It helps git avoid storing duplicate content, making it space-efficient.

# echo "Hello, World!" > hello.txt
# git add hello.txt (#874heuehdec8yvoirwjf)

# 2. Tree:
#   - Represents a directory in Git.
#   - Tree points to blobs (files) and other trees (subdirectories).
#   - It forms a hirarchical layout of the project, allowing Git to track the structure of the repository.
#   - Each tree is identified by a SHA-1 hash of its content, which includes the names and hashes of the blobs and trees it contains.