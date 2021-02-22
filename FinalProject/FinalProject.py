class cook:
    def __init__(self, explain, prep, cooked, total, servings, yields):
        self.explain = explain
        self.prep = prep
        self.cook = cooked
        self.total = total
        self.servings = servings
        self.yields = yields

    def prepare_garlic_taco(self):
        print(self.explain, self.prep, self.cook, self.total, self.servings, self.yields)
        ingredients = ["1 tablespoon olive oil", "4 cloves garlic, minced", "1 pound chicken tenderloins, diced",
                       "½ onion, diced", "½ red bell pepper, diced", "½ (15 ounce) can black beans, rinsed and drained",
                       "¼ cup chopped fresh cilantro, or to taste", "½ cup chunky salsa",
                       "4 large flour tortillas, or as needed", "¼ cup shredded Mexican cheese blend, or to taste"]
        print("### Garlic Chicken Taco İngredients ###")
        print(ingredients)
        print("Enjoy your meal!\n")

    def prepare_sicilian_spaghetti(self):
        print(self.explain, self.prep, self.cook, self.total, self.servings, self.yields)
        ingredients = ["1 pound spaghetti", "4 tablespoons olive oil", "3 cloves garlic, crushed",
                       "1 (2 ounce) can anchovy fillets, chopped", "1 cup fine bread crumbs",
                       "1 cup chopped fresh parsley", "ground black pepper to taste",
                       "4 tablespoons freshly grated Parmesan cheese"]
        print("### Sicilian Spaghetti İngredients ###")
        print(ingredients)
        print("Enjoy your meal!\n")

    def prepare_orange_sunrise_smoothie(self):
        print(self.explain, self.prep, self.cook, self.total, self.servings, self.yields)
        ingredients = ["½ cup orange juice", "1 banana, frozen and chunked", "1 peach, peeled and sliced",
                       "½ cup honeydew melon, cubed", "1 (8 ounce) container orange yogurt", "1 teaspoon white sugar",
                       "½ cup ice"]
        print("### Orange Sunrise Smoothie İngredients ###")
        print(ingredients)
        print("Enjoy your meal!\n")


class garlic_chicken_tacos(cook):
    def __init__(self, explain, prep, cooked, total, servings, yields):
        super().__init__(explain, prep, cooked, total, servings, yields)


class sicilian_spaghetti(cook):
    def __init__(self, explain, prep, cooked, total, servings, yields):
        super().__init__(explain, prep, cooked, total, servings, yields)


class orange_sunrise_smoothie(cook):
    def __init__(self, explain, prep, cooked, total, servings, yields):
        super().__init__(explain, prep, cooked, total, servings, yields)


class developed:
    print("### Developed by Güven Eren ###")


Chicken_taco = garlic_chicken_tacos("Garlic Chicken Taco =>\n", "15 Mins prep\n", "15 Mins cooked\n",
                                    "Total preparation 30 mins\n", "4 Servings",
                                    "4 Yields\n")

sicilian_spaghetti = sicilian_spaghetti("Sicilian Spaghetti =>\n", "10 Mins prep\n", "5 Mins cooked\n",
                                        "Total preparation 15 mins\n", "8 Serving\n", "8 Yield\n")

orange_sunrise_smoothie = orange_sunrise_smoothie("Orange Sunrise Smoothie =>\n", "15 Mins prep\n",
                                                  "Refrigerate for 5 minutes\n", "Total preparation 15 mins\n",
                                                  "2 Serving\n", "2 Yield\n")

Chicken_taco.prepare_garlic_taco()
sicilian_spaghetti.prepare_sicilian_spaghetti()
orange_sunrise_smoothie.prepare_orange_sunrise_smoothie()
developed = developed()
