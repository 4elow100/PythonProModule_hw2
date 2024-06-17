from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

contacts_list_grouped = []
for contact in contacts_list:
  FIO = " ".join(contact[:3]).split(" ")[:3]
  trig = True
  for ind, rows in enumerate(contacts_list_grouped):
    if rows[:2] == FIO[:2]:
      if FIO[2] and not rows[2]:
        contacts_list_grouped[ind][2] = FIO[2]
      for i in [3, 4, 5, 6]:
        if not rows[i] and contact[i]:
          contacts_list_grouped[ind][i] = contact[i]
      trig = False
  if trig:
    contacts_list_grouped.append(FIO + contact[3:])

for contact in contacts_list_grouped:
  pattern = re.compile("\\d")
  numbers = pattern.findall(contact[5])
  phone_num = ''
  if len(numbers) >= 11:
    phone_num = (f'+7({numbers[1]}{numbers[2]}{numbers[3]})'
                 f'{numbers[4]}{numbers[5]}{numbers[6]}-'
                 f'{numbers[7]}{numbers[8]}-'
                 f'{numbers[9]}{numbers[10]}')
    if len(numbers) > 11:
      phone_num += f' доб.{"".join([numbers[i] for i in range(11, 15)])}'
  contact[5] = phone_num

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_grouped)
