import re,sys
s=open('index.html',encoding='utf-8').read()
head=re.search(r'<head>(.*)</head>',s,re.S).group(1)
head=re.sub(r'<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*','',head)
body=re.search(r'<body>(.*)</body>',s,re.S).group(1)
open('/tmp/claude-0/s/artefact.html','w',encoding='utf-8').write(head+'\n'+body)
