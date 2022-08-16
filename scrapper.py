from googlesearch import search

searchName = input("please insert search title : ")

sites = ["sgegrv8ergs4sd555dsfa6bv8ajfg545.xyz", "dl2.sermovie.xyz"]

queries = []
for siteName in sites:
    queries.append(searchName + " site:" + siteName)
for m in queries:
  for i in search(m, num=10, start=0, stop=30, pause=5):
        print(i)
