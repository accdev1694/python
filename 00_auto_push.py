import subprocess

def git_add_commit_push(commit_message):
    try:
        # Add all files to staging area
        subprocess.run(["git", "add", "."])

        # Commit changes with the provided message
        subprocess.run(["git", "commit", "-m", commit_message])

        # Push changes to the remote repository
        subprocess.run(["git", "push"])
        print("Changes successfully pushed to GitHub.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Prompt the user to enter the commit message
    commit_message = input("Enter commit message: ")

    # Call the function to add, commit, and push changes
    git_add_commit_push(commit_message)
