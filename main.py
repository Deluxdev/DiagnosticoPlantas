from tkinter import *
from pyswip import Prolog

class DiagnosticoPlantas:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Diagnóstico de Pragas e Doenças em Plantas")

        # Seção para inserir os sintomas
        self.sintomas_label = Label(master, text="Insira os sintomas da planta (separados por vírgula):")
        self.sintomas_label.pack()

        self.sintomas_entry = Entry(master)
        self.sintomas_entry.pack()

        # Seção para exibir os diagnósticos
        self.resultados_label = Label(master, text="")
        self.resultados_label.pack()

        # Botão para diagnosticar
        self.diagnosticar_button = Button(master, text="Diagnosticar", command=self.diagnosticar)
        self.diagnosticar_button.pack()

        # Botão para sair
        self.sair_button = Button(master, text="Sair", command=master.quit)
        self.sair_button.pack()

        # Carregar a base de conhecimento Prolog
        self.prolog = Prolog()
        try:
            self.prolog.consult("database.pl")
            print("Base de conhecimento carregada com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar a base de conhecimento: {e}")

    def diagnosticar(self):
        # Obter os sintomas da planta
        sintomas_input = self.sintomas_entry.get()
        sintomas = [sintoma.strip() for sintoma in sintomas_input.split(",")]

        # Formatar a lista de sintomas para a consulta Prolog
        sintomas_str = "[" + ",".join(f"'{sintoma}'" for sintoma in sintomas) + "]"
        
        # Debug: imprimir a consulta Prolog
        print(f"Consulta Prolog: diagnostico({sintomas_str}, Problema)")

        # Consultar a base de conhecimento Prolog
        try:
            query = f"diagnostico({sintomas_str}, Problema)"
            resultados = list(self.prolog.query(query))

            # Debug: imprimir resultados da consulta
            print(f"Resultados da consulta: {resultados}")

            # Exibir os resultados do diagnóstico
            if resultados:
                problemas = [resultado['Problema'] for resultado in resultados]
                texto_resultados = "Possíveis problemas: " + ", ".join(problemas)
                self.resultados_label.config(text=texto_resultados)
            else:
                self.resultados_label.config(text="Nenhum problema encontrado para esses sintomas.")
        except Exception as e:
            print(f"Erro na consulta Prolog: {e}")
            self.resultados_label.config(text="Erro ao realizar o diagnóstico.")

# Iniciar a interface gráfica
root = Tk()
diagnostico_plantas = DiagnosticoPlantas(root)
root.mainloop()
