import os
from restaurant.model import db
from restaurant.model import Restaurant
from restaurant import pjdir

# Remove exsisting db
try: 
    os.remove(os.path.join(pjdir, 'data_restaurant.sqlite'))
except:
    print('No db to remove')

# Insert all restaurants into db 
db.create_all()

place_ids = []
with open(os.path.join(pjdir, 'place_id.txt'), 'r') as r_file:
    for line in r_file:
        line = line.strip()
        place_ids.append(line)

for id in place_ids:
    r = Restaurant(id)
    db.session.add(r)
db.session.commit()

# r_all = Restaurant.query.all()
# for r in r_all:
#     print(r) 
