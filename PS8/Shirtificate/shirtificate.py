from fpdf import FPDF


class PDF():
    def __init__(self):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 35)
        self._pdf.cell(text="CS50 Shirtificate", center=True)
        self._pdf.image("shirtificate.png",x=10, y=60, w=self._pdf.epw)

    def words(self, name):
        self._pdf.ln(110)
        self._pdf.set_font("helvetica", "I", 25)
        self._pdf.set_text_color(r=255, g=255, b=255)
        self._pdf.cell(text=f"{name} took CS50", center=True)

    def output(self, shirt):
        self._pdf.output(shirt)


name = input("Name: ")
string = PDF()
string.words(name)
string.output("shirtificate.pdf")

