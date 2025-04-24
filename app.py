import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if altura <= 0:
            raise ValueError("Altura inválida.")
        imc = peso / (altura ** 2)

        if imc < 18.5:
            resultado = "Abaixo do peso"
            cor = "#d3d3d3"
        elif imc < 24.9:
            resultado = "Você está no peso normal"
            cor = "#90ee90"
        elif imc < 29.9:
            resultado = "Você está com sobrepeso"
            cor = "#ffff66"
        elif imc < 34.9:
            resultado = "Você está com obesidade grau 1"
            cor = "#ffa500"
        elif imc < 39.9:
            resultado = "Você está com obesidade grau 2"
            cor = "#ff6347"
        else:
            resultado = "Você está com obesidade mórbida"
            cor = "#8b0000"

        label_resultado.config(text=f"{resultado} (IMC: {imc:.2f})", bg=cor, fg='black')

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

# Criar a interface
root = tk.Tk()
root.title("Calculadora de IMC")
root.configure(bg='#1e1e1e')  # Fundo escuro

tk.Label(root, text="Peso (kg):", bg='#1e1e1e', fg='white').pack(pady=5)
entry_peso = tk.Entry(root, bg='#2e2e2e', fg='white', insertbackground='white')
entry_peso.pack()

tk.Label(root, text="Altura (m):", bg='#1e1e1e', fg='white').pack(pady=5)
entry_altura = tk.Entry(root, bg='#2e2e2e', fg='white', insertbackground='white')
entry_altura.pack()

tk.Button(root, text="Calcular IMC", command=calcular_imc, bg='#3e3e3e', fg='white').pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12), width=40, height=3, bg='#1e1e1e', fg='white')
label_resultado.pack(pady=10)

# Mostrar a janela
root.mainloop()
