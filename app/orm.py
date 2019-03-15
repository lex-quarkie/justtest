from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    author = Column(String(255))
    year = Column(Integer)
    datetime_added = Column(DateTime, nullable=False,
                            default=datetime.utcnow)
    pages_count = Column(Integer)

    def dump(self):
        obj_dict = dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])

        inner_dict = {"type": "books",
                      "id": obj_dict.pop('id'),
                      "attributes": obj_dict, }
        return {"data": inner_dict}


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
