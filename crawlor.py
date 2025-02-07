import json
import os.path
import re
from datetime import datetime
import requests

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
 'accept':'*/*',
 'accept-language':'en-US,en;q=0.5',
 'accept-encoding':'gzip',
 'content-type':'application/x-www-form-urlencoded',
 'x-fb-friendly-name':'ProfileCometTimelineFeedRefetchQuery',
 'x-fb-lsd':'dzmJ2QAME39tGlYIwsqgq-',
 'x-asbd-id':'129477',
 'content-length':'3085',
 'origin':'https://www.facebook.com',
 'referer':'https://www.facebook.com/HuaweiKE',
 'sec-fetch-dest':'empty',
 'sec-fetch-mode':'cors',
 'sec-fetch-site':'same-origin',
 'priority':'u=0',
 'pragma':'no-cache',
 'cache-control':'no-cache',
 'te':'trailers',
 'cookie':'dpr=1.3636363636363635; datr=CeWlZxZEis64BrH_-6G3JqKQ; sb=15KkZ3XgTWhOy12p0b6jbyTd; fr=1QM2wm0cwYA7oso7W.AWUSFlS2nsIgfqVE-bEKpva7PgysNT_wUAOayQ.BnpKxd..AAA.0.0.BnpeUr.AWWjX8MznJg; wd=1877x1027; locale=ar_AR; ps_l=1; ps_n=1; c_user=61572475985989; xs=30%3Akq-4jv72EuaBPA%3A2%3A1738925353%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1738925386552%2C%22v%22%3A1%7D'}



tsls=[1388505600, 1420041600, 1451577600, 1483200000, 1514736000, 1546272000, 1577808000, 1609430400, 1640966400, 1672502400, 1704038400, 1735660800]

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
        cursor, index = '', 1
        afterTime = str(tsls[i])
        beforeTime = str(tsls[i + 1])
        print(os.path.exists(f'./data/{uid}-{afterTime}-{beforeTime}-{index}.json'))
        if not os.path.exists(f'./data/{uid}-{afterTime}-{beforeTime}-{index}.json'):
            while True:
                try:
                    payload = ('av=61572475985989&__aaid=0&__user=61572475985989&__a=1&__req=17&__hs=20126.HYP:comet_pkg.2.1...1&dpr=1&__ccg=EXCELLENT&__rev=1019926383&__s=qyq64c:sgc67p:ps06i5&__hsi=7468627621020114671&__dyn=7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUaqwh8ngS3q2ibwNwnof8boG0x8bo6u3y4o2Gwfi0LVEtwMw6ywIK1Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C0Mo4G1hx-3m1mzXw8W58jwGzE8FU5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0SEuwLyEbUGdG0HE88cA0z8c84q58jyUaUbGxe6Uak0zU8oC1hxB0qo4e4UcEeE-3WVU-4FqwIK6E4-mEbUaU3ywo8&__csr=gT1Jd2k8gB6YlMP5Rdkt7imZRcJiRlHlN7Ncj5NkAgKykF7KhmF4lniRlfUBRF9lJEylcC9ih7pkZe9VW9EC_Gh4h9GOlBleFkjLlLmnyevzVHjVbZarJ4WnG4KvKilemjzFfyFk-FUB5Wmi-K4oWVO2oGAK9J4hEx12FXG6E98-il3eGybhuLAWGuUWF8O7kFrxfyoC9ggyam9Dxm8iy8oxnwzzoS8xi59byEKmaKiaDBVpokyFbz8OcyUeUyEC6oGu4oSm2aZKfxm2e2y5Uce2qUlz8aE8VouwPxW598boryUGbyof8ak2eczo9oO0IU1Svxm5oc85O1LzA0BEaEGewkFU3zwYCg12E4G16wgE2cc11zo5-6U7IM2Swok0SE4q1lxq17wRx2l1He0EEM-8gqgS18g3-wb91xOUN9d90aS4U1a815o05eHwf600WkQ09mweG0tqlS0vO09Ng46O0eXwmo20gbU2Bw31UG680Iu0g605to0Ti1Dw2Wk086xW0na02jS1Zw15YM0Vt01Au0c4w3KU2lw1RIw0LSpk1Bwbt06YG0LA&__comet_req=15&fb_dtsg=NAcN1hqlk612XlF1kBMWauaUiGNJllKO1Cf9SUYz2hQA06TTeTtRWIA:30:1738925353&jazoest=25273&lsd=dzmJ2QAME39tGlYIwsqgq-&__spin_r=1019926383&__spin_b=trunk&__spin_t=1738925376&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=ProfileCometTimelineFeedRefetchQuery&variables={"'
                               'afterTime":%s,"beforeTime":%s,"count":3,"cursor":"%s","feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"memorializedSplitTimeFilter":null,"omitPinnedPost":true,"postedBy":{"group":"OWNER"},"privacy":{"exclusivity":"INCLUSIVE","filter":"ALL"},"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1,"stream_count":1,"taggedInOnly":false,"trackingCode":null,"useDefaultActor":false,'
                               '"id":"%s","__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}&server_timestamps=true&doc_id=9585490784795618'
                               % (afterTime, beforeTime, cursor, uid)
                               )
                    response = requests.request("POST", "https://www.facebook.com/api/graphql/", headers=headers, data=payload)
                    datas = json.loads('[' + response.text.replace('\n', ',') + ']')
                    with open(f"./data/{uid}-{afterTime}-{beforeTime}-{index}.json", 'w', encoding='utf-8') as f:
                        json.dump(datas, f, ensure_ascii=False, indent=4)
                    cursor = re.findall(r'"end_cursor":"(.*?)"', response.text)[0]
                    print(str(datetime.now()) + f'./data/{uid}-{afterTime}-{beforeTime}-{index}.json')
                    index += 1
                except IndexError as e:
                    print('No more data')
                    break
        else:
            print(f'./data/{uid}-{afterTime}-{beforeTime}-{index}.json' + 'done')
            break
