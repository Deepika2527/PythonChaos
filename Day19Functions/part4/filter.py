names = ["tarannum","sara","fathima","nikath","bonkers","bonky"]

# res = list(filter(lambda st: st.startswith("b"),names))
# print(res)
# res = list(filter(lambda st: [s if st.startswith('b') else 'not starts with b' for s in st],names))
# print(res)
marks = [35,78,99,56,34,56]
res2 = list(filter(lambda m : m>=35,marks))
print(res2)