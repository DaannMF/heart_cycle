import numpy as np
import matplotlib.pyplot as plt

def wiggers_diagram(state="Reposo"):
    # Parámetros de cada estado fisiológico
    heart_rate = {"Reposo": 60, "Correr": 150, "Dormir": 50, "Caminar": 80, "Trotar": 120}
    systolic_pressure = {"Reposo": 120, "Correr": 180, "Dormir": 100, "Caminar": 130, "Trotar": 160}
    diastolic_pressure = {"Reposo": 80, "Correr": 110, "Dormir": 60, "Caminar": 85, "Trotar": 100}
    end_diastolic_volume = {"Reposo": 120, "Correr": 140, "Dormir": 110, "Caminar": 125, "Trotar": 135}
    end_systolic_volume = {"Reposo": 50, "Correr": 60, "Dormir": 55, "Caminar": 58, "Trotar": 65}

    # Parámetros del estado seleccionado
    freq = heart_rate.get(state, 60) / 60  # Frecuencia cardíaca en Hz
    press_syst = systolic_pressure.get(state, 120)
    press_diast = diastolic_pressure.get(state, 80)
    vol_diast = end_diastolic_volume.get(state, 120)
    vol_syst = end_systolic_volume.get(state, 50)

    # Tiempo para un ciclo cardíaco
    t = np.linspace(0, 1, 500)  # Simulación de 1 segundo (un ciclo cardíaco)

    # Simulación de las ondas de presión y volumen
    aortic_pressure = press_diast + (press_syst - press_diast) * np.sin(2 * np.pi * freq * t) ** 2
    ventricular_pressure = 0.6 * aortic_pressure  # Aproximación para la presión ventricular izquierda
    atrial_pressure = 0.2 * aortic_pressure + 5   # Aproximación para la presión auricular izquierda
    ventricular_volume = vol_syst + (vol_diast - vol_syst) * (1 + np.sin(2 * np.pi * freq * t)) / 2
    
    # ECG simulado
    ecg = np.sin(8 * np.pi * freq * t) ** 20  # Pico del ECG que representa el QRS

    # Crear la figura y los subplots
    fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

    # Gráfico de presión aórtica
    axs[0].plot(t, aortic_pressure, 'r-', label="Presión Aórtica")
    axs[0].plot(t, ventricular_pressure, 'b-', label="Presión Ventricular Izquierda")
    axs[0].plot(t, atrial_pressure, 'g-', label="Presión Auricular Izquierda")
    axs[0].set_ylabel("Presión (mmHg)")
    axs[0].legend(loc="upper right")
    axs[0].set_title(f"Diagrama de Wiggers - Estado: {state}")

    # Gráfico del volumen ventricular izquierdo
    axs[1].plot(t, ventricular_volume, 'purple', label="Volumen Ventricular Izquierdo")
    axs[1].set_ylabel("Volumen (ml)")
    axs[1].legend(loc="upper right")

    # Gráfico de ECG
    axs[2].plot(t, ecg, 'k-', label="ECG")
    axs[2].set_ylabel("ECG")
    axs[2].legend(loc="upper right")

    # Gráfico de eventos cardíacos (Apertura y cierre de válvulas)
    mitral_open = (ventricular_pressure < atrial_pressure).astype(int)  # Válvula mitral abierta
    aortic_open = (ventricular_pressure > aortic_pressure).astype(int)  # Válvula aórtica abierta
    axs[3].plot(t, mitral_open, 'c-', label="Apertura Mitral")
    axs[3].plot(t, aortic_open, 'm-', label="Apertura Aórtica")
    axs[3].set_yticks([0, 1])
    axs[3].set_yticklabels(["Cerrada", "Abierta"])
    axs[3].set_ylabel("Válvulas")
    axs[3].set_xlabel("Tiempo (s)")
    axs[3].legend(loc="upper right")

    fig.tight_layout()
    plt.show()

# Ejemplo de uso
wiggers_diagram("Correr")
