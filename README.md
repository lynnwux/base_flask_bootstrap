# Repo is a base foundation for a Flask/Bootstrap app

## Includes:
- package.json with: 
    - scripts:
        - script for creating venv
        - script for installing python dependecies from requirements.txt
        - script for running flask app within venv
    - dependencies:
        - concurrently
- static and templates directories with starter files
    - blank styles.css
    - blank scripts.js
    - base templates
        - layout.html
        - home.html
- skeleton flask app.py
- base .gitignore file
- this readme

to view this readme as markdown preview in vscode:  
```ctrl+shift+v```

## Repo structure
```plaintext
BASE_FLASK_BOOTSTRAP/
├── app.py                              # Main Flask application file
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore file for excluding files/directories
├── README.md                           # Project documentation
├── package.json                        # NPM config file with scripts
├── package-lock.json                   # NPM config file with additional dependancy info
├── static/                             # Static dir (CSS, JavaScript, images)
│   ├── css/
│   │   └── bootstrap.min.css           # Boostrap v5.3 CSS
│   │   └── styles.css                  # Custom CSS
│   ├── js/
│   │   └── bootstrap.bundle.min.js     # Bootstrap v5.3 JavaScript bundle
│   │   └── scripts.js                  # Custom JavaScript
│   └── images/                         # Image dir
└── templates/                          # HTML templates for Flask
    ├── layout.html                     # Base layout template
    └── home.html                       # Home page template
```

## To install from repo

1. **Clone to local machine from github:**  
(in parent dir where other project dirs are located)  
``` git clone <repository-url> <new-directory-name> ```  
e.g.:  
``` git clone https://github.com/jreffsin/base_flask_bootstrap.git sample_new_project_name ```

2. **Install node dependecies:**  
(in project dir)  
``` npm install ```

3. **Setup python virtual env and install python dependecies:**  
(in project dir)  
``` npm run install-python-deps ```

## To run Flask app 
1. Runs app within venv without needing to first activate venv:  
(in project dir)  
``` npm run dev ```

## To link and push new local instance of repo to new giithub repo (after clone)

1. **Remove link to original remote**  
(in project dir)  
``` git remote remove origin ```

2. **Create new blank repo on github (same name as new local instance)**  
copy the new repo URL

3. **Link local repo to new github repo**  
``` git remote add origin <new repo url> ```  

4. **Push to new remote repo**  
``` git push origin main ```



