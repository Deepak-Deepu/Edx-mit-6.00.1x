class Adopter(AdoptionCenter):
        def __init__(self,name,desired_species):
                self.name=name
                self.desired_species=desired_species
        def get_name(self):
                return self.name
        def get_desired_species(self):
                return self.desired_species
        def get_score(self, adoption_center):
                score = 1.0*adoption_center.get_number_of_species(self.desired_species)
                assert(score>=0)
                return score

