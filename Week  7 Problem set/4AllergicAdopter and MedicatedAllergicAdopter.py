class AllergicAdopter(Adopter):
        allergic_species=[]
        def __init__(self, name, desired_species,allergic_species):
                Adopter.__init__(self,name,desired_species)
                self.allergic_species=allergic_species

        def get_score(self, adoption_center):
                list2=[]
                list3=[]
                list4=[]
                for i in self.allergic_species:
                        if i not in list2:
                                list2.append(i)
                for i in adoption_center.species_types.keys():
                        if i not in list3:
                                list3.append(i)
                if len(list2)<1:
                        return 0.0
                if len(list3)<=1:
                        return 0.0
                for i in list2:
                        if i in list3:
                                return 0.0

                return(float(Adopter.get_score(self,adoption_center)))


class MedicatedAllergicAdopter(AllergicAdopter):
        medicine_effectiveness={}
        def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
                AllergicAdopter.__init__(self,name,desired_species,allergic_species)
                self.medicine_effectiveness=medicine_effectiveness

        def get_score(self, adoption_center):
                list5=[]
                list6=[]
                list7=[]
                list5=adoption_center.species_types.keys()

                for i in self.allergic_species:
                        if i not in list6:
                                list6.append(i)

                for i in list5:
                        if i in  list6:
                                list7.append(self.medicine_effectiveness[i])


                if len(list7)<=0:
                        return(float(Adopter.get_score(self,adoption_center)))
                else:
                        return(float(min(list7)*(Adopter.get_score(self,adoption_center))))


