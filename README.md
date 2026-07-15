# Remove Background Project

Yeh ek Flask-based web application hai jo users ko images ka background remove karne ki suvidha deti hai.

---

### 🚀 Kaise Deploy Karein (Step-by-Step)

Agar aap beginner hain, toh niche diye gaye steps follow karke aap isse apne system par chala sakte hain:

#### 1. Requirements
Aapke system mein ye install hona chahiye:
* [Python 3.x](https://www.python.org/)
* [Git](https://git-scm.com/)

#### 2. Project Clone Karein
Apne terminal ya Command Prompt mein ye command run karein:
```bash
git clone [https://github.com/raunakkumar9529-lgtm/aws-remove-bg-project.git](https://github.com/raunakkumar9529-lgtm/aws-remove-bg-project.git)
cd aws-remove-bg-project
3. Virtual Environment Setup Karein
Apne project ke liye ek alag environment banayein:-
Windows:-
python -m venv venv
venv\Scripts\activate
Linux/Mac:-
python3 -m venv venv
source venv/bin/activate
4. Dependencies Install Karein
Saari zaroori libraries install karne ke liye ye command chalayein:-
pip install -r requirements.txt
5. Project Run Karein
Ab application start karne ke liye:-
python app.py
Aapka app ab http://127.0.0.1:5000 par live ho jayega!
🛠️ Tech Stack
Backend: Python, Flask
Cloud: AWS S3 (Storage)
Version Control: Git & GitHub
💡 Note
Agar aap AWS S3 features ka use karna chahte hain, toh apni AWS_ACCESS_KEY aur SECRET_KEY ko environment variables mein zaroor set karein.
