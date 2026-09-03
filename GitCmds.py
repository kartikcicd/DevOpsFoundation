# 0. git init
# Initializes a new Git repository in the current directory. 
# Creates a .git subdirectory that contains all the necessary metadata for the repository.

# 1. git status
# Shows the current status of my repo - staged, unstaged, untracked files, etc.

# 2. git add <file-name>
# Stages a file for commit. You can also use "git add ." to stage all files in the current directory.

# 3. git commit -m "commit message"
# Commits the staged changes to the local repository with a descriptive message.

# 4. git branch <branch-name>
# Creates a new branch with the specified name.

# 5. git checkout <branch-name>
# Switches to the specified branch.

# 6. git merge <branch-name>
# Merges the specified branch into the current branch.

# 7. git pull
# Fetches and merges changes from the remote repository into the current branch.
# Req: Remote repo url must be set up. Use "git remote add origin <remote-url>" to set it up.

# 8. git push
# Pushes the committed changes from the local repository to the remote repository.

# 9. git log
# Shows the commit history of the current branch.

# 10. git clone <remote-url>
# Creates a local copy of a remote repository.

# 11. Create and switch to a new branch in one command:
# git checkout -b <branch-name>

# 12. Delete a branch:
# git branch -d <branch-name>  # Deletes a local branch
# git push origin --delete <branch-name>  # Deletes a remote branch

# 13. Git Auth Commands
# git config --global user.name "Your Name"  # Set your name for commits
# git config --global user.email "your@email.com" # Set your email for commits
# git config --list  # List all Git configurations
# git config --global color.ui true  # Enable helpful color output in Git commands

# 14. git version
# Displays the installed Git version.

# 15. git add .
#     git add -p : "Patch" mode, allows you to interactively choose which changes to stage.  

# git rm <file-name>  # Removes a file from the working directory and stages the removal for commit.

# Git Hosting Platforms:
# 1. GitHub: A web-based platform for hosting Git repositories, offering collaboration features like pull requests, issues, 
# and project management tools.
# 2. GitLab: A web-based DevOps platform that provides Git repository management, CI/CD pipelines, and project management features.
# 3. Bitbucket: A web-based platform for hosting Git repositories, offering features like pull requests, issue tracking,
# and CI/CD integration.