
from skaner import sprawdz_sygnature
from energia import bilans_energetyczny
from bezpieczenstwo import sprawdz_licznik_glodu


typ_odpadu = "Butelka-PET"
masa_plastiku = 12 

print("--- RAPORT DO BOWY PETA-PREDATORA ---")

if sprawdz_sygnature(typ_odpadu):
    stan = bilans_energetyczny(masa_plastiku)
    print(f"[STATUS ENERGETYCZNY]: {stan}")
    

    if "DEFICYT" in stan:
        sprawdz_licznik_glodu(5) 
else:
    print("[!] Omijam obiekt chroniony.")

print("\n--- KONIEC RAPORTU ---")
