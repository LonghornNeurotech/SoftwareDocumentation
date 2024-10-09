# A Complete Guide to Using GitHub

GitHub is a web-based platform that uses Git, a version control system, to help developers collaborate on projects. GitHub provides tools to manage code, track changes, and work together efficiently.

---

## Table of Contents

1. [Introduction to Git and GitHub](#introduction-to-git-and-github)
2. [Setting Up Git and GitHub](#setting-up-git-and-github)
3. [Basic Git Commands](#basic-git-commands)
4. [Creating a Repository on GitHub](#creating-a-repository-on-github)
5. [Working with Repositories](#working-with-repositories)
6. [Branching and Merging](#branching-and-merging)
7. [Collaborating on GitHub](#collaborating-on-github)
8. [Standards for Effective Team Operation](#standards-for-effective-team-operation)
9. [Conclusion](#conclusion)

---

## Introduction to Git and GitHub

Before diving into GitHub, it's essential to understand **Git** and how it forms the foundation of GitHub's functionality.

### **What is Git?**

**Git** is a distributed version control system. It allows multiple developers to work on the same project simultaneously without interfering with each other's changes. The Git system tracks the history of changes made to files, enabling you to:

- **Version Control:** Keep track of every modification to the code, allowing you to revert to previous states if needed.
- **Collaboration:** Work seamlessly with others, merging changes from different sources.
- **Branching:** Experiment with new features without affecting the main codebase.

### **What is GitHub?**

**GitHub** is a cloud-based platform that hosts **repositories** (storage locations for your project's code). Key features of GitHub include:

- **Repository Hosting:** Store and manage your Git repositories online.
- **Issue Tracking:** Report and manage bugs or feature requests.
- **Project Management:** Organize tasks and workflows using boards and milestones.
- **Collaboration Tools:** Facilitate code reviews, discussions, and pull requests.
- **Integration:** Connect with other tools and services to automate workflows.

---

## Setting Up Git and GitHub

To start using GitHub, you'll need to set up Git on your local machine and create a GitHub account.

### Install Git

**Why Install Git?**

Git is the underlying tool that enables version control on your computer. Installing Git allows you to interact with GitHub repositories from your local environment (i.e. your personal computer).


**Installation Steps:**

- **For Windows:**
  1. Download the Git installer from [Git for Windows](https://git-scm.com/download/win).
  2. Run the installer and follow the setup instructions.

- **For macOS:**
    1. The download for macOS is not as simple since there is no official installer.
    2. First try running ```bash git --version```. For 90% of you this should install Git
    3. If this does not work, install Homebrew [Homebrew Home](https://brew.sh/)
    4. Then run ```bash brew install git```

- **For Linux:**
  - You probably don't need this tutorial lol

*After installation, you can verify Git is installed by running:*
```bash
git --version
```

### Create a GitHub Account

**Why Create an Account?**

A GitHub account allows you to host repositories, collaborate with others, and access GitHub's suite of tools and features.

**What is a GitHub Account?**

A GitHub account is your personal profile on GitHub, where you can create and manage repositories, collaborate with others, and contribute to projects.

**Steps to Create an Account:**

1. **Visit GitHub:**
   - Go to [GitHub.com](https://github.com/).
2. **Sign Up:**
   - Click on the **"Sign up"** button.
   - Enter a unique **username**, a valid **email address**, and a **password**.
   - Please use your UTexas email if you are creating a new account!
3. **Verify Email:**
   - After signing up, GitHub will send a verification email.
   - Click the verification link in the email to activate your account.

### Configure Git

**Why Configure Git?**

Configuring Git with your username and email ensures that your commits are properly attributed to you. This information appears in the commit history and is crucial for collaboration and accountability.

**What is Configuration in Git?**

Configuration in Git involves setting up your identity (name and email) so that your contributions are correctly labeled in the project history.

**Configuration Steps:**

Open your terminal or command prompt and run the following commands, replacing `"Your Name"` and `"youremail@example.com"` with your actual name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

- The `--global` flag applies these settings to all Git repositories on your machine.
- If you need to set different credentials for a specific repository, you can omit the `--global` flag while inside that repository.

*Proper configuration ensures that your contributions are correctly identified in projects.*

---

## Basic Git Commands

Understanding and using basic Git commands is essential for managing your repositories effectively. Below are some fundamental commands, along with explanations of why and when to use them.

### **Initialize a Repository**

**What is a Repository?**

A **repository** (or "repo") is a storage location where your project's files and their revision history are kept. It can be hosted locally on your computer or on a platform like GitHub.

**Command:**
```bash
git init
```

**What It Does:**

- Initializes a new Git repository in the current directory.
- Creates a hidden `.git` folder to track changes.

**Why Use It:**

- Converts a project directory into a Git repository, enabling version control.
- Necessary before you can start tracking changes and using Git features.

**When to Use It:**

- When starting a new project that you want to version control.
- To turn an existing project into a Git repository.

### **Clone a Repository**

**What is Cloning?**

**Cloning** is the process of creating a local copy of a remote repository. This allows you to work on the project on your own machine. You would use this when you first start collaborating on our projects.

**Command:**
```bash
git clone <repository_url>
```

**What It Does:**

- Creates a local copy of a remote repository.
- Copies all the files, history, and branches from the remote repository to your local machine.

**Why Use It:**

- Allows you to work on a project locally while keeping it synchronized with the remote repository.
- Essential for collaborating with others by providing access to the project's codebase.

**When to Use It:**

- When you want to contribute to an existing project.
- To set up your development environment with the latest code.

### **Check Repository Status**

**What is the Repository Status?**

**Repository status** refers to the current state of your working directory and staging area. It shows which changes have been made, which are staged for the next commit, and which files are untracked.

**Command:**
```bash
git status
```

**What It Does:**

- Displays the state of the working directory and staging area.
- Shows which changes have been staged, which haven't, and which files are untracked.

**Why Use It:**

- Helps you understand what changes have been made since the last commit.
- Essential for tracking progress and ensuring you're committing the right changes.

**When to Use It:**

- Before committing changes to review what will be included.
- To check if there are any uncommitted changes that need attention.

### **Add Files to Staging Area**

**What is the Staging Area?**

The **staging area** is a preparatory space where you can gather changes you want to include in your next commit. It allows you to craft commits carefully, including only the changes you intend to make to the codebase.

**Command:**
```bash
git add <file_name>
# Or add all changes
git add .
```

**What It Does:**

- `git add <file_name>` stages a specific file.
- `git add .` stages all changes in the current directory and subdirectories.

**Why Use It:**

- Prepares changes to be included in the next commit.
- Allows selective staging of changes, enabling more organized and meaningful commits.

**When to Use It:**

- After modifying files and before committing them.
- To control which changes are included in a commit, especially when working on multiple features simultaneously.

### **Commit Changes**

**What is a Commit?**

A **commit** is a snapshot of your repository at a specific point in time. It records the changes you've staged, along with a message describing those changes.

**Command:**
```bash
git commit -m "Your commit message"
```

**What It Does:**

- Records the staged changes in the repository's history.
- Associates the changes with a commit message describing what was done.

**Why Use It:**

- Creates a snapshot of your project's current state.
- Facilitates tracking of changes over time and understanding the evolution of the project.

**When to Use It:**

- After staging changes with `git add`.
- To save progress at logical points in development, such as after completing a feature or fixing a bug.

### **Push Changes to Remote Repository**

**What is Pushing?**

**Pushing** is the process of uploading your local repository commits to a remote repository on platforms like GitHub. It updates the remote branch with your local commits.

**Command:**
```bash
# don't push to main it wont work :)
git push -u origin branch-name
```

**What It Does:**

- Uploads local repository commits to the remote repository on GitHub.
- Updates the remote branch (`main` in this case) with your local commits.

**Why Use It:**

- Shares your changes with others, enabling collaboration.
- Backs up your work to a remote server, ensuring it's safe and accessible from anywhere.

**When to Use It:**

- After committing changes that you want to share or collaborate on.
- To synchronize your local repository with the remote repository.

### **Pull Updates from Remote Repository**

**What is Pulling?**

**Pulling** is the process of fetching and integrating changes from a remote repository into your current branch. It ensures your local repository is up-to-date with the latest changes made by others.

**Command:**
```bash
git pull origin main
```

**What It Does:**

- Fetches and integrates changes from the remote repository into your current branch.
- Combines `git fetch` and `git merge` to update your local repository.

**Why Use It:**

- Keeps your local repository up-to-date with the latest changes from collaborators.
- Prevents conflicts by ensuring you have the most recent code before making new changes.

**When to Use It:**

- Before starting new work to ensure you're building on the latest code.
- Regularly while working on a project to stay synchronized with team members.
- Before pushing your code to the remote repository to avoid merge conflicts

### **What is a Remote Repository?**

A **remote repository** is a version of your project hosted on the internet or another network. GitHub is a common platform for remote repositories. It allows multiple collaborators to work on the same project from different locations.

**Why Add a Remote Repository?**

- **Collaboration:** Enables multiple team members to contribute to the project.
- **Backup:** Provides a remote backup of your code, safeguarding against local data loss.
- **Deployment:** Facilitates deploying your application to servers or other environments.

**When to Add a Remote Repository:**

- **After Initializing a Local Repository:** When you’re ready to share your project with others or back it up online.
- **Cloning a Repository:** Automatically sets up the remote repository, but you might need to add additional remotes.
- **Managing Multiple Remotes:** When working with forks or multiple sources.

**How to Add a Remote Repository:**

1. **Obtain the Remote Repository URL:**

   - Navigate to the repository on GitHub.
   - Click the **"Code"** button.
   - Copy the repository URL (HTTPS or SSH).

   *Example URL:*
   ```
   https://github.com/yourusername/your-repository.git
   ```

2. **Add the Remote Repository to Your Local Project:**

   ```bash
   git remote add origin https://github.com/yourusername/your-repository.git
   ```

   - **What It Does:**
     - `git remote add`: Adds a new remote repository.
     - `origin`: The name of the remote. `origin` is the default name for the primary remote repository.
     - The URL specifies the location of the remote repository.

3. **Verify the Remote Repository:**

   ```bash
   git remote -v
   ```

   - **What It Does:**
     - Lists all configured remote repositories.
     - Shows the URLs for fetching and pushing.

   *Example Output:*
   ```
   origin  https://github.com/yourusername/your-repository.git (fetch)
   origin  https://github.com/yourusername/your-repository.git (push)
   ```

4. **Push Your Local Repository to the Remote:**

   ```bash
   git push -u origin main
   ```

   - **What It Does:**
     - Pushes your local `main` branch to the `origin` remote.
     - The `-u` flag sets `origin/main` as the default upstream branch for your local `main` branch, simplifying future push and pull commands.

   *After this initial push, you can simply use `git push` and `git pull` without specifying the remote and branch.*

---

## Creating a Repository on GitHub

### 1. **Navigate to Your GitHub Profile**

**Steps:**

1. **Log In:**
   - Go to [GitHub.com](https://github.com/) and sign in with your account.
2. **Access Repositories:**
   - Click on your profile icon in the top-right corner.
   - From the dropdown menu, select **"Your repositories"**.

### 2. **Create a New Repository**

**What is Creating a Repository?**

Creating a **repository** on GitHub sets up a new project space where you can store and manage your code, track issues, and collaborate with others. 

**Steps:**

1. **Initiate Creation:**
   - Click on the **"New"** button to start creating a new repository.

2. **Fill Repository Details:**
   - **Repository Name:** Choose a unique and descriptive name for your project.
   - **Description:** (Optional) Provide a brief description of your project to inform others about its purpose.
   - **Privacy Settings:**
     - **Public:** Anyone can see this repository. Choose this if you want to share your project openly.
     - **Private:** Only you and people you explicitly share with can access the repository.
   - **Initialize Repository:**
     - **Add a README:** Initializes the repository with a README file, which is a good place to describe your project.
     - **.gitignore:** Specifies intentionally untracked files to ignore. Useful for excluding files like logs or temporary files.
     - **Choose a License:** Defines how others can use, modify, and distribute your project.

### 3. **Create Repository**

**Steps:**

- After filling in the necessary details, click **"Create repository"** to finalize the process.

*Your new repository is now ready for you to add files, collaborate, and manage your project.*

---

## Working with Repositories

Once you've created or cloned a repository, you can start managing and contributing to it. This section covers essential workflows for working with repositories.

### Cloning a Repository

**Why Clone a Repository?**

Cloning creates a local copy of a remote repository on your computer, allowing you to work on the project offline and push changes back to GitHub.

**Steps to Clone:**

1. **Copy Repository URL:**
   - Navigate to the repository on GitHub.
   - Click on the **"Code"** button and copy the repository URL (HTTPS or SSH).

2. **Run Clone Command:**
   ```bash
   git clone https://github.com/LonghornNeurotech/SoftwareDocumentation.git
   ```

*Clone this repository if you haven't already.*

### Making Changes

After cloning, you can start making changes to the project files. Here's a step-by-step guide.

#### 1. **Navigate to the Repository**

**What is Navigation in Git?**

Navigating refers to changing your current working directory to the repository's folder on your local machine. This ensures you're working within the correct project context.

**Command:**
```bash
cd your-repository
```

#### 2. **Create or Modify Files**

**What is File Modification?**

Creating or modifying files involves adding new content or changing existing content in your project. This is where you develop features, fix bugs, or update documentation.

**Steps:**

- NOTE: Get into the habit of branching before making edits
- Use your preferred text editor or Integrated Development Environment (IDE) to create new files or modify existing ones.
- For example, you can use editors like VS Code or Xcode. Most of the team will be using VSCode

**Why Use It:**

- Develop features, fix bugs, or update documentation by editing project files.

#### 3. **Check Status**

**Command:**
```bash
git status
```

**What It Does:**

- Displays the current state of the working directory and staging area.
- Shows which files have been modified, added, or deleted.

**Why Use It:**

- Helps you understand which changes are pending and what needs to be committed.

#### 4. **Stage Changes**

**Command:**
```bash
git add <file_name>
# Or add all changes
git add .
```

**What It Does:**

- `git add <file_name>` stages a specific file for the next commit.
- `git add .` stages all changes in the current directory and its subdirectories.

**Why Use It:**

- Prepares your changes to be saved in the repository's history.
- Allows you to control which changes are included in each commit for better organization.

#### 5. **Commit Changes**

**Command:**
```bash
git commit -m "Describe your changes"
```

**What It Does:**

- Records the staged changes in the repository with a descriptive message.

**Why Use It:**

- Saves a snapshot of your project at a specific point in time.
- Facilitates tracking and understanding the history of changes.

#### 6. **Push Changes to GitHub**

**Command:**
```bash
git push origin main
```

**What It Does:**

- Uploads your local commits to the remote repository on GitHub.
- Updates the `main` branch with your changes.

**Why Use It:**

- Shares your changes with collaborators.
- Ensures your work is backed up on GitHub.

---

## Branching and Merging

Branches allow you to work on different parts of a project simultaneously without interfering with the main codebase. This section explains how to create, switch, and merge branches.

### What is a Branch?

A **branch** is an independent line of development in Git. The default branch is usually named `main` or `master`. Creating a new branch allows you to work on features, fixes, or experiments without affecting the main code.

### Creating a Branch

**Command:**
```bash
git branch feature-branch
```

**What It Does:**

- Creates a new branch named `feature-branch`.

**Why Use It:**

- Isolates your work, making it easier to manage and review changes.
- Prevents the main branch from becoming unstable due to experimental changes.
- Since the main branch is almost always protected you wont be able to push to it.

**When to Use It:**

- When starting work on a new feature or bug fix.
- To experiment with new ideas without affecting the main codebase.

### Switching Branches

**Command:**
```bash
git checkout feature-branch
```

**What It Does:**

- Switches your working directory to the `feature-branch`.
- Updates the files in your directory to match the state of the `feature-branch`.

**Why Use It:**

- Allows you to work on the new branch independently.
- Ensures changes are made in the correct context.

**When to Use It:**

- Before starting work on a different feature or task.
- To review or modify code in another branch.

### Shortcut to Create and Switch

**Command:**
```bash
git checkout -b feature-branch
```

**What It Does:**

- Combines the creation of a new branch and switching to it in one step.
- Equivalent to running `git branch feature-branch` followed by `git checkout feature-branch`.

**Why Use It:**

- Saves time by performing two actions with a single command.
- Streamlines the workflow when starting new work.

### Merging Branches

**What is Merging?**

**Merging** is the process of integrating changes from one branch into another. Typically, this involves combining a feature branch back into the main branch.

**Steps to Merge:**

1. **Switch to Main Branch**

   **Command:**
   ```bash
   git checkout main
   ```

   **Why Use It:**

   - Prepares the main branch to receive changes from the feature branch.

2. **Merge Feature Branch**

   **Command:**
   ```bash
   git merge feature-branch
   ```

   **What It Does:**

   - Combines the changes from `feature-branch` into `main`.
   - Integrates the commit history of the feature branch.

3. **Resolve Conflicts**

   - If both branches have changes in the same parts of the same files, Git may encounter **merge conflicts**.
   - Git will prompt you to manually resolve these conflicts by editing the affected files.
   - After resolving, you need to stage the resolved files and complete the merge.

**Why Use It:**

- Incorporates completed features or fixes into the main codebase.
- Maintains a clean and organized project history.

*Regularly merging branches helps keep the project up-to-date and ensures that new features are integrated smoothly.*

---

## Collaborating on GitHub

Collaboration is at the heart of GitHub. This section covers how to contribute to others' projects and manage collaborative workflows.

### Forking a Repository

**What is Forking?**

**Forking** creates a personal copy of someone else's repository on your GitHub account. This allows you to experiment and make changes without affecting the original project.

**Why Fork a Repository?**

- Enables you to propose changes to someone else's project without needing direct access to the original repository.
- Allows you to customize a project for your own use while still benefiting from updates made to the original.
- You can also clone the repository and still collaborate, but forking gives you more freedom.

**Steps to Fork a Repository:**

1. **Navigate to the Repository:**
   - Go to the GitHub page of the repository you want to contribute to.

2. **Click on the "Fork" Button:**
   - Located in the top-right corner of the repository page.
   - This action creates a copy of the repository under your GitHub account.

### Making Pull Requests

**What is a Pull Request (PR)?**

A **Pull Request (PR)** is a way to propose changes to a repository. It allows the repository maintainers to review and discuss your changes before merging them.

**Why Use Pull Requests?**

- Facilitates code review and discussion.
- Ensures that changes meet the project's standards before integration.
- Provides a clear history of contributions and changes.

**Steps to Create a Pull Request:**

1. **Commit and Push Changes:**

   **Commands:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature-branch
   ```

   **What It Does:**

   - Stages all changes.
   - Commits the changes with a descriptive message.
   - Pushes the `feature-branch` to your forked repository on GitHub.

2. **Create the Pull Request:**

   - Navigate to your forked repository on GitHub.
   - Click on **"Compare & pull request"**.
   - Fill in the **title** and **description** fields with clear and concise information about your changes.
   - Click **"Create pull request"** to submit.