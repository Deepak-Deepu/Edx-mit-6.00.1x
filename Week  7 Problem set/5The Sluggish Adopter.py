class SluggishAdopter(Adopter):
        def __init__(self, name, desired_species, location):
                Adopter.__init__(self,name,desired_species)
                self.location = (float(location[0]),float(location[1]))

        def get_linear_distance(self, to_location):
                from math import sqrt
                d=sqrt((self.location[0]-to_location[0])**2+(self.location[1]-to_location[1])**2)
                return d


        def get_score (self, adoption_center):
                distance = self.get_linear_distance(adoption_center.get_location())
                if distance <1:
                        return  (Adopter.get_score(self,adoption_center))
                elif distance <3:
                        return (random.uniform(0.7,0.9)*(Adopter.get_score(self,adoption_center)))
                elif distance <5:
                        return (random.uniform(0.5,0.7)*(Adopter.get_score(self,adoption_center)))
                elif distance>=5:
                         return (random.uniform(0.1,0.5)*(Adopter.get_score(self,adoption_center)))


