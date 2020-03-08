class sensory_words_class():
    def __init__(self):
        from nltk.stem import PorterStemmer
        stemming = PorterStemmer()
        #from nltk.tokenize import word_tokenize
        #self.sight = []
        #with open('data/sensory_words/sight.txt') as file:
        #    text = file.read()
        #self.sight = word_tokenize(text)
        self.sight = [stemming.stem(word) for word in ['Angular', 'Azure', 'Billowy', 'Black', 'Bleary', 'Bloated', 'Blonde', 'Blue', 'Blurred', 'Blushing', 'Branching', 'Bright', 'Brilliant', 'Broad', 'Brown', 'Brunette', 'Bulbous', 'Bulky', 'Camouflaged', 'Chubby', 'Circular', 'Colorful', 'Colorless', 'Colossal', 'Contoured', 'Cosmic', 'Craggy', 'Crimson', 'Crinkled', 'Crooked', 'Crowded', 'Crystalline', 'Curved', 'Dark', 'Dazzling', 'Deep', 'Dim', 'Dingy', 'Disheveled', 'Distinct', 'Drab', 'Dreary', 'Dull', 'Dusty', 'Elegant', 'Enchanting', 'Engaging', 'Enormous', 'Faded', 'Fancy', 'Fat', 'Filthy', 'Flashy', 'Flat', 'Flickering', 'Foggy', 'Forked', 'Freckled', 'Fuzzy', 'Gargantuan', 'Gaudy', 'Gigantic', 'Ginormous', 'Glamorous', 'Gleaming', 'Glimpse', 'Glistening', 'Glitter', 'Glittering', 'Globular', 'Gloomy', 'Glossy', 'Glowing', 'Gold', 'Graceful', 'Gray', 'Green', 'Grotesque', 'Hazy', 'Hollow', 'Homely', 'Huge', 'Illuminated', 'Immense', 'Indistinct', 'Ivory', 'Knotty', 'Lacy', 'Lanky', 'Large', 'Lavender', 'Lean', 'Lithe', 'Little', 'Lofty', 'Long', 'Low', 'Malnourished', 'Maroon', 'Massive', 'Miniature', 'Misshapen', 'Misty', 'Motionless', 'Mottled', 'Mountainous', 'Muddy', 'Murky', 'Narrow', 'Obtuse', 'Olive', 'Opaque', 'Orange', 'Oval', 'Pale', 'Peered', 'Petite', 'Pink', 'Portly', 'Pristine', 'Prodigious', 'Purple', 'Quaint', 'Radiant', 'Rectangular', 'Red', 'Reddish', 'Rippling', 'Rotund', 'Round', 'Ruby', 'Ruddy', 'Rusty', 'Sabotaged', 'Shadowy', 'Shallow', 'Shapeless', 'Sheer', 'Shimmering', 'Shiny', 'Short', 'Silver', 'Skinny', 'Small', 'Smudged', 'Soaring', 'Sparkling', 'Sparkly', 'Spherical', 'Spotless', 'Spotted', 'Square', 'Steep', 'Stormy', 'Straight', 'Strange', 'Striped', 'Sunny', 'Swooping', 'Tall', 'Tapering', 'Tarnished', 'Teeny-tiny', 'Tiny', 'Towering', 'Translucent', 'Transparent', 'Triangular', 'Turquoise', 'Twinkling', 'Twisted', 'Ugly', 'Unsightly', 'Unusual', 'Vibrant', 'Vivid', 'Weird', 'White', 'Wide', 'Wiry', 'Wispy', 'Wizened', 'Wrinkled', 'Wrinkly', 'Yellow']]

        # self.smell = []
        # with open('data/sensory_words/smell.txt') as file:
        #     text = file.read()
        # self.smell = word_tokenize(text)
        self.smell = [stemming.stem(word) for word in ['Ambrosial', 'Antiseptic', 'Aroma', 'Aromatic', 'Briny', 'Citrusy', 'Decayed', 'Decomposed', 'Doggy', 'Fetid', 'Floral', 'Flowery', 'Foul-smelling', 'Fragrant', 'Gamy', 'Gaseous', 'Horrid', 'Inodorous', 'Malodorous', 'Mephitic', 'Musky', 'Musty', 'Odiferous', 'Odor', 'Odorless', 'Old', 'Perfumed', 'Piney', 'Polluted', 'Pungent', 'Putrid', 'Rancid', 'Rank', 'Redolent', 'Reeking', 'Scent', 'Scented', 'Sickly', 'Skunky', 'Smell', 'Smoky', 'Stagnant', 'Stench', 'Stinky', 'Sweaty', 'Tempting', 'Acrid', 'Burnt', 'Fishy', 'Fresh', 'Fruity', 'Lemony', 'Minty', 'Moldy', 'Mouth-watering', 'Rotten', 'Salty', 'Sour', 'Spicy', 'Spoiled', 'Sweet', 'Tantalizing']]

        # self.sound = []
        # with open('data/sensory_words/sound.txt') as file:
        #     text = file.read()
        # self.sound = word_tokenize(text)
        self.sound = [stemming.stem(word) for word in ['Babble', 'Bang', 'Barking', 'Bawled', 'Bawling', 'Bellow', 'Blare', 'Blaring', 'Bleat', 'Boom', 'Booming', 'Bray', 'Buzz', 'Buzzing', 'Cackle', 'Cackling', 'Chatter', 'Chattering', 'Cheer', 'Chiming', 'Chirping', 'Chuckle', 'Clamor', 'Clang', 'Clanging', 'Clap', 'Clapping', 'Clicking', 'Clink', 'Clinking', 'Cooing', 'Coughing', 'Crackle', 'Crackling', 'Crashing', 'Creak', 'Croaking', 'Crow', 'Crunch', 'Crunching', 'Crunchy', 'Cry', 'Crying', 'Deafening', 'Distorted', 'Dripping', 'Ear-piercing', 'Earsplitting', 'Exploding', 'Faint', 'Fizzing', 'Gagging', 'Gasping', 'Giggle', 'Giggling', 'Grate', 'Grating', 'Growl', 'Grumble', 'Grunt', 'Grunting', 'Guffaw', 'Gurgle', 'Gurgling', 'Hanging', 'Hiss', 'Hissing', 'Honking', 'Howl', 'Hubbub', 'Hum', 'Humming', 'Hush', 'Jabber', 'Jangle', 'Jangling', 'Laughing', 'Moaning', 'Monotonous', 'Mooing', 'Muffled', 'Mumble', 'Mumbling', 'Murmur', 'Mutter', 'Muttering', 'Noisy', 'Peeping', 'Piercing', 'Ping', 'Pinging', 'Plopping', 'Pop', 'Purring', 'Quacking', 'Quiet', 'Rant', 'Rapping', 'Rasping', 'Raucous', 'Rave', 'Ringing', 'Roar', 'Roaring', 'Rumble', 'Rumbling', 'Rustle', 'Rustling', 'Scratching', 'Scream', 'Screaming', 'Screech', 'Screeching', 'Serene', 'Shout', 'Shouting', 'Shrieking', 'Shrill', 'Sigh', 'Silent', 'Sing', 'Singing', 'Sizzling', 'Slam', 'Slamming', 'Snap', 'Snappy', 'Snoring', 'Snort', 'Splashing', 'Squawking', 'Squeaky', 'Stammer', 'Stomp', 'Storm', 'Stuttering', 'Tearing', 'Thudding', 'Thump', 'Thumping', 'Thunder', 'Thundering', 'Ticking', 'Tingling', 'Tinkling', 'Twitter', 'Twittering', 'Wail', 'Warbling', 'Wheezing', 'Whimper', 'Whimpering', 'Whine', 'Whining', 'Whir', 'Whisper', 'Whispering', 'Whistle', 'Whooping', 'Yell', 'Yelp']]

        # self.taste = []
        # with open('data/sensory_words/taste.txt') as file:
        #     text = file.read()
        # self.taste = word_tokenize(text)
        self.taste = [stemming.stem(word) for word in ['Acidic', 'Appetizing', 'Bitter', 'Bittersweet', 'Bland', 'Buttery', 'Charred', 'Contaminated', 'Creamy', 'Crispy', 'Delectable', 'Delicious', 'Doughy', 'Earthy', 'Fermented', 'Flavorful', 'Flavorless', 'Floury', 'Garlicky', 'Gingery', 'Gritty', 'Hearty', 'Juicy', 'Luscious', 'Medicinal', 'Mellow', 'Melted', 'Nauseating', 'Nutritious', 'Nutty', 'Palatable', 'Peppery', 'Pickled', 'Piquant', 'Raw', 'Refreshing', 'Rich', 'Ripe', 'Salted', 'Savory', 'Scrumptious', 'Stale', 'Sugary', 'Syrupy', 'Tangy', 'Tart', 'Tasteless', 'Unripe', 'Vinegary', 'Yummy', 'Zesty', 'Acrid', 'Burnt', 'Fishy', 'Fresh', 'Fruity', 'Lemony', 'Minty', 'Moldy', 'Mouth-watering', 'Rotten', 'Salty', 'Sour', 'Spicy', 'Spoiled', 'Sweet', 'Tantalizing']]

        # self.touch = []
        # with open('data/sensory_words/touch.txt') as file:
        #     text = file.read()
        # self.touch = word_tokenize(text)
        self.touch = [stemming.stem(word) for word in ['Abrasive', 'Balmy', 'Biting', 'Boiling', 'Breezy', 'Bristly', 'Bubbly', 'Bubby', 'Bumpy', 'Burning', 'Bushy', 'Chilled', 'Chilly', 'Clammy', 'Coarse', 'Cold', 'Cool', 'Cottony', 'Crawly', 'Creepy', 'Cuddly', 'Cushioned', 'Damp', 'Dank', 'Dirty', 'Downy', 'Drenched', 'Dry', 'Elastic', 'Feathery', 'Feverish', 'Fine', 'Fleshy', 'Fluff', 'Fluffy', 'Foamy', 'Fragile', 'Freezing', 'Furry', 'Glassy', 'Gluey', 'Gooey', 'Grainy', 'Greasy', 'Gritty', 'Gushy', 'Hairy', 'Heavy', 'Hot', 'Humid', 'Ice-Cold', 'Icy', 'Itchy', 'Knobbed', 'Leathery', 'Light', 'Lightweight', 'Limp', 'Lukewarm', 'Lumpy', 'Matted', 'Metallic', 'Moist', 'Mushy', 'Numbing', 'Oily', 'Plastic', 'Pointed', 'Powdery', 'Pulpy', 'Rocky', 'Rough', 'Rubbery', 'Sandy', 'Scalding', 'Scorching', 'Scratchy', 'Scummy', 'Serrated', 'Shaggy', 'Sharp', 'Shivering', 'Shivery', 'Silky', 'Slimy', 'Slippery', 'Sloppy', 'Smooth', 'Smothering', 'Soapy', 'Soft', 'Sopping', 'Soupy', 'Splintery', 'Spongy', 'Springy', 'Sputter', 'Squashy', 'Squeal', 'Squishy', 'Steamy', 'Steely', 'Sticky', 'Stifled', 'Stifling', 'Stinging', 'Stony', 'Stubby', 'Tangled', 'Tapered', 'Tender', 'Tepid', 'Thick', 'Thin', 'Thorny', 'Tickling', 'Tough', 'Unsanitary', 'Velvety', 'Warm', 'Waxy', 'Wet', 'Woolly']]

if __name__ == '__main__':
    sensory = sensory_words_class()
    print('sight:\n',sensory.sight)
    print('smell:\n',sensory.smell)
    print('sound:\n',sensory.sound)
    print('taste:\n',sensory.taste)
    print('touch:\n',sensory.touch)
