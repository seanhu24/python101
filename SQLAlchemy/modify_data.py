from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Artist, Album

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a session
Session=sessionmaker(bind=engine)
session=Session()

# query
res=session.query(Artist).filter(Artist.name=="Kutless").first()
print(res.name)

# change the name
res.name="Beach Boys"
session.commit()

# editing album data
artist, album=session.query(Artist,Album).filter(Artist.id==Album.artist_id).filter(Album.title=="Thrive").first()
album.title="Step Up to the Microphone"
session.commit()