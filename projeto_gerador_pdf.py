from fpdf import FPDF

def createPdf():

    projeto = str(input("Digite a descrição do Projeto: "))
    horas_previstas = int(input("Digite a quantidade de horas prevista: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))  
    prazo = str(input("Digite o prazo do projeto: "))

    valor_total = horas_previstas * valor_hora

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("Arial")

    pdf.image("template.png", x=0, y=0) 

    pdf.text(115, 145, projeto)
    pdf.text(115, 160, str(horas_previstas))  
    pdf.text(115, 175, str(valor_hora))  
    pdf.text(115, 190, prazo)
    pdf.text(115, 205, str(valor_total))

    pdf.output("orcamento.pdf")

    print("Sucesso!")

createPdf()
