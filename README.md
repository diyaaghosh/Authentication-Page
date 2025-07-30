#  Authentication Page

A **simple login-sign-up authentication system** built using **Flask (Python backend)** with a basic **HTML/CSS frontend**. This project was created to understand backend fundamentals like routing, sessions, and form handling.

---

##  Features

- User **Sign Up** and **Login** functionality
- Basic **form validation**
- **Session management** using Flask
- Clean and responsive **UI**
- Organized folder structure:
  - `static/` – CSS or image files
  - `templates/` – HTML files
  - `instance/` – For user data (if used)
  
---

##  Tech Stack

- **Frontend**: HTML, CSS  
- **Backend**: Python, Flask  
- **Other tools**: Jinja2 templating, Flask session, GitHub, Render

---

##  How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/diyaaghosh/Authentication-Page.git
cd Authentication-Page
```
# 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```
# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Run the app
```bash
python app.py
```
 Live Deployment
 https://authentication-page-bsyb.onrender.com/

 Folder Structure
```
Authentication-Page/
│
├── static/          # CSS or static assets
├── templates/       # HTML templates
├── instance/        # User-specific or database files
├── app.py           # Main application file
├── requirements.txt # Python dependencies
├── procfile         # For deployment on platforms like Render
└── README.md
```
 GitHub

 License
This project is licensed under the MIT License.
