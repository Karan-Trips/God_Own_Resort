<<<<<<< HEAD
#!/bin/bash
set -e
echo "BUILD START"
# Install dependencies
python3.9 -m pip install -r requirements.txt
# Collect static files
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
=======
echo " BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo " BUILD END" 
>>>>>>> 7eb7d782d019cdb7e6405c7f335c44ab972d7a8e
