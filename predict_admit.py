import numpy as np
from keras.models import load_model
import tkinter as tk
from tkinter import messagebox, ttk

modelo = load_model("modelo_treinado.keras")

def validar_valor(valor, minimo, maximo, nome):
    try:
        v = float(valor)
        if v < minimo or v > maximo:
            raise ValueError
        return v
    except:
        messagebox.showerror("Erro", f"{nome} deve estar entre {minimo} e {maximo}.")
        return None

def prever():
    gre = validar_valor(entry_gre.get(), 0, 340, "Nota GRE")
    toefl = validar_valor(entry_toefl.get(), 0, 120, "Nota TOEFL")
    university = validar_valor(entry_university.get(), 1, 5, "Avaliação da Universidade")
    sop = validar_valor(entry_sop.get(), 1, 5, "SOP")
    lor = validar_valor(entry_lor.get(), 1, 5, "LOR")
    cgpa = validar_valor(entry_cgpa.get(), 0, 10, "CGPA")
    research = validar_valor(entry_research.get(), 0, 1, "Pesquisa")

    if None in [gre, toefl, university, sop, lor, cgpa, research]:
        return

    entrada = np.array([gre, toefl, university, sop, lor, cgpa, research]).reshape(1, -1)
    predicao = modelo.predict(entrada)
    chance = float(predicao[0][0]) * 100

    progress_var.set(chance)
    label_resultado.config(text=f"Chance prevista: {chance:.2f}%", fg="#005500")

janela = tk.Tk()
janela.title("Predição de Chance de Admissão")
janela.geometry("500x650")
janela.configure(bg="#f9f9f9")

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("TLabel", background="#f9f9f9", font=("Helvetica", 11))
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=6, background="#4CAF50", foreground="white")
style.configure("TEntry", padding=5)

frame = ttk.Frame(janela, padding=20)
frame.pack(fill="both", expand=True)

def criar_campo(texto):
    label = ttk.Label(frame, text=texto)
    label.pack(anchor="w", pady=(10, 0))
    entry = ttk.Entry(frame, font=("Helvetica", 10))
    entry.pack(fill="x", pady=5)
    return entry

entry_gre = criar_campo("Nota GRE (0-340)")
entry_toefl = criar_campo("Nota TOEFL (0-120)")
entry_university = criar_campo("Avaliação da Universidade (1-5)")
entry_sop = criar_campo("SOP (1-5)")
entry_lor = criar_campo("LOR (1-5)")
entry_cgpa = criar_campo("CGPA (0-10)")
entry_research = criar_campo("Pesquisa (0 = Não, 1 = Sim)")

btn_prever = tk.Button(frame, text="Prever Chance", command=prever, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
btn_prever.pack(pady=20, fill="x")

label_resultado = tk.Label(frame, text="", font=("Helvetica", 14, "bold"), bg="#f9f9f9")
label_resultado.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.pack(fill="x", pady=10)

janela.mainloop()
