from googlesearch import search

searchName = input("please insert search title : ")
query = searchName + " site:sgegrv8ergs4sd555dsfa6bv8ajfg545.xyz"

for i in search(query, num=10, start=0, stop=30, pause=2):
    print(i)
