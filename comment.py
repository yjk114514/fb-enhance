import json

import requests
import base64

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
 'accept':'*/*',
 'accept-language':'en-US,en;q=0.5',
 'accept-encoding':'gzip',
 'content-type':'application/x-www-form-urlencoded',
 'x-fb-friendly-name':'CometFocusedStoryViewUFIQuery',
 'x-fb-lsd':'Oq9Au8bKSqTJQTzv9HNGkP',
 'x-asbd-id':'129477',
 'content-length':'2186',
 'origin':'https://www.facebook.com',
 'referer':'https://www.facebook.com/HuaweiKE',
 'sec-fetch-dest':'empty',
 'sec-fetch-mode':'cors',
 'sec-fetch-site':'same-origin',
 'priority':'u=0',
 'pragma':'no-cache',
 'cache-control':'no-cache',
 'te':'trailers',
 'cookie':'fr=1V5SGzu4O0lA6dN0q.AWV8-Sp34aHqml9rvn7UAhDKu02Uf_Y8_RNA8Q.Bnoz38..AAA.0.0.Bnoz38.AWWeJuA0j2s; ps_l=1; ps_n=1; datr=0dBuZ9JOSOLYOnYn6CQHVuQQ; sb=0dBuZ1XK5chQP176gBHqCqYH; c_user=100038307016563; xs=24%3AJ90GKOyFDhMNZA%3A2%3A1735468798%3A-1%3A-1%3A%3AAcVDwYHOvYq50L4xarGNU_FrJCIJ86CS6X_3zIcjOH8; wd=1159x785; dpr=1.3636363636363635; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1738752391894%2C%22v%22%3A1%7D'}
payload=('av=100038307016563&__aaid=0&__user=100038307016563&__a=1&__req=2b&__hs=20124.HYP:comet_pkg.2.1...1&dpr=1&__ccg=EXCELLENT&__rev=1019851578&__s=wy81ub:5papqb:hlgor2&__hsi=7467884626958678990&__dyn=7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUaqwh8ngS3q2ibwNwnof8boG0x8bo6u3y4o2Gwfi0LVEtwMw6ywIK1Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C0Mo4G1hx-3m1mzXw8W58jwGzE8FU5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0SEuwLyEbUGdG0HE88cA0z8c84q58jyUaUbGxe6Uak0zU8oC1hxB0qo4e4UcEeE-3WVU-4EdrxG1fBG2-2K2G0JUmw&__csr=goMlNY449jNcrb2G68IqyiPZjl4IIIWNn5PiOgx58ybcJkCgIHeZfOvjtEgFsAJRdqqFkGjEOAjp4yIJaAHFKhkV58n89-Bm8mjhlgCEG8HiTmLWnXm9meGAFpumuiLAGExaEWDripkmWBFGAXUGmh4AA9jG_zXWyVeWDBz99r8m9gyupDKq4EjGcgCECmeAV8xaGhGgrK8K-2i8UGJvADBWHBV889EC6oixa7uq8Gdy9o-5kULG8yKrhFk2eEkCGbxCU-EryEGC9BDFxurxmucyE-qUapVVUuxi7oy9whoO26dxO1Fx67ULwhUG4Ey4oGcwkrUyjVo9EswCDG13xu5pUmxe9wqUoz8y4o7O0xU3-yoswKwro1zoi81rw9CdwhEmwnk580wUo2C3m2y3W1Yx60k9wrk1tAwfu3K11xdwPwQxGEGpS6ouyoco3pGtS4E-Gw8622e-q5EWEmwVwse9GdG1uw0pMe0sy2W5o4W00RFEaU139VU2ew9q2m0om9Bw2K81gU2vw8O072Ueoco5S04F81No0hng0yO4E1kU1fPGt02-i383Pix91jwnk0zE1Ge0jC0me08jwjU-0vwM0-HK0vO06eA0SE1hE7oE0VahwaeU1cER0fK0Trwbu0mS06yEhw9J02Uy0&__comet_req=15&fb_dtsg=NAcOMS_Oz8lecdNC6BO73pqWOCuMoNnaMJ1tHEW4gJNkFaZ0TKLqMEQ:24:1735468798&jazoest=25333&lsd=Oq9Au8bKSqTJQTzv9HNGkP&__spin_r=1019851578&__spin_b=trunk&__spin_t=1738752384&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometFocusedStoryViewUFIQuery&variables={"contextData":null,"feedbackID":"%s","feedbackSource":110,"feedLocation":"DEDICATED_COMMENTING_SURFACE","scale":1,'
         '"storyID":"UzpfSTEwMDA2NDc3Mzg0NzAyNToxMDk3NDYyOTM5MDg5NDkxOjEwOTc0NjI5MzkwODk0OTE=","__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}&server_timestamps=true&doc_id=28411098708505415' % (feedback_id))

response0 = requests.request("POST", "https://www.facebook.com/api/graphql/", headers=headers, data=payload)

print(response0.text)
with open('cmt.json', 'w') as f:
    json.dump(response0.json(), f)