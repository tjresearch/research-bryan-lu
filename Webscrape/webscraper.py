from bs4 import BeautifulSoup

html = "C:/Syslab/Webscrape/Problems/isl1979/IMO Shortlist.html"
f = open(html, encoding="utf8")
soup = BeautifulSoup(f, "html.parser")
f.close()

outfile = open("geoproblems.txt", "a+")

allproblems = soup.find_all("div", class_="cmty-view-post-item-text")#"cmty-view-posts-item cmty-view-post-item-w-label cmty-vp-both")
cleanedproblems = []
for problem in allproblems:  # replace with the indexeses of the geo problems.... # of A, C probs + 3: first + # of probs
    currentprob = ""
    for itm in problem.contents:
        if issubclass(type(itm), str):
            currentprob += itm
        elif itm.name == "img":
                currentprob += itm['alt']
        elif itm.name == "span":
            for piece in itm.contents:
                if issubclass(type(piece), str):
                    currentprob += piece
                else:
                    currentprob += piece['alt']
    currentprob = currentprob.replace("$", "")
    currentprob = currentprob.replace("\\", "")
    cleanedproblems.append(currentprob)
    outfile.write(currentprob + "\n")

print(cleanedproblems)
