title = ""
intro = ""
tags = ""

while title=="" or intro=="":
        title = input("Digite um titulo para o site: ")
        intro = input("Digite um introdução para o site: ")
        tags = input("Digite algumas tags para o seu site (lembre-se de colocar virgula entre elas): ")

f = open("index.html","w+")
f.write('<!Doctype html>\n<html>\n\t<head>\n\t\t<title>'+title+'<title>\n\t\t<meta charset="UTF-8">\n\t\t<meta name="description" content="'+intro+'">\n\t\t<meta name="keywords" content="'+tags+'">\n\t\t<meta name="viewport" content="width=device-width,initial-scale=1.0">\n\t\t<style>\n\n\t\t</style>\n\t</head>\n\t<body>\n\t\t<div id="main">\n\n\t\t</div> \n\t</body> \n</html>')
f.close()
