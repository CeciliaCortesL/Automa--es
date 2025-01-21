import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_treinos = os.listdir("Treinos")
lista_treinos.sort()
print(lista_treinos)

for treino in lista_treinos:
    if ".pdf" in treino:
        merger.append(f"treinos/{treino}")

merger.write("PDF Treinos.pdf")
