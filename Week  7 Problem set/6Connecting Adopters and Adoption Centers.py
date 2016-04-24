def get_ordered_adoption_center_list(Adopter, Centers):
                T=[]; [T.append ((Adopter.get_score(c),c)) for c in Centers]
                T.sort (key=lambda t: (-t[0],t[1].get_name()))
                return [t[1] for t in T]

def get_adopters_for_advertisement(Center,Adopters,n):
                T=[]; [T.append ((a.get_score(Center), a)) for a in Adopters]
                T.sort (key=lambda t: (-t[0],t[1].get_name()))
                return [t[1] for t in T[:n]]


