import fpdf
import pandas

pdf = fpdf.FPDF(orientation="P",format='A4',unit='mm')
pdf.set_auto_page_break(auto=False,margin=0)

df = pandas.read_csv("topics.csv")
print(df["Topic"])
print(df["Pages"])

for index, row in df.iterrows():
    for i in range(int(row["Pages"])):
        pdf.add_page()
        pdf.set_fill_color(100, 100, 100)
        #Header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(50,100,50)
        pdf.cell(w=0,h=12,txt=row["Topic"],align="L",border = 0)
        pdf.set_line_width(2)
        pdf.line(10,20,200,20)

        # ruled lines
        for line in range(30,270,10):
            pdf.set_line_width(0.25)
            pdf.line(10,line,200,line)

        # Footer
        pdf.ln(260)
        pdf.set_line_width(1)


        pdf.line(10, 270, 200, 270)
        pdf.set_font(family="Times",style="I",size=10)
        pdf.set_text_color(254,0,0)
        pdf.cell(w=0,h=10,txt=row["Topic"],align="R",border=0)

# pdf.cell(w=0,h=12,txt="Hello I am pdf line1",align="L",ln=1,border=0)
# pdf.cell(w=0,h=12,txt="HI I am pdf line2",align="L",ln=1,border=0)
pdf.output("output.pdf")

