from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True)
    email = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    def __repr__(self):
        return f"\n<User " \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}, " \
            + f"last_name={self.last_name}, " \
            + f"username={self.username}, " \
            + f"email={self.email}, " \
            + f"created_at={self.created_at}, " \
            + f"updated_at={self.updated_at}" \
            + " >"
            
            
class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String, default="Unknown")
    
    def __repr__(self):
        return f"\n<Meal "\
            + f"id={self.id}," \
            + f"name={self.name}," \
            + " >"  