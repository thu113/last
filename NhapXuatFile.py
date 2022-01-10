import csv

with open('TaiKhoan.csv', 'w', newline='') as f:
    fieldName = ['user', 'password']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({"user" : "1952" , "password" : "0123"})

with open('TaiKhoan.csv', newline='') as f:
    reader = csv.DictReader(f)
    for r in reader:
        u = r["user"]
        p = r["password"]
print(u)
print(p)

for i in s:
    d[i] = 0
for i in s:
    for key in d.keys():
        if i == key:
            d[i] += 1


