from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey

Base = declarative_base()
metadata1 = Base.metadata

Log_Base = declarative_base()
metadata2 = Log_Base.metadata

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    age = Column(Integer)
    note = Column(String(200))
    create_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    

class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    street = Column(String(90))
    city = Column(String(90))
    state = Column(String(2))
    zip = Column(Integer)
    
    def __repr__(self):
        return f"id: {self.id}, \
                 name: {self.name}, \
                 street: {self.state}, \
                 city: {self.city}, \
                 state: {self.state}, \
                 zip: {self.zip}"
    
    
class Classes(Log_Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    class_number = Column(Integer)
    class_name = Column(String(60))
    class_description = Column(String(200))
    class_credits = Column(Integer)
    
    def __repr__(self):
        return f"id: {self.id}, number: {self.class_number}, name: {self.class_name}"

