def sprawdz_licznik_glodu(poziom):
    """Sprawdza, czy Ideonella nie potrzebuje dokarmienia plastikiem."""
    if poziom < 10:
        return "KRYTYCZNY"
    elif poziom < 30:
        return "NISKI"
    else:
        return "OK"
