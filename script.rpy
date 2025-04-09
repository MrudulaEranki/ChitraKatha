image bg BengalGram = im.Scale("BengalGram.jpg", 1920, 1080)
image bg BengalGramMap = im.Scale("BengalGramMap.jpg", 1920, 1080)
image bg GreenGram = im.Scale("GreenGram.jpg", 1920, 1080)
image bg GreenGramMap = im.Scale("GreenGramMap.jpg", 1920, 1080)
image bg pond_side = im.Scale("pond_side.jpg", 1920, 1080)
image bg TelanganaMap = im.Scale("TelanganaMap.jpg", 1920, 1080)
image bg House= im.Scale("House.jpg", 1920, 1080)
image bg HouseFire= im.Scale("HouseFire.jpg", 1920, 1080)     
image bg  plain_stove1 = im.Scale("plain_stove1.jpg", 1920, 1080)
image bg batter_pour2 = im.Scale("batter_pour2.jpg", 1920, 1080)
image bg brown_attu4 = im.Scale("brown_attu4.jpg", 1920, 1080)
image bg attu_onstove3 = im.Scale("attu_onstove3.jpg", 1920, 1080)
image bg brown_attu_spoon5 = im.Scale("brown_attu_spoon5.jpg", 1920, 1080)

image a_curious = im.FactorScale("a_curious.png",1)
image a_disappointed = im.FactorScale("a_disappointed.png",1)
image a_eating = im.FactorScale("a_eating.png",1)   
image a_eyesclose_smilewide = im.FactorScale("a_eyesclose_smilewide.png",1)
image a_mouthopen = im.FactorScale("a_mouthopen.png",1)
image a_normal = im.FactorScale("a_normal.png",1)
image a_pouting = im.FactorScale("a_pouting.png",1)
image a_smiletalk = im.FactorScale("a_smiletalk.png",1)
image a_smilewide = im.FactorScale("a_smilewide.png",1)
image a_sad = im.FactorScale("a_sad.png",1)


image k_curious = im.FactorScale("k_curious.png",1)
image k_disappointed = im.FactorScale("k_disappointed.png",1)   
image k_eating = im.FactorScale("k_eating.png",1)
image k_eyesclose_smilewide = im.FactorScale("k_eyesclose_smilewide.png",1)
image k_mouthopen = im.FactorScale("k_mouthopen.png",1)
image k_normal = im.FactorScale("k_normal.png",1)
image k_pouting = im.FactorScale("k_pouting.png",1)
image k_smiletalk = im.FactorScale("k_smiletalk.png",1)
image k_smilewide = im.FactorScale("k_smilewide.png",1)
image k_sad = im.FactorScale("k_sad.png",1)




define ami = Character('Amidalraji')
define kon = Character('Kontamalli')



label start:

    #Scene 1
    scene bg pond_side
    with fade
    "As the sun began to set, casting a golden hue over the village, Amidalraji and Kontamalli found themselves relaxing under the shade of a large banyan tree. The gentle rustle of leaves and the chirping of birds created a serene atmosphere, perfect for their afternoon chat."

    show a_smiletalk at left
    ami "You know, Kontamalli, I’ve been craving atlu all day. Wouldn’t it be wonderful to make some?"

    call game

    show k_smilewide at right
    kon  "Atlu? Yes! That sounds delicious! We should gather some ingredients from the fields."

    

    menu:
        "Want to know more about atlu? ":
            jump exp_choice1
        "I'm Good!":
            jump common1

label game:
    "Let's play a quick mini-game!"
    call krix  # This calls your mini-game
    "Nice! You scored [pointk] points!"

label krix:
    call screen krixx
    return

screen krixx():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "This is your mini-game!" size 30
        text "You scored [pointk] points"

        # Button to end mini-game and return to story
        textbutton "Continue" action Return()

    
