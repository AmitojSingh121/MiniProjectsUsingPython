from glob import glob
from pikepdf import Pdf
# create a new pdf file 
new_pdf = Pdf.new()

# glob is a module that finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
for file in glob("*.pdf"):
    # open the file 
    old_pdf = Pdf.open(file)
    new_pdf.pages.extend(old_pdf.pages)
new_pdf.save("demo.pdf")

# from glob import glob
# from pikepdf import Pdf

# # create a new pdf file
# new_pdf = Pdf.new()

# for file in glob("*.pdf"):
#     old_pdf = Pdf.open(file)
#     print(old_pdf.pages)
#     new_pdf.pages.extend(old_pdf.pages)
# new_pdf.save("demo.pdf")
