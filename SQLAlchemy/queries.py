from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Artist, Album

engine=create_engine("sqlite:///mymusic.db", echo=True)

# create a session
Session=sessionmaker(bind=engine)
session=Session()

# select * from ...
res=session.query(Artist).all()
for artist in res:
    print(artist.name)

# select the first 1 row
res=session.query(Artist).filter(Artist.name=='Newsboys').first()
print(res.name)

# sort
res=session.query(Album).order_by(Album.title).all()
for album in res:
    print(album.title)

# join query
qry=session.query(Artist, Album)
qry=qry.filter(Artist.id==Album.artist_id)
artist,album=qry.filter(Album.title=='Step Up to the Microphone').first()
print(artist.name,":",album.title)

# query with like
res=session.query(Album).filter(Album.publisher.like("S%a%")).all()
for item in res:
    print(item.publisher)