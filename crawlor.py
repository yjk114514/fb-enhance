import json
import re
from datetime import datetime

import requests
import requests
import base64
import requests
import base64

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
 'accept':'*/*',
 'accept-language':'en-US,en;q=0.5',
 'accept-encoding':'gzip',
 'content-type':'application/x-www-form-urlencoded',
 'x-fb-friendly-name':'ProfileCometTimelineFeedRefetchQuery',
 'x-fb-lsd':'HD2_w0HxWcMdmPxzgkUScx',
 'x-asbd-id':'129477',
 'content-length':'3314',
 'origin':'https://www.facebook.com',
 'referer':'https://www.facebook.com/deutschewellenews',
 'sec-fetch-dest':'empty',
 'sec-fetch-mode':'cors',
 'sec-fetch-site':'same-origin',
 'priority':'u=0',
 'te':'trailers',
 'cookie':'dpr=1.3636363636363635; datr=15KkZ_URQFmyHdPIKo8LRsEz; sb=15KkZ3XgTWhOy12p0b6jbyTd; fr=0YtshtZAymXVAnq9S.AWVy39Mz47QJQwZL8Q4XfOssU1dBss4FG-jyIQ.BnpJLY..AAA.0.0.BnpJN4.AWXBglqVg8g; wd=1877x1027; locale=ar_AR; c_user=61572475985989; xs=40%3AmyjFEw-ddYGIKQ%3A2%3A1738838792%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1738838910834%2C%22v%22%3A1%7D; ps_l=1; ps_n=1'}


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
                payload = ('av=61572475985989&__aaid=0&__user=61572475985989&__a=1&__req=2e&__hs=20125.HYP:comet_pkg.2.1...1&dpr=1&__ccg=EXCELLENT&__rev=1019888288&__s=2rvor6:g0hy3m:36kg04&__hsi=7468256226017506869&__dyn=7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUao4u5QdwSwAyUco5S3O2Saw8i2S1DwUx60GE3Qwb-q7oc81EEbbwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2au1jwUBwJK14xm3y11xfxmu3W3rwxwjFovUaU6a1TxW2-awLyESE2KwwwOg2cwMwhEkxebwHwKG4UrwFg2fwxyo566k1FwgUjwOwWzUfHDzUiBG2OUqwjVqwLwHwGwbu1ww&__csr=g9Ap1P7Mz2s4RiMPb2Ap5NYjsIchlMzkmz_jlRbFt9EABjJrmylKjm_trieQJhsGnXFiGJ4tPmHqF9BOF9J6Zq8GVbmAKejulVpdR-ZpfiTRlHyF4IyHhmipdbQl6HjQcTQLDgBKmjAHFvZt2fDHLGiq9mAqtaUGmUVfGvhrLh9fAF4GXBhQVbyqx3yZeuAh7_LgSdGjGSb-VAgxFUObAxmiicx2GKfh8jWVUgLKHqy9GF5yXUmAzUSeG9V4uF4iKrRBKqFKES4RyWmcGdDKuEKuUyeyA8xGF9WQHBBBDGFFqxfxiiFFaCGqcFehe2SqbzEOdyUoxm9iBxKeBGmmFohUsAgyu2m9yokAwYxa2ueBwx9ximi6ui2qi4lF2oLDzbK8CyEK2t1m6UlxuqaDxDV8aE8E7it2ES0IFU4-2q78CUgxqFAFf9wVxi1jw7lzE3Xxu1RxW0j1xt1q6Frx6JlLh82Ow9q0BE9E9ag3Ww8C7e2PxR7g2twsUnG8AwAwzp83cy43yEgauaBwr9Ga3q0lO0GpEC5Q9Z1amagG2W0ma0To0lgKE1O81FC0iK0hCu1Kw0Adw0eo60yA0pK08fxR05Gxe5cwnwLw6nDwncw1-83wwqU2Axqu09pw8KeyE31g6e1Nwfu5i4Dx50g82Mxp0riyU4yfw7nzU0Eq0PU0HSu0mm3S04RE4R00wpw7sw_xG4U5l011S5cw1KU1dU7d01Au1T808fw9ecg1SE1eo10o0mSCm04-IwjwjFU5wE0xKE63xu1pBio659woEH5O0&__comet_req=15&fb_dtsg=NAcM8wKEsPnmV7SnWNxpK20cxNgZPYEy8s1Q_kiXrryP-CAzaXwkR_Q:40:1738838792&jazoest=25650&lsd=HD2_w0HxWcMdmPxzgkUScx&__spin_r=1019888288&__spin_b=trunk&__spin_t=1738838904&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=ProfileCometTimelineFeedRefetchQuery&variables='
                   '{"afterTime":"%s","beforeTime":"%s","count":3,"cursor":"%s",'
                   '"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"memorializedSplitTimeFilter":null,"omitPinnedPost":true,"postedBy":{"group":"OWNER"},"privacy":{"exclusivity":"INCLUSIVE","filter":"ALL"},"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1,"stream_count":1,"taggedInOnly":false,"trackingCode":null,"useDefaultActor":false,'
                   '"id":"%s","__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}&server_timestamps=true&doc_id=9028586980511841'
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