label exp_choice1:
    scene bg brown_attu4
    with fade
    "Atlu, a delightful food item from Telangana, is a type of crepe or dosa that embodies the essence of traditional South Indian cuisine. These thin, crispy delights are made from various flours, with rice flour being the most common base."

    "The Allure of Atlu- Imagine biting into a perfectly cooked attu, its surface golden brown and slightly crisp. The aroma of freshly ground spices wafts through the air as you savor the first bite."
    "The texture is delightfully chewy yet crisp, with a hint of spice that dances on your palate. "

    "Atlu can be prepared using different flours such as rice flour, maize flour, or even jowar flour, each bringing its own character to the dish."


    "The process of making atlu is as exciting as eating them! From grinding the grains to mixing in spices and cooking them on a hot griddle, every step is filled with anticipation."
    "As the batter sizzles on the pan, it transforms into a golden masterpiece that beckons you to indulge. Atlu can be served in various ways—paired with spicy chutneys, tangy pickles, or even sweet accompaniments like jaggery syrup for those who enjoy contrasting flavors."
    " Whether enjoyed as breakfast, a snack, or part of a festive meal, atlu brings people together around the table. In Telangana, where culinary traditions run deep, atlu stand out as not just food but as a celebration of local ingredients and flavors."

    jump common1

label common1:

    scene bg TelanganaMap
    "The two friends exchanged excited glances, their minds already racing with thoughts of fluffy atlu. They knew that to make the batter, they would need a variety of grains and pulses native to their region. "

    show a_normal at left
    ami "Let’s collect some tasty gram. They’ll add a lovely flavor to our batter!"
    hide a_normal

    "With their plan in mind, Amidalraji and Kontamalli set off into the fields. The air was filled with the earthy scent of soil and growing crops. As they walked, Amidalraji pointed out different grains along the way. "

    jump scene2

label scene2:
    
    scene bg GreenGram

    show a_curious at left  
    ami "Look at those green gram plants! They’re so vibrant and healthy. Did you know green gram is packed with protein? It’s a staple in our diet."

menu:
    "Want to know more about Green Gram? ":
        jump exp_choice2
    "I'm Good!":
        jump common2

label exp_choice2:  

    scene bg GreenGramMap
    with fade    

    "Green gram, commonly known as Pesaru pappu, is a treasured native grain of Telangana that embodies the spirit of the region’s agricultural heritage."

    "Green Gram is popularly harvested in Sangareddy, Vikarabad, Narayanpet, Asifabad, Mahabubabad and Khammam in Telangana." 

    show bg GreenGram
    with dissolve
    "With its vibrant green color and rich nutritional profile, this legume is not just a staple; it's a source of pride for local farmers and families alike." 

    scene bg GreenGram
    with fade

    "Nutritional Marvel: Packed with protein, fiber, and essential vitamins, green gram is a powerhouse of nutrition. It contains approximately 24\% protein, making it an excellent choice for those seeking healthy, plant-based options. "
    show bg GreenGram
    with dissolve
    "Its high fiber content aids digestion and provides a sense of fullness, making it a beloved ingredient in many households."
    show bg GreenGram
    with dissolve
    "Culinary Versatility: In Telangana, green gram is celebrated for its versatility in the kitchen. Whether used whole in salads, cooked into comforting dals, or ground into flour for delicious **atlu**,  each preparation showcases its unique flavor and texture. "
    
    show bg GreenGram
    with dissolve
    "Cultural Significance: Beyond its culinary uses, green gram holds a special place in the hearts of the people of Telangana. It thrives in the region's fertile soil and is often grown alongside rice, symbolizing the harmony between crops that sustain families and communities."
    
    show bg GreenGram
    with dissolve
    "Green gram is more than just a grain; it represents nourishment, tradition, and community in Telangana. With every dish made from this vibrant legume—especially the beloved atlu—there’s a story of resilience and connection to the land. "
    
    jump common2

label common2:
    jump scene3

label scene3:

    scene bg BengalGram

    show k_smiletalk at right
    kon "Absolutely! And over there are the Bengal gram plants. They’re known for their nutty flavor and are perfect for making dal or adding to our attu batter."

menu:
    "Want to know more about Bengal Gram? ":
        jump exp_choice3
    "I'm Good!":
        jump common3

