import os, shutil

sourcePath = "./source"
L = [x for x in os.listdir(sourcePath) if x.endswith("md") or x.endswith("rst") ]
shutil.copy2(sourcePath+"/"+L[0],".")
print(L)