import math
import numpy as np

class sphere(object):
    def __init__(self, samples):
        self.points = np.array([0,0,0])
        self.points_center = np.array([0,0,0])
        phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians
        nb_points = range(0,int(samples+1))
        for i in nb_points:
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius = math.sqrt(1 - y * y)  # radius at y

            theta = phi * i  # golden angle increment

            x = math.cos(theta) * radius
            z = math.sin(theta) * radius
         #   self.points = np.vstack((self.points, np.array([x,y,z])))
        #self.points = np.delete(self.points, (0), axis = 0)


    def translation(self, center):
        centre=np.array(center)
        print(centre)
        for i in range(0,len(self.points)):
            #print(self.points[i])
            #print(center)
            print(self.points[i], centre)
            print(len(self.points[i]+centre))
            self.points_center = np.vstack((self.points_center, self.points[i]+centre))


    def __str__(self):596
        return("{}".format(self.points))

class vector(object):
    def __init__(self, sphere, maxi, centre):
        self.vector = np.array([0,0,0]) # x, y, z, x', y', z'
        for i in range(0,len(sphere.points_center)):

            pass

    def __str__(self):
        return("{}".format(self.vector))




def fs(samples=1, centre=[0,0,0], rayon=1):

    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append((x, y, z))

    return points


