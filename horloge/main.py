import time

# Variable pour indiquer si l'horloge est en pause
en_pause = False

# Fonction pour afficher l'heure au format hh:mm:ss
def afficher_heure(heure, mode_12h=False):
    if mode_12h:
        am_pm = "AM" if heure[0] < 12 else "PM"
        heure[0] = (heure[0] - 1) % 12 + 1  # Convertir l'heure au format 12h
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}")
    else:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

# Fonction pour régler l'heure
def regler_heure(heure, nouvelles_heures, nouvelles_minutes, nouvelles_secondes):
    heure = (nouvelles_heures, nouvelles_minutes, nouvelles_secondes)
    return heure

# Fonction pour régler l'alarme
def regler_alarme(alarme, heures_alarme, minutes_alarme, secondes_alarme):
    alarme = (heures_alarme, minutes_alarme, secondes_alarme)
    return alarme

# Fonction pour vérifier si l'alarme doit être déclenchée
def verifier_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print("Alarme ! L'heure programmée est atteinte.")

# Fonction pour choisir le mode d'affichage (12 heures ou 24 heures)
def choisir_mode_affichage():
    mode_12h = input("Choisissez le mode d'affichage (12h ou 24h) : ").lower()
    return mode_12h == "12h"

# Fonction pour mettre en pause ou reprendre l'horloge
def mettre_en_pause():
    global en_pause
    en_pause = not en_pause

# Heure initiale
heure_actuelle = (0, 0, 0)

# Alarme initiale
alarme = (0, 0, 10)

# Mode d'affichage initial
mode_12h = choisir_mode_affichage()

# Boucle pour actualiser l'heure toutes les secondes
try:
    while True:
        # Vérifier si l'horloge est en pause
        while en_pause:
            time.sleep(1)

        # Afficher l'heure actuelle
        afficher_heure(heure_actuelle, mode_12h)

        # Vérifier l'alarme
        verifier_alarme(heure_actuelle, alarme)

        # Attendre une seconde
        time.sleep(1)

        # Actualiser l'heure
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

        # Vérifier et ajuster les heures, minutes, secondes
        if heure_actuelle[2] == 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
        if heure_actuelle[1] == 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])
        if heure_actuelle[0] == 24:
            heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])

except KeyboardInterrupt:
    print("Programme arrêté par l'utilisateur.")
