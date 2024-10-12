import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def naplat(cislo, pocet_platnych_cislic):
    if cislo == 0:
        return 0  # Ak je číslo nula, vrátiť nulu
    return np.around(cislo, -int(np.floor(np.log10(abs(cislo))) - (pocet_platnych_cislic - 1)))



# ÚLOHA 1

#Zoznamy dát
objemy_zř_st_DNA = {
    'v1': 0.0,
    'v2': 0.5,
    'v3': 1.0,
    'v4': 1.5,
    'v5': 2.0,
    'v6': 2.5
}

objemy_fyzio_r = {
    'v1': 2.5,
    'v2': 2.0,
    'v3': 1.5,
    'v4': 1.0,
    'v5': 0.5,
    'v6': 0.0
}

absorbance_st_DNA = {
    'A1': 0.000,
    'A2': 0.076,
    'A3': 0.157,
    'A4': 0.234,
    'A5': 0.314,
    'A6': 0.401
}

# Absorbancia neznámeho vzorku DNA
absorbance_neznámé_DNA = 0.468

# Koncentrácia DNA v zř st DNA
koncentracia_st_DNA = 0.025  # mg/ml

# Funkcia na výpočet koncentrácií DNA
def vypocitaj_koncentracie(objemy_zř_st_DNA, objemy_fyzio_r, koncentracia_st_DNA):
    koncentracie = {}
    for key in objemy_zř_st_DNA:
        # Spočítať celkový objem (zř st DNA + fyzio roztok)
        total_volume = objemy_zř_st_DNA[key] + objemy_fyzio_r[key]
        # Vypočítať koncentráciu DNA v danom roztoku
        if total_volume > 0:
            koncentracia = (objemy_zř_st_DNA[key] * koncentracia_st_DNA) / total_volume
        else:
            koncentracia = 0  # Ak je celkový objem 0, koncentrácia je tiež 0
        koncentracie[key] = koncentracia
    return koncentracie
# Výpočet koncentrácií pre štandardné roztoky (in a variable)
koncentracie = vypocitaj_koncentracie(objemy_zř_st_DNA, objemy_fyzio_r, koncentracia_st_DNA)

# Prevod koncentrácií na list a zodpovedajúcich absorbancií
koncentracie_list = list(koncentracie.values())
absorbance_list = list(absorbance_st_DNA.values())

# Funkcia pre vytvorenie kalibračnej krivky a určenie koncentrácie neznámeho vzorku
def kalibracna_krivka(koncentracie_list, absorbance_list, absorbance_neznámé_DNA):
    # Lineárna regresia
    slope, intercept, r_value, p_value, std_err = linregress(koncentracie_list, absorbance_list)
    
    # Zobrazenie rovnice kalibračnej krivky
    print(f'Rovnica kalibračnej krivky: y = {slope:.4f}x + {intercept:.4f}')
    
    # Určenie koncentrácie neznámeho vzorku na základe absorbancie
    koncentracia_neznámeho_zř = (absorbance_neznámé_DNA - intercept) / slope
    absorpčný_koeficient = absorbance_neznámé_DNA / koncentracia_neznámeho_zř
    koncentracia_neznámeho = koncentracia_neznámeho_zř * 40
    print(f'Koncentrácia neznámeho vzorku DNA: {naplat(koncentracia_neznámeho,3)} mg/ml')

    # Porovnanie so známymi hodnotami absorpčných koeficientov
    absorbance_ds_DNA = 0.5  # ml.mg-1.cm-1 pre ds-DNA
    absorbance_ss_DNA = 0.6  # ml.mg-1.cm-1 pre ss-DNA
    hranice = absorbance_ds_DNA + ((absorbance_ss_DNA-absorbance_ds_DNA)/2)
    
    # Porovnanie vypočítaného koeficientu so známymi hodnotami
    if absorbance_neznámé_DNA < hranice:
        print(f'Vzorka obsahuje nativnú DNA (ds-DNA)')
    elif hranice < absorbance_neznámé_DNA:
        print(f'Vzorka obsahuje denaturovanú DNA (ss-DNA)')

    print(f'Absorpčný koeficient: {naplat(absorpčný_koeficient,3)} ml.mg-1.cm-1')

    # Graf kalibračnej krivky
    plt.figure(figsize=(8, 6))
    plt.scatter(koncentracie_list, absorbance_list, color='blue', label='Štandardné vzorky')
        
    # Vyznačenie neznámeho bodu na grafe
    plt.scatter(koncentracia_neznámeho_zř, absorbance_neznámé_DNA, color='purple', label='Neznáma vzorka', zorder=5)
    
    # Rovnica priamky
    x_vals = np.linspace(0, max(koncentracie_list), 100)
    y_vals = slope * x_vals + intercept
    plt.plot(x_vals, y_vals, color='red', label=f'y = {slope:.4f}x + {intercept:.4f}')

    # Pridanie názvov a legendy
    plt.title('Graf závislosti absorbance na koncentraci')
    plt.xlabel('Koncentrácia (mg/ml)')
    plt.ylabel('Absorbancia (260 nm)')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend()
    plt.grid(True)
    plt.savefig(('kalibrační křivka.png'), bbox_inches='tight')
    # plt.show()
# Vypočítanie kalibračnej krivky a určenie koncentrácie neznámeho vzorku
kalibracna_krivka(koncentracie_list, absorbance_list, absorbance_neznámé_DNA)