label exp_choice3:

    scene bg BengalGramMap
    with fade
    "Bengal gram, known locally as Chana or Chickpea, is a cherished native grain of Telangana, deeply woven into the region's agricultural and culinary fabric. This vibrant legume is a nutritional powerhouse—rich in protein, fiber, and essential vitamins."
    "Bengal gram is cultivated in districts like Adilabad, Nirmal, Nizamabad, Kamareddy, Sangareddy and Gadwal in Telangana."

    scene bg BengalGram
    with dissolve
    "Culinary Delight: In Telangana, Bengal gram shines in the preparation of **atlu**, the delicious crepes that are a staple in local cuisine. Imagine the aroma of freshly ground Bengal gram mingling with spices, creating a batter that transforms into golden, crispy atlu on the hot griddle."

    "Each bite is a celebration of texture and taste, evoking memories of home-cooked meals shared with family and friends."

    "Cultural Heartbeat: Beyond its culinary versatility, Bengal gram holds cultural significance. It represents the heart of Telangana's farming community, thriving in the region's semi-arid climate and enriching the soil."

    "In every atlu made with Bengal gram, there’s a story—a connection to the land and to each other. It’s this emotional bond that makes Bengal gram an irreplaceable part of Telangana’s identity."

    jump common3

label common3:

    scene bg pond_side 
    with fade   
    "They continued their exploration, admiring the variety of crops around them."

    "As they gathered their ingredients, Amidalraji couldn’t help but feel grateful for the abundance of nature around them. Finally, with their bags filled with green gram, Bengal gram, pigeon peas, and other seeds native to Telangana, they returned to their shady spot under the tree. "

    show a_smiletalk at left
    ami "Now that we have everything, let’s soak these seeds and grind them into a batter."

    show k_smilewide at right
    kon "I can already imagine how soft and fluffy those atlu will be!"

    "With laughter and excitement in the air, they prepared to create their delicious meal together. The aroma of fresh ingredients filled their senses as they looked forward to enjoying the fruits of their labor."

label home:

    scene bg House
    with fade

    "After gathering a variety of seeds, they returned home, their bags full and their spirits high. "

    show a_normal at left
    ami "Now that we have everything, let’s soak these seeds and grind them together."

    show k_normal at right
    kon "I’ll start grinding while you go wash up at the pond. We need to hurry before it gets too hot!"

menu:
    "KONTAMALLI’S POV(STAY AT HOME AND PREPARE ATLU?)":
        jump main_a

    "AMIDALRAJI’S POV(GO TO THE POND?)":
        jump main_b

label main_a:

    scene bg House 
    with fade

    "Amidalraji nodded and dashed off to the pond, leaving Kontamalli to prepare the attu batter. "

    

    show bg HouseFire
    with dissolve
    show k_smilewide at right   
    kon  "'The atlu will be perfect if I pour the batter now. They’ll be hot and fluffy!'"

    show bg plain_stove1
    with dissolve
    kon "Kontamalli set up the stove to heat the pan and anticipated the first sizzle of the batter."
    

    show bg batter_pour2
    with dissolve
    kon " As she poured the batter onto the cast iron pan, she couldn’t help but feel excited about the delicious meal ahead."

    show bg attu_onstove3   
    with dissolve
    "(cooking)"

    show bg brown_attu4
    with dissolve
    "The attu turns golden brown, the aroma filling the room."


    hide k_smilewide
    show k_smilewide at left
    show bg brown_attu_spoon5
    with dissolve
    kon "This attu is ready and let's make some more!"

    show bg House
    with dissolve
    hide k_smilewide
    "Time passed, and Amidalraji took longer than expected. Kontamalli’s stomach grumbled as she glanced at the steaming atlu. "

    show k_mouthopen at right
    kon "The atlu are ready! I can’t wait any longer."

    show k_eating at right
    "She quickly grabbed two atlu for herself, savoring each bite. "

    show k_pouting at right
    "After finishing her second attu, she thought about Amidalraji's return."

    show k_eating at right
    kon "'I should save some for her... but just one more won't hurt!' She devoured another attu, leaving only one behind as she heard footsteps approaching."


    show a_curious at left
    ami "I’m back! What about the atlu? I was so hungry!"

    show k_smiletalk at right
    kon "Well... I ate them all."
    
    show a_disappointed at left
    ami "How could you eat them all? We worked so hard to gather those ingredients!"

