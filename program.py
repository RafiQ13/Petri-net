class Arc:
    def __init__(self, source, target, weight):
        if type(source) != type(target):
            self.source = source
            self.target = target
            self.weight = weight
        else:  
            raise ValueError("Arcs must connect objects of different types.")
    # Function to create an Arc with error handling
    def create_arc():
        while True:
            try:
                source_name = input("Enter the name of the source: ")
                if source_name != place.name and source_name != transition.name:
                    raise ValueError("Source name does not exist. Please enter an existing place or transition name.")
                
                target_name = input("Enter the name of the target: ")
                if target_name != place.name and target_name != transition.name:
                    raise ValueError("Target name does not exist. Please enter an existing place or transition name.")
                
                weight = int(input("Enter the weight of the arc: "))
                
                # Create source and target objects based on user input
                source = place if source_name == place.name else transition
                target = place if target_name == place.name else transition
                
                return Arc(source, target, weight)
            except ValueError as e:
                print(e)

class Place:
    def __init__(self, name, tokens=0):
        self.name = name
        self.tokens = tokens

    def add_tokens(self, num_tokens):
        self.tokens += num_tokens

    def remove_tokens(self, num_tokens):
        if self.tokens >= num_tokens:
            self.tokens -= num_tokens
        else:
            print("Error: Not enough tokens in the place.")
    # Function to create a Place with error handling
    def create_place():
        while True:
            try:
                name = input("Enter the name of the place: ")
                initial_tokens = int(input("Enter the initial number of tokens for the place: "))
                return Place(name, initial_tokens)
            except ValueError:
                print("Invalid input. Please enter a valid number for initial tokens.")

class Transition:
    def __init__(self, name):
        self.name = name


    # Function to create a Transition with error handling
    def create_transition():
        while True:
            name = input("Enter the name of the transition: ")
            return Transition(name)




# Create objects with error handling
while True:
    try:
        place = Place.create_place()
        transition = Transition.create_transition()
        arc = Arc.create_arc() 
        break
    except ValueError as e:
        print(e)

# Output
print("Place created:", place.name)
print("Transition created:", transition.name)
print("Arc created from", arc.source.name, "to", arc.target.name, "with weight", arc.weight)
