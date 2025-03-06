[![Feature Validation](https://github.com/sr-hawk/SP25_DS5111_etk3pu/actions/workflows/validations.yml/badge.svg)](https://github.com/sr-hawk/SP25_DS5111_etk3pu/actions/workflows/validations.yml)

# Data Collection Pipeline Project

This repository sets up a data collection pipeline using a headless Chrome browser and a Python virtual environment. The instructions below will allow anyone (e.g., a new Data Scientist) to quickly set up a new VM with all the required tools.

---
**1. System Preparation:**

* **Update Package Lists:**
    ```bash
    sudo apt update
    ```
    This ensures you have the latest package information from your repositories. It's crucial for installing dependencies correctly.

* **Git Credentials:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```
    Configuring your Git credentials allows you to properly attribute your commits. This identifies you as the author of changes.

* **SSH Key Generation:**
    ```bash
    ssh-keygen -t rsa -b 4096 -C "you@example.com"
    ```
    Generating an SSH key provides secure authentication for Git operations. Add the public key to your GitHub account for seamless repository access.

**2. Repository Setup:**

* **Clone Repository:**
    ```bash
    git clone git@github.com:yourusername/your-repo.git
    cd your-repo
    ```
    This downloads the repository to your local machine. Navigate into the cloned directory to proceed with setup.

* **Initial Setup Script:**
    ```bash
    sudo bash init.sh
    ```
    This script automates initial installations and configuration. It sets up essential components for the project's environment.

* **Install Google Chrome:**
    ```bash
    cd scripts
    sudo bash install_chrome.sh
    ```
    This installs Google Chrome, which may be required for web-based functionalities within the project. It uses a provided script for streamlined installation.

* **Install Dependencies:**
    ```bash
    make update
    ```
    The `make update` command uses `pip` to install packages listed in `requirements.txt`. This ensures all necessary Python libraries are installed.

* **Create Sample Data Directory:**
    ```bash
    make sample_data
    ```
    This creates the `sample_data` directory, which will hold example datasets. It provides a structured location for test data.

**3. Testing:**

* **Generate Sample Data:**
    ```bash
    make ygainers.csv
    ```
    This command generates a sample `ygainers.csv` file within the `sample_data` directory. It validates data processing and output.

* **Verify Directory Structure:**
    ```bash
    tree SP25_DS5111_etk3pu -I env
    ```
    This command displays the directory structure, excluding the `env` virtual environment. It confirms that files and directories are organized as expected, including the created ygainers.csv.

   If everything is set up correctly your tree should like this with ygainers.csv downloaded to the sample_data folder
```
# we're missing the triple ticks to make the tree readable
SP25_DS5111_etk3pu
├── README.md
├── init.sh
├── makefile
├── requirements.txt
├── sample_data
│   ├── ygainers.csv
│   └── ygainers.html
└── scripts
    └── install_chrome.sh
```
**Lab 3**

* **Create new branch:**
    ```bash
    git checkout -b LAB-03_csv_normalizer
    git push --set-upstream origin LAB-03_csv_normalizer
    ```
    This creates and pushes a new branch specifically for the CSV normalizer feature.

**2. Create code to normalize csv sheets:**

* **Set up directory and file for your code:**
    ```bash
    mkdir bin
    touch bin/normalize_csv.py
    ```
    This creates the directory and file for your normalization script.
* **Feature description and directions for writing your first draft:**
    Write a Python script in `bin/normalize_csv.py` to normalize CSV files as per the lab requirements. Ensure clear code, input/output assertions, descriptive variable names, and logging.

**3. Pushing your code and submitting pull request:**

* **Push Changes and Submit Pull Request:**
    ```bash
    git add bin/normalize_csv.py
    git commit -m "Implement CSV normalization script"
    git push
    ```
    Push your code to the remote branch and create a pull request on GitHub with a descriptive title and message.

**Lab 4**
**Add Pylint to `requirements.txt`:**
    Ensure `pylint` is listed in your `requirements.txt` file.
* **Update Dependencies:**
    ```bash
    make update
    ```
    This installs Pylint into your virtual environment.

**2. Setting up Pylint Config:**

* **Generate `pylintrc`:**
    ```bash
    pylint --generate-rcfile >> pylintrc
    ```
    This creates a configuration file for Pylint.
* **Verify `pylintrc` Usage:**
    Modify the `indent-string` in `pylintrc` to confirm Pylint is using the configuration file. Then, revert the change.
* **Add `lint` job to Makefile:**
    ```makefile
    lint:
        source env/bin/activate && pylint bin/normalize_csv.py
    ```
    This creates a Makefile target to run Pylint.

**3. Getting the Code Up to Standard:**

* **Run `make lint`:**
    Execute the lint job and review the Pylint output.
* **Refactor Code:**
    Address the Pylint errors and warnings to improve the code's score.

**4. Setting up Pytest:**

* **Add Pytest to `requirements.txt`:**
    Ensure `pytest` is listed in `requirements.txt` and run `make update`.
* **Create `tests` directory and test file:**
    ```bash
    mkdir tests
    touch tests/test_normalize_csv.py
    ```
* **Add test file setup:**
    In `tests/test_normalize_csv.py`, add:
    ```python
    import sys
    sys.path.append('.')
    import bin.normalize_csv
    ```
* **Write Pytest functions:**
    Create test functions that begin with `test_` and include assertions.
* **Add `test` job to Makefile:**
    ```makefile
    test: lint
        source env/bin/activate && pytest -vv tests
    ```
    This creates a Makefile target to run Pytest, including the `lint` target.

**5. The Goal: Using Linter, Tests, and Git in Parallel:**

* **Iterate and Refactor:**
    Run `make test`, address issues, and repeat until tests pass and the Pylint score is 10/10.
* **Use Git Frequently:**
    Commit changes regularly, especially when reaching a milestone.
* **Documentation:**
    Reference Pylint and Pytest documentation to understand feedback and features.

**Lab 5**
**Create Workflow Directory:**
    Create the `.github/workflows` directory.
* **Create Workflow File:**
    Create a `validations.yml` file within the workflow directory.
* **Commit and Push Changes:**
    Commit and push the workflow file to your repository.
* **Verify Workflow Execution:**
    Check the "Actions" tab on your GitHub repository to confirm the workflow is running.

* **Add Badge to README:**
    Add a workflow status badge to your `README.md`.
* **Update `requirements.txt` with Package Versions:**
    Add the precise versions of your Python packages to your `requirements.txt` file.
* **Add OS Test:**
    Implement a test that verifies the operating system is Linux.
* **Add Python Version Test:**
    Implement a test that verifies the Python version is either 3.10 or 3.11.
* **Add Python 3.11 to GitHub Actions Workflow:**
    Modify your `validations.yml` file to include Python 3.11 in the test matrix.

```
wasn't sure how to add this, so I put the comment here... nice that you added a separate directory for
sample_data, keep things organized and declutter the root directory. Makes it easier to get a sense
of what is in the repo
```
