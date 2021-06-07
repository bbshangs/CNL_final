import os
from app import app
from app.restaurant import pjdir
from app.restaurant.model import db
from app.restaurant.model import Restaurant

# Insert all restaurants into db 
place_ids = []
with open(os.path.join(pjdir, 'place_id.txt'), 'r') as r_file:
    for line in r_file:
        line = line.strip()
        place_ids.append(line)

db.create_all()
for id in place_ids:
    r = Restaurant(id)
    db.session.add(r)
db.session.commit()