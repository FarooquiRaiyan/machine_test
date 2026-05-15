from fastapi import FastAPI, Depends, HTTPException
from db import Base, engine, Session, get_db
from schema import ProductCreate, CategoryCreate, ProductUpdate, CategoryUpdate, ProductwithCategory
from models import Products, Category
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {
        "message": "FastAPI is working"
    }
    
@app.get('/api/products')
def get_all_products(page:int = 1, limit : int=10, db:Session= Depends(get_db)):
    skip = (page - 1) * limit
    products = db.query(Products).offset(skip).limit(limit).all()
    print("Products insides get all products", products)
    
    total = db.query(Products).count()
    
    return {
        "page":page,
        "limit":limit,
        "total":total,
        "products":products
    }    



@app.get('/api/products/{id}', response_model=ProductwithCategory)
def get_single_products(id:int, db : Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Products not Found")
    return product



@app.post('/api/products')
def add_products(product:ProductCreate, db :Session= Depends(get_db)):
    db_product = Products(name=product.name, category_id = product.category_id)
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product





@app.put('/api/products/{id}')
def product_update(id:int, product:ProductUpdate, db: Session= Depends(get_db)):
    db_product = db.query(Products).filter(Products.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="No Product Found to Update")
    category = db.query(Category).filter(Category.id == product.category_id).first()
    
    if not category:
        raise HTTPException(status_code=404,detail="Category not Found")
    
    db_product.name = product.name
    db_product.category_id = product.category_id
    db.commit()
    db.refresh(db_product)
    return db_product



@app.delete('/api/products/{id}')
def update_product(id: int, db:Session = Depends(get_db)):
    db_product = db.query(Products).filter(Products.id == id).first()
    
    if not db_product:
        raise HTTPException(status_code=404, detail="Can't find the Product to delete with this id ")
    
    db.delete(db_product)
    db.commit()
    return {"message":"Product Deleted Successfully"}
    
   
   
    


@app.get('/api/categories')
def get_category(page:int = 1, limit : int=10,db:Session = Depends(get_db)):
    skip = (page -1 )* limit
    categories = db.query(Category).offset(skip).limit(limit).all()
    total = db.query(Category).count()
    return {
        "page":page, 
        "limit":limit, 
        "total":total, 
        "categories":categories
    }


@app.get('/api/categories/{id}')
def get_single_category(id:int,db:Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Not found the Category by this id ")
    
    return category





@app.post('/api/categories')
def add_category(category:CategoryCreate, db :Session= Depends(get_db)):
    db_category= Category(id=category.id, category_name = category.category_name)
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category




@app.put('/api/categories/{id}')
def update_category(id:int,category :CategoryUpdate, db:Session= Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == id).first()
    
    if not db_category:
        raise HTTPException(status_code=404, detail="No id found gor Update")
    
    # db_category.id = category.id
    db_category.category_name = category.category_name
    db.commit()
    db.refresh(db_category)
    return db_category


@app.delete('/api/categories/{id}')
def delete_category(id:int, db:Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == id).first()
    
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(db_category)
    db.commit()
    return {"message":"Cateory Deleted Successfully"}
    
    
    
  



