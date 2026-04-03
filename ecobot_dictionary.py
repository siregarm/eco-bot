tree_facts = {
    1: "Trees are perennial plants with a woody stem, trunk, branches, and leaves.",
    2: "Trees absorb carbon dioxide from the air and release oxygen through photosynthesis.",
    3: "The roots of a tree help anchor it in the soil and absorb water and nutrients.",
    4: "Some trees can live for hundreds or even thousands of years.",
    5: "Oak trees are known for producing acorns.",
    6: "Pine trees are evergreen, which means they keep their needles year-round.",
    7: "Tree rings can show the age of a tree and reveal past climate conditions.",
    8: "Rainforests contain some of the greatest diversity of tree species in the world.",
    9: "Trees provide shelter and food for many animals, birds, and insects.",
    10: "Maple trees are famous for producing sap that can be made into maple syrup.",
    11: "Leaves on trees can change color in autumn because of pigment changes.",
    12: "Trees help prevent soil erosion by holding the soil together with their roots.",
    13: "Baobab trees can store large amounts of water in their trunks.",
    14: "Coconut trees grow in tropical climates and produce coconuts.",
    15: "Dead or fallen trees can still support ecosystems by feeding fungi and insects.",
    16: "Some trees, like willows, grow especially well near water.",
    17: "Trees can communicate chemically by releasing signals when under attack from pests.",
    18: "The tallest trees in the world are coast redwoods.",
    19: "Fruit trees such as apple and mango trees provide food for humans and animals.",
    20: "Urban trees can help cool cities by providing shade and reducing heat."
}

environment_facts = {
    1: "Pollution is the introduction of harmful substances or energy into the environment.",
    2: "Air pollution can come from vehicles, factories, wildfires, and burning fossil fuels.",
    3: "Water pollution happens when harmful chemicals, waste, or plastics enter rivers, lakes, and oceans.",
    4: "Soil pollution can reduce land fertility and harm plants, animals, and microorganisms.",
    5: "Plastic pollution is a major problem because plastic can take hundreds of years to break down.",
    6: "Greenhouse gases include carbon dioxide, methane, nitrous oxide, and water vapor.",
    7: "The greenhouse effect is a natural process that helps keep Earth warm enough for life.",
    8: "Human activities have strengthened the greenhouse effect by increasing greenhouse gas concentrations.",
    9: "Burning coal, oil, and natural gas is one of the biggest sources of carbon dioxide emissions.",
    10: "Methane is a powerful greenhouse gas released by livestock, landfills, and fossil fuel production.",
    11: "Deforestation contributes to the greenhouse effect because fewer trees are available to absorb carbon dioxide.",
    12: "Excess greenhouse gases trap more heat in the atmosphere, leading to global warming.",
    13: "Air pollution can harm human lungs and increase the risk of heart and respiratory diseases.",
    14: "Smog is a type of air pollution formed when pollutants react in sunlight.",
    15: "Acid rain can form when sulfur dioxide and nitrogen oxides mix with water in the atmosphere.",
    16: "Ocean pollution can damage marine life and disrupt entire ecosystems.",
    17: "Reducing waste, recycling, and reusing materials can help lower pollution.",
    18: "Using renewable energy sources like solar and wind can reduce greenhouse gas emissions.",
    19: "Public transportation, biking, and walking can help reduce air pollution from cars.",
    20: "Protecting forests and planting trees can help reduce the effects of the greenhouse effect."
}

waste_facts = {
    1: "Waste is any material that people no longer need or use.",
    2: "Solid waste includes items like paper, plastic, metal, glass, and food scraps.",
    3: "Organic waste, such as fruit peels and leaves, can decompose naturally.",
    4: "Plastic waste can remain in the environment for a very long time.",
    5: "Hazardous waste includes batteries, chemicals, paints, and medical waste.",
    6: "Electronic waste, or e-waste, includes old phones, computers, and other devices.",
    7: "Improper waste disposal can pollute land, air, and water.",
    8: "Landfills are places where large amounts of waste are buried.",
    9: "Incineration is the process of burning waste to reduce its volume.",
    10: "Recycling helps turn used materials into new products.",
    11: "Composting is a way to turn organic waste into nutrient-rich soil.",
    12: "Reducing waste means using fewer materials in the first place.",
    13: "Reusing items can help decrease the amount of waste sent to landfills.",
    14: "Sorting waste makes recycling and disposal more effective.",
    15: "Food waste is a major global problem that wastes water, energy, and labor.",
    16: "Marine animals can be harmed by waste that enters oceans and rivers.",
    17: "Waste management systems help collect, transport, process, and dispose of waste safely.",
    18: "Single-use products often create more waste than reusable alternatives.",
    19: "Community clean-up programs can help reduce waste in public places.",
    20: "Good waste management helps protect human health and the environment."
}

organic_trash = """
Organic trash is waste that comes from living things and can break down naturally.
Examples include food scraps, fruit peels, vegetable leftovers, eggshells, and dry leaves.
This type of trash can often be turned into compost.
"""

recyclable_trash = """
Recyclable trash is waste that can be processed and made into new products.
Examples include paper, cardboard, glass bottles, aluminum cans, and some plastic containers.
This type of trash should be separated properly to make recycling easier.
"""

hazardous_trash = """
Hazardous trash is waste that can be harmful to people, animals, or the environment.
Examples include batteries, expired medicine, paint, chemicals, and electronic waste.
This type of trash needs special handling and should not be thrown away carelessly.
"""

def tree_pass(length):
    import random
    tree_emojis = ["🌲", "🌳", "🌴", "🎍", "🪵", "🌱", "🌿", "🍃", "🍂", "🍁"]
    password = ""

    for i in range(length):
        password += random.choice(tree_emojis)
    return password

common_trees = [
    "Oak",
    "Pine",
    "Maple",
    "Birch",
    "Cedar",
    "Willow",
    "Palm",
    "Mango",
    "Apple",
    "Coconut"
]

tree_hints = {
    "Oak": "This tree is known for being strong and producing acorns.",
    "Pine": "This tree has needles instead of broad leaves and stays green all year.",
    "Maple": "This tree is famous for syrup and colorful autumn leaves.",
    "Birch": "This tree often has white bark with black markings.",
    "Cedar": "This tree is known for its fragrant wood and is often used in furniture.",
    "Willow": "This tree has long, drooping branches and often grows near water.",
    "Palm": "This tree is common in tropical places and has large fan-like or feather-like leaves.",
    "Mango": "This tree produces a sweet tropical fruit.",
    "Apple": "This tree grows a very common round fruit often used in pies.",
    "Coconut": "This tree grows in tropical beaches and produces large hard-shelled fruit."
}
