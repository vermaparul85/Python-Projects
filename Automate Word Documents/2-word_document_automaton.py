# Import necessary python libraries
from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

doc = DocxTemplate('template-my-info-new.docx')
my_context = {'my_name': 'Mark', 'my_phone':'123-456-789',
           'my_email': 'abc@gmail.com', 'my_address': '123 abc, India',
           'today_date': datetime.today().strftime('%d %b, %Y')}

# Read the CSV file and fetch all the columns into dictionary
data = pd.read_csv('fake_profiles.csv')
for index, row in data.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone': row['phone'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']
              }

    context.update(my_context)
    doc.render(context)
    doc.save(f'generated_doc_{index}.docx')
