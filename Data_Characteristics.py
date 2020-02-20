#Tugas 1 Data Mining
#Galuh Fadillah Grandis
#175150200111075

age_data = [13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]
print("-----TUGAS DATA CHARACTERISTICS-----")
print()

# ----Mean----
jumlah_data = 0

for i in age_data:
    jumlah_data += i
panjang_data = len(age_data)
mean = jumlah_data/panjang_data

print("1. Mean")
print("Nilai Mean dari age data adalah: ", mean)

# ----Mode----

modCount = {i:age_data.count(i) for i in age_data}
get_mode = dict(modCount) 

mode = [urut for urut, kemunculan in get_mode.items() if kemunculan == max(list(modCount.values()))] 
  
if len(mode) == len(age_data): 
    get_mode = "Nilai mode dari age data adalah: "+0
else: 
    get_mode = "Nilai Mode dari age data adalah: " + ', '.join(map(str, mode)) 

print()
print("2. Mode")
print(get_mode)

# max = 0
# max1 = 0
# mode = []
# multi_mode = []
# modCount = {i:age_data.count(i) for i in age_data}
# key_mode = list(modCount.keys())
# val_mode = list(modCount.values())
# get_mode = dict(modCount)
# # for i in age_data:
# #     if modCount.get(i) >= max:
# #         max = modCount.get(i)
# #         mode = key_mode[val_mode.index(max)]
# mode = [urut for urut, kemunculan in modCount.items() if kemunculan == max(list(val_mode))]

# if len(mode) == len(age_data): 
#     get_mode = "Nilai mode dari age data adalah: "+0
# else: 
#     get_mode = "Nilai Mode dari age data adalah: " + ', '.join(map(str, mode)) 

# print()
# print("2. Mode")
# print(get_mode)

# ----Five Number Summary----
l = len(age_data)

# Minimum
min = age_data[l-l]

# Maximum
max = age_data[l-1]

# Q1, Q2, Q3
q1 = age_data[l * 1 // 4]
q2 = age_data[l * 2 // 4]
q3 = age_data[l * 3 // 4]
if l % 2 == 0:
    med_bawah = age_data[l / 2]
    med_atas = age_data[l / 2 - 1]
    median = (med_bawah+med_atas)/2
else:
    median = age_data[(l//2)]

print()
print("3. Five-Number Summary")
print("Nilai min dari age data adalah: ", min)
print("Nilai max dari age data adalah: ",max)
print("Nilai Q1 dari age data adalah: ", str(q1))
print("Nilai Q2 dari age data  adalah: ", str(q2))
print("Nilai Q3 dari age data  adalah: ", str(q3))

# ----Outlier Detection----
outlier = {}
iqr = q3 - q1
batas_outlier = 1.5 * iqr

outlier_bawah = q1 - batas_outlier
outlier_atas = q3 + batas_outlier

for i in age_data:
    if i < outlier_bawah:
        outlier["atas"] = i
    elif i > outlier_atas:
        outlier["bawah"] = i
print()
print("4. Outlier Detections")
print("Nilai Outlier dari age data: ", str(outlier))