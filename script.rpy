image bg BengalGram = im.Scale("BengalGram.jpg", 1920, 1080)
image bg BengalGramMap = im.Scale("BengalGramMap.jpg", 1920, 1080)
image bg GreenGram = im.Scale("GreenGram.jpg", 1920, 1080)
image bg GreenGramMap = im.Scale("GreenGramMap.jpg", 1920, 1080)

image bg pond_side = im.Scale("pond_side.jpg", 1920, 1080)

image bg pond = im.Scale("minigame_fish_catcher/pond_side.jpg", 1920, 1080)

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
    play music "throughout_the_game.mp3"
    #Scene 1
    scene bg pond_side
    with fade
    "The sun was going down. Amidalraji and Kontamalli sat under a big banyan tree. The leaves rustled, and birds chirped. It was a nice, quiet time to talk."

    show a_smiletalk at left
    ami  "Kontamalli, I really want some atlu!"

    show k_smilewide at right
    kon  "Yum! Let’s go get what we need from the fields but before that let’s play a mini game!!"
    play sound "excited_twinkle1.mp3"
    
    menu:
        "What are atlu? ":
            jump exp_choice1
        "Continue the game!":
            jump common1
    
label exp_choice1:
    scene bg brown_attu4
    with fade
    play sound "atly_sizling.mp3"
    "Amidalraji and Kontamalli loved atlu! Atlu are yummy, thin pancakes from Telangana. They can be soft or crispy, and you can make them in many fun ways!
    Some atlu are made with rice flour and spicy stuff like chili, onions, and curry leaves. Others are sweet and soft, like the ones made with corn. You can even mix in veggies like ridge gourd to make them extra tasty!
    Cooking atlu is fun too! Pour the batter on a hot pan, wait for the sizzle... and flip! It smells so good! You can eat them with chutney, pickles, or even a little jaggery for sweetness. Mmm... so many flavors!"
    jump common1

label common1:

    scene bg TelanganaMap
    "Amidalraji and Kontamalli smiled big. They were already thinking about soft, yummy atlu!"

    show a_normal at left
    ami  "Let’s get some gram—it’ll make our batter super tasty!"
    hide a_normal

    "Off they went into the fields. The air smelled fresh, and little plants danced in the breeze."
    jump scene2

label scene2:
    play sound "page_turn.mp3"
    scene bg GreenGram

    show a_curious at left  
    ami "Wow! Look at those green gram plants! So green and strong! They help us grow big and strong too!"

menu:
    "Learn about Green Gram? ":
        jump exp_choice2
    "I'm Good!":
        jump common2

label exp_choice2:  
    play sound "info.mp3"
    scene bg GreenGramMap
    with fade    

    "Green gram is called Pesaru pappu (పెసర పప్పు)  in Telangana. It’s small, green, and full of good stuff that helps you grow strong! You can eat it in salads, make yummy dal, or even mix it into atlu batter. Farmers love it, and so do families!"
    "Green Gram is popularly harvested in Sangareddy, Vikarabad, Narayanpet, Asifabad, Mahabubabad and Khammam in Telangana." 

    show bg GreenGram
    with dissolve
     
    jump common2

label common2:
    jump scene3

label scene3:
    play sound "page_turn.mp3"
    scene bg BengalGram

    show k_smiletalk at right
    kon "Absolutely! And over there are the Bengal gram plants. They’re known for their nutty flavor and are perfect for making dal or adding to our attu batter."

menu:
    "Learn about Bengal Gram?":
        jump exp_choice3
    "I'm Good!":
        jump common3

label exp_choice3:

    scene bg BengalGramMap
    with fade
    "Bengal gram is also called Chana or Chickpea “సెనగ పప్పు”. It’s round, yellowish, and super healthy! People in Telangana use it to make crunchy, golden atlu and many other dishes. It’s a food full of flavor and love, passed down through generations."
    "Bengal gram is cultivated in districts like Adilabad, Nirmal, Nizamabad, Kamareddy, Sangareddy and Gadwal in Telangana."

    jump common3

