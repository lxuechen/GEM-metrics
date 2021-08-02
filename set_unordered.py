# An example of why the old code is wrong and induces annoying behavior...
# BertScore may come after BLEURT which uses TF, causing OOM; this is even when the 
# input order is correct.
l = ["hey", "how", "are"]
s = list(set(l))
print(s)

