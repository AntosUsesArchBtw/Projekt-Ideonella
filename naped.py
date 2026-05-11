import random

def oblicz_predkosc(energia_z_plastiku):
   
    bazowa_predkosc = 2.0
    bonus = energia_z_plastiku * 0.5
    return round(bazowa_predkosc + bonus, 2)

def plyn_do_celu(cel):
    kierunki = ["Północ", "Południe", "Wschód", "Zachód"]
    kierunek = random.choice(kierunki)
    print(f"[NAWIGACJA] Wykryto plastik w lokalizacji: {cel}")
    print(f"[NAPĘD] Wić białkowa pracuje. Kierunek: {kierunek}")
