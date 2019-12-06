import json
file72 ='faber-castell72.json'
file60 ='faber-castell60.json'
color_72={"白色":"801", "鋅黄":"802","浅阳红":"815","柠檬黄":"803","橙黄":"804","深橙":"807","":""}
color_60={"白色":"301", "鋅黄":"304", "浅阳红":"319"}
with open(file72,'w') as f_obj:
    json.dump(color_72,f_obj)
with open(file60,'w') as f60_obj:
    json.dump(color_60,f60_obj)

with open(file72) as r_obj:
    color_list72=json.load(r_obj)
# print(color_list)
# for  colors in set(color_list.keys()):
#     print(colors)
with open(file60) as r_obj:
    color_list60=json.load(r_obj)
print("颜色","骑士","城堡",sep='\t')
for key60,value60 in color_list60.items():
    for key72,value72 in color_list72.items():
        if key60 == key72:
            print(key60,value60,value72,sep='\t')
# print(color_list60)
# print(color_list72)