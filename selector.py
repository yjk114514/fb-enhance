import os
import json
import re
from datetime import datetime
washed_data=[]
should_num=0
def search():
    for filepath in os.listdir('./fb'):
        with open(filepath, 'r') as f:
            datas = json.load(f)
            for data in datas:

                if data.get("label",None) == 'CometNewsFeed_viewerConnection$stream$CometNewsFeed_viewer_news_feed':
                    story = data['data']['node']['comet_sections']['content']['story']

                elif data.get("label",None) == "None":
                    story = data['data']['viewer']['news_feed']['edges'][0]['node']['comet_sections']['content']['story']
                else:
                    continue
                try:
                    washed_data.append(
                        {
                            'name':
                                story['actors'][0]['name'],
                            'text':
                                story['message']['text'],
                            'url':
                                story['wwwURL'],
                            'create_at': datetime.fromtimestamp(
                                int(re.findall(r"'creation_time': (\d+)", str(data))[0])
                            ).strftime(
                                '%Y-%m-%d %H:%M:%S'),
                        })
                    print("Got "+str(len(washed_data)))
                except:
                    pass

def profile():
    should_num=0
# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/comet_sections/attached_story/story/attached_story/comet_sections/attached_story_layout/story/comet_sections/message/story/message/text
# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/comet_sections/attached_story/story/attached_story/comet_sections/attached_story_layout/story/message/text
# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/attached_story/comet_sections/message/story/message/text
# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/attached_story/message/text
    for filepath in os.listdir('./data'):
        with open('./data/'+filepath, 'r',encoding='utf-8') as f:
            datas = json.load(f)
            should_num += len(datas)
            if filepath == '1704038400-1735660800-4.json':
                # for data in datas:
                #     if data.get("label", None) != None:
                #         content = data['data']['node']['comet_sections']['content']['story']
                #         feedback = data['data']['node']['comet_sections']['feedback']['story']
                #     elif data.get("label", None) == None:
                #         content = \
                #         data['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections'][
                #             'content']['story']
                #         feedback = \
                #         data['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections'][
                #             'feedback']['story']

                print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            for data in datas:
                try:
                    if data.get("label", None) != None:
                        content = data['data']['node']['comet_sections']['content']['story']
                        feedback = data['data']['node']['comet_sections']['feedback']['story']
                    elif data.get("label", None) == None:
                        content = data['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']
                        feedback = data['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']

                    washed_data.append(
                        {
                            'name':
                                "Huawei  Kenya",
                            'text':
                                list(set(re.findall(r"'text': \"(.*?)\"",str(content))+re.findall(r"'text': '(.*?)'",str(content)))),
                            'create_at': datetime.fromtimestamp(
                                int(re.findall(r"'creation_time': (\d+)", str(data))[0])
                            ).strftime(
                                '%Y-%m-%d %H:%M:%S'),
                            'like':int(re.findall(r"'i18n_reaction_count': '(\d+)'", str(feedback))[0]),
                            'comment':int(re.findall(r"'total_count': (\d+)", str(feedback))[0]),
                            'share':int(re.findall(r"'i18n_share_count': '(\d+)'", str(feedback))[0]),
                        })

                except Exception as e:
                    print(filepath+'[[[]]]'+str(e))
                    print(data.get("label", None))

            print(len(datas))
            print("Got " + str(len(washed_data)))
            print("Should " + str(should_num))
    with open('./washed_data.json', 'w', encoding='utf-8') as f:
        json.dump(washed_data, f, ensure_ascii=False, indent=4)







profile()



# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/comet_sections/message/story/message/text

# /1/data/node/comet_sections/content/story/comet_sections/message/story/message/text

# /1/data/node/comet_sections/content/story/message/text

# /0/data/node/timeline_list_feed_units/edges/0/node/comet_sections/content/story/message/text