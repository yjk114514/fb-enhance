from getUserID import getUserID
urlls=[
    'https://www.facebook.com/TheJapanfoundation?locale=zh_CN',
    'https://www.facebook.com/sejonghakdang.org?locale=zh_CN',
    'https://www.facebook.com/InstCervantes?locale=zh_CN',
    'https://www.facebook.com/goetheinstitut?locale=zh_CN',
    'https://www.facebook.com/britishcouncil?locale=zh_CN',
    'https://www.facebook.com/Alliance.francaise.Paris?locale=zh_CN'
]
idls=[]
for url in urlls:
    idls.append(getUserID(url))
print(idls)