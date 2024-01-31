from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text


# Adds recipes
def seed_recipes():

    # Meitong

    recipe701 = Recipe(
        title='Tom Yum Vodka', description="""I think by now, Thailand's famous Tom Yum Goong (hot and sour prawn soup) is a household name around the world. But this is more than just a soup. Tom yum's hot, spicy, sour, packed-with-herbs flavour is used in everything from potato chips to instant noodles.

So I had a stroke of genius.

Why not use this flavour to turn plain old vodka into a masterpiece?

The delicious, aromatic herbs give this drink a unique scent that you just can't find anywhere else, and chili and garlic a little some fire.

The best part?

It's so easy to make, you can have this recipe done in just 5 minutes today. And tomorrow, you can reap the reward of a delicious, sophisticated little beverage.""", authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/FZ2/8QSC/KTPSYXDD/FZ28QSCKTPSYXDD.jpg?auto=webp&frame=1&width=552&height=1024&fit=bounds&md=f596ae9807c182a3b39b52ae88ce2df0')

    recipe702 = Recipe(
        title='Frozen Strawberry Lemonade Slushies',
        description="""This has been a very hot summer so far. For this Water Instructable, I decided I wanted to make a refreshing drink made with 4 cups of water and some of my favorite ingredients. Nothing tastes better than to sit back with an icy cold drink to cool you. And fresh lemonade traditionally can be such a special summertime treat! To make it even better, I decided to freeze the water to make frozen lemonade slushies. Then I thought to add some strawberries and how about some mint from my garden too? I had my idea of the perfect summer frozen drink! It was so very tasty and definitely hit the spot that I wanted to hit!! You can make it too by following these steps. """,
        authorId=2,
        ingredientPhoto='https://content.instructables.com/ORIG/FE3/5PBQ/KR4X9504/FE35PBQKR4X9504.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=62676314745e3eafcf31d0ca8b292949')

    recipe703 = Recipe(
        title='Halloween Themed Chocoflan',
        description="""Warning!!!!!!!

The following recipe contains eggs and cocoa, if you are allergic to these please DO NOT do this recipe. If you do not like chocolate cake you can always replace it with any other type of cake.

Also, this recipe has medium to hard difficulty so please try at your own risk""",
        authorId=3,
        ingredientPhoto='https://content.instructables.com/ORIG/F5G/AEY8/GYLZWZN3/F5GAEY8GYLZWZN3.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=f52c991a7c3b58d95dccd3b4549217cb')

    recipe704 = Recipe(
        title="Spirited Away Cake: No Face's Feast", description="""Hello!

If you've ever watched Hayao Miyazaki's award winning film "Spirited Away,' you might recall a certain food scene. In it, No-Face, a spirit, ravenously consumes pounds of delicious food in front of his hosts. Miyazaki is such a master with animated food I felt compelled to make a cake honoring such a fun scene.

Be warned though, this is not an easy cake! It took me wayyy to long to finish inbetween work and school. If anyone wants to re-create this, I have suggestions on each step to make the process a little easier. :)

Enough rambling, onto the cake!

(no-face drawing by Valentina Hramov)""", authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/F4Z/QCJZ/KSUD6CY1/F4ZQCJZKSUD6CY1.png?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=5c5f098b41d393dd081793ba7c1d3b6f')

    recipe705 = Recipe(
        title='RECIPE |MANDARIN AVOCADO SALAD', description="""Spring is finally here! With 15 degree weather, I am forcing myself to believe that spring is here to stay even after that random snow storm we had last week. With Spring, comes warmer weather and cooler dishes like this Mandarin Avocado Salad. I've been trying to get back into my salad routine to cure my skin issues. After all, you are what you eat.

In the past year, my skin has rewound back to my teenage years when acne haunted me. I had awful cystic acne where I would get nasty volcano-like zits on my forehead, nose or chin. I was lucky in the fact that I didn't get a zillion red blemishes all over my face but life decided to be fair by giving me exactly that all over forehead along with little white bumps. At first I thought I wasn't cleaning off my makeup as well as I should, even though I would triple cleanse! (Yes triple cleanse with 3 different types of cleanser. Don't worry I've reduced that down to 2 cleansers now so I don't dry out my skin). Then I thought maybe there is too much oil in my diet but that wasn't it either. I swapped up my skin regime multiple times to figure out what was going wrong. I searched high and low for the answer and I finally figured it out. I found this YouTuber who explained that it was an fungal infection underneath my skin, hence the numerous white bumps that would turn into red little blemishes. The cause for the infection was an influx of yeast and sugars from white carbohydrates in my diet. It makes sense as I've been eating a lot more white carbs to replace my meat intake. Now don't get me wrong, not everyone will experience these same symptoms because every one is different. So please don't be convinced that you need to lower your carb intake and increase your meat intake. But I really needed to force myself to eat more whole grains not just white breads/pastas which is common sense. I am not just a fan of the taste in whole grains? Long story, short: I've returned back to eating more greens, fruits, and replacing white carbs with whole grain ones. So far, so good. My skin is clearing day by day!

So if you're also experiencing some skin issues, first think about what you eat. Do some research and try to understand what the cause is. I would say that 80% of our skin issues are based on our diet. Then to assist with the healing, look into active oils or serums that will speed up the healing process. But just remember you can apply all the serums in the world but if you eat garbage, it will still reflect on your skin. As they say, "Beauty comes from within."
Anyway I hope you guys give this salad a shot. It's one of my favourites and I used to eat it daily before my wedding and I remember having glowing clear skin! It's filled with Vitamin C, Folate, and antioxidants which fight the skin-villains. Easy, quick to make and wonderful for the new Spring season. In this recipe, I'm using the Super Greens salad box by Organic Girl which you can find at major Canadian grocers. If you do end up making this recipe, take a picture of it, tag @christieathome on Instagram and it may be featured. If you're not on Instagram please share this recipe with your family and friends!

Disclaimer: I am not sponsored by the companies listed in this post.""", authorId=4, ingredientPhoto='https://content.instructables.com/ORIG/FCA/QAOF/J1QP0HWE/FCAQAOFJ1QP0HWE.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=ccb44c5e51c5e090a32132fff232b14b')

    recipe706 = Recipe(
        title='Parmesan Baked Olives - Easy Appetizer!',
        description=""" a crunchy shell of parmesan cheese filled with olives - doesn't that sound delicious?

- it certainly is!

Spoil your guests with this impressive, but easy to make fingerfood.

comes great with a glass of red wine or just as a snack for itself.

Only a few ingredients, about 30 minutes of your time

and your taste buds will be thrilled! - that's a promise!""",
        authorId=5,
        ingredientPhoto='https://content.instructables.com/ORIG/F5Z/EL5C/KNRGTACH/F5ZEL5CKNRGTACH.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=4812535626cf3fcdd6cd4e099bd9d907')
    recipe707 = Recipe(
        title='Grilled Ribeye With Mint Vinaigrette',
        description="""In this recipe you will be making a very good mint vinaigrette to enjoy with your grilled ribeye. I mean has mint, oil and vinegar ever been a bad combo? No! If you think that that is a great combo, start making this recipe right away and I know you will like it.""",
        authorId=12,
        ingredientPhoto='https://content.instructables.com/ORIG/FE9/4KFH/KQGMRBRN/FE94KFHKQGMRBRN.jpg?auto=webp&frame=1&width=678&height=1024&fit=bounds&md=a5e1e68c5bff75ce68995f2919a5c6ab')

    recipe708 = Recipe(
        title='Rigatoni With Sausage, Spinach, & Goat Cheese',
        description="""This creamy, tangy, and delicious Rigatoni with Sausage, Spinach, and Goat Cheese dish will quickly become a family favorite. This recipe has basic ingredients, but it turns into magic when the melted goat cheese brings them together. The whole meal can come together very quickly, so it's great for a last-minute dinner. """,
        authorId=13,
        ingredientPhoto='https://content.instructables.com/ORIG/FJ8/DQLK/KKWL8KF2/FJ8DQLKKKWL8KF2.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=91c503cc91fba32a95d95a07bee4f7e9')

    recipe709 = Recipe(
        title='Best Ever Chocolate Chip Cookie Recipe',
        description="""The winning cookies taste like they came from a high-end bakery, I'm not even kidding you. But you can make them yourself - it's easy!

I tell you this, Instructables fans, I hesitated to share the results of this experiment with you. It is now one of the most potent tools in my recipe belt, and I have secretly entertained fantasies of launching my own bakery, based on the inspiration provided by this recipe alone. But alas, I already have an awesome job here at Instructables HQ, and it would be criminal of me to keep this secret to myself.

If you follow this recipe, you'll soon be known wide and far for your amazing chocolate chip cookie skills, and will be called upon to provide them at every function. I recommend making up a huge batch and storing them in the freezer. What could be better than surprising your guests with freshly-baked, bakery-quality chocolate chip cookies in fifteen minutes?

Nothing. That's what.""",
        authorId=14,
        ingredientPhoto='https://content.instructables.com/ORIG/FXM/0GPY/GD2J2URC/FXM0GPYGD2J2URC.jpg?auto=webp&frame=1&width=915&height=1024&fit=bounds&md=6aec64dc29532b4fd4810099d4c97778')

    recipe710 = Recipe(
        title='No Bake Halloween Bat Snack',
        description="""Bats! You can cut chocolate wafer cookies in half and stick them into pretty much anything and they'll look like bats. This is a super fast treat that requires no cooking- a 10 minute snack.

The first version I made used chocolate graham crackers but then I tried Keebler Deluxe Fudge covered graham crackers and they're just as delicious, though a little less "healthy". """,
        authorId=12,
        ingredientPhoto='https://content.instructables.com/ORIG/FOH/QCA0/IUHMTP3R/FOHQCA0IUHMTP3R.jpg?auto=webp&frame=1&width=653&height=1024&fit=bounds&md=b48342912ebeca0f08111a50b3f38c7d')

    # Johnny/Darren

    recipe501 = Recipe(
        title='Southwesten Bruschetta Appetizers', description="""
            Grilling doesn't always mean steaks and ribs.

            Sometimes we like to use the grill to toast sliced French bread rounds for a light snack of bruschetta.

            The key to great bruschetta is fresh ingredients and extra virgin olive oil.

            We took this bruschetta to a whole new level by laying the traditional diced tomato mixture onto a bed of freshly prepared guacamole.

            Great, simple eats!

            Let's get started!
        """, authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/FTA/F854/IBM250NB/FTAF854IBM250NB.jpg?auto=webp&frame=1&fit=bounds&md=9a77465e7deaffe427e7ba4f34dbd316')


    recipe502 = Recipe(
        title="Baked Pork Collar (Neck) With Potatoes", description="""
            Pork Collar is a VERY underrated cut of meat, not many people even know something like this exists. It's from the neck part of the pig and it's a bit higher in fat content. Maybe that's the reason for the low popularity which is ironic in a way because we all know that fat is actually the carrier of flavor, right?

            So let's put the prejudice away, and let me show you how to bake a large piece of pork collar in the oven on a base of onions, along with some potatoes that will serve as the side.
        """, authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/FIY/EJRM/KUGYA4VV/FIYEJRMKUGYA4VV.jpg?auto=webp&frame=1&fit=bounds&md=26a5669bf4924557fefa638fcbaec19a')


    recipe503 = Recipe(
        title='Mini Dessert Bowls Out of Chocolate', description="""
            Everything tastes better when you eat out of a bowl that can be eaten itself! These mini bowls made of chocolate are easy to make but impressive to serve.
        """, authorId=9, ingredientPhoto='https://content.instructables.com/ORIG/F4P/T75K/IJRFGPO8/F4PT75KIJRFGPO8.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=3e55c08b595f68e9ae2f9cdb52ca8407')


    recipe504 = Recipe(
        title='Spicy Gummy Snacks', description="""
            These gummy candies may look sweet, but beware….they are deceptively spicy.
        """, authorId=9, ingredientPhoto='https://content.instructables.com/ORIG/FW8/KLNP/INPE8TH9/FW8KLNPINPE8TH9.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=3cef8bcc16caf7118b1a315de07cc78a')


    recipe505 = Recipe(
        title='The Perfect Summer Drink', description="""
            are you looking for the perfect summer drink? well look no further!
            a hint of lemon and mint, then gin and juice, topped of with ginger ale for some sparkly goodness. everything a nice drink needs.

            and if you don't drink alcohol, not a problem, just don't put any gin inside, it will still taste amazing.

            unfortunately my great drink does not have a name yet, if you can think of a good one, suggest away!
        """, authorId=10, ingredientPhoto='https://content.instructables.com/ORIG/F7R/3AHO/HIGFFX5S/F7R3AHOHIGFFX5S.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=41efcdec3a7788b79c4271f750173ca2')


    recipe506 = Recipe(
        title='Homemade Gyoza Making Made Easy', description="""
            Don't have a Japanese restaurant next door to satisfy your gyoza/potsticker craving? Here's how you can make a whole bunch o' gyozas in about half an hour (including prep time) using just a few key ingredients.
        """, authorId=10, ingredientPhoto='https://content.instructables.com/ORIG/FHO/EMNL/H8AZCSUM/FHOEMNLH8AZCSUM.jpg?auto=webp&frame=1&fit=bounds&md=09c2e4d01df0bbd5e16df9950eff8789')


    recipe507 = Recipe(
        title='One Pot Chicken Curry', description="""
            Chicken curry is a dish originating from the Indian subcontinent. Indian cuisine has a large amount of regional variation, with many variations on the basic chicken curry recipe. This recipe is the easiest recipe for a beginner. It is a very simple and easy dish to make. it is a go to recipe. we have made this recipe with a few ingredients and managed to keep Indian traditions alive with its amazing taste and concluded it in one pot challenge!
        """, authorId=11, ingredientPhoto='https://content.instructables.com/ORIG/FKN/6XGC/KKZG04FU/FKN6XGCKKZG04FU.jpg?auto=webp&frame=1&fit=bounds&md=45db907e1b55821ce7de1d4679b512b0')


    recipe508 = Recipe(
        title='Pomegranate Ice-cream', description="""
            Pomegranate ice cream is a delicious and refreshing dessert recipe that you can prepare for your family and friends in summer.(Only summer?) Is there any specific season to have ice-cream? For me, No! I have ice-cream throughout the year. It is Refreshing on a hot summer day, and delightful after dinner dessert. This pomegranate ice cream has bold flavor. It's tart and sweet, and super creamy. The best part, it can be made with a few ingredients and is super easy to make. I'm sure you're gonna be tempted reading this blog and you'll make this ice-cream right away. Without wasting any time let's start making it.
        """, authorId=11, ingredientPhoto='https://content.instructables.com/ORIG/FLB/IPG9/KRWGGLYM/FLBIPG9KRWGGLYM.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=6403e89551b25f45f62351f5d93b321a')


    recipe901 = Recipe(
        title='Chile Con Queso', description="""
            Chile con queso is the ultimate Mexican side dish! Comforting cheese dip for any snacks like nachos, tortilla chips or vegetables.

            Spicy, delicious and hearty dish that you need to have for Cinco de Mayo or Mexican party.

            Simple cheese dipping sauce that everyone will love (because who doesn't love cheese?). We enjoyed it with corn chips, while watching the movie, and it was so addictive! This is our go-to dipping sauce from now on!
        """, authorId=15, ingredientPhoto='https://content.instructables.com/ORIG/FMO/LOKJ/KNG1CRSH/FMOLOKJKNG1CRSH.png?auto=webp&frame=1&width=1024&fit=bounds&md=53c38078fd145a70005294b4cb003d4f')


    recipe902 = Recipe(
        title='Mango and Mint Tea Watermelon Slushie *Sugar Free*', description="""
            Need a simple sugar free recipe that will keep you cool and refreshed on a hot summer's day? Well I've got one for you! Watermelon is the quintessential summer fruit and can hold its own, but when combined with sweet and creamy mango and a fresh hint of mint tea, you've got yourself a whole new appreciation for the mighty melon!

            You can change up the amounts of each ingredient, bringing out a different flavor profile. This recipe allows the watermelon to truly stand out while the mint tea and mango subtly play in the background. If apple cider vinegar doesn't suit you, try lemon or lime juice to cut through the sweetness.
        """, authorId=15, ingredientPhoto='https://content.instructables.com/ORIG/FU8/RGFO/HIXPVTQ8/FU8RGFOHIXPVTQ8.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e2e571fe971019e5635c2842457f1295')

    # Jami
    #21
    recipe21 = Recipe(
        title='Tomato Wine (from Soup Production Waste)', description="Making wine is a hobby of mine. I've discovered over the years, that wine can be made out of almost anything.  In this Ingestible, I'll show you how I made a wonderful dry white wine out of tomato soup production waste.", authorId=8, ingredientPhoto='https://content.instructables.com/ORIG/FSA/3CUS/KN8W3OI0/FSA3CUSKN8W3OI0.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=56a6ec8de5a7f05b68e33474d636d7b5')
    recipe22 = Recipe(
        title='Legend of Zelda Hot Chocolate', description="Put down your boring hot coco powdery hot chocolate and grab your Breath of the Wild Apron, cause we are going to make the best hot chocolate recipe ever! Well, at least the geekiest hot chocolate recipe ever!  This is a Breath of the Wild inspired hot chocolate recipe, full of flavor, savory, chocolaty, totally delicious.  Taste buds be warned. It's gonna be amazing", authorId=7, ingredientPhoto='https://content.instructables.com/ORIG/FI4/416E/KIKA4JZQ/FI4416EKIKA4JZQ.png?auto=webp&frame=1&width=800&fit=bounds&md=e559946e14301f301ec90b7a2da83cdf')
    recipe23 = Recipe(
        title='Rainbow Brownie Ice Cream Sandwiches', description="Rainbows........ Brownies........ Ice cream Sandwiches.......... Excuse me what?!?!?!?!?!  These ice cream sandwiches are so much fun to make and everyone will love them!!! The fudgy brownies are so delicious and rich with a creamy vanilla ice cream balances all the flavours perfectly. Also these are Gluten free!!!!  Plus the multicolour rainbow will brighten anyone's day and celebration. You have beautiful rainbow treats and you can make your own ice cream from scratch!!!  I hope you love these as much as we do!!! Also Happy pride month!!!", authorId=7, ingredientPhoto='https://content.instructables.com/ORIG/FGV/IOIA/KQ57CNYR/FGVIOIAKQ57CNYR.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=5a1a6a2edd12045de17be38d4263b18b')
    recipe24 = Recipe(
        title='Mourning Buns', description="These flaky creepy confections are made up of apple and puff pasty. They are to die for.", authorId=7, ingredientPhoto='https://content.instructables.com/ORIG/F22/1JRC/KNG1B6DD/F221JRCKNG1B6DD.jpg?auto=webp&frame=1&crop=2:3&width=369&height=1024&fit=bounds&md=3ddeb9d50009eacd751199f4840a0329')
    recipe25 = Recipe(
        title='Creamy Cheese Nuggets', description="Hi everyone! Today we are making these delicious creamy cheese nuggets. If you love Mozzarella sticks or fried mac & cheese balls, this will be an new one to try! These breaded nuggets filled with a combination of stretchy and creamy cheeses.  Mozzarella sticks are great but the problem is that they kind of lack flavor. Mozzarella is such a mild tasting cheese that after it cools down, it is pretty much a tasteless piece of chewy 'meh' cheese...(think cold leftover pizza)  For this recipe, we are going to use multiple kind of cheeses so that it remains creamy even after it cools down to room temperature. The main ingredients of this recipe is cottage cheese. If you had Cheese Manicotti before, you know how creamy and milky the filling is inside those pasta shells. Besides cottage cheese, we also be adding some mozzarella and a little bit of cheddar for a nice yellow color. You could also use different type of stretchy cheeses of your liking, Muenster is highly recommended! We will also be using American cheese slices to make a lovely cheese sauce as the main base ingredients for the nugget to hold it's shape.", authorId=6, ingredientPhoto='https://content.instructables.com/ORIG/F0D/WL8G/KNYM0P7B/F0DWL8GKNYM0P7B.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=cba003e684a8166bdd4324bcba1b5d81')
    recipe26 = Recipe(
        title='To Dye for Boozy Deviled Eggs', description="This Easter I wanted to try my hand at Deviled Eggs. My Mom usually makes them, but since I was hosting, I wanted to do my own version  Finding inspiration online for the coloring, and also the varieties of filling, I came up with something of my own using ingredients I had on hand. You can certainly make substitutes depending on what's available to you  They look cute, and have an interesting and wonderful flavor  Nutrition, taste, and uniqueness are all wrapped up into one package with these crowd-pleasing appetizers!", authorId=7, ingredientPhoto='https://content.instructables.com/ORIG/FO2/BLQD/KN36CAG4/FO2BLQDKN36CAG4.jpg?auto=webp&frame=1&width=284&height=1024&fit=bounds&md=1860218b9983ea707694e089851b8e8a')
    recipe27 = Recipe(
        title='Fish-shaped Potato Mash With Tuna', description="Hi! Today we're gonna be making a potato and tuna based fake-fish! I think it is a delicious recipe for a family dinner and a great way to experiment with shapes and food 'sculpture'. No cooking needed, just a mixer and your ability! I hope you'll have fun making it as much as I did :)", authorId=8, ingredientPhoto='https://content.instructables.com/ORIG/FTV/CKP3/KFZEJGHL/FTVCKP3KFZEJGHL.png?auto=webp&frame=1&crop=3:2&width=653&fit=bounds&md=bbfe0506053448f661f25f908e3d562f')
    recipe28 = Recipe(
        title='Diner Style Burger, Fries & Shake at Home', description="Burgers are the absolute best thing on the planet, and what’s the only thing that makes them better? Eating one with a side of salty french fries and washing it down with a super thick milkshake. American diners do this meal combo so well, it's ridiculous! If I could, I'd go to one every week. However, there's just one slight problem. I live in Australia, where diners aren't really a thing. Popping over to America every week to go to a diner seems a little excessive, so I decided to replicate the meal, but also make it accessible for the at home cook  My version of the classic is amped up by baking homemade brioche buns, pickling red onion and mixing together a special burger sauce. I also chose to bake the french fries instead of deep frying them. I figured the mess, huge quantity of oil needed and high heat not worth the effort for something that can easily be achieved in an oven, which isn't as hands on  And finally, we get to the milkshake. My recipe for a chocolate milkshake is so simple but SO good, and the best part is you can make variations of it with other flavours by using vanilla ice-cream and including different flavoured syrups or fruits. I also decided to go one step further and added the can of whipped cream and a maraschino cherry as toppings. Totally indulgent, but completely necessary. We are going for the full diner experience after all!", authorId=6, ingredientPhoto='https://content.instructables.com/ORIG/FHV/WCVP/KAB2MKY8/FHVWCVPKAB2MKY8.png?auto=webp&frame=1&fit=bounds&md=6c2a8ac7f32fcfca87b6d08aba39bbc9')
    recipe29 = Recipe(
        title='Stuffed Red Cherry Tomatoes', description="Stuffed tomatoes are a standard classic French pre-takeaway takeaway and interestingly are slow rather than fast food. Every traiteur and charcuterie has them in season as a ready-made dish to take home and warm up or to be heated up in the shop and eaten as a picnic. Most butchers' shops in France offer a daily, cooked hot dish and stuffed tomatoes à la bonne femme is a a seasonal favourite. I've always thought how interesting it is that many countries, France is just one, maintain this old tradition and link with the past, when people didn't necessarily have ovens in their homes or alternatively wanted a ready-cooked meal without going to a restaurant  Here I'm using cherry tomatoes and these make great hot savouries in a bite sized edition so I guess they should be called 'bon enfant'...maybe  Cherry tomatoes are very easy to grow in a small space in a container or hanging basket. If you have a greenhouse or a window sill you can keep them producing right up to the first frosts. Tomatoes are perennials, so with care you can keep the plants from year to year.", authorId=6, ingredientPhoto='https://content.instructables.com/ORIG/FBO/W3W8/KQQMU174/FBOW3W8KQQMU174.jpg?auto=webp&frame=1&width=799&height=1024&fit=bounds&md=1d1389601c231fbfb3a4ca92f252d1d5')
    recipe30 = Recipe(
        title='Edible Plastic Pouches', description="I have the most amazing life hack for you guys!  Have you ever tried being on a hike and trying to stuff a handful of trail mix into your mouth, hands dirty and all, while dropping way too much of the precious nibbles along the way? Or have you tried letting the kids eat snacks in the car and then found half of it scattered all over the back seat afterwards?  I have the perfect solution! Welcome: edible plastic pouches containing trail mix (or whatever else you like)! They are perfectly pocket-sized and spill-free.  Gone are the days when edible plastic was only a fun and tasteless decorating addition on fancy cakes. Now, this science hack can actually be used for something useful.  The idea behind this edible plastic is actually quite simple. First, we gel water using agar or gelatine, and then, this gel is dehydrated to create an edible, plastic-like sheet that can be used for a variety of purposes.  Sounds good? If you don't care about the nerdy science behind this, go straight to the next step. Otherwise, keep reading.  Agar and gelatine can both be used to solidify a liquid, but they are structurally quite different. Agar is a carbohydrate, and gelatin is a protein. While gelatin is derived from animal collagen, agar comes from algae and is thus plant based (and vegan). Agar melts around 85 degrees C (185 F) whereas gelatin melts at 35 degrees C (95 F), making it less stable. This also means that gelatin will melt in your mouth while agar will not.", authorId=8, ingredientPhoto='https://content.instructables.com/ORIG/F8P/BFEJ/JGGTFZST/F8PBFEJJGGTFZST.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=f197835c8db3be396cd024837dc19cdb')

    # Johnny/Darren
    #31

    recipe903 = Recipe(
        title='Paneer Satay on a Stick', description="""
            Imbued with dynamic flavors, this Paneer Satay is an incredible recreation of the customary Indian kebab. It's fresh, succulent and alive and so good that it melts in your mouth! Making kebabs involves persistence and craftsmanship. But this dish is very simple and easy to make. Satay is commonly well known in Southeast Asian nations. It's anything but a piece of marinated meat simmered on sticks however setting up a veggie lover variant of it, I pick protein-rich paneer. I have made this indo-chinese recipe using a few ingredients. So let's get started.
        """, authorId=16, ingredientPhoto='https://content.instructables.com/ORIG/F91/G8WD/KQTHRAPC/F91G8WDKQTHRAPC.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=8173b49c329a784d6489b18bdd8604a5')


    recipe904 = Recipe(
        title='Tacos With a Twist', description="""
            Making Dos Capas is super easy with only a few steps!  Its also easy to eat...with the soft shell holding in the hard shell and fillings it makes it less messy to chow down!
        """, authorId=16, ingredientPhoto='https://content.instructables.com/ORIG/FB1/RXZ4/HSYO278D/FB1RXZ4HSYO278D.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=332e45c6ce6400fd18014c59e667afa5')


    recipe905 = Recipe(
        title='Paan Bahaar Ice cream', description="""
            It is an ice cream flavoured with paan (betel leaves) and gulkand (sweet preserve of rose petals). Paan (betel leaves) giving traditional taste of india while gulkand adds sweet tooth factor and its sweet fragrance to this ice -cream. Thus giving a pleasing taste to your tongue along with sweet aroma of rose thereby completing the frozen desert at its best.
        """, authorId=17, ingredientPhoto='https://content.instructables.com/ORIG/FF0/3W9F/HJKBZ7YV/FF03W9FHJKBZ7YV.jpg?auto=webp&frame=1&fit=bounds&md=8d52631b162e53dde6da9c4b1f446628')


    recipe906 = Recipe(
        title='African Style Beef Stew', description="""
            This is flavorful African style stew with tomatoes and beef. Such an easy and delicious meal that your family will love. This comfort food can feed the crowd!

            I used dried spices and herbs for this stew, so it can be quickly prepared. It is about 6 portions, but you can divide it to smaller servings with rice or vegetables on the side.

            African stew is a versatile dish! You can add chopped potatoes or carrots about 30 minutes before the end of cooking.

            African beef stew is commonly served in Nigeria, Kenya, Ghana and other African countries. There are different variations of this stew across the continent. Try it at your home!
        """, authorId=17, ingredientPhoto='https://content.instructables.com/ORIG/FQW/3821/KTPSX0RW/FQW3821KTPSX0RW.jpg?auto=webp&frame=1&fit=bounds&md=45d063efc0c86c95ac235b1a2df0b900')


    db.session.add(recipe701)
    db.session.add(recipe702)
    db.session.add(recipe703)
    db.session.add(recipe704)
    db.session.add(recipe705)
    db.session.add(recipe706)
    db.session.add(recipe707)
    db.session.add(recipe708)
    db.session.add(recipe709)
    db.session.add(recipe710)


    db.session.add(recipe501)
    db.session.add(recipe502)
    db.session.add(recipe503)
    db.session.add(recipe504)
    db.session.add(recipe505)
    db.session.add(recipe506)
    db.session.add(recipe507)
    db.session.add(recipe508)
    db.session.add(recipe901)
    db.session.add(recipe902)

    db.session.add(recipe21)
    db.session.add(recipe22)
    db.session.add(recipe23)
    db.session.add(recipe24)
    db.session.add(recipe25)
    db.session.add(recipe26)
    db.session.add(recipe27)
    db.session.add(recipe28)
    db.session.add(recipe29)
    db.session.add(recipe30)

    db.session.add(recipe903)
    db.session.add(recipe904)
    db.session.add(recipe905)
    db.session.add(recipe906)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()




def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))
        
    db.session.commit()