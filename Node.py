class Node:
    def __init__(self, x, y, known_value=None):
        self.x = x
        self.y = y


        if known_value is None:
            self.possible_values = {1,2,3,4,5,6,7,8,9}
            self.value = 0 
            self.known_value = False
        else:
            self.possible_values = {known_value}
            self.value = known_value
            self.known_value = True

    def update_val(self):
        if self.known_value:
            raise ValueError("Node with known value cannot be updated")
        # Return False if no possible values left
        if len(self.possible_values) == 0:
            return False

        self.value = self.possible_values.pop()
        return True
    
    def reset(self):
        if self.known_value:
            raise ValueError("Node with known value cannot be reset")
        self.possible_values = {1,2,3,4,5,6,7,8,9}
        self.value = 0