label common3:

    scene bg pond_side 
    with fade   
    "They continued their exploration, admiring the variety of crops around them."

    "As they gathered their ingredients, Amidalraji couldn’t help but feel grateful for the abundance of nature around them. Finally, with their bags filled with green gram, Bengal gram, pigeon peas, and other seeds native to Telangana, they returned to their shady spot under the tree. "

    show a_smiletalk at left
    ami "Now that we have everything, let’s soak these seeds and grind them into a batter."
    play sound "collectgrains.mp3"
    show k_smilewide at right
    kon "I can already imagine how soft and fluffy those atlu will be!"

    "With laughter and excitement in the air, they prepared to create their delicious meal together. The aroma of fresh ingredients filled their senses as they looked forward to enjoying the fruits of their labor."

label home:
    play sound "footsteps.mp3"
    scene bg House
    with fade

    "After gathering a variety of seeds, they returned home, their bags full and their spirits high. "

    show a_normal at left
    ami "Now that we have everything, let’s soak these seeds and grind them together."
    play sound "paper-rustle.mp3"
    show k_normal at right
    kon "I’ll start grinding while you go wash up at the pond. We need to hurry before it gets too hot!"
    play sound "decision_twinkle.mp3"

menu:
    "KONTAMALLI’S POV(Stay at home and prepare Yummy atlu?)":
        jump main_a

    "AMIDALRAJI’S POV(Head to pond for a splash and wash-up?)":
        jump main_b

label main_a:
    play sound "intro_to_game.mp3"

    scene bg House 
    with fade

    "Amidalraji nodded and dashed off to the pond, leaving Kontamalli to prepare the attu batter. "

    show bg HouseFire
    with dissolve
    show k_smilewide at right   
    kon  "'The atlu will be perfect if I pour the batter now. They’ll be hot and fluffy!'"

    show bg plain_stove1
    with dissolve
    "She carefully poured the batter into the hot pan. Ssssss!"
    play sound "atly_sizling.mp3"

    show bg batter_pour2
    with dissolve
    "As she poured the batter onto the cast iron pan, she couldn’t help but feel excited about the delicious meal ahead."

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
    "The kitchen smelled amazing."
    "But Amidalraji was taking a long time… and Kontamalli’s tummy was rumbling."
    show k_mouthopen at right
    kon "The atlu are ready! I can’t wait any longer."

    show k_eating at right
    "She quickly grabbed two atlu for herself, savoring each bite. "

    show k_pouting at right
    "After finishing her second attu, she thought about Amidalraji's return."
    play sound "mischief.mp3"

    show k_eating at right
    kon "'I should save some for her... but just one more won't hurt!' She devoured another attu, leaving only one behind as she heard footsteps approaching."
    play sound "crunch.mp3"
    play sound "footsteps.mp3"

    show a_curious at left
    ami "I’m back! What about the atlu? I was so hungry!"

    show k_smiletalk at right
    kon "Well... I ate them all."
    
    show a_disappointed at left
    ami "How could you eat them all? We worked so hard to gather those ingredients!"
    play sound "decision_twinkle.mp3"

menu:
    "Be cheeky":
        jump main_a_1
    "Apologize to Amidalraji":
        jump main_a_2

label main_a_1:
    hide k_smiletalk
    show k_eating at right
    kon  "'I ate them like this!' She mimicked taking big bites, hoping to bring a smile back to Amidāl Rāji's face."
    play sound "eat_crunchy.mp3"
    jump main_a_common

label main_a_2:
    play sound "transition_from_scenetoscene.mp3"
    hide k_smiletalk
    show k_pouting at right
    kon "I’m sorry Amidalraji"
    show k_mouthopen at right
    kon  "I couldn’t resist! They were so hot and delicious. Look, I saved one for you." 
    jump main_a_common

label main_a_common:
    show a_disappointed at left
    " Amidalraji sighed. She was a little sad... but also couldn’t stop smiling at her silly friend."
    show a_smiletalk at left    
    ami "Next time, let’s do it together. I won’t go to the pond if it means missing out on our atlu."

    show k_smiletalk at right
    kon "Only if you promise to send me to wash up again! That way, I can enjoy my share without waiting."

    show a_eyesclose_smilewide at left
    show k_eyesclose_smilewide at right
    "Only if I get to wash up next time. That way, I get the first bite!"
    play sound "laughing.mp3"
    "The two friends burst into laughter."
    return

label main_b:
    play sound "transition_from_scenetoscene.mp3"
    scene bg pond_side
    with fade
    
    "As Amidalraji made her way to the pond, she felt a mix of excitement and anticipation. The prospect of enjoying the atlu they had worked so hard to prepare filled her with joy. "

