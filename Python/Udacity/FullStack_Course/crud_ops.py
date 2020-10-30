from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base,Restaurant,MenuItem



engine = create_engine('sqlite:///restaurantmenun.db')
Base.metadata.bind = engine
DBSession =  sessionmaker(bind=engine)
session =  DBSession()

pot_b = Restaurant(name = "Pot Biriyani")
session.add(pot_b)
session.commit()


pot_b_menu = MenuItem(name="Chicken Biriyani",price = '200',restaurant = pot_b)
session.add(pot_b_menu)
session.commit()

cb_query = session.query(MenuItem).filter_by(name="Chicken Biriyani").first()
cb_query.price = 175

up_query = session.query(MenuItem).filter_by(name="Chicken Biriyani").first()
print up_query.price