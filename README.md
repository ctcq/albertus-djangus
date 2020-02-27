# albertus-djangus
Internes Wiki des Albertus Magnus Kollegs

Prerequisites: Should be able to ignore errors.
sudo apt-get install libjpeg8 libjpeg-dev libpng12-0 libpng12-dev

###Setting Up Virtual Env
1. virtualenv -p python3 wikienv
2. source wikienv/bin/activate
3. pip install Pillow
4. pip install --upgrade Pillow
5. pip install wiki

###In desired directory with wikienv active:
1. git clone https://github.com/livengooddaily/albertus-djangus.git
2. cd albertus-djangus
3. source wikienv/bin/activate
4. cd dj_wiki
5. python3 manage.py runserver
