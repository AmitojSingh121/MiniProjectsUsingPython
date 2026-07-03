import pikepdf

old_pdf = pikepdf.Pdf.open(
    r"C:\Users\hp\Downloads\Dsa.pdf"
)

not_extract = pikepdf.Permissions(extract = False)

old_pdf.save("pro_new.pdf"  ,
            #  This is the Argument for the password protection of the pdf file
             encryption = pikepdf.Encryption(owner = "AmitojSingh" , user = "200311DS" , allow = not_extract)
              )