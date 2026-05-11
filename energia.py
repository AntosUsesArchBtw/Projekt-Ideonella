def bilans_energetyczny(zjedzony_plastik):
    
    koszt_zycia = 10
    zysk = zjedzony_plastik * 2
    
    bilans = zysk - koszt_zycia
    
    if bilans > 20:
        return "NADPRODUKCJA - Można się rozmnażać"
    elif bilans >= 0:
        return "STABILNIE - Energia wystarcza na ruch"
    else:
        return "DEFICYT - Aktywacja oszczędzania (Eko-Mode)"