menu:
    "Be cheeky":
        jump main_a_1
    "Apologize to Amidalraji":
        jump main_a_2

label main_a_1:
    hide k_smiletalk
    show k_eating at right
    kon  "'I ate them like this!' She mimicked taking big bites, hoping to bring a smile back to Amidāl Rāji's face."
    jump main_a_common

label main_a_2:
    hide k_smiletalk
    show k_pouting at right
    kon "I’m sorry Amidalraji"
    show k_mouthopen at right
    kon  "I couldn’t resist! They were so hot and delicious. Look, I saved one for you." 
    jump main_a_common

label main_a_common:
    show a_disappointed at left
    "Amidalraji sighed, feeling a mix of disappointment and amusement at her friend’s antics."

    show a_smiletalk at left    
    ami "Next time, let’s do it together. I won’t go to the pond if it means missing out on our atlu."

    show k_smiletalk at right
    kon "Only if you promise to send me to wash up again! That way, I can enjoy my share without waiting."

    show a_eyesclose_smilewide at left
    show k_eyesclose_smilewide at right
    "The two friends laughed together, their bond strengthened by shared experiences and a love for food. They decided that no matter what happened next time, they would enjoy their cooking adventure together. This dialogue captures their friendship and the light-hearted nature of their cooking adventure."

    return

label main_b:

    scene bg pond_side
    with fade
    
    "As Amidalraji made her way to the pond, she felt a mix of excitement and anticipation. The prospect of enjoying the atlu they had worked so hard to prepare filled her with joy. "

    show a_curious at left
    ami "Finally, some time to freshen up! I can’t wait to dive into those hot atlu once I’m back."

    "As she reached the pond, she took a moment to appreciate the tranquility of the water, the gentle ripples reflecting the sunlight. "
    
    show a_normal at left
    ami "Ah, this feels refreshing! A quick wash will do wonders. I hope Kontamalli is grinding that batter well."

    "After bathing and washing her clothes, Amidalraji felt rejuvenated. She glanced back toward their spot under the tree, eager to return. "

    show a_smiletalk at left
    ami  "I hope she’s not waiting too long. Those atlu will be perfect when they’re hot!"

    "With a spring in her step, she hurried back, her stomach rumbling in anticipation of the delicious meal. As she approached their resting place, the aroma of freshly cooked atlu wafted through the air, making her mouth water. "

    show bg HouseFire
    with dissolve

    show a_smilewide at left
    ami "Kontamalli! I’m back! I can already smell those atlu!"

    show k_sad at right
    "Upon seeing Amidāl Rāji's expectant face, Kontamalli couldn’t help but feel a twinge of guilt as she recalled how hungry she was. "

    show a_curious at left
    ami "What about the atlu? I was very hungry and came back to eat them."

    show k_normal at right
    kon "Well... I ate them all."

    show a_disappointed at left
    "Kontamalli watched as Amidāl Rāji's expression shifted from excitement to disappointment. "

    kon "I couldn’t resist! They were so hot and delicious. Look, I saved one for you!"

menu:
    "Decide to scold her":
        jump main_b_1
    " Forgive Kontamalli":
        jump main_b_2

label main_b_1:

    show a_disappointed at left
    ami "How could you eat them all? We worked so hard to gather those ingredients!"

    show k_eating at right
    kon "'I ate them like this!' She mimicked taking big bites, hoping to bring a smile back to Amidāl Rāji's face."

label main_b_2:

    show a_sad at left
    ami "It’s quite alright, I guess it wasn’t in my fate to taste the atlu even after putting so much labor into the process."

    show k_disappointed at right
    kon "I’m so sorry, I’ll let you have the extra atlu next time."

label main_b_common:

    show a_smiletalk at left
    "Despite Amidāl Rāji’s frown, Kontamalli and Amidalraji felt a sense of camaraderie in their shared experience. "

    show k_smiletalk at right
    kon "Next time, let’s do it together! But you know what? I’ll only help if you send me off to the pond again for a wash!"

    show a_eyesclose_smilewide at left
    show k_eyesclose_smilewide at right
    "With laughter bubbling between them, Amidalraji realized that even in moments of mischief, their friendship remained strong. The bond they shared over food and fun was what truly mattered."

    return
