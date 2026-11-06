import sys
from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_page_background(None)
        self.set_font("Helvetica", "B", 45)
        self.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def create_shirt(self, name):
        self.image("shirtificate.png", x=15, y=65, w=180)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 24)
        self.set_y(130)
        self.cell(0, 10, f"{name} took CS50", align="C")

def main():
    name = input("Name: ")
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.create_shirt(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
