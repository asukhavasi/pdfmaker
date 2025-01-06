import fpdf
import pandas

pdf = fpdf.FPDF(orientation="P",format='A4',unit='mm')



df = pandas.read_csv("topics.csv")
print(df["Topic"])
print(df["Pages"])

for index, row in df.iterrows():
    for i in range(int(row["Pages"])):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(50,100,50)
        pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1,border = 0)
        pdf.set_line_width(2)
        pdf.line(10,20,200,20)


# pdf.cell(w=0,h=12,txt="Hello I am pdf line1",align="L",ln=1,border=0)
# pdf.cell(w=0,h=12,txt="HI I am pdf line2",align="L",ln=1,border=0)
pdf.output("output.pdf")

