import pikepdf

old_pdf = pikepdf.Pdf.open(
    r"C:\Users\hp\Downloads\Dsa.pdf"
)
print(old_pdf.pages)

for i in old_pdf.pages:
    i.Rotate = 180
    old_pdf.save("new_pdf.pdf")
