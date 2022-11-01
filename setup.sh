sudo apt update
sudo apt install python-is-python3
python -m venv venv
source venv/bin/activate || source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
