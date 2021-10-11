def aantal_kluizen_vrij() :
    kluizentxt = open("fa_kluizen.txt", "r")
    kluiscodes = kluizentxt.readlines()
    kluizenover = 12 - len(kluiscodes)
    kluizentxt.close()
    print("Op het moment zijn er", kluizenover, "kluizen over")
    return kluizenover

aantal_kluizen_vrij()
