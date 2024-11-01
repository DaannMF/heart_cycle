import numpy as np
import matplotlib.pyplot as plt

def simulate_heart_cycle(state="Reposo"):
    # Parámetros de cada estado fisiológico
    heart_rate = {"Reposo": 60, "Correr": 150, "Dormir": 50, "Caminar": 80, "Trotar": 120, "Muerto" : 0}
    systolic_pressure = {"Reposo": 120, "Correr": 180, "Dormir": 100, "Caminar": 130, "Trotar": 160, "Muerto" : 0}
    diastolic_pressure = {"Reposo": 80, "Correr": 110, "Dormir": 60, "Caminar": 85, "Trotar": 100, "Muerto" : 0}
    end_diastolic_volume = {"Reposo": 120, "Correr": 140, "Dormir": 110, "Caminar": 125, "Trotar": 135, "Muerto" : 0}
    end_systolic_volume = {"Reposo": 50, "Correr": 60, "Dormir": 55, "Caminar": 58, "Trotar": 65, "Muerto" : 0}

    # Parámetros del estado seleccionado
    freq = heart_rate.get(state, 60) / 60  # Frecuencia cardíaca en Hz
    press_syst = systolic_pressure.get(state, 120)
    press_diast = diastolic_pressure.get(state, 80)
    vol_diast = end_diastolic_volume.get(state, 120)
    vol_syst = end_systolic_volume.get(state, 50)

    # Tiempo para un ciclo cardíaco
    t = np.linspace(0, 1, 500)  # Simulación de 1 segundo (un ciclo cardíaco)
    
    # Simulación de la presión aórtica
    pressure_wave = press_diast + (press_syst - press_diast) * np.sin(2 * np.pi * freq * t) ** 2

    # Simulación del volumen ventricular izquierdo
    volume_wave = vol_syst + (vol_diast - vol_syst) * (1 + np.sin(2 * np.pi * freq * t)) / 2

    # Crear la figura y los subplots
    plt.figure(f"Simulación del Ciclo Cardíaco - Estado: {state}")

    # Gráfico de presión aórtica
    ax1 = plt.subplot(211)
    ax1.plot(t, pressure_wave, 'r-', label="Presión Aórtica (mmHg)")
    ax1.set_ylabel("Presión (mmHg)", color="r")
    ax1.tick_params(axis="y", labelcolor="r")
    ax1.legend(loc="lower center")
    ax1.grid(True)

    # Segundo eje y para el volumen ventricular
    ax2 = plt.subplot(212)
    ax2.plot(t, volume_wave, 'tab:pink', label="Volumen Ventricular Izquierdo (ml)")
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Volumen (ml)", color="tab:pink")
    ax2.tick_params(axis="y", labelcolor="tab:pink")
    ax2.legend(loc="lower center")
    ax2.grid(True)

    # Mostrar gráfica
    plt.show()

# Ejemplo de uso
simulate_heart_cycle("Dormirccl")
