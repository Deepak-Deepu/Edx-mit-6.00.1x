import random as rand
import string

class AdoptionCenter(object):
        species_types={}
        location=()
        def __init__(self,name,species_types,location):
                self.name=name
                self.species_types=species_types
                self.location=location

        def get_number_of_species(self,animal):
                list1=[]
                list1=self.species_types.keys()
                if animal in list1:
                        return self.species_types[animal]
                else:
                        return 0

        def get_location(self):
                return tuple(map(float,self.location))

        def get_species_count(self):
                for key in self.species_types.keys():
                        if self.species_types.get(key,0) <0:
                                del self.species_types[key]
                return self.species_types.copy()

        def get_name(self):
                return self.name

        def adopt_pet(self,species):
                for i in self.species_types.keys():
                        if i == species:
                                self.species_types[i] -= 1
                                if self.species_types.get(i,0) <=0:
                                        del self.species_types[i]

