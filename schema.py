from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category_id : int
    

class ProductUpdate(BaseModel):
    name: str
    category_id: int


# class ProductwithCategory(BaseModel):
#     id : int
#     name: str
#     category_id : int
#     category_name:CategoryCreate


class CategoryCreate(BaseModel):
    id : int
    category_name: str
    
    class Config:
        from_attributes = True

    
    
class CategoryUpdate(BaseModel):
    id : int
    category_name: str
    
    class Config:
        from_attributes = True
    

class ProductwithCategory(BaseModel):
    id : int
    name: str
    category_id : int
    category : CategoryCreate
    
    class Config:
        from_attributes = True