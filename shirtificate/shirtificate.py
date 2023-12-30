from fpdf import FPDF


def main():
    name = input('Name: ')

    # creates pdf of A4 format and set default unit to 'mm' and orientation to 'Portrait'
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # add header
    pdf.set_font('helvetica', 'B', 30)
    pdf.cell(200, 50, 'CS50 Shirtificate', align='C')

    # add shirt
    pdf.image('shirtificate.png', x=20, y=80, w=170)

    # print in shirt
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(20, 200)  # setting coordinates for the text
    pdf.cell(170, 10, f'{name} took CS50', align='C')

    # save pdf
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()
