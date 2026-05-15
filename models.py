from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base



class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key = True, index = True)
    category_name = Column(String(255))
    products = relationship("Products", back_populates= "category")
    
    
class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String , index = True)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products")