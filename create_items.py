from market import app, db
from market.models import Item

with app.app_context():

    items = [
        Item(
            name="Veg Biryani",
            image="veg_biryani.jpg",
            description="Delicious Veg Biryani"
        ),
        Item(
            name="Paneer Curry",
            image="paneer_curry.jpg",
            description="Paneer Curry with spices"
        ),
        Item(
            name="Chicken Biryani",
            image="chicken_biryani.jpg",
            description="Special Chicken Biryani"
        )
    ]

    db.session.add_all(items)
    db.session.commit()

print("Items added successfully!")