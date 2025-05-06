"""
Kieu du lieu trong Python
"""
'''So nguyen'''
a= 5
print(type(a))

'''So thuc'''
b= 3.14
print(type(b))

'''Chuoi'''
c= "Python"
print(type(c))

'''Danh sach'''
d=[1,3.14,"hello"]
print(type(d))

'''key-value'''
student= {
    "name": "Tam",
    "age": 25
}

print(type(student))

"""
Cau dieu kien va vong lap
"""
'''Cau dieu kien'''
x=9
if x>9:
    print("Lon hon 9")
elif x<9:
    print("Nho hon 9")
else:
    print("x = 9")

'''Vong lap for'''

# for i in range(5):
#     print(i)

'''Vong lap while'''

count=0
while count < 5:
    print(count)
    count +=1
"""
Ham trong Python
"""

'''Dinh nghia ham def va goi ham'''
def hello(name):
    print("Hello", name)

hello("World")

'''Ham co gia tri tra ve (return)'''

def add(a,b):
    return a + b

result = add(3,4)
print(result)

"""Bai tap thuc te"""

'''Tính trung bình điểm
Yêu cầu: Nhập điểm các môn từ danh sách, 
tính điểm trung bình và xếp loại.'''

def tinh_diem_trung_binh(diem_list):
    return sum(diem_list)/ len(diem_list)

def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Gioi"
    elif diem_tb >=6.5:
        return "Kha"
    elif diem_tb >= 5:
        return "Trung binh"
    else:
        return "Yeu"

so_mon= int(input("Nhap so luong mon hoc"))
diem = []
for i in range(so_mon):
    d = float(input(f"Nhap diem mon thu {i+1}: "))
    diem.append(d)

diem_tb = tinh_diem_trung_binh(diem)
loai = xep_loai(diem_tb)
print("\n---Ket Qua---")
print("Diem trung binh", round(diem_tb,2))
print("Xep loai", loai)
