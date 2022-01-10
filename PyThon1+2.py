"""
#Bai 1

n = int(input("Nhập n: "))
print("Giá trị đã nhập là: ",n)

#a
for i in range(0,n):
  print("*"*n)

#b
for i in range(0,n):
    print("*" * (i+1))
#c
for i in range (0,n):
    print(" "* (n-i) + "*"*(i+1) )
#d
for i in range (0,n):
    print(" "* (n-i) + "*"*((2*i)+1))
    if i == int((n/2)):
        break

# Bài 2
def SoDuongAmLonNhat():
    k = int(input("Nhập số phần tử của mảng : "))
    if k <= 0:
        print('Nhập số phải lớn hơn 0!')
    else:
        print("Đã nhập: ", k)
        a = []
        for i in range(0, k):
            a.append(int(input("a[%d] = " % (i + 1))))

        for i in a:
            print(i)
        soLonNhat = max(a)
        soNhoNhat = min(a)
        if (soLonNhat < 0):
            print("số dương lớn nhất là *")
        else:
            print("số dương lớn nhất là", soLonNhat)
        if soNhoNhat > 0:
            print("số âm nhỏ nhất là *")
        else :
            print("số âm nhỏ nhất là", soNhoNhat)
 #
SoDuongAmLonNhat()

#Bai 3

def tuDien ():
    dict = { 'Apple' : 'Quả táo',
             'Banana' : 'Trái chuối',
              'nut'   : 'Hạt'
            }
    print(dict)
    dict.update({'Peach': 'Trái đào'})
    print(dict)
    print("số phần tử: ",len(dict))

    co = 'f'
    key = input("Nhập từ khóa: ")
    for k in dict.keys():
        if k.upper() == key.upper():
            print( k + " : "+dict[k])
            del dict[k]
            co = 't'
            break
    if co == 'f':
        print ('Không tìm thấy')
    else:
       print ('Đã xóa')
       print(dict)
tuDien()

#Bai 4

class Bai4():
   ListNV = [
         {"MaNV" : "1" , "TenNV" : "Nguyễn Văn A"},
         {"MaNV": "2", "TenNV": "Nguyễn Văn B"},
         {"MaNV": "3", "TenNV": "Nguyễn Văn C"}
   ]
   n = len(ListNV)
   def showNV(self):
       print("======== HIỂN THỊ NV =============")
       for i in range(0,self.n):
           print("Mã Nhân Viên: {0} ". format(self.ListNV[i]["MaNV"]))
           print("Tên Nhân Viên: {0} ". format( self.ListNV[i]["TenNV"]))
   def timKiemNV(self,keyName):
       print("=== KẾT QUẢ TÌM KIẾM ==== ")
       co = 'f'
       for i in range(0,self.n):
           #if keyName.upper() == self.ListNV[i]["TenNV"].upper():
           if self.ListNV[i]["TenNV"].upper().find(keyName.upper()) != -1:
               print("Mã Nhân Viên: {0} ".format(self.ListNV[i]["MaNV"]))
               print("Tên Nhân Viên: {0} ".format(self.ListNV[i]["TenNV"]))
               co = 't'
               break;
       if(co == 'f'):
           print ("Không tìm thấy nhân viên có tên", keyName)

   def themNV(self):
       id = input("Nhập mã nhân viên cần thêm: ")
       for i in range(0,self.n):
           if self.ListNV[i]["MaNV"].find(id) != -1 :
               print("Mã NV đã tồn tại")
               return -1

       tenNV = input("Nhập tên NV: ")
       newNV = {"MaNV" : id , "TenNV": tenNV}
       self.ListNV.append(newNV)
       self.n = len(self.ListNV)
       return 1

   def xoaNV(self,id):
       for i in range(0, self.n):
           if self.ListNV[i]["MaNV"].find(id) != -1:
                del self.ListNV[i]
                self.n = len(self.ListNV)
                return 1
       return -1

a = Bai4()
a.showNV()
a.timKiemNV(input("Nhập tên nhân viên cần tìm: "))
if a.themNV() == 1 :
    print("thêm thành công")
    a.showNV()
else:
    print("Thêm thất bại")

if a.xoaNV(input("Nhập mã nhân viên muốn xóa : ")) == 1 :
    print("xóa thành công")
    a.showNV()
else:
    print("Không tìm thấy mã nhân viên cần xóa")
"""
import re


class BT2:
    def cau1 (self):
        n = int(input("Nhập số n: "))
        d = dict()
        for i in range(1,n+1):
            d[i] = i*i
        print(d)
    def cau2(self):
        s = input("Nhập chuỗi: ")
        print(s.upper())
    def cau3(self):
        s= input("Nhập chuỗi: ")
        items = s.split(",")
        items.sort()
        print(",".join(items))
    def cau4(self):
        s = input("Nhập chuỗi: ")
        so = 0
        chu = 0
        for i in s:
            if i.isdigit():
                so += 1
            if i.isalpha():
                chu+=1
        print("Số chữ cái là: ",chu)
        print("Số chữ số là: ",so)
    def cau5(self):
        s = input("Nhập chuỗi: ")
        thuong = 0
        hoa= 0
        for i in s:
            if i.islower():
                thuong +=1
            if i.isupper():
                hoa +=1
        print("Số chữ thường là: ", thuong)
        print("Số chữ hoa là: ",hoa)
    def cau6(self):
        s = input("Nhập chuỗi: ")
        items = s.split(",")
        kq =[]
        for i in items:
            if re.search("[a-z]",i):
                if re.search("[0-9]", i):
                    if re.search("[A-Z]", i):
                        if re.search("[$#@]", i):
                            if len(i)>= 6 and len(i) <=12:
                                kq.append(i)
        print(kq)

    def cau7(self):
        s = input("Nhập chuỗi: ")
        d = dict()
        for i in s:
            d[i] = 0
        for i in s:
            for key in d.keys():
                  if i == key:
                     d[i] += 1

        for i in d.keys():
            print( format(i), format(d[i]) )

    def cau8(self):
        info = {"Name : hello"}
        f = open("test.txt","a")
        f.writelines(info)

        f = open("test.txt", mode = 'r')
        r = f.read()
        print(r)


bt2 = BT2()
#bt2.cau1()
#bt2.cau2()
#bt2.cau3()
#bt2.cau4()
#bt2.cau5()
#bt2.cau6()
#bt2.cau7()
bt2.cau8()









