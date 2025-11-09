from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    position = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    chats = relationship("ChatHistory", back_populates="employee")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    query = Column(Text, nullable=False)
    response = Column(Text)
    employee = relationship("Employee", back_populates="chats")