################GAME GAME GAME GAME ######################################################
    python:
        import random
        import pygame
 
        class Fish():
            def __init__( self ):
                self.image = Image( "minigame_fish_catcher/fish.png" )
                self.active = False
                self.dimensions = [ 100, 150 ]
                self.position = [ 0, 0 ]
                self.speed = [ 0, 10 ]
                self.maxY = 500
            # __init__
 
            def createNew( self ):
                #self.position[0] = random.randrange( 0, 8 ) * 100
                self.position[0] = random.randrange(160, 1560 - self.dimensions[0])
                self.position[1] = 0 - self.dimensions[1]                  # Start off-screen
                self.speed[1] = random.randrange( 2, 7 )
                self.active = True
            # createNew
 
            def update( self, deltaTime ):
                if ( self.active ):
                    self.position[1] += self.speed[1]
 
                if ( self.position[1] > self.maxY ):
                    self.active = False
            # update
 
            def isCaught( self, dogPosition, dogDimensions ):
                if ( dogPosition[0] < self.position[0] + self.dimensions[0] and
                        dogPosition[0] + dogDimensions[0] > self.position[0] and
                        dogPosition[1] < self.position[1] + self.dimensions[1] and
                        dogPosition[1] + dogDimensions[1] > self.position[1] ):
                    self.active = False
                    return True
 
                return False
            # isCaught
 
            def render( self, renderer, shownTimebase, animationTimebase ):
                if ( self.active ):
                    r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                    renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render 
        # Fish
 
        class Player():
            def __init__( self ):
                self.image = Image( "minigame_fish_catcher/dog.png" )
                self.dimensions = [ 100, 150 ]
                self.position = [ 960, 700 ]
                self.speed = [ 100, 10 ]
                self.grabCounter = 0
                self.grabCounterMax = 20
                self.action = "NONE"
                self.score = 0
            # __init__
 
            def handleInput( self, action ):
                if ( self.grabCounter <= 0 ):
                    self.action = action
            # handleInput
 
            def update( self, deltaTime ):
                if ( self.grabCounter > 0 ):
                    if ( self.grabCounter > self.grabCounterMax/2 ):
                        self.position[1] -= self.speed[1] * deltaTime
                    else:
                        self.position[1] += self.speed[1] * deltaTime
 
                    self.grabCounter -= 1
                    if ( self.grabCounter == 0 ):
                        self.position[1] = 700
 
                else:
                    if ( self.action == "LEFT" and self.grabCounter <= 0 ):
                        self.position[0] -= self.speed[0] * deltaTime
 
                    elif ( self.action == "RIGHT" and self.grabCounter <= 0 ):
                        self.position[0] += self.speed[0] * deltaTime
 
                    elif ( self.action == "GRAB" and self.grabCounter <= 0 ):
                        self.grabCounter = self.grabCounterMax
 
                    # Adjust position - can't go off screen!
                    if ( self.position[0] < 0 ):
                        self.position[0] = 0
                    elif ( self.position[0] > 1800 - self.dimensions[0] ):
                        self.position[0] = 1800 - self.dimensions[0] 
 
                self.action = "NONE"
            # update
 
            def render( self, renderer, shownTimebase, animationTimebase ):
                r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render
        # Player
 
        class FishCatcherGame( renpy.Displayable ):
 
            def __init__( self ):
                renpy.Displayable.__init__( self )
 
                # Maybe I'll write a sub-class for this stuff
                self.player = Player()
 
                self.debug = []
                self.counter = 0
 
                self.fish = []
                self.fishCaught = 0
 
                self.lastStart = None   
                self.frameRate = 60
 
                self.clock = pygame.time.Clock()
                self.countdown = 30
                self.milliseconds = 0
 
                self.gameover = False
            # __init__
 
            def event( self, event, x, y, shownTimebase ):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.handleInput( "GRAB" )
                    # Up Key
 
                    if event.key == pygame.K_LEFT:
                        self.player.handleInput( "LEFT" )
                    # Left Key
 
                    if event.key == pygame.K_RIGHT:
                        self.player.handleInput( "RIGHT" )
                    # Right Key
                # KEYDOWN
 
            # event
 
            def update( self, shownTimebase, animationTimebase ):
                delta = self.getDelta( shownTimebase )
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate
 
                if ( self.gameover == False ):
 
                    chance = random.randrange( 0, 20 )
                    if ( chance == 0 and len( self.fish ) < 2 ):
                        fish = Fish()
                        fish.createNew()
                        self.fish.append( fish )
 
                    removalList = []
                    # TODO: There is probably a more Python-idiomatic way to do this
                    for fish in self.fish:
                        fish.update( 1 )
 
                        if ( fish.isCaught( self.player.position, self.player.dimensions ) ):
                            self.player.score += 1
 
                        if ( fish.active == False ):
                            removalList.append( fish )
 
                    for fish in removalList:
                        self.fish.remove( fish )
 
                    self.player.update( 1 )
 
                    if ( self.milliseconds > 1000 ):
                        self.countdown -= 1
                        self.milliseconds = 0
 
                    self.milliseconds += self.clock.tick_busy_loop( 60 )
                    if ( self.countdown <= 0 ):
                        self.gameover = True
 
                    # TODO: Remove
                    del self.debug[:]
                    self.debug.append( "Debugging" )
                    self.debug.append( "Random: " + str( chance ) )
                    self.debug.append( "Dog Position: " + str( self.player.position[0] ) + ", " + str( self.player.position[1] ) )
                    for fish in self.fish:
                        self.debug.append( "Fish position: " + str( fish.position[0] ) + ", " + str( fish.position[1] ) + ", Active: " + str( fish.active ) )
                    self.debug.append( "Delta: " + str( delta ) )
 
                # Run while game is not over
            # update

            def render( self, width, height, shownTimebase, animationTimebase ):
                self.update( shownTimebase, animationTimebase )
                renderer = renpy.Render( width, height )
 
                if ( self.gameover == False ):
                    for fish in self.fish:
                        fish.render( renderer, shownTimebase, animationTimebase )
 
                    self.player.render( renderer, shownTimebase, animationTimebase )
 
                    counter = 0
                    for debug in self.debug:
                        txt = Text( _( debug ), size=10 )
                        textRender = renpy.render( txt, 800, 600, shownTimebase, animationTimebase )
                        renderer.blit( textRender, ( 0, 10 * counter ) )
                        counter += 1
 
                else: #Gameover
                    renpy.jump( "continuation" )
                    

 
                txtScore = Text( _( "Time: " + str( self.countdown ) ), size=20 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 0 ) )
 
                txtScore = Text( _( "Fish Caught: " + str( self.player.score ) ), size=20 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 20 ) )
 
 
                renpy.redraw( self, 0 )
 
                return renderer
            # render
 
            def per_interact( self ):
                renpy.timeout( 0 )
                renpy.redraw( self, 0 )
            # per_interact
 
            def getDelta( self, shownTimebase ):
                if self.lastStart is None:
                    self.lastStart = shownTimebase
 
                delta = shownTimebase - self.lastStart
                self.lastStart = shownTimebase
 
 
 
                return delta
            # updateRate
        # FishCatcherGame

 
    label fish_catcher:    
        window hide None

    scene bg pond
    with fade
 
    python:
        ui.add( FishCatcherGame() )
        ui.interact( suppress_overlay=True, suppress_underlay=True )
    
    
