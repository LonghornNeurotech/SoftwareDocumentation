# Getting Started with Conda: Installation and First Environment Setup

This guide will walk through the process of downloading and installing Conda, and creating a Conda environment on both Windows and macOS systems.

## Table of Contents

- [What is Conda?](#what-is-conda?)
- [Download and Install Conda](#download-and-install-conda)
  - [Windows](#windows)
  - [macOS](#macos)
- [Create Your First Conda Environment](#create-your-first-conda-environment)
- [Additional Resources](#additional-resources)

---
## What is Conda?

Conda is an open-source package management and environment management system that allows users to quickly install, update, and manage software packages and dependencies. It is very useful for creating isolated environments that are reproducible on any operating system.

## Download and Install Conda

We will use **Miniconda**, a minimal installer for Conda, which includes Conda and its dependencies.

### Windows

#### 1. Download Miniconda Installer

- Visit the [Miniconda Windows installers](https://docs.conda.io/en/latest/miniconda.html#windows-installers).
- Choose the **64-bit** or **32-bit** installer based on your system.
- Click on the **"Miniconda3 Windows 64-bit/32-bit installer"** link to download.

#### 2. Run the Installer

- Locate the downloaded `.exe` file and double-click to run it.
- Follow the on-screen instructions.

#### 3. Add Conda to PATH Variable

While it's not generally recommended, adding Conda to your PATH variable simplifies command-line usage, and issues are rare.

- **During Installation**:
  - In the **"Advanced Installation Options"** screen, check the box that says:
    - **"Add Miniconda3 to PATH environment variable"**
- Continue with the installation and complete it.

#### 4. Verify the Installation

- Open the **Command Prompt**:
  - Press `Win + R`, type `cmd`, and press `Enter`.
- Type the following command and press `Enter`:

  ```bash
  conda --version
  ```

- You should see the Conda version displayed.

### macOS

#### 1. Download Miniconda Installer

- Visit the [Miniconda macOS installers](https://docs.conda.io/en/latest/miniconda.html#macosx-installers).
- Choose the **64-bit (bash installer)**.
- Click on the **"Miniconda3 macOS 64-bit pkg installer"** link to download.
- if you have an M1 chip or better make sure to use the M1 pkg installer

#### 2. Run the Installer

- Locate the downloaded `.pkg` file and double-click to run it.
- Follow the on-screen instructions to complete the installation.

#### 3. Initialize Conda

- Open the **Terminal** application.
- Initialize Conda by running:

  ```bash
  conda init
  ```

- Restart your terminal for the changes to take effect.

#### 4. Verify the Installation

- In the terminal, type:

  ```bash
  conda --version
  ```

- You should see the Conda version displayed.

---

## Create Your First Conda Environment

Now that Conda is installed, let's create your first environment.

### Steps (Same for Windows and macOS)

1. **Open Command Prompt (Windows) or Terminal (macOS)**.

2. **Update Conda (Optional but Recommended)**:

   ```bash
   conda update -n base -c defaults conda
   ```

3. **Create a New Environment**:

   Replace `myenv` with the name you want for your environment.

   ```bash
   conda create -n myenv python=3.9
   ```

   - This command creates a new environment named `myenv` with Python 3.9 installed.
   - Through testing we have found python 3.9 to be the most stable version

4. **Activate the Environment**:

   ```bash
   conda activate myenv
   ```

   - Your command prompt should now reflect the active environment.

5. **Install Packages (Example)**:

   ```bash
   conda install numpy pandas
   ```

6. **Deactivate the Environment**:

   ```bash
   conda deactivate
   ```

---

## Additional Resources

- **Conda Documentation**: [https://docs.conda.io](https://docs.conda.io)
- **Managing Environments**: [Conda Environment Management](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

---

If you run into any issues feel free to reach out to Nathan or your team lead. If issues are resolved, please edit this documentation accordingly.
