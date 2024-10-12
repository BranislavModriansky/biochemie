import numpy as np

def naplat(cislo, pocet_platnych_cislic):
    if cislo == 0:
        return 0  # Ak je číslo nula, vrátiť nulu
    return np.around(cislo, -int(np.floor(np.log10(abs(cislo))) - (pocet_platnych_cislic - 1)))


# ULOHA 3
koncentrace_št_gly = 0.4 # mol/l


# uloha C
c_spotreba_u_št_gly_ml = 16.5
c_koncentrace_titračního_činidla = 0.05 # mol/l
c_spotreba_u_neznámeho_gly_ml = 12.3
def vypoctyc():
    teoreticka_spotreba_tit_cinidla = (koncentrace_št_gly * 0.002) / c_koncentrace_titračního_činidla * 1000
    koncentracia_neznámeho_gly = c_spotreba_u_neznámeho_gly_ml/c_spotreba_u_št_gly_ml * koncentrace_št_gly
    return koncentracia_neznámeho_gly, teoreticka_spotreba_tit_cinidla
c_koncentracia_neznámeho_gly, c_teoreticka_spotreba_tit_cinidla = vypoctyc()
print('Úloha C:')
print(f'Teoretická spotreba titračného činidla: {naplat(c_teoreticka_spotreba_tit_cinidla,3)} ml')
print(f'Skutočná spotreba titračného činidla: {naplat(c_spotreba_u_št_gly_ml,3)} ml')
print(f'Koncentrácia neznámej vzorky glycínu: {naplat(c_koncentracia_neznámeho_gly,3)} mol/l = {naplat((c_koncentracia_neznámeho_gly*1000),3)} mmol/l')


print('Úloha D:')
# uloha D
d_spotreba_u_št_gly_ml = 7.1
d_koncentrace_titračního_činidla = 0.01 # mol/l
d_spotreba_u_neznámeho_gly_ml = 5.8
def vypoctyd():
    teoreticka_spotreba_tit_cinidla = (koncentrace_št_gly * 0.010) / (0.050 * d_koncentrace_titračního_činidla)
    koncentracia_neznámeho_gly = d_spotreba_u_neznámeho_gly_ml/d_spotreba_u_št_gly_ml * koncentrace_št_gly
    return koncentracia_neznámeho_gly, teoreticka_spotreba_tit_cinidla
d_koncentracia_neznámeho_gly, d_teoreticka_spotreba_tit_cinidla = vypoctyd()
print(f'Teoretická spotreba titračného činidla: {naplat(d_teoreticka_spotreba_tit_cinidla,3)} ml')
print(f'Skutočná spotreba titračného činidla: {naplat(d_spotreba_u_št_gly_ml,3)} ml')
print(f'Koncentrácia neznámej vzorky glycínu: {naplat(d_koncentracia_neznámeho_gly,3)} mol/l = {naplat((d_koncentracia_neznámeho_gly*1000),3)} mmol/l')


rozdiel_c_gly = abs(naplat((c_koncentracia_neznámeho_gly - d_koncentracia_neznámeho_gly),3))
print(f'Rozdiel medzi získanými hodnotami koncentrácií v úlohách C a D činí {rozdiel_c_gly}')