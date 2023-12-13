import time

en_pause = False


def afficher_heure(heure, mode_12h=False):
    if mode_12h:
        am_pm = "AM" if heure[0] < 12 else "PM"
        heure[0] = (heure[0] - 1) % 12 + 1  # Convertir l'heure au format 12h
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}")
    else:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def regler_heure(heure, nouvelles_heures, nouvelles_minutes, nouvelles_secondes):
    heure = (nouvelles_heures, nouvelles_minutes, nouvelles_secondes)
    return heure

def regler_alarme(alarme, heures_alarme, minutes_alarme, secondes_alarme):
    alarme = (heures_alarme, minutes_alarme, secondes_alarme)
    return alarme

def verifier_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print("Alarme ! L'heure programmée est atteinte.")

#  (12 heures ou 24 heures)
def choisir_mode_affichage():
    mode_12h = input("Choisissez le mode d'affichage (12h ou 24h) : ").lower()
    return mode_12h == "12h"

# en pause
def mettre_en_pause():
    global en_pause
    en_pause = not en_pause

heure_actuelle = (0, 0, 0)

#alarme
alarme = (0, 0, 10)

# Mode d'affichage initial
mode_12h = choisir_mode_affichage()

try:
    while True:
        
        while en_pause:
            time.sleep(1)

        afficher_heure(heure_actuelle, mode_12h)

        
        verifier_alarme(heure_actuelle, alarme)

        
        time.sleep(1)

        
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

        if heure_actuelle[2] == 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
        if heure_actuelle[1] == 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])
        if heure_actuelle[0] == 24:
            heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])

except KeyboardInterrupt:
    print("Programme arrêté par l'utilisateur.")
