# Data Collection Pipeline Project

This repository sets up a data collection pipeline using a headless Chrome browser and a Python virtual environment. The instructions below will allow anyone (e.g., a new Data Scientist) to quickly set up a new VM with all the required tools.

---

## 1. Generic VM Bootstrap

### 1.1 Pre-Setup on a New VM

Before cloning this repository, on your new VM you should:

1. **Manually update package lists:**  
	sudo apt update

2. **Add git credentials**
   Set up your Git credentials (name and email) using:
	git config --global user.name "Your Name" 
	git config --global user.email "you@example.com"

3. **Create SSH key and add to github**
   Create an SSH key:
	ssh-keygen -t rsa -b 4096 -C "you@example.com"
   Make sure to add the key to your github account

4. **Clone github repository**
	git clone git@github.com:yourusername/your-repo.git
	cd your-repo

5. **Run init.sh for initial installs**
	sudo bash init.sh

6. **Install Google Chrome**
	cd scripts
	sudo bash install_chrome.sh

7. **requirements.txt and make**
   Running the make file will install all needed packages from requirements.txt
	make update

8. **Create sample_data folder**
	make sample_data

8. **Test**
	make ygainers.csv
	tree SP25_DS5111_etk3pu -I env
   If everything is set up correctly your tree should like this with ygainers.csv downloaded to the sample_data folder

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

