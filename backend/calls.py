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
