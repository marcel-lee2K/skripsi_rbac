untuk ke komputer lain;
git clone https://github.com/username/skripsi_rbac.git
cd skripsi_rbac
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py runserver

kalau mau ngepush file lagi yg sudah di update;
cd C:\Users\acer\PycharmProjects\PythonProject3\myproject
git add .
git commit -m "Deskripsi perubahan kamu"
git push

untuk cek file apa saja yang berubah;
git status
Commit sesering mungkin dengan pesan jelas, misalnya “Add requirements.txt”, “Update permission view”, dll.
