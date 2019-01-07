def merge_the_tools(string, k):
    from collections import OrderedDict
    chopt = [string[i:i+k] for i in range(0, len(string), k)]
    for x in range(len(chopt)):
        print("".join(OrderedDict.fromkeys(chopt[x])))
