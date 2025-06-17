def demsolanxuathien(lst):
    countdict={}
    for item in lst:
        if item in countdict:
            countdict[item]+=1
        else:
            countdict[item]=1
    return countdict
input_string=input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list=input_string.split()
solanxuathien=demsolanxuathien(word_list)
print("Số lần xuất hiện của các phần tử", solanxuathien)