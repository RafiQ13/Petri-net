from pnet import PetriNet, Place, Transition, Arc

# Function to create a Petri net with user input for places, transitions, and arcs
def create_petri_net():
    # Create a new Petri net
    net = PetriNet("My Petri Net")
    
    # Lists to store created places and transitions
    places = []
    transitions = []
    
    # Function to create a place with user input
    def create_place():
        while True:
            try:
                name = input("Enter the name of the place: ")
                initial_tokens = int(input("Enter the initial number of tokens for the place: "))
                place = Place(name, initial_tokens)
                places.append(place)
                net.add_place(place)
                return place
            except ValueError:
                print("Invalid input. Please enter a valid number for initial tokens.")
    
    # Function to create a transition with user input
    def create_transition():
        while True:
            try:
                name = input("Enter the name of the transition: ")
                transition = Transition(name)
                transitions.append(transition)
                net.add_transition(transition)
                return transition
            except ValueError:
                print("Invalid input. Please enter a valid name for the transition.")
    
    # Function to create an arc with user input
    def create_arc():
        while True:
            try:
                source_name = input("Enter the name of the source (place or transition): ")
                target_name = input("Enter the name of the target (place or transition): ")
                weight = int(input("Enter the weight of the arc: "))
                
                # Find the source and target objects based on user input
                source = next((place for place in places if place.name == source_name), None)
                target = next((place for place in places if place.name == target_name), None)
                
                if source is None and target is None:
                    raise ValueError("Source and target names do not exist. Please enter existing place or transition names.")
                elif source is None:
                    raise ValueError("Source name does not exist. Please enter an existing place or transition name.")
                elif target is None:
                    raise ValueError("Target name does not exist. Please enter an existing place or transition name.")
                
                # If both source and target are places, or both are transitions, raise an error
                if (isinstance(source, Place) and isinstance(target, Place)) or (isinstance(source, Transition) and isinstance(target, Transition)):
                    raise ValueError("Arcs must connect objects of different types.")
                
                # Create and add the arc to the Petri net
                arc = Arc(source, target, weight)
                net.add_arc(arc)
                return arc
            except ValueError as e:
                print(e)
    
    # Create objects with user input and error handling
    while True:
        try:
            place = create_place()
            transition = create_transition()
            arc = create_arc()
            create_more = input("Do you want to create more places and transitions? (yes/no): ")
            if create_more.lower() != "yes":
                break
        except ValueError as e:
            print(e)
    
    return net

# Create a Petri net
net = create_petri_net()

# Output
print("Petri net created with the following components:")
print("Places:", [place.name for place in net.places])
print("Transitions:", [transition.name for transition in net.transitions])
print("Arcs:", [(arc.source.name, arc.target.name, arc.weight) for arc in net.arcs])
