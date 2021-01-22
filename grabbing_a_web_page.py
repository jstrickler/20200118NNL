import requests
import os

URL = "https://www.energy.gov/nnsa/nuclear-security-nonproliferation"

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    page_source = response.content.decode()   # convert bytes to str
    print(page_source)


PDF_URL = "https://www.energy.gov/sites/prod/files/2014/03/f12/cng_h2_workshop_agenda.pdf"

response = requests.get(PDF_URL)

local_pdf_file = 'nnl.pdf'

if response.status_code == requests.codes.OK:
    with open(local_pdf_file, 'wb') as nnl_out:
        nnl_out.write(response.content)

os.system(local_pdf_file)
