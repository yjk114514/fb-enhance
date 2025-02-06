import json
import re
from datetime import datetime

import requests
import base64
# “缅甸汉语招聘”“老挝汉语招聘”
query = '老挝汉语招聘'
washed_data, cursor, index = [], '', 0
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'accept-encoding': 'gzip',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-friendly-name': 'SearchCometResultsPaginatedResultsQuery',
    'x-fb-lsd': 'S9qwEZKCgBowWy4957CAYD',
    'x-asbd-id': '129477',
    'content-length': '5228',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/search/top?q=pgc2024',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'te': 'trailers',
    'cookie': 'fr=0ssvjSmKuiVdQgCIv.AWXypz9iRzTCSrVQURkgO0-mRLQ.BnbtDQ..AAA.0.0.Bnb_DR.AWV_3viJ63g; ps_l=1; ps_n=1; datr=0dBuZ9JOSOLYOnYn6CQHVuQQ; sb=0dBuZ1XK5chQP176gBHqCqYH; wd=755x865; dpr=1.5; c_user=100038307016563; xs=12%3ALevWNRkUi1LD_A%3A2%3A1735389392%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1735389548570%2C%22v%22%3A1%7D'}

while True:
    try:
        payload = ('av=100038307016563&__aaid=0&__user=100038307016563&__a=1&__req=4j&__hs=20086.HYP:comet_pkg.2.1.0'
                   '.2.1&dpr=1&__ccg=EXCELLENT&__rev=1019094924&__s=obnjgl:sxcrtq:a17po4&__hsi=7453755759681933786'
                   '&__dyn=7xeXxaU5a5Q1ryaxG4Vp41twWwIxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb'
                   '-q7oc81EEc87m221Fwgo9oO0'
                   '-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K1yw9q2'
                   '-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE-3WVU-4EdrxG1fBG2-2K2G0JUmw&__csr'
                   '=gbY4AD0wYl5MDNstsD6kGtNs_PiT4YDtTeziZZ9t-OkG8Z9W9sJaV5_XbGhd6RLGOfLKRmLmmEy_yksxahfCZ9CBjm4Xy'
                   '-8JBiDmRCVeAFEnBQWAKi44EkyeWK8QFQjGq-4QVp8Su8hEOdAVUyuu291W6VEO7o-ch8-UW2-i444'
                   '-he14zFqCzu18xm8ABxi26223inwZAx2fzVFohx66oaoaEeU17o2SyUfo9831w9i2u0EE2nAw6bw1lS0qlm6E0JK0kB0iU'
                   '054O0avKi0nW00_Pmq8gKlw2bo0Gy3O0Coy0o5282Lw5mg1zES18w6Pw7xw9m0b_yE0hiw0BZw0qE9U0hiwbC'
                   '&__comet_req=15&fb_dtsg=NAcNXxi5DoiOHoE3axW9tnzyL-dDSUJXWERBkP1WPQQhHXylqMNmr-A:12:1735389392'
                   '&jazoest=25509&lsd=Q1p3l_KGnXTEEY6WXJJqFb&__spin_r=1019094924&__spin_b=trunk&__spin_t=1735462751&__jssesw=1'
                   '&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometResultsPaginatedResultsQuery'
                   '&variables={"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,'
                   '"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"0d94dd07-db21-4e40-8058-e47a8c8d9a19","tsid":null},'
                   '"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"POSTS_TAB"},"filters":[],'
                   '"text":"%s"},"count":5,"cursor":"%s","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,'
                   '"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,'
                   '"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider"'
                   ':false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,'
                   '"__relay_internal__pv__IsWorkUserrelayprovider":false,'
                   '"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}'
                   '&server_timestamps=true&doc_id=8774939689226917' % (query, cursor))

        # print(payload)
        index += 1
        response0 = requests.request("POST", "https://www.facebook.com/api/graphql/", headers=headers, data=payload)
        print(response0.status_code)
        with open('example.txt', 'w') as f:
            f.write(response0.text)

        data = json.loads('[' + response0.text.replace('\n',
                                                       ',') + ']')
        edges = data[0]['data']['serpResponse']['results']['edges']
        try:
            for edge in edges:
                def get_time(edge):
                    try:
                        return edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'context_layout']['story']['comet_sections']['metadata'][0]['story'][
                                'creation_time']
                    except:
                        return edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][1]['story']['creation_time']

                washed_data.append(
                    {
                        #
                        #     /1/rendering_strategy/view_model/click_model/story/comet_sections/content/story/actors/0/name
                        #     /0/data/serpResponse/results/edges/2/rendering_strategy/view_model/click_model/story/comet_sections/feedback/story/story_ufi_container/story/feedback_context/feedback_target_with_context/comet_ufi_summary_and_actions_renderer/feedback/comment_rendering_instance/comments/total_count
                        'comment_count':
                            edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'feedback']['story']['story_ufi_container']['story']['feedback_context'][
                                'feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback'][
                                'comment_rendering_instance']['comments']['total_count'],
                        # /0/data/serpResponse/results/edges/1/rendering_strategy/view_model/click_model/story/comet_sections/content/story/message/text

                        'text':
                        # /0/data/serpResponse/results/edges/1/rendering_strategy/view_model/click_model/story/comet_sections/content/story/comet_sections/message/story/message/text
                            edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'content']['story']['message']['text'],
                        #     /0/data/serpResponse/results/edges/1/rendering_strategy/view_model/click_model/story/comet_sections/content/story/wwwURL
                        'url':
                            edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'content']['story']['wwwURL'],
                        'name':
                            edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'content']['story']['actors'][0]['name'],
                        'create_at': datetime.fromtimestamp(get_time(edge)).strftime('%Y-%m-%d %H:%M:%S'),
                        # /0/data/serpResponse/results/edges/0/rendering_strategy/view_model/click_model/story/comet_sections/context_layout/story/comet_sections/metadata/1/story/creation_time
                        'i18n':
                            edge['rendering_strategy']['view_model']['click_model']['story']['comet_sections'][
                                'feedback']['story']['story_ufi_container']['story']['feedback_context'][
                                'feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback'][
                                'i18n_reaction_count'],
                    }
                )
                print(len(washed_data))
        except Exception as e:
            print(e)
        with open(f"./fb/{index}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # try:
        cursor = re.findall(r'"end_cursor":"(.*?)"', response0.text)[0]
        print(cursor)
        if len(cursor) == 88:
            break
            # except Exception as e:
        #     print(e)
        #     break
    #      /data/
    except Exception as e:

        print(e)
    # News1.json:5
    # print(response0.text)
    # av=100038307016563&__aaid=0&__user=100038307016563&__a=1&__req=1a&__hs=20085.HYP:comet_pkg.2.1.0.2.1&dpr=1&__ccg=EXCELLENT&__rev=1019092663&__s=dah5i6:suaoa1:m3dwqk&__hsi=7453441295719487814&__dyn=7xeXxaU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3VwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgU4q3Gfw-Kufxa3mUqwjVqwLwHwGwbu&__csr=gckn2Hb5htN2sWtPhCNGtikD8T68DkZlJWh6xip59jW4fOF5tb4XlilAjSXWlkBZOp4aKjheXyQH_p5mFdmi8WAHU8JyBQvgN0FGqcKWVVlKUiUCmHiKEGmhosx538gxaaKu59E9azK9Upwi8G2a8yE8UmyUdqDwHJ2Uym11xi3-3ui6Ua89EDzEbUd8kwwxm1DwnU3Lwo8pwiE0Fe8xG05hA1zw1jhopxzw53w0rsE1QE03MDwd669U1I9U1r81Xo3Fw0zrwqEgxW0ePw0hjE3sg07Wq0hq02dG&__comet_req=15&fb_dtsg=NAcOZwJcK4UUbRzdrbYKxLnGhdXsMYHL7AtSK1P12_xJoZKSrBKtImQ:12:1735389392&jazoest=25525&lsd=S9qwEZKCgBowWy4957CAYD&__spin_r=1019092663&__spin_b=trunk&__spin_t=1735389534&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometResultsPaginatedResultsQuery&variables={"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"1c3ff538-0e1f-44b7-91af-2d7a470b2449","tsid":null},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GLOBAL_SEARCH"},"filters":[],"text":"PGC2024"},"count":5,"cursor":"Abr-rbIYii6dZkglzGDtiXk5VF2DHhQVpiMYF19o4S3x5mnvySqsN2A3vjUil3n-ohFA_JBxrf3_WBZgjECHUSIwANs3l_yjTjsvksdcgprtOJKm0FE9SrSCB0KUie8_o0RWolfRA1DwlZS_ZhiiYjFosIV-EZJyr6duq2ikCqw95ae-4fXViGMhs_okS04GvYMt9bCkDNS5r78p7itweQcG6EyFXFEcVsOrjrhzNVWMzBX0qEW2ny-6NX-FelzcBJuBZw1hgdDQw4pmOo7ouCUcOzZUxFBo71XlZin5EZ8N42omGYy0OpwK_g3HJJQIkVGV5_euUaLbh2_vpL8fFnLHSWQ2TJzC80ROWvTM2RPbYzSFydURprmEczmpMx1Ex06Wy6DGXgr77KlHsapk2ZgFQpYfZSYkOzfnkhwCRH4XVH8xdFK2I7IXHCwYPo7FiADjmiIYaETq0pPi2AUtMcRd5682pHIWbzYcbkvsGz_SUTCvh3hhwANhqb-Bs7YLc2TdZ7KKmWQWZa8O4UIv-SJ_0jc9AAz560zb5SXUgrymg4qw-h-27mC8ll3lID_S8nKHqMT-tyNLk0QsMN2TldxwvMMAhbqOZWAdkvSQXU-hw-1S7JT4lWQEstL_Qlu4F_JrEFPDJLcqDHwmHZHZKQdhAYFJoZ77x4XV_vJQlO9uvEXwlts5GK741_2BC48qEXRoK98kQSYrv4jnXGF130S8CY2r1TjiasF-qxu1xvtSjx0SsUa6fJwYgaMNy8L-6vpQEcH1AN5b5xGHe5YykP1JsjfAoCJ2uqBYlQcplFP0DXe6DlkXhkviPvZurS0NL2CZ9x6el5AAYFDTEiwMAZx3yhskEGU-6sg0SFpCH56BzlHcnxYN4LwwNn7yH3c0R6ZQEimVIHXRFxrUEphvumm7x2t3mfxyeVFb9D5dK_R1COv7CeGTrut48xSW7oVlmHMPTl9auIaPt_E4AunazLosXG3tjy9OedlnAvHyDQX_HymZScllNzhKi-n_f5DCa41d7Pqkl6Q-wZBwMKEjddJnO8cIxTigaD2VMFUuhVMVlSvqlbP751hPmb4MIa7UK5iKOWUj4CYClGMJwJ6S4hPun7CylaYao5kkPaJPhO4AfypwpXm0Z7gv8-FhPBvfUlc33uPKvhTUa_E9rqY4YjOm3b_kZMv12ngGaordohk-IHNBhLSsSJ8LMezODiOatPe1nN9D5jq64CHbrXxoJ_H9IYir1dhOdpbHFDAB29VNArt_XqDCUXIHNuRAbh_M4zUfqgYzku6ZrH8oTjrATn0SAth2s5BneA0B0bZC_MA0emFs8UHG3OPRSKFWcGYdbGT1Ot-5i17CVQqJHcQsF6he4eg1UbQL_De2ZpKrkpDydFY2KAyNaneoLa4_5CS0_w_sve0bUAD7KANM9GhZCsYmgACu33tG4kH6B3LbR6DoxMN7_PPcspLKhAvo7sQIOR3A6zweMefGvysIV6tsBW7qaTi4RybQiKqQEesnoHqvf0-INhMhDHLVFGkPJPLLlQjQMfkIzYGjY0mFOBh_R9dMoWBUnT3ZNpirMIL6MisudauobCeAGlMj3ZOxaA8TCgwHkucPJUBkaRK7pSCY4BslLkdQdJ4x-Cn8LPuagpILsOquH0LkGoHemiEp5hQzwr1f-unApK6WIO_x1-_tX-Mbrdvm2uRxTPuGlPGjvGK4RrNfiHaY3mKf0-g1yzy0h9VstcF9Z-cLyg0ZBitnJVZ4FgA3xL3EuA3UJPF6im3OWPBDG1OmQkXVvmcxN_iKltUkKE42X1fEWiv393odG8xwcR8SW5ts12xJDQh_ncTdS697wD23RTnJPD1RJAHQX1j3D_YK6U0D9asL0dTeUUNUvC4KdYA90KMqVcV0OU_y1WJErEmg-AdDp8wxxSvqY5gt2mH8MDj3JcU940PyxQwGF_czY_ABT5qEmXRe74oWc30uw9B2q2p2hfC48BHAeYeLdruIhBtlCoXUXeW9MKMUHjr5WWffv6ySY98ggoqMkf3wnByTDvneWs0Js0RBQ9VeH6OFBXwTzFOXIM0EVMtHQycqkW_Yv4oWivPSydzh4Xw0mA9Gj5tTQ0m3O0D-CNg","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}&server_timestamps=true&doc_id=8774939689226917
    finally:
        with open(r'D:\Project\fb-enhance\laowo.json', 'w', encoding='utf-8') as f:
            json.dump(washed_data, f, ensure_ascii=False, indent=4)
