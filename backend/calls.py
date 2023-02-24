import main
import requests
import util


def current_event_name():
    """
    Gets the Current event name as requested by the ID in main
    Returns
    -------

    """
    cookies = {
        '_fbp': 'fb.1.1665564095779.861512526',
        'X-SID': '54e47c5724ec3408d26d4cec_1665564119',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en;q=0.9',
        'referer': 'https://fantasy.dpworldtour.com/team',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    response = requests.get('https://fantasy.dpworldtour.com/json/events.json', cookies=cookies, headers=headers)
    for item in response.json():
        if main.EVENT_NUMBER == item['id']:
            name = item['name']
    return {'name': name}


def get_current_standings():
    """
    Get current standing of the Klopperij league
    Returns
    -------

    """
    cookies = {
        '_fbp': 'fb.1.1666766218235.340612310',
        'gig_canary': 'false',
        'gig_canary_ver': '13584-3-27904020',
        '_ga': 'GA1.1.770277567.1674242758',
        'gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q': '_gigya_ver4',
        'G_ENABLED_IDPS': 'google',
        'glt_4_LtiNVJuKIvw_FXO5qOsf6Q': 'st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3',
        'X-SID': '126aff190843cb1967d21fc9_1674242777',
        '_ga_EEZ9D5CWFT': 'GS1.1.1674242757.1.1.1674243316.0.0.0',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'referer': 'https://fantasy.dpworldtour.com/leagues/5528/table',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'page': '1',
        'limit': '20',
    }

    response = requests.get('https://fantasy.dpworldtour.com/api/fantasy/rankings/5528/rankings', params=params,
                            cookies=cookies, headers=headers)

    return response.json()

def get_my_selected_players(db, tournament_no):
    """
    Call to extract my own players
    Parameters
    ----------
    db
    tournament_no

    Returns
    -------

    """
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
    my_players = util.process_custom_data(db, my_players, tournament_no, contents['success']['team']['captain'])

    return my_players
def get_rival_players(player_id, tournament_no, db):
    """
    Get Players from other players but me by id
    Parameters
    ----------
    player_id
    tournament_no
    db

    Returns
    -------

    """
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
    players = contents['success']['team']['lineup']
    players = util.process_custom_data(db, players, tournament_no, contents['success']['team']['captain'])

    return players

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
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-Modified-Since': 'Thu, 07 Jul 2022 15:35:08 GMT',
        'If-None-Match': '"008113792b9168849dca4d8ecc2a4cfe"',
        'Cache-Control': 'max-age=0',
    }

    response = requests.get(f'https://fantasy.dpworldtour.com/json/players/{tournament_no}.json', cookies=cookies,
                            headers=headers)
    db = {}

    for item in response.json():
        db[item['id']] = item

    return db


def get_player_scorecard(tournament_no, player_id):
    """
    Get the scorecard of the requested player for the provided tournament
    Parameters
    ----------
    tournament_no
    player_id

    Returns
    -------

    """

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