################GAME GAME GAME GAME ######################################################
    label continuation:
        play sound "water_splash.mp3"

        show a_curious at left     
        play sound "water_splash.mp3"
        play sound "water_splash.mp3"
    
        ami "Time for a quick splash! I’ll feel fresh—and ready for hot atlu!"
        show a_normal at left
        ami "Ah, this feels refreshing! A quick wash will do wonders. I hope Kontamalli is grinding that batter well."
        "She dipped her hands in the cool water and smiled. The pond sparkled in the sunlight, and little fish zipped by."
        "With a spring in her step, she hurried back, her stomach rumbling in anticipation of the delicious meal. As she approached their resting place, the aroma of freshly cooked atlu wafted through the air, making her mouth water. "

        show bg HouseFire
        with dissolve
        play sound "footsteps.mp3"

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
        play sound "decision_twinkle.mp3"

menu:
    "Decide to scold her":
        jump main_b_1
    " Forgive Kontamalli":
        jump main_b_2

label main_b_1:
    play sound "transition_from_scenetoscene.mp3"
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

    play sound "laughing.mp3"
    show a_eyesclose_smilewide at left
    show k_eyesclose_smilewide at right
    "With laughter bubbling between them, Amidalraji realized that even in moments of mischief, their friendship remained strong. The bond they shared over food and fun was what truly mattered."
    
    return
