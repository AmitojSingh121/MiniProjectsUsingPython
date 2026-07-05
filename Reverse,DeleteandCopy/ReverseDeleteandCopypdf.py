# 1st pdf reverse
# 2nd pdf delete
# 3rd pdf copy

# import pikepdf

# old_pdf = pikepdf.Pdf.open(r"C:\Users\hp\Downloads\No9to5_Chapter01.md.pdf")
# old_pdf.pages.reverse()
# old_pdf.save("Reversed_No9to5_Chapter01.md.pdf") 

# 2nd Delete Pdf
# import pikepdf

# old_pdf = pikepdf.Pdf.open(r"C:\Users\hp\Downloads\No9to5_Chapter01.md.pdf")

# del old_pdf.pages[1:4]  # Delete the second page (index 1)
# old_pdf.save("Deleted_No9to5_Chapter02.md.pdf")

# 3rd Copy Pdf
import pikepdf
old_pdf = pikepdf.Pdf.open(r"C:\Users\hp\Downloads\No9to5_Chapter01.md.pdf")
old_pdf.pages[7] = old_pdf.pages[0]  # Copy the first page (index 0) to the ninth page (index 8)
old_pdf.save("Copied_No9to5_Chapter01.md.pdf")

# jase 0 page teh joh page ha means oh page copy ho jayega 7 page teh
# then after that oh page save ho jayega