from models import Dog
from sqlalchemy import create_engine

def create_table(base,engine):
        engine = create_engine('sqlite:///dogs.db')    
        base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return [dog for dog in session.query(Dog).all()]

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%'))
    for record in query:
        return record

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id.like(f'%{id}%'))
    for record in query:
        return record

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%'),Dog.breed == f'{breed}')
    for record in query:
        return record

def update_breed(session, dog, breed):
    query = session.query(Dog).filter(Dog.name.like(f'%{dog.name}%'))
    for record in query:
        record.breed = breed
    session.commit()