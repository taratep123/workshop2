#จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"

#จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"

#จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด

#จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "tiger"
txt = "i am  the best programmer"
print(myname) #แสดงชื่อ
print(txt.format(myname))
print(len(txt)) #1
print(txt[0])   #2
print(txt[10:14])#3 
print(txt.replace(" " , ""))#4
print(txt.upper())#5
print(txt.lower())#6
print(txt.replace("e", "z"))#7

myname = "tiger"
txt ="{} is the best programmer"
print(txt.format(myname))