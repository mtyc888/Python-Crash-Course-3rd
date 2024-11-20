from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        #All walks start at (0, 0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        #Keep taking steps until the walk reaches the desired length
        #as long as x_value is lower than 5000 (limit) continue to run the loop
        while len(self.x_value) < self.num_points:
            
            x_step = self.fill_steps()
            y_step = self.fill_steps()

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            #To get the next x-value for the walk, we add the value in x_step to the last value stored in x_values. Do the same for y as well
            #x_value[-1] refers to the last element of the x_value array
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            #When we have the new point's coodinates, append them to x_values and y_values
            self.x_value.append(x)
            self.y_value.append(y)

    def fill_steps():
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8]) 

        steps = direction * distance
        return steps