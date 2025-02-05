import json
import re
from datetime import datetime

import requests
import requests
import base64

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',
 'accept':'*/*',
 'accept-language':'en-US,en;q=0.5',
 'accept-encoding':'gzip',
 'content-type':'application/x-www-form-urlencoded',
 'x-fb-friendly-name':'ProfileCometTimelineFeedRefetchQuery',
 'x-fb-lsd':'sVIMwbZH4roYjILpFnhEy2',
 'x-asbd-id':'129477',
 'content-length':'3792',
 'origin':'https://www.facebook.com',
 'referer':'https://www.facebook.com/HuaweiKE',
 'sec-fetch-dest':'empty',
 'sec-fetch-mode':'cors',
 'sec-fetch-site':'same-origin',
 'te':'trailers',
 'cookie':'fr=1ORsv7TNYOj5lwKZE.AWUW4EgBO4ycA-zxWD-BLQBBRf24UU8lkqULTw.BnoJZ3..AAA.0.0.BnoJZ3.AWURDA_o-eg; ps_l=1; ps_n=1; datr=0dBuZ9JOSOLYOnYn6CQHVuQQ; sb=0dBuZ1XK5chQP176gBHqCqYH; c_user=100038307016563; xs=24%3AJ90GKOyFDhMNZA%3A2%3A1735468798%3A-1%3A-1%3A%3AAcXwqSCVCNk97yPUE4ToQz7mgerUrilYpxRyDcAAcg; wd=1162x786; dpr=1.3636363636363635; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1738577621258%2C%22v%22%3A1%7D'}
# payload=base64.b64decode("YXY9MTAwMDM4MzA3MDE2NTYzJl9fYWFpZD0wJl9fdXNlcj0xMDAwMzgzMDcwMTY1NjMmX19hPTEmX19yZXE9MWkmX19ocz0yMDEyMi5IWVAlM0Fjb21ldF9wa2cuMi4xLi4uMSZkcHI9MSZfX2NjZz1FWENFTExFTlQmX19yZXY9MTAxOTc3OTQ3MiZfX3M9YXo3Yzk5JTNBODl1OWxhJTNBdHhmOTR3Jl9faHNpPTc0NjcxMzM5NzY5NTg1MzgxNzgmX19keW49N3hlWHpXSzFpeHQwbVV5RXF4ZW1oMG5vZUViOG53Z1VhcXdoOG5nUzNxMmlid053bm9mOGJvRzB4OGJvNnUzeTRvMkd3ZmkwTFZFdHdNdzZ5d0lLMVJ3d3dxbzQ2Mm1jd2ZHMTJ3T3g2Mkc1VXN3OW0xWXdCZ0s3bzZDME1vNEcxaHgtM20xbXpYdzhXNThqd0d6RThGVTVlM3ltMlNVNGk1b2U4NDY0LTVwVWZFZTg4bzRXbTctMkswU0V1d0x5RWJVR2RHMEhFODhjQTB6OGM4NHE1OGp5VWFVYkd4ZTZVYWswelU4b0MxaHhCMHFvNGU0VWNFZUUtM1dWVS00RWRyeEcxZkJHMi0ySzJHMEpVbXcmX19jc3I9Z3FNbTg5aEFoM185MkFoaWRzdGNJSVlybjJSaHY2RWo5YnY5NFJzQ1FJSDU0OXVSRk9pbGZrQmxsRGFta0RzajlJeXFIaTl0bGg5QW5SQXItQThucGNEOUptQUNYSmFTbDduREY3anpmRjlkYWx2R0FpR0p5R1dqeWVYQUR5QWlsOUpyeVdGcWpGNmg5TFZwZWFYeU9hYi11RmFoUVRLZnFCcEh4MTZsby1tRThVV2JBWGhFWjRnRENHZkFDQkNEeXBFeXFlSFZxeW94NHpWQnk4eUVteW9vUXJ5b0s0RU54T2N4Tzc5RTktM0c5LWFDd3lwYVF1RXg1eENtNFVoQUdiRER3S3o4SHpwcks0LTh4Mm0xc0YxdUVqVWFvOFU4VTRXNVVXYXpVOG95OXhpMm0yQ2N5RS02UWR4aTFrd3h3bTg0YTJtNEU1dTI2Y3dVd1p3NTl5RTF5aTA2RXdCd1N4Z3g4NTZFMkJ3NjZ5VVc4aFJvNWkyNjBOVGl4eTFtdzhsMDQwaEVCaDgtMUN3djhvd3M4OEV5MjYwd0VvRHVFeWR3OHk4Z3lFa0h4dmc3eTBJVWNiREwtY0R3MGt3ODBqd1UwU0swYmV3Mm9VZktlaGs3ODBYVzRvMDJMTHlvMERhMHBxNDhzZ0Mwd0UweWUwa1cwaEcxQncxd2ExUndrRTBoeHcyUjgwU1YwZmU0RTBUMjh3NFN3NGRQLTB1aXUxRmczUkRnR2x3NzF3YkowbXBud2RhMGY0ZzNYdzQxYTNxMDRHbzM0V3cxR0s1ODBCcTBUeXdCdzRKZzBJU2J3ZmUxb3dYdzRZdzR4d2RxMDZhNDBwZTFneUUwSGVhQ2cmX19jb21ldF9yZXE9MTUmZmJfZHRzZz1OQWNNRGdmNjRLTVhiTVhKbXVkSTN1ZFhQQzgySjZfVERxVWVjck1fRFVwS1dRZzdFdDQycy1BJTNBMjQlM0ExNzM1NDY4Nzk4Jmphem9lc3Q9MjUyNzYmbHNkPXNWSU13YlpINHJvWWpJTHBGbmhFeTImX19zcGluX3I9MTAxOTc3OTQ3MiZfX3NwaW5fYj10cnVuayZfX3NwaW5fdD0xNzM4NTc3NjEwJl9fanNzZXN3PTEmZmJfYXBpX2NhbGxlcl9jbGFzcz1SZWxheU1vZGVybiZmYl9hcGlfcmVxX2ZyaWVuZGx5X25hbWU9UHJvZmlsZUNvbWV0VGltZWxpbmVGZWVkUmVmZXRjaFF1ZXJ5JnZhcmlhYmxlcz0lN0IlMjJhZnRlclRpbWUlMjIlM0FudWxsJTJDJTIyYmVmb3JlVGltZSUyMiUzQW51bGwlMkMlMjJjb3VudCUyMiUzQTMlMkMlMjJjdXJzb3IlMjIlM0ElMjJDZzhPYjNKbllXNXBZMTlqZFhKemIzSUpBQUFCcjBGUlNGSTJURjluWlhJNGRsbDBWMWhYU2t0bmRuQldOVzFXYjBWTFEwcG1SR1I0UXpSRGJWTkxTRkp6YWw5aVoxVTJWRkZ2VDJsbmNEaHhWSFIyZUZWaWRsbFNWSGRDVTBwVVR6VkhjR1ZXVG0xemNFSlVlaTF2UzJ4bWJFZFlXbXRhVDNkb1FYZHROak5rVW5vd1dqQk1jRWxTTFVsWWMwVk9SRXBpT0dGNldETlFTMEZuYlhkV1pVazFkWFkyV25wdVRGUjJaRXBuWVhWdVNVTXpSVk5VWTJSQmEzcFhWemxpT1ROM2FrSkRYMnhPYmtaamIzWkdPRTV3TjNsSmJtWlNWakZGTnpSWlJHTkllbHB1TjFRelNsSjNlRGR1UjB4cVEyOWtPRFoxUm5oSWFIWkRPVkJWZUhOa09VcE9WekpwVVRCaWFHVmhRMDlIUkhKek1YRlJhemxhVUV4S2JYQjNkM1ZNYUVGZlRqQXhXRFJhV1ZsVVVVZElURFpmUzJ4d1RtbDJlVkkxVmtKR1MxQkdOa1V6YWt4Mk5UUmxOMDFoU1ZkWWIyWXhjV3c0VEZGMWVsOVNNbkl4Y2kxRU4yRkhha05KYjI4MGExOWxOamQwTUV0MmJrdHROemREV1hWM2JtczBiekJuTm1aWWJGWnJkVzVLTVZSa1FtMXhYMWxvY1RCUU1DMVJkMlZKTWxGSk5tTjVhWE41ZUdaWFUxQk5XRVoxT1VSUE1GSklaWFJzWW5sa1JqWTVUVGhKRHdsaFpGOWpkWEp6YjNJT0R3OW5iRzlpWVd4ZmNHOXphWFJwYjI0Q0FBOEdiMlptYzJWMEFnQVBFR3hoYzNSZllXUmZjRzl6YVhScGIyNEMlMkZ3RSUzRCUyMiUyQyUyMmZlZWRMb2NhdGlvbiUyMiUzQSUyMlRJTUVMSU5FJTIyJTJDJTIyZmVlZGJhY2tTb3VyY2UlMjIlM0EwJTJDJTIyZm9jdXNDb21tZW50SUQlMjIlM0FudWxsJTJDJTIybWVtb3JpYWxpemVkU3BsaXRUaW1lRmlsdGVyJTIyJTNBbnVsbCUyQyUyMm9taXRQaW5uZWRQb3N0JTIyJTNBdHJ1ZSUyQyUyMnBvc3RlZEJ5JTIyJTNBJTdCJTIyZ3JvdXAlMjIlM0ElMjJPV05FUiUyMiU3RCUyQyUyMnByaXZhY3klMjIlM0FudWxsJTJDJTIycHJpdmFjeVNlbGVjdG9yUmVuZGVyTG9jYXRpb24lMjIlM0ElMjJDT01FVF9TVFJFQU0lMjIlMkMlMjJyZW5kZXJMb2NhdGlvbiUyMiUzQSUyMnRpbWVsaW5lJTIyJTJDJTIyc2NhbGUlMjIlM0ExJTJDJTIyc3RyZWFtX2NvdW50JTIyJTNBMSUyQyUyMnRhZ2dlZEluT25seSUyMiUzQW51bGwlMkMlMjJ0cmFja2luZ0NvZGUlMjIlM0FudWxsJTJDJTIydXNlRGVmYXVsdEFjdG9yJTIyJTNBZmFsc2UlMkMlMjJpZCUyMiUzQSUyMjEwMDA2NDc3Mzg0NzAyNSUyMiUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19HSExTaG91bGRDaGFuZ2VBZElkRmllbGROYW1lcmVsYXlwcm92aWRlciUyMiUzQWZhbHNlJTJDJTIyX19yZWxheV9pbnRlcm5hbF9fcHZfX0dITFNob3VsZENoYW5nZVNwb25zb3JlZERhdGFGaWVsZE5hbWVyZWxheXByb3ZpZGVyJTIyJTNBZmFsc2UlMkMlMjJfX3JlbGF5X2ludGVybmFsX19wdl9fSXNXb3JrVXNlcnJlbGF5cHJvdmlkZXIlMjIlM0FmYWxzZSUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19Db21ldEZlZWRTdG9yeUR5bmFtaWNSZXNvbHV0aW9uUGhvdG9BdHRhY2htZW50UmVuZGVyZXJfZXhwZXJpbWVudFdpZHRocmVsYXlwcm92aWRlciUyMiUzQTUwMCUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19Db21ldEltbWVyc2l2ZVBob3RvQ2FuVXNlckRpc2FibGUzRE1vdGlvbnJlbGF5cHJvdmlkZXIlMjIlM0FmYWxzZSUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19Xb3JrQ29tZXRJc0VtcGxveWVlR0tQcm92aWRlcnJlbGF5cHJvdmlkZXIlMjIlM0FmYWxzZSUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19Jc01lcmdRQVBvbGxzcmVsYXlwcm92aWRlciUyMiUzQWZhbHNlJTJDJTIyX19yZWxheV9pbnRlcm5hbF9fcHZfX0ZCUmVlbHNNZWRpYUZvb3Rlcl9jb21ldF9lbmFibGVfcmVlbHNfYWRzX2drcmVsYXlwcm92aWRlciUyMiUzQXRydWUlMkMlMjJfX3JlbGF5X2ludGVybmFsX19wdl9fQ29tZXRVRklSZWFjdGlvbnNFbmFibGVTaG9ydE5hbWVyZWxheXByb3ZpZGVyJTIyJTNBZmFsc2UlMkMlMjJfX3JlbGF5X2ludGVybmFsX19wdl9fQ29tZXRVRklTaGFyZUFjdGlvbk1pZ3JhdGlvbnJlbGF5cHJvdmlkZXIlMjIlM0F0cnVlJTJDJTIyX19yZWxheV9pbnRlcm5hbF9fcHZfX1N0b3JpZXNBcm1hZGlsbG9SZXBseUVuYWJsZWRyZWxheXByb3ZpZGVyJTIyJTNBdHJ1ZSUyQyUyMl9fcmVsYXlfaW50ZXJuYWxfX3B2X19FdmVudENvbWV0Q2FyZEltYWdlX3ByZWZldGNoRXZlbnRJbWFnZXJlbGF5cHJvdmlkZXIlMjIlM0FmYWxzZSU3RCZzZXJ2ZXJfdGltZXN0YW1wcz10cnVlJmRvY19pZD04ODgwMjU1NzQ1NDE3MTY5")

# response0 = requests.request("POST", "https://www.facebook.com/api/graphql/", headers=headers, data=payload)




tsls=[1388505600, 1420041600, 1451577600, 1483200000, 1514736000, 1546272000, 1577808000, 1609430400, 1640966400, 1672502400, 1704038400, 1735660800]

# https://www.facebook.com/TheJapanfoundation?locale=zh_CN
# https://www.facebook.com/sejonghakdang.org?locale=zh_CN
# https://www.facebook.com/InstCervantes?locale=zh_CN
# https://www.facebook.com/goetheinstitut?locale=zh_CN
# https://www.facebook.com/britishcouncil?locale=zh_CN
# https://www.facebook.com/Alliance.francaise.Paris?locale=zh_CN
idls=['100068979227279', '100064812213669', '100064569166827', '100064668674767', '100064629196375', '100064682377408']

def get_time(edge):
    try:
        return \
            edge['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0][
                'story']['creation_time']
    except:
        return \
            edge['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][1][
                'story']['creation_time']
for uid in idls:
    for i in range(len(tsls)):
        washed_data, cursor, index = [], '', 0
        while True:
            afterTime = str(tsls[i])
            beforeTime = str(tsls[i+1])
            try:
                payload = ('av=100038307016563&__aaid=0&__user=100038307016563&__a=1&__req=8s&__hs=20122.HYP:comet_pkg.2.1...1&dpr=1&__ccg=EXCELLENT&__rev=1019779472&__s=rpfh16:89u9la:txf94w&__hsi=7467133976958538178&__dyn=7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUaqwh8ngS3q2ibwNwnof8boG0x8bo6u3y4o2Gwfi0LVEtwMw6ywIK1Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C0Mo4G1hx-3m1mzXw8W58jwGzE8FU5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0SEuwLyEbUGdG0HE88cA0z8c84q58jyUaUbGxe6Uak0zU8oC1hxB0qo4e4UcEeE-3WVU-4EdrxG1fBG2-2K2G0JUmw&__csr=gqMm89hAh1d2AhidstcIIYrn2Rhv6Etbv94RsCQIG5A9aRFOihliiRpOBB9T4Or8CGQynlkijhvmh_WgxtAOsCRqkyjJaSZ7nDF5QUPWijiBnWF4GHoGKAUzKV9Aah9kCRKbGBFeAp4C_BAUHKb8ELVWAF6ruUZF4pHx14RmfBG2eegGjJ5gZ4gDCGfACBCDypEyqeHVqyox4zVBy8yEmyooQryoK4ENxOcxO79E9-5UnyEDUGq29AHjKEx5xCm4UhAGbDDwKz8HzprK4-8x2mq1lF1uEjUao8U8U4W5UWazU8oy9xi2m2CcyE-6Qdxi1kwxwm84a2m4E5u26cwUwZw4JxKaw6980qy2m3q524wkqwam0oqbzEx7lwl88o37ta685q0xk0g16yl4zU6q1Yxy1Mwyy88o22xytWy8S0y8x2axiK5Z0u82PwMKu_UOu01i0w1e3w3qU0IW09zw-UV5gsw3LEhw0aZR129w2sE1BEgxN2o22w28U1jE16E6m060E7m1iw1660bkw3rA0YUiw3s8y0jq0gTfU1V9U6B0fmt2Fm0s60KQ1pBu0QE0Yh0fK0g4EdE0iFwcjG06GUkw2lE3ua2m0iR02PoK0YU5y3K0jO0i60RE0oEg1AU52aw2IUGp0&__comet_req=15&fb_dtsg=NAcMDgf64KMXbMXJmudI3udXPC82J6_TDqUecrM_DUpKWQg7Et42s-A:24:1735468798&jazoest=25276&lsd=sVIMwbZH4roYjILpFnhEy2&__spin_r=1019779472&__spin_b=trunk&__spin_t=1738577610&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=ProfileCometTimelineFeedRefetchQuery&variables={"afterTime":%s,"beforeTime":%s'
                           ',"count":3,"cursor":"'
                           '%s","feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"memorializedSplitTimeFilter":null,"omitPinnedPost":true,"postedBy":{"group":"OWNER"},"privacy":{"exclusivity":"INCLUSIVE","filter":"ALL"},"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1,"stream_count":1,"taggedInOnly":false,"trackingCode":null,"useDefaultActor":false,"id":"%s","__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}&server_timestamps=true&doc_id=8880255745417169'
                           % (afterTime,beforeTime,cursor,uid))
                index += 1
                response = requests.request("POST", "https://www.facebook.com/api/graphql/", headers=headers, data=payload)
                print(index)
                datas = json.loads('[' + response.text.replace('\n', ',') + ']')
                with open(f"./data/{uid}-{afterTime}-{beforeTime}-{index}.json", 'w', encoding='utf-8') as f:
                    json.dump(datas, f, ensure_ascii=False, indent=4)
                cursor = re.findall(r'"end_cursor":"(.*?)"', response.text)[0]
            except IndexError as e:
                print('No more data')
                break

