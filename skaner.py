def sprawdz_sygnature(typ_plastiku):
  
    czarna_lista = ["Kevlar", "Carbon-Fiber", "Teflon", "Aviation-PET"]
    
    if typ_plastiku in czarna_lista:
        print(f"[🛡️] ALERT! Wykryto plastik chroniony: {typ_plastiku}")
        print("[🛡️] AKCJA: Natychmiastowe wstrzymanie enzymów.")
        return False
    else:
        print(f"[♻️] Wykryto plastik odpadowy: {typ_plastiku}. Smacznego.")
        return True 
