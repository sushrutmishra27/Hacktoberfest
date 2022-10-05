import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):

    list2=[]
#devides string into n equal parts of size k
    list1 = textwrap.wrap(string, k)

    for i in list1:
        list2.append("".join(OrderedDict.fromkeys(i)))

    for i in list2:
        print(i)
