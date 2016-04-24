class FlexibleAdopter(Adopter):
        considered_species=[]
        def __init__(self, name, desired_species, considered_species):
                Adopter.__init__(self,name,desired_species)
                self.considered_species=considered_species

        def get_score(self, adoption_center):
                num_other=0
                for i in self.considered_species:
                        num_other =num_other+ 1.0*adoption_center.get_number_of_species(i)

                adopter_score=Adopter.get_score(self,adoption_center)
                score=adopter_score+0.3 * num_other
                if score<=-1:
                        return 0.0
                else:
                        return float(score)

class FearfulAdopter(Adopter):
        def __init__(self, name, desired_species, feared_species):
                Adopter.__init__(self,name,desired_species)
                self.feared_species=feared_species

        def get_score(self, adoption_center):
                num_feared=0
                num_feared =num_feared+ 1.0*adoption_center.get_number_of_species(self.feared_species)

                adopter_score=Adopter.get_score(self,adoption_center)
                score1= adopter_score-0.3 * num_feared
                if score1 <= -1:
                        return 0.0
                else:
                        return float(score1)


