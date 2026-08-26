# GitHub & Git Workflow Summary

Here is a summary of all the GitHub-related tasks and instructions we covered today.

## 1. Connecting to a GitHub Repository
- **Repository URLs**: Clarified that to clone a repository, you need the full repository URL (e.g., `https://github.com/3viru/alsu2.git`), rather than just a user profile URL.
- **Verification**: Verified your local repository setup. Your project is successfully cloned and located at:
  `C:\Users\tallerespa\Documents\git\alsu2`

## 2. Authentication using a Personal Access Token (PAT)
- GitHub no longer accepts account passwords for terminal authentication.
- **How to use it**: When prompted for a password during `git clone` or `git push`, you must paste your PAT instead.
- **Windows Credential Manager**: Once entered, Windows securely saves this token so you don't have to enter it every time.

## 3. Logging Out / Changing Git Credentials
If you need to switch accounts or update an expired token:
1. Open the Windows Start Menu and search for **Credential Manager** (Administrador de credenciales).
2. Go to **Windows Credentials**.
3. Under "Generic Credentials", find the entry starting with `git:https://github.com`.
4. Click **Remove** to delete it. Git will prompt you for your credentials again on your next action.
*(Alternative terminal command: `cmdkey /delete:LegacyGeneric:target=git:https://github.com`)*

## 4. Standard Workflow to Upload Files (Push)
To upload new or updated files to your GitHub repository, always follow this 3-step sequence from inside your project folder:

```bash
# 1. Stage the files (track new or modified files)
git add .

# 2. Commit the changes (save a snapshot with a message)
git commit -m "Describe your changes here"

# 3. Push to GitHub (upload the snapshot)
git push
```

## 5. Troubleshooting: "My files don't appear on GitHub"
If you modified a file locally but it isn't showing up on GitHub, it usually means one of the steps above was skipped. 
To fix this, you can check your repository status:
```bash
git status
```
This command will tell you if you have files that need to be added (`git add`) or commits that need to be pushed (`git push`).
