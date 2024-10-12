import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# ÚLOHA 1

# Zoznamy dát - praktická časť B
objem_s_B = {
    'v1': 0.5,
    'v2': 1.0,
    'v3': 1.5,
    'v4': 2.0,
    'v5': 2.5,
    'v6': 3.0
}
objem_r_B = {
    'v1': 4.5,
    'v2': 4.0,
    'v3': 3.5,
    'v4': 3.0,
    'v5': 2.5,
    'v6': 2.0
}

absorbance_B = {
    'A1': 0.125,
    'A2': 0.224,
    'A3': 0.327,
    'A4': 0.432,
    'A5': 0.529,
    'A6': 0.626
}

# Zoznamy dát - praktická časť C
objem_s_C = {
    'v1': 0.2,
    'v2': 0.4,
    'v3': 0.6,
    'v4': 0.8,
    'v5': 1.0
} 
objem_r_C = {
    'v1': 1.8,
    'v2': 1.6,
    'v3': 1.4,
    'v4': 1.2,
    'v5': 1.0
} 

absorbance_C = {
    'A1': 0.111,
    'A2': 0.208,
    'A3': 0.313,
    'A4': 0.417,
    'A5': 0.487
}

# Zoznamy dát - praktická časť D
objem_s_D = {
    'v1': 0.02,
    'v2': 0.04,
    'v3': 0.06,
    'v4': 0.08,
    'v5': 0.10
}
objem_r_D = {
    'v1': 1.98,
    'v2': 1.96,
    'v3': 1.94,
    'v4': 1.92,
    'v5': 1.90
} 

absorbance_D = {
    'A1': 0.136,
    'A2': 0.228,
    'A3': 0.328,
    'A4': 0.421,
    'A5': 0.514
}

def zadaj_zoznamy(dict1, dict2, dict3):
    def vypocitej_koncentrace(dict1, dict2):


        # Základná koncentrácia (mol/l)  !!! V ulohe A a B [0.001]. V ulohe D [0.01] !!!
        c = 0.01  


        vypocetni_koncentrace = {}
        
        for key in dict1:
            concentration = np.round((c * dict1[key] / (dict1[key] + dict2[key]) * 1000), 4)  # Calculate concentration
            vypocetni_koncentrace[key] = [concentration, 'mmol.l-1']
            print(f'koncentrace v směsi {key} je {concentration:.1f} {vypocetni_koncentrace[key][1]}')

        return vypocetni_koncentrace
    koncentrace = vypocitej_koncentrace(dict1, dict2)

    def kalibrační_graf(dict3):
        # Extracting concentrations and absorbance values for plotting
        concentration_values = [value[0] for value in koncentrace.values()]
        absorbance_values = list(dict3.values())

        # Ensuring the graph starts from (0, 0)
        concentration_values.insert(0, 0)  # Add a point at (0, 0) for x-axis
        absorbance_values.insert(0, 0)  # Add a corresponding absorbance value of 0

        # Plotting the absorbance curve
        plt.figure(figsize=(8, 6))
        plt.scatter(concentration_values, absorbance_values, color='blue', label='Data Absorbance')

        # Linear regression to find the line equation
        slope, intercept, r_value, p_value, std_err = linregress(concentration_values, absorbance_values)

        # Plotting the line
        line_x = np.linspace(0, max(concentration_values), 100)
        line_y = slope * line_x + intercept
        plt.plot(line_x, line_y, color='red', label=f'Line: y = {slope:.3f}x + {intercept:.3f}')

        # Molar absorptive coefficient (ε)
        elypson = slope  # Since slope = ε (molar absorptive coefficient)
        print(f'Molární Absorpční Koeficient (ε): {elypson:.3f} mmol.l-1')

        # Adding labels and title
        plt.title('Graf Závislosti Absorbance na Koncentraci')
        plt.xlabel('Koncentrace (mmol.l-1)')
        plt.ylabel('Absorbance (420 nm)')
        plt.xlim(left=0)  # Ensure x-axis starts at 0
        plt.ylim(bottom=0)  # Ensure y-axis starts at 0
        plt.legend()
        plt.grid()
        plt.savefig(('kalibrační křivka.png'), bbox_inches='tight')
        #plt.show()
    kalibrační_graf(dict3)
#Zadaj zoznamy v poradí: objem_s_(príslušná praktická časť), objem_r_(príslušná praktická časť), absorbance_(príslušná praktická časť)  a v riadku č. 87 (vo funkcii) zmeniť základnú koncentráciu 
zadaj_zoznamy(objem_s_B, objem_r_B, absorbance_B) 