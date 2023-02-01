import requests


def get_player_scorecard(tournament_no, player_id):
    import requests

    cookies = {
        '_gcl_au': '1.1.1955687119.1661951521',
        '_fbp': 'fb.1.1661951523732.1420167544',
        'qcSxc': '1661951523875',
        'gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q': '_gigya_ver4',
        'G_ENABLED_IDPS': 'google',
        '__qca': 'P0-1434189941-1661951523872',
        '_hjSessionUser_1411640': 'eyJpZCI6IjgzYjIzOGM2LTcyZWItNWQzYS1iMzI5LThmNDU3YjlmY2JiMiIsImNyZWF0ZWQiOjE2NjE5NTE1MjM5OTksImV4aXN0aW5nIjp0cnVlfQ==',
        '__gads': 'ID=8d4c672df17d5562:T=1661951535:S=ALNI_MYF5Kdf7oVLKILFMwG94yl7bI1s9g',
        '__lxG__consent__v2': '1%7C1%7C1661951527128%7C161%7C1665564003679%7C2%7C1%7C1%7C1663836003679%7C1',
        '__lxG__consent__v2_daisybit': 'CPema1cPfuTnlA_ADAENChCsAP_AAH_AAAAAJANd_H__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4Eu1LBIQNlHMHUDUmwaokVryHsak2cpzNKJ7JEknMZOydYGF9vmxtj-YKY7_5_9_bx2D-t_9v239z378Xf3_d5_2_-_vCfV5_9jfn9fR_789KP9_58v-_8_____3____3_79wSAAJMNW4gC7MscGbQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgE-sIGACAUARgRAhxBRgQCAAASAJCIAJAiwQCIAiAQAAgARCIQAMTAILACwMAgABANAxRCgAECQgyICIpTAgKgSCA1sqEEoK9DTCAOs8AKDRGxUACJJARSAAJCwcAwRICViwQNMUb5ACMEKAUSoVgAA.YAAAAAAAAAAA',
        '__lxG__consent__v2_gdaisybit': '~1~39.43969.13.64.15.9527417132.10.39.21.4697.12.92.18.76.14.5.20.65131.11..29.4.14.453.10.629664544.29.453162.19.1.17..10.91862834.142.4.50..15.1.17.18.10..25..10..25.5.18.97.41.24.18..24.427652.14..18.73228.28.863.10.4.20.2.13.4.10..11.13.22..16.26824.11.65.33..11.81.10..28..12.1.24.27619.30..17.49.15.873.12.9417.12..13..22..13.2.12.2.10.14.15.2494547.13.5.15.4.13.4.14.82.15.2562212.14.74829.10..18..12..13.2.18.113119.25.41.19.84535484222.14.2.13.426963435236.10..11.63.19..11.31239.19..11..15.3.10..13.434633331116.11.311.11.61.10.52632243227.15.7.12.2133454322531112916915217.10..11.1311213261.12.813112277141261211311411218174321353961.15..10..28.122.12.341634713113153134114212122242122241112211112111221121217122121111211321181115216511111223114112211431412123112411151363152341231421222111111.11.131122523351116112519411317145172111211142.13.1131223121112131111241512438229722121461711',
        'gig_canary': 'false',
        'glt_4_LtiNVJuKIvw_FXO5qOsf6Q': 'st2.s.AcbHOvGwVg.oPE5MFymJr20S28ul-tBdjAmYCptWypFATSnfCQDIGKs839zS8jE6zjdqCbHROn3zPEgC28DQnC75Ztd4o0kyCr0RWfu3sICQhh9JwM5q9s.JNDHO4RCLqjyUTP8QSM-bXFOLP1ntlbPLRc1Nl0HWlD5gsjmMTcaWlHSBqoMWAOx_Ng7Yob0wQHSckoCs3gEiA.sc3',
        '_gid': 'GA1.2.2090477817.1664272626',
        '_hjSession_1411640': 'eyJpZCI6IjA2MzBlMjllLTY5ZDQtNDFiZS1iZWRiLWNlNWVhNzdjNmQxNSIsImNyZWF0ZWQiOjE2NjQ0NzMyMzIxMTAsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_pbjs_userid_consent_data': '2583781852158826',
        '_gat_UA-132881508-1': '1',
        '_dc_gtm_objectObject': '1',
        '_gat_UA-144426812-3': '1',
        'gig_canary_ver': '13406-3-27741150',
        '_hjIncludedInSessionSample': '0',
        '_dc_gtm_UA-132881508-1': '1',
        '_ga': 'GA1.2.1589499720.1661951521',
        '_awl': '2.1664474151.0.5-5d050034fd06d83862cadfc3317999bb-6763652d6575726f70652d7765737431-0',
        '_ga_2Z1KRCE5HY': 'GS1.1.1664472872.38.1.1664474151.0.0.0',
        'cto_bundle': '19zgU18lMkY1QnVkVjhqSEdMRCUyRnRqSnl3VVFFUCUyQnRJZjc1JTJGWnZQTyUyQk5OWG9uTll2cFVhVkklMkZQeFYxVEM5TzFkWU5ZZmViVmtNR1pxN2JoR213T1dRWHpBdFY5aUx4cXBORjRCczJhV0tRRFF6YWVNZWhXZk5lbktNY0JBMzEwYzZ2T2xROCUyQkRGZTBEb3plRU4wJTJGaktFZ25Kd0VvRmEyVm16OWxFcnJ0UkxMZUllNnFoanluUVRxRW0xOVV3TzlIcXRERDlMWU5rNEFRVVFHVmhZbHQwWms5JTJGeDF3JTNEJTNE',
    }

    headers = {
        'authority': 'www.europeantour.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/json; charset=utf-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1955687119.1661951521; _fbp=fb.1.1661951523732.1420167544; qcSxc=1661951523875; gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q=_gigya_ver4; G_ENABLED_IDPS=google; __qca=P0-1434189941-1661951523872; _hjSessionUser_1411640=eyJpZCI6IjgzYjIzOGM2LTcyZWItNWQzYS1iMzI5LThmNDU3YjlmY2JiMiIsImNyZWF0ZWQiOjE2NjE5NTE1MjM5OTksImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=8d4c672df17d5562:T=1661951535:S=ALNI_MYF5Kdf7oVLKILFMwG94yl7bI1s9g; __lxG__consent__v2=1%7C1%7C1661951527128%7C161%7C1665564003679%7C2%7C1%7C1%7C1663836003679%7C1; __lxG__consent__v2_daisybit=CPema1cPfuTnlA_ADAENChCsAP_AAH_AAAAAJANd_H__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4Eu1LBIQNlHMHUDUmwaokVryHsak2cpzNKJ7JEknMZOydYGF9vmxtj-YKY7_5_9_bx2D-t_9v239z378Xf3_d5_2_-_vCfV5_9jfn9fR_789KP9_58v-_8_____3____3_79wSAAJMNW4gC7MscGbQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgE-sIGACAUARgRAhxBRgQCAAASAJCIAJAiwQCIAiAQAAgARCIQAMTAILACwMAgABANAxRCgAECQgyICIpTAgKgSCA1sqEEoK9DTCAOs8AKDRGxUACJJARSAAJCwcAwRICViwQNMUb5ACMEKAUSoVgAA.YAAAAAAAAAAA; __lxG__consent__v2_gdaisybit=~1~39.43969.13.64.15.9527417132.10.39.21.4697.12.92.18.76.14.5.20.65131.11..29.4.14.453.10.629664544.29.453162.19.1.17..10.91862834.142.4.50..15.1.17.18.10..25..10..25.5.18.97.41.24.18..24.427652.14..18.73228.28.863.10.4.20.2.13.4.10..11.13.22..16.26824.11.65.33..11.81.10..28..12.1.24.27619.30..17.49.15.873.12.9417.12..13..22..13.2.12.2.10.14.15.2494547.13.5.15.4.13.4.14.82.15.2562212.14.74829.10..18..12..13.2.18.113119.25.41.19.84535484222.14.2.13.426963435236.10..11.63.19..11.31239.19..11..15.3.10..13.434633331116.11.311.11.61.10.52632243227.15.7.12.2133454322531112916915217.10..11.1311213261.12.813112277141261211311411218174321353961.15..10..28.122.12.341634713113153134114212122242122241112211112111221121217122121111211321181115216511111223114112211431412123112411151363152341231421222111111.11.131122523351116112519411317145172111211142.13.1131223121112131111241512438229722121461711; gig_canary=false; glt_4_LtiNVJuKIvw_FXO5qOsf6Q=st2.s.AcbHOvGwVg.oPE5MFymJr20S28ul-tBdjAmYCptWypFATSnfCQDIGKs839zS8jE6zjdqCbHROn3zPEgC28DQnC75Ztd4o0kyCr0RWfu3sICQhh9JwM5q9s.JNDHO4RCLqjyUTP8QSM-bXFOLP1ntlbPLRc1Nl0HWlD5gsjmMTcaWlHSBqoMWAOx_Ng7Yob0wQHSckoCs3gEiA.sc3; _gid=GA1.2.2090477817.1664272626; _hjSession_1411640=eyJpZCI6IjA2MzBlMjllLTY5ZDQtNDFiZS1iZWRiLWNlNWVhNzdjNmQxNSIsImNyZWF0ZWQiOjE2NjQ0NzMyMzIxMTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _pbjs_userid_consent_data=2583781852158826; _gat_UA-132881508-1=1; _dc_gtm_objectObject=1; _gat_UA-144426812-3=1; gig_canary_ver=13406-3-27741150; _hjIncludedInSessionSample=0; _dc_gtm_UA-132881508-1=1; _ga=GA1.2.1589499720.1661951521; _awl=2.1664474151.0.5-5d050034fd06d83862cadfc3317999bb-6763652d6575726f70652d7765737431-0; _ga_2Z1KRCE5HY=GS1.1.1664472872.38.1.1664474151.0.0.0; cto_bundle=19zgU18lMkY1QnVkVjhqSEdMRCUyRnRqSnl3VVFFUCUyQnRJZjc1JTJGWnZQTyUyQk5OWG9uTll2cFVhVkklMkZQeFYxVEM5TzFkWU5ZZmViVmtNR1pxN2JoR213T1dRWHpBdFY5aUx4cXBORjRCczJhV0tRRFF6YWVNZWhXZk5lbktNY0JBMzEwYzZ2T2xROCUyQkRGZTBEb3plRU4wJTJGaktFZ25Kd0VvRmEyVm16OWxFcnJ0UkxMZUllNnFoanluUVRxRW0xOVV3TzlIcXRERDlMWU5rNEFRVVFHVmhZbHQwWms5JTJGeDF3JTNEJTNE',
        'if-none-match': '"BSK7fZzP0SgtTD9fNh21qp6rXfbGI5mGaM9o7DhV6o8LZfLKwgembuoy0a9JY04r7mJ1rvVBBayjS4hK8gx1XA"',
        'referer': 'https://www.europeantour.com/dpworld-tour/alfred-dunhill-links-championship-2022/leaderboard?round=1',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://www.europeantour.com/api/sportdata/Scorecard/Strokeplay/Event/{tournament_no}/Player/{player_id}', cookies=cookies,
        headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def get_all_players(tournament_no):
    cookies = {
        '_fbp': 'fb.1.1657208105279.1235282127',
        'X-SID': '8d1bd0c6ca12752bbba8025b_1657208265',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'nl,en-US;q=0.7,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'https://fantasy.dpworldtour.com/team',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1657208105279.1235282127; X-SID=8d1bd0c6ca12752bbba8025b_1657208265',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-Modified-Since': 'Thu, 07 Jul 2022 15:35:08 GMT',
        'If-None-Match': '"008113792b9168849dca4d8ecc2a4cfe"',
        'Cache-Control': 'max-age=0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(f'https://fantasy.dpworldtour.com/json/players/{tournament_no}.json', cookies=cookies,
                            headers=headers)
    db = {}

    for item in response.json():
        db[item['id']] = item

    return db


def check_none(element):
    return 0 if element is None else element


def process_custom_data(db, my_players, tournament_no, captain):
    my_lineup = []

    for player_loop in my_players:
        my_lineup.append(db[player_loop])

    # leaderboard = get_event_stats(tournament_no)
    # projected_cut = leaderboard['Players'][leaderboard['CutValue'] - 1]['ScoreToPar']

    event_stats = []

    counter = 0
    for sel_player in my_lineup:

        position = None
        position_available = False
        if str(tournament_no) in sel_player['stats']['positions']:
            position_available = True
        if position_available:
            tied = sel_player['stats']['positions'][str(tournament_no)]['is_tie']
            position = sel_player['stats']['positions'][str(tournament_no)]['position']
            str_position = str(position)
            if tied:
                str_position = "T" + str(position)
            

        data = {'firstname': sel_player['firstname'],
                'lastname': sel_player['lastname'],
                'captain': True if captain == sel_player['id'] else False,
                'albatross': check_none(sel_player['event_stats']['albatross']),
                'eagles': check_none(sel_player['event_stats']['eagles']),
                'birdies': check_none(sel_player['event_stats']['birdies']),
                'pars': check_none(sel_player['event_stats']['pars']),
                'bogeys': check_none(sel_player['event_stats']['bogeys']),
                'double_bogeys': check_none(sel_player['event_stats']['double_bogeys']),
                'triple_bogeys_or_worse': check_none(sel_player['event_stats']['triple_bogeys_or_worse']),
                'score': sel_player['event_stats']['score'],
                'position': "T150" if position is None else str_position,
                'true_pos': 150 if position is None else position,
                'above_cut_off': sel_player['above_cut_off'],
                'scorecard': get_player_scorecard(tournament_no, sel_player['id'])
                }

        # # likelyhood_to_make_cut = projected_cut - data['score']
        #
        possible_scores = ['albatross',
                           'eagles',
                           'birdies',
                           'pars',
                           'bogeys',
                           'double_bogeys',
                           'triple_bogeys_or_worse']
        #
        total_holes_played = 0
        for x in possible_scores:
            total_holes_played += data[x]

        on_hole = "-"

        if total_holes_played > 0 and total_holes_played < 18:
            on_hole = total_holes_played
        elif total_holes_played == 18:
            on_hole = "-"
        elif total_holes_played > 18 and total_holes_played < 36:
            on_hole = total_holes_played - 18
        elif total_holes_played == 36:
            on_hole = "-"
        elif total_holes_played > 36 and total_holes_played < 54:
            on_hole = total_holes_played - 36
        elif total_holes_played == 54:
            on_hole = "-"
        elif total_holes_played > 54 and total_holes_played < 72:
            on_hole = total_holes_played - 54
        elif total_holes_played == 72:
            on_hole = "-"
        else:
            on_hole = "-"


        # chance_albatross = data['albatross'] / total_holes_played
        # chance_eagles = data['eagles'] / total_holes_played
        # chance_birdie = data['birdies'] / total_holes_played
        # chance_pars = data['pars'] / total_holes_played
        # chance_bogeys = data['bogeys'] / total_holes_played
        # chance_double_bogeys = data['double_bogeys'] / total_holes_played
        # chance_triple_bogeys_or_worse = data['triple_bogeys_or_worse'] / total_holes_played

        finishing_hole_today = 0
        if total_holes_played < 18:
            finishing_hole_today = 18
        elif total_holes_played >= 18 and total_holes_played < 36:
            finishing_hole_today = 36
        elif total_holes_played >= 36 and total_holes_played < 54:
            finishing_hole_today = 54
        else:
            finishing_hole_today = 72
        #
        remaining_holes_to_be_played = finishing_hole_today - total_holes_played
        #
        data['total_holes_player'] = total_holes_played
        data['remaining_holes_today'] = remaining_holes_to_be_played
        data['on_hole'] = on_hole
        # data['albatross_chance'] = chance_albatross
        # data['eagles_chance'] = chance_eagles
        # data['birdies_chance'] = chance_birdie
        # data['pars_chance'] = chance_pars
        # data['bogeys_chance'] = chance_bogeys
        # data['double_bogeys_chance'] = chance_double_bogeys
        # data['triple_bogeys_or_worse_chance'] = chance_triple_bogeys_or_worse
        # data['score_off_cut'] = likelyhood_to_make_cut
        # if likelyhood_to_make_cut < 0:
        #     data['below_projected_cut'] = True
        # else:
        #     data['below_projected_cut'] = False
        #
        event_stats.append(data)
        counter += 1
    return event_stats


def get_top_dogs(limit: str, EVENT_NUMBER, all_players):
    import requests

    cookies = {
        '_fbp': 'fb.1.1652271886639.994733280',
        'X-SID': 'c899849a9e7c656de2e34963_1657778331',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_fbp=fb.1.1652271886639.994733280; X-SID=c899849a9e7c656de2e34963_1657778331',
        'pragma': 'no-cache',
        'referer': 'https://fantasy.dpworldtour.com/leaderboard',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    params = {
        'limit': limit,
        'page': '1',
    }

    response = requests.get('https://fantasy.dpworldtour.com/api/fantasy/rankings/1/rankings', params=params,
                            cookies=cookies, headers=headers)

    top_dog_list = response.json()['success']['ranking']

    top_dog_ids = []
    for top_dog in top_dog_list:
        top_dog_ids.append(top_dog['user_id'])

    players = []
    for player_id in top_dog_ids:
        players.append(get_rival_players(player_id, EVENT_NUMBER, all_players))

    captains = []
    normal_players = []

    for top_dog in players:
        for selected_player in top_dog:
            if selected_player['captain']:
                captains.append(selected_player['firstname'] + " " + selected_player['lastname'])
            else:
                normal_players.append(selected_player['firstname'] + " " + selected_player['lastname'])

    res_captains = {}
    res_normal = {}

    for i in captains:
        res_captains[i] = captains.count(i)

    for i in normal_players:
        res_normal[i] = normal_players.count(i)

    sorted_res_normal = sorted(res_normal.items(), key=lambda x: x[1], reverse=True)
    sorted_res_captains = sorted(res_captains.items(), key=lambda x: x[1], reverse=True)

    return {'players': sorted_res_normal,
            'captains': sorted_res_captains}


def get_my_selected_players(db, tournament_no):
    cookies = {
        '_fbp': 'fb.1.1666766218235.340612310',
        'gig_canary': 'false',
        'gig_canary_ver': '13584-3-27904020',
        '_ga': 'GA1.1.770277567.1674242758',
        'gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q': '_gigya_ver4',
        'G_ENABLED_IDPS': 'google',
        'glt_4_LtiNVJuKIvw_FXO5qOsf6Q': 'st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3',
        'X-SID': '126aff190843cb1967d21fc9_1674242777',
        '_ga_EEZ9D5CWFT': 'GS1.1.1674242757.1.1.1674243013.0.0.0',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_fbp=fb.1.1666766218235.340612310; gig_canary=false; gig_canary_ver=13584-3-27904020; _ga=GA1.1.770277567.1674242758; gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q=_gigya_ver4; G_ENABLED_IDPS=google; glt_4_LtiNVJuKIvw_FXO5qOsf6Q=st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3; X-SID=126aff190843cb1967d21fc9_1674242777; _ga_EEZ9D5CWFT=GS1.1.1674242757.1.1.1674243013.0.0.0',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://fantasy.dpworldtour.com/api/fantasy_team/show_my/{tournament_no}',
                            cookies=cookies,
                            headers=headers)
    contents = response.json()

    my_players = contents['success']['team']['lineup']

    my_players = process_custom_data(db, my_players, tournament_no, contents['success']['team']['captain'])

    # my_lineup = []
    #
    # for player_loop in my_players:
    #     my_lineup.append(db[player_loop])
    #
    # leaderboard = get_event_stats()
    # projected_cut = leaderboard['Players'][leaderboard['CutValue'] - 1]['ScoreToPar']
    #
    #
    #
    # event_stats = {}
    #
    # counter = 0
    # for sel_player in my_lineup:
    #     data = {'firstname': sel_player['firstname'],
    #             'lastname': sel_player['lastname'],
    #             'albatross': check_none(sel_player['event_stats']['albatross']),
    #             'eagles': check_none(sel_player['event_stats']['eagles']),
    #             'birdies': check_none(sel_player['event_stats']['birdies']),
    #             'pars': check_none(sel_player['event_stats']['pars']),
    #             'bogeys': check_none(sel_player['event_stats']['bogeys']),
    #             'double_bogeys': check_none(sel_player['event_stats']['double_bogeys']),
    #             'triple_bogeys_or_worse': check_none(sel_player['event_stats']['triple_bogeys_or_worse']),
    #             'score': sel_player['event_stats']['score'],
    #             'above_cut_off': sel_player['above_cut_off'],
    #             }
    #
    #     likelyhood_to_make_cut = projected_cut - data['score']
    #
    #
    #     possible_scores = ['albatross',
    #                        'eagles',
    #                        'birdies',
    #                        'pars',
    #                        'bogeys',
    #                        'double_bogeys',
    #                        'triple_bogeys_or_worse']
    #
    #     total_holes_played = 0
    #     for x in possible_scores:
    #         total_holes_played += data[x]
    #
    #
    #
    #     chance_albatross = data['albatross'] / total_holes_played
    #     chance_eagles = data['eagles'] / total_holes_played
    #     chance_birdie = data['birdies'] / total_holes_played
    #     chance_pars = data['pars'] / total_holes_played
    #     chance_bogeys = data['bogeys'] / total_holes_played
    #     chance_double_bogeys = data['double_bogeys'] / total_holes_played
    #     chance_triple_bogeys_or_worse = data['triple_bogeys_or_worse'] / total_holes_played
    #
    #     finishing_hole_today = 0
    #     if total_holes_played < 18:
    #         finishing_hole_today = 18
    #     elif total_holes_played >= 18 and total_holes_played < 36:
    #         finishing_hole_today = 36
    #     elif total_holes_played >= 36 and total_holes_played < 54:
    #         finishing_hole_today = 54
    #     else:
    #         finishing_hole_today = 72
    #
    #     remaining_holes_to_be_played = finishing_hole_today - total_holes_played
    #
    #     data['total_holes_player'] = total_holes_played
    #     data['remaining_holes_today'] = remaining_holes_to_be_played
    #     data['albatross_chance'] = chance_albatross
    #     data['eagles_chance'] = chance_eagles
    #     data['birdies_chance'] = chance_birdie
    #     data['pars_chance'] = chance_pars
    #     data['bogeys_chance'] = chance_bogeys
    #     data['double_bogeys_chance'] = chance_double_bogeys
    #     data['triple_bogeys_or_worse_chance'] = chance_triple_bogeys_or_worse
    #     data['score_off_cut'] = likelyhood_to_make_cut
    #     if likelyhood_to_make_cut < 0:
    #         data['below_projected_cut'] = True
    #     else:
    #         data['below_projected_cut'] = False
    #
    #     event_stats[counter] = data
    #     counter += 1

    return my_players


def get_rival_players(player_id, tournament_no, db):
    # MARTIJNS REQUEST:
    # cookies = {
    #     '_fbp': 'fb.1.1657208105279.1235282127',
    #     'X-SID': '8d1bd0c6ca12752bbba8025b_1657208265',
    # }
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Accept-Language': 'nl,en-US;q=0.7,en;q=0.3',
    #     'Connection': 'keep-alive',
    #     'Referer': f'https://fantasy.dpworldtour.com/team/{player_id}/{tournament_no}',
    #     # Requests sorts cookies= alphabetically
    #     # 'Cookie': '_fbp=fb.1.1657208105279.1235282127; X-SID=8d1bd0c6ca12752bbba8025b_1657208265',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     # Requests doesn't support trailers
    #     # 'TE': 'trailers',
    # }

    cookies = {
        '_fbp': 'fb.1.1666766218235.340612310',
        'gig_canary': 'false',
        'gig_canary_ver': '13584-3-27904020',
        '_ga': 'GA1.1.770277567.1674242758',
        'gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q': '_gigya_ver4',
        'G_ENABLED_IDPS': 'google',
        'glt_4_LtiNVJuKIvw_FXO5qOsf6Q': 'st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3',
        'X-SID': '126aff190843cb1967d21fc9_1674242777',
        '_ga_EEZ9D5CWFT': 'GS1.1.1674242757.1.1.1674243220.0.0.0',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': '_fbp=fb.1.1666766218235.340612310; gig_canary=false; gig_canary_ver=13584-3-27904020; _ga=GA1.1.770277567.1674242758; gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q=_gigya_ver4; G_ENABLED_IDPS=google; glt_4_LtiNVJuKIvw_FXO5qOsf6Q=st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3; X-SID=126aff190843cb1967d21fc9_1674242777; _ga_EEZ9D5CWFT=GS1.1.1674242757.1.1.1674243220.0.0.0',
        'referer': f'https://fantasy.dpworldtour.com/team/{player_id}/{tournament_no}',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://fantasy.dpworldtour.com/api/fantasy_team/show_rival_team/{player_id}/{tournament_no}',
        cookies=cookies, headers=headers)

    contents = response.json()
    my_players = contents['success']['team']['lineup']
    my_players = process_custom_data(db, my_players, tournament_no, contents['success']['team']['captain'])
    # my_lineup = []
    #
    # for player_loop in my_players:
    #     my_lineup.append(db[player_loop])

    return my_players


def get_event_stats(tournament_no):
    import requests

    cookies = {
        '_gcl_au': '1.1.1986663528.1652340349',
        '_fbp': 'fb.1.1652340348943.1499916189',
        'gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q': '_gigya_ver4',
        'G_ENABLED_IDPS': 'google',
        'glt_4_LtiNVJuKIvw_FXO5qOsf6Q': 'st2.s.AcbHtTh3Cw.C69Jaaw03-wlF8Qcd3Ck_O0Uodq2k3lY26vfpj99yorQMueXLBooe7232_Es_zsVkjsXpnFcTrSqYsTIFr05ruQPD1hVsKtUe-TRUwZ8qC4.6caWaaBO-E63FUVQSQ3vu_Xc5mDK_N7Ki3G-vaKsIc0cXbANrTWDyMBFvRpXR4r4y28pLYWg49PFYUmqZ_W9Cw.sc3',
        '_hjSessionUser_1411640': 'eyJpZCI6IjFiMTVjY2I1LTE2YzYtNTZmMC04OGUyLTMwMGQ1MTdkZGM0YyIsImNyZWF0ZWQiOjE2NTIzNDAzNDk5MTQsImV4aXN0aW5nIjp0cnVlfQ==',
        '__gads': 'ID=7424b346cdb4222d:T=1652340372:S=ALNI_MbLrsqHMHWbWBeRUBSFzvSkZh3kcg',
        '__lxG__consent__v2': '1%7C1%7C1652340349849%7C149%7C1658305832718%7C2%7C1%7C1%7C1656577832718%7C1',
        '__lxG__consent__v2_daisybit': 'CPY3yDiPbZbeXA_ADAENCVCsAP_AAH_AAAAAI3Nd_X__bX9j-_5_aft0eY1P9_r37uQzDhfFs-8F3L_W_LwXw2E7NF36pq4KmR4Eu3LBIQNlHMHUTUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGH9Pn9lDuYKY7_5___bx2D-t_t_-39T378Xf3_d5_2_--vCfV599jfn9fV_789DP___9v-_8__________3wRrAJMNW4gC7MscGTQMIoUQIwrCQqgUAEFAMLRFYAODgp2VgEuoIWACAVIRgRAgxBRgwCAAQSAJCIgJACwQCIAiAQAAgARAIQAETAILACwMAgAFANCxACgAECQgyICI5TAgKgSiglsrEEoK9jTCAOs8AKBRGRUACJJAQSAgJCwcRwBICXiyQNMUL5ACMEKAUAAAAA.YAAAAAAAAAAA',
        '__lxG__consent__v2_gdaisybit': '~1~39.43969.13.64.15.9527417132.10.39.21.4697.12.92.18.76.14.5.20.65131.11..29.4.14.453.10.629664544.29.4531622.17.1.17..10.91862834.142.4.50..15.1.17.18.10..25..10..25.5.18.97.41.24.18..24.4216652.14..18.73228.28.863.10.4.20.2.13.464.11.13.22..16.26824.11.6.38..11.81.10..28..12.1.24.27619.30..17.49.15.873.12.9417.12..13..22..13.2.12.2.10.5.15.2494547.13.5.15.4.13.4.14.82.15.25512212.14.74829.10..18..12..13.2.18.113119.25.41.19.84535484222.14.2.13.426963435236.10..11.63.19..11.31239.19..11..15.3.10..13.434633331116.11.311.11.61.10.52632243227.15.7.12.2133454322413111291691521728.11.1311213261.12.813112277141261211311411218174321353961.15..10..28.122.12.3416347131131531322114212122242122241112211112111221121217122121111211321181115216511111223114112211431412123112411151363152341231421222111111.11.131122523351116112519411317145172111211142.13.113122312111213111124151243822972321461711',
        '_pbjs_userid_consent_data': '902362917952702',
        '_gid': 'GA1.2.305484059.1657116419',
        '_ga_2Z1KRCE5HY': 'GS1.1.1657277426.33.1.1657277431.0',
        'gig_canary': 'true',
        'gig_canary_ver': '13232-3-27621240',
        '_ga': 'GA1.2.1654423165.1652340349',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_1411640': 'eyJpZCI6ImRiMDY2YjQwLWQwNDItNGZkYy1iMmI0LWZlNzk4ZDgzZDQ1MCIsImNyZWF0ZWQiOjE2NTcyNzc0NDEwNzksImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '1',
        '_gat_UA-132881508-1': '1',
        '_awl': '2.1657277440.0.5-be12643fc6514aa69a43cde2be8c90bc-6763652d6575726f70652d7765737431-0',
        'cto_bundle': 'yQEc6l9pU3BsRU51RmplMUY5QXp1NTJKWTRCQ0Q2RXR4NlNJUkRYZkRVUCUyRlE0ZGpOQmNMUzI4SE9LU2hTSE0lMkJjb1JUTjhZcmUlMkYlMkJJd3FzT0htc0JaMGd2cWJxM2VYT1V6elJZcENvMVlOYldSamtkUUh0dlduUU50VzFSJTJGT3djMiUyQnZGS1pmb2k0MTQ0YmoxMWJtemx4N0RqY05Jem0lMkI4VXJLY2Z0VGtkT2VrOGF5UEthOTJia0RnampOcURHZk12dlg5NGpKNWs4ejRaemJ5YmlPWTFjbzV3bEElM0QlM0Q',
    }

    headers = {
        'authority': 'www.europeantour.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=utf-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1986663528.1652340349; _fbp=fb.1.1652340348943.1499916189; gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q=_gigya_ver4; G_ENABLED_IDPS=google; glt_4_LtiNVJuKIvw_FXO5qOsf6Q=st2.s.AcbHtTh3Cw.C69Jaaw03-wlF8Qcd3Ck_O0Uodq2k3lY26vfpj99yorQMueXLBooe7232_Es_zsVkjsXpnFcTrSqYsTIFr05ruQPD1hVsKtUe-TRUwZ8qC4.6caWaaBO-E63FUVQSQ3vu_Xc5mDK_N7Ki3G-vaKsIc0cXbANrTWDyMBFvRpXR4r4y28pLYWg49PFYUmqZ_W9Cw.sc3; _hjSessionUser_1411640=eyJpZCI6IjFiMTVjY2I1LTE2YzYtNTZmMC04OGUyLTMwMGQ1MTdkZGM0YyIsImNyZWF0ZWQiOjE2NTIzNDAzNDk5MTQsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=7424b346cdb4222d:T=1652340372:S=ALNI_MbLrsqHMHWbWBeRUBSFzvSkZh3kcg; __lxG__consent__v2=1%7C1%7C1652340349849%7C149%7C1658305832718%7C2%7C1%7C1%7C1656577832718%7C1; __lxG__consent__v2_daisybit=CPY3yDiPbZbeXA_ADAENCVCsAP_AAH_AAAAAI3Nd_X__bX9j-_5_aft0eY1P9_r37uQzDhfFs-8F3L_W_LwXw2E7NF36pq4KmR4Eu3LBIQNlHMHUTUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGH9Pn9lDuYKY7_5___bx2D-t_t_-39T378Xf3_d5_2_--vCfV599jfn9fV_789DP___9v-_8__________3wRrAJMNW4gC7MscGTQMIoUQIwrCQqgUAEFAMLRFYAODgp2VgEuoIWACAVIRgRAgxBRgwCAAQSAJCIgJACwQCIAiAQAAgARAIQAETAILACwMAgAFANCxACgAECQgyICI5TAgKgSiglsrEEoK9jTCAOs8AKBRGRUACJJAQSAgJCwcRwBICXiyQNMUL5ACMEKAUAAAAA.YAAAAAAAAAAA; __lxG__consent__v2_gdaisybit=~1~39.43969.13.64.15.9527417132.10.39.21.4697.12.92.18.76.14.5.20.65131.11..29.4.14.453.10.629664544.29.4531622.17.1.17..10.91862834.142.4.50..15.1.17.18.10..25..10..25.5.18.97.41.24.18..24.4216652.14..18.73228.28.863.10.4.20.2.13.464.11.13.22..16.26824.11.6.38..11.81.10..28..12.1.24.27619.30..17.49.15.873.12.9417.12..13..22..13.2.12.2.10.5.15.2494547.13.5.15.4.13.4.14.82.15.25512212.14.74829.10..18..12..13.2.18.113119.25.41.19.84535484222.14.2.13.426963435236.10..11.63.19..11.31239.19..11..15.3.10..13.434633331116.11.311.11.61.10.52632243227.15.7.12.2133454322413111291691521728.11.1311213261.12.813112277141261211311411218174321353961.15..10..28.122.12.3416347131131531322114212122242122241112211112111221121217122121111211321181115216511111223114112211431412123112411151363152341231421222111111.11.131122523351116112519411317145172111211142.13.113122312111213111124151243822972321461711; _pbjs_userid_consent_data=902362917952702; _gid=GA1.2.305484059.1657116419; _ga_2Z1KRCE5HY=GS1.1.1657277426.33.1.1657277431.0; gig_canary=true; gig_canary_ver=13232-3-27621240; _ga=GA1.2.1654423165.1652340349; _hjIncludedInSessionSample=0; _hjSession_1411640=eyJpZCI6ImRiMDY2YjQwLWQwNDItNGZkYy1iMmI0LWZlNzk4ZDgzZDQ1MCIsImNyZWF0ZWQiOjE2NTcyNzc0NDEwNzksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gat_UA-132881508-1=1; _awl=2.1657277440.0.5-be12643fc6514aa69a43cde2be8c90bc-6763652d6575726f70652d7765737431-0; cto_bundle=yQEc6l9pU3BsRU51RmplMUY5QXp1NTJKWTRCQ0Q2RXR4NlNJUkRYZkRVUCUyRlE0ZGpOQmNMUzI4SE9LU2hTSE0lMkJjb1JUTjhZcmUlMkYlMkJJd3FzT0htc0JaMGd2cWJxM2VYT1V6elJZcENvMVlOYldSamtkUUh0dlduUU50VzFSJTJGT3djMiUyQnZGS1pmb2k0MTQ0YmoxMWJtemx4N0RqY05Jem0lMkI4VXJLY2Z0VGtkT2VrOGF5UEthOTJia0RnampOcURHZk12dlg5NGpKNWs4ejRaemJ5YmlPWTFjbzV3bEElM0QlM0Q',
        'if-none-match': '"caPk3zESLkTvzIBJguOl-7gOv6hOuoChnpkp03JfTVX1D-c1hBjCokcVJxqGs0fT7mJ1rvVBBayjS4hK8gx1XA"',
        'pragma': 'no-cache',
        'referer': 'https://www.europeantour.com/dpworld-tour/genesis-scottish-open-2022/leaderboard?round=1',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://www.europeantour.com/api/sportdata/Leaderboard/Strokeplay/{tournament_no}',
                            cookies=cookies, headers=headers)

    return response.json()
