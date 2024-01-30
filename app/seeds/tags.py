from app.models import db, Tag


# Adds tags
def seed_tags():

    tag701 = Tag(
        name="beverage", recipeId=1)
    tag702 = Tag(
        name="vodka", recipeId=1)
    tag703 = Tag(
        name="ginger", recipeId=1)
    tag704 = Tag(
        name="alcohol", recipeId=1)

    tag705 = Tag(
        name="beverage", recipeId=2)
    tag706 = Tag(
        name="strawberry", recipeId=2)
    tag707 = Tag(
        name="lemonade", recipeId=2)
    tag708 = Tag(
        name="slushie", recipeId=2)
    tag709 = Tag(
        name="cake", recipeId=3)
    tag710 = Tag(
        name="chocolate", recipeId=3)
    tag711 = Tag(
        name="dessert", recipeId=3)

    tag712 = Tag(
        name="cake", recipeId=4)
    tag713 = Tag(
        name="dessert", recipeId=4)
    tag714 = Tag(
        name="appetizer", recipeId=5)
    tag715 = Tag(
        name="salad", recipeId=5)
    tag716 = Tag(
        name="avocado", recipeId=5)

    tag717 = Tag(
        name="appetizer", recipeId=6)
    tag718 = Tag(
        name="olives", recipeId=6)
    tag719 = Tag(
        name="cheese", recipeId=6)
    tag720 = Tag(
        name="entree", recipeId=7)
    tag721 = Tag(
        name="steak", recipeId=7)
    tag722 = Tag(
        name="beef", recipeId=7)
    tag723 = Tag(
        name="grill", recipeId=7)
    tag724 = Tag(
        name="entree", recipeId=8)
    tag725 = Tag(
        name="pasta", recipeId=8)
    tag726 = Tag(
        name="italian", recipeId=8)
    tag727 = Tag(
        name="sausage", recipeId=8)

    tag728 = Tag(
        name="snack", recipeId=9)
    tag729 = Tag(
        name="cookie", recipeId=9)

    tag730 = Tag(
        name="snack", recipeId=10)
    tag731 = Tag(
        name="cookie", recipeId=10)



    tag501 = Tag(
        name="appetizer", recipeId=11)
    tag501a = Tag(
        name="bruschetta", recipeId=11)
    tag501b = Tag(
        name="italian", recipeId=11)
    tag502 = Tag(
        name="entree", recipeId=12)
    tag502a = Tag(
        name="pork", recipeId=12)
    tag503 = Tag(
        name="dessert", recipeId=13)
    tag503a = Tag(
        name="chocolate", recipeId=13)
    tag504 = Tag(
        name="snack", recipeId=14)
    tag504a = Tag(
        name="spicy", recipeId=14)
    tag505 = Tag(
        name="beverage", recipeId=15)
    tag505a = Tag(
        name="gin", recipeId=15)
    tag505b = Tag(
        name="alcohol", recipeId=15)
    tag506 = Tag(
        name="appetizer", recipeId=16)
    tag506a = Tag(
        name="gyoza", recipeId=16)
    tag507 = Tag(
        name="entree", recipeId=17)
    tag507a = Tag(
        name="curry", recipeId=17)
    tag508 = Tag(
        name="dessert", recipeId=18)
    tag508a = Tag(
        name="ice cream", recipeId=18)

    tag901 = Tag(
        name="snack", recipeId=19)
    tag901a = Tag(
        name="nacho", recipeId=19)
    tag902 = Tag(
        name="beverage", recipeId=20)
    tag902a = Tag(
        name="slushie", recipeId=20)



    jamiTag1 = Tag(
        name="beverage", recipeId=21)
    jamiTag2 = Tag(
        name="wine", recipeId=21)
    jamiTag3 = Tag(
        name="beverage", recipeId=22)
    jamiTag4 = Tag(
        name="chocolate", recipeId=22)
    jamiTag5 = Tag(
        name="dessert", recipeId=23)
    jamiTag6 = Tag(
        name="ice cream", recipeId=23)
    jamiTag7 = Tag(
        name="dessert", recipeId=24)
    jamiTag8 = Tag(
        name="apple", recipeId=24)
    jamiTag9 = Tag(
        name="appetizer", recipeId=25)
    jamiTag10 = Tag(
        name="cheese", recipeId=25)
    jamiTag11 = Tag(
        name="appetizer", recipeId=26)
    jamiTag12 = Tag(
        name="eggs", recipeId=26)
    jamiTag13 = Tag(
        name="entree", recipeId=27)
    jamiTag14 = Tag(
        name="tuna", recipeId=27)
    jamiTag15 = Tag(
        name="entree", recipeId=28)
    jamiTag16 = Tag(
        name="burger", recipeId=29)
    jamiTag17 = Tag(
        name="snack", recipeId=29)
    jamiTag18 = Tag(
        name="tomato", recipeId=29)
    jamiTag19 = Tag(
        name="snack", recipeId=30)
    jamiTag20 = Tag(
        name="plastic", recipeId=30)



    tag903 = Tag(
        name="appetizer", recipeId=31)
    tag904 = Tag(
        name="entree", recipeId=32)
    tag905 = Tag(
        name="dessert", recipeId=33)
    tag905a = Tag(
        name="ice cream", recipeId=33)
    tag906 = Tag(
        name="entree", recipeId=34)
    tag906a = Tag(
        name="beef", recipeId=34)





    db.session.add(tag701)
    db.session.add(tag702)
    db.session.add(tag703)
    db.session.add(tag704)
    db.session.add(tag705)
    db.session.add(tag706)
    db.session.add(tag707)
    db.session.add(tag708)
    db.session.add(tag709)
    db.session.add(tag710)
    db.session.add(tag711)
    db.session.add(tag712)
    db.session.add(tag713)
    db.session.add(tag714)
    db.session.add(tag715)
    db.session.add(tag716)
    db.session.add(tag717)
    db.session.add(tag718)
    db.session.add(tag719)
    db.session.add(tag720)
    db.session.add(tag721)
    db.session.add(tag722)
    db.session.add(tag723)
    db.session.add(tag724)
    db.session.add(tag725)
    db.session.add(tag726)
    db.session.add(tag727)
    db.session.add(tag728)
    db.session.add(tag729)
    db.session.add(tag730)
    db.session.add(tag731)



    db.session.add(tag501)
    db.session.add(tag502)
    db.session.add(tag503)
    db.session.add(tag504)
    db.session.add(tag505)
    db.session.add(tag506)
    db.session.add(tag507)
    db.session.add(tag508)
    db.session.add(tag901)
    db.session.add(tag902)
    db.session.add(tag501a)
    db.session.add(tag502a)
    db.session.add(tag503a)
    db.session.add(tag504a)
    db.session.add(tag505a)
    db.session.add(tag506a)
    db.session.add(tag507a)
    db.session.add(tag508a)
    db.session.add(tag901a)
    db.session.add(tag902a)
    db.session.add(tag501b)
    db.session.add(tag505b)



    db.session.add(jamiTag1)
    db.session.add(jamiTag2)
    db.session.add(jamiTag3)
    db.session.add(jamiTag4)
    db.session.add(jamiTag5)
    db.session.add(jamiTag6)
    db.session.add(jamiTag7)
    db.session.add(jamiTag8)
    db.session.add(jamiTag9)
    db.session.add(jamiTag10)
    db.session.add(jamiTag11)
    db.session.add(jamiTag12)
    db.session.add(jamiTag13)
    db.session.add(jamiTag14)
    db.session.add(jamiTag15)
    db.session.add(jamiTag16)
    db.session.add(jamiTag17)
    db.session.add(jamiTag18)
    db.session.add(jamiTag19)
    db.session.add(jamiTag20)


    db.session.add(tag903)
    db.session.add(tag904)
    db.session.add(tag905)
    db.session.add(tag905a)
    db.session.add(tag906)
    db.session.add(tag906a)



    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()
