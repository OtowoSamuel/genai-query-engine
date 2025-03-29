from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from app.database import SessionLocal
from app.database import engine

class SalesData(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    category = Column(String)
    amount = Column(Float)
    region = Column(String)
    date = Column(String)  # Simplified (use DateTime if time permits)

# Create tables on startup
def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Insert mock data
    db.add_all([
        SalesData(product="Laptop", category="Tech", amount=1200, region="North", date="2023-11-01"),
        SalesData(product="Phone", category="Tech", amount=800, region="South", date="2023-11-05"),
        SalesData(product="Desk", category="Furniture", amount=300, region="East", date="2023-11-10"),
    ])
    db.commit()