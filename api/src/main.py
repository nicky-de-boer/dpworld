import pandas
from .util import get_all_players, get_my_selected_players, get_rival_players, get_top_dogs
import json
import sqlite3

# UP Event number accordingly by one
EVENT_NUMBER = 2023108
DAVID = 48269
MARTIJN = 43042
JOHAN = 48912
JOP = 50347


def connect_to_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    sqlite_insert_query = """INSERT or REPLACE INTO nicky
                              (date, score) 
                               VALUES 
                              ('2022-10-16',21158)"""
    # cursor.execute("SELECT * FROM nicky")
    #
    # count = cursor.execute(sqlite_insert_query)
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print(cursor.fetchall())
    return conn


def create_db_table():
    conn = connect_to_db()
    try:
        conn.execute('''
            CREATE TABLE nicky (
                date DATE PRIMARY KEY NOT NULL,
                score INTEGER NOT NULL
            );
        ''')
        conn.commit()
    except:
        print("user table creation failed")
    finally:
        conn.close()


def get_scores():
    return {'16-10-2022': {'Birdy-D': 20764, 'Nickydb12': 21158, 'mvandoor': 21660, 'JopWiel': 19079},
            '23-10-2022': {'Birdy-D': 21719, 'Nickydb12': 22244, 'mvandoor': 22543, 'JopWiel': 19668},
            '9-11-2022': {'Birdy-D': 22765, 'Nickydb12': 23102, 'mvandoor': 23275, 'JopWiel': 20287},
            '14-11-2022': {'Birdy-D': 23614, 'Nickydb12': 23953, 'mvandoor': 24209, 'JopWiel': 21329},
            '19-01-2023': {'Birdy-D': 0, 'Nickydb': 0, 'martijnvandooren': 0, 'Jopwiel': 0, 'Johan': 0},
            '26-01-2023': {'Birdy-D': 1016, 'Nickydb': 853, 'martijnvandooren': 861, 'Jopwiel': 1103, 'Johan': 1044}
            }

    # create_db_table()
    #
    # conn = sqlite3.connect('database.db')
    # cursor = conn.cursor()
    #
    # sqlite_insert_query = """INSERT or REPLACE INTO nicky
    #                               (date, score)
    #                                VALUES
    #                               ('2022-10-16',21158)"""
    # cursor.execute("SELECT * FROM nicky")
    #
    # count = cursor.execute(sqlite_insert_query)
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print(cursor.fetchall())
    #
    # # # def connect_to_db():
    # # conn = sqlite3.connect('database.db')
    # # cursor = conn.cursor()
    # # #
    # # # sqlite_insert_query = """INSERT or REPLACE INTO martijn
    # # #                           (date, score)
    # # #                            VALUES
    # # #                           ('2022-10-16',21660)"""
    # # cursor.execute("SELECT date, score FROM david")
    # # rows = cursor.fetchall()
    # # count = cursor.execute(sqlite_insert_query)
    # # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # # print(cursor.fetchall())
    # # return conn
    # conn = sqlite3.connect('database.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT date, score FROM david")
    # scores = {'david': cursor.fetchall()[0][1]}
    # cursor.execute("SELECT date, score FROM martijn")
    # scores = {'martijn': cursor.fetchall()[0][1]}
    # cursor.execute("SELECT date, score FROM nicky")
    # scores = {'nicky': cursor.fetchall()[0][1]}
    # return scores


def get_name():
    import requests

    cookies = {
        '_fbp': 'fb.1.1665564095779.861512526',
        'X-SID': '54e47c5724ec3408d26d4cec_1665564119',
    }

    headers = {
        'authority': 'fantasy.dpworldtour.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_fbp=fb.1.1665564095779.861512526; X-SID=54e47c5724ec3408d26d4cec_1665564119',
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

    # name = ''
    # #
    # df = pandas.DataFrame(response.json())
    # # df["dateStart"] = pandas.to_datetime(df["dateStart"][0], errors='coerce').dt.date

    # event_info = response.json()

    # for event in event_info:
    #     pandas.to_datetime(event['dateStart']).date






    # df = df[df.status != "cancelled"]
    # df = df[df.status != "complete"]

    # import datetime
    # #
    # # def change_date(x):
    # #     clean = x.split("T", 1)[0]
    # #     return datetime.datetime.strptime(clean, '%Y-%m-%d')
    # #
    # # print('before')
    # # df['dateStart'] = df['dateStart'].apply(change_date)
    # print('after')
    # #
    # # for column in df['dateStart']:
    # #     clean = column.split("T", 1)[0]
    # #     test = datetime.datetime.strptime(clean, '%Y-%m-%d')
    # #     df.at[column, 'ifor'] = test
    # #     print(column)
    # #
    # df = df.set_index('dateStart')
    # dt = '2022-10-22'

    # import pytz

    # utc = pytz.UTC

    # ok = df.index.get_indexer(utc.localize(datetime.datetime.now()), method='nearest')
    # ok2 = df.index[ok]
    # #
    # tournament_info = df.loc[[ok2]]
    # tournament_id = int(tournament_info['id'][0])

    # # tournament_id = tournament_info['id']
    # # cool = df.index.get_loc(dt, method='nearest')


    for item in response.json():
        if EVENT_NUMBER == item['id']:
            name = item['name']
            # print(item)
    return {'name': name}


def get_standings():
    import requests

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
        # 'cookie': '_fbp=fb.1.1666766218235.340612310; gig_canary=false; gig_canary_ver=13584-3-27904020; _ga=GA1.1.770277567.1674242758; gig_bootstrap_4_LtiNVJuKIvw_FXO5qOsf6Q=_gigya_ver4; G_ENABLED_IDPS=google; glt_4_LtiNVJuKIvw_FXO5qOsf6Q=st2.s.AcbHutnxfg.PuhTEq2R0_w7Ij8ZriJh1Nbl-FkcpVl2OoyXdogUwvvYC7lQ7zvRI_OoPLAQ3bo4NDEihq8chqe_H9xipcr3HZPpEEZLpJVEEKoJjsiuoN0.xvsOxt1gjEKUs35zttrT7FRyvEdvtG-b6Ykxrj7kI5ZQV4xM_gmUQZqDWnHdiwEKSAK1Rpmrwqkc4VFoG2Zm0A.sc3; X-SID=126aff190843cb1967d21fc9_1674242777; _ga_EEZ9D5CWFT=GS1.1.1674242757.1.1.1674243316.0.0.0',
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


def handle_player_request(player):
    all_players = get_all_players(EVENT_NUMBER)
    my_players = get_my_selected_players(all_players, EVENT_NUMBER)
    martijns_players = get_rival_players(MARTIJN, EVENT_NUMBER, all_players)
    davids_players = get_rival_players(DAVID, EVENT_NUMBER, all_players)
    johan_players = get_rival_players(JOHAN, EVENT_NUMBER, all_players)
    jop_players = get_rival_players(JOP, EVENT_NUMBER, all_players)


    if player == "Nicky":
        df_my_players = pandas.DataFrame(my_players)
        df_my_players.sort_values(by=['score'], ascending=True, inplace=True)
        jsonfiles = json.loads(df_my_players.to_json(orient='records'))
        return [jsonfiles]
    if player == "David":
        df_david_players = pandas.DataFrame(davids_players)
        # df_david_players.sort_values(by=['score'], ascending=True, inplace=True)
        jsonfiles = json.loads(df_david_players.to_json(orient='records'))
        return [jsonfiles]
    if player == "Martijn":
        df_martijn_players = pandas.DataFrame(martijns_players)
        # df_martijn_players.sort_values(by=['score'], ascending=True, inplace=True)
        jsonfiles = json.loads(df_martijn_players.to_json(orient='records'))
        return [jsonfiles]
    if player == "All":
        df_martijn_players = pandas.DataFrame(martijns_players)
        df_david_players = pandas.DataFrame(davids_players)
        df_my_players = pandas.DataFrame(my_players)

        df_martijn_players.sort_values(by=['score'], ascending=True, inplace=True)
        df_david_players.sort_values(by=['score'], ascending=True, inplace=True)
        df_my_players.sort_values(by=['score'], ascending=True, inplace=True)

        jsonfile_martijn = json.loads(df_martijn_players.to_json(orient='records'))
        jsonfile_david = json.loads(df_david_players.to_json(orient='records'))
        jsonfile_my = json.loads(df_my_players.to_json(orient='records'))

        return [jsonfile_martijn, jsonfile_david, jsonfile_my]

    if player == "Matchups":

        standings = get_standings()

        start_score = get_scores()['26-01-2023']


        # Name
        # Points
        # Difference
        standings_overview = []
        idx = 0
        for entry in standings['success']['ranking']:

            if len(standings_overview) == 0:
                standings_overview.append({'Name': entry['team_name'],
                                           'StartPoints': start_score[entry['team_name']],
                                           'Points': entry['points'] - start_score[entry['team_name']],
                                           'Movement': 0,
                                           'Difference': 0,
                                           'TotalPoints': start_score[entry['team_name']] + (entry['points'] - start_score[entry['team_name']])
                                           })
            else:
                switcher = 'nicky'
                curr_diff = standings_overview[idx - 1]['StartPoints'] + standings_overview[idx - 1]['Points'] - entry['points']
                start_diff = standings_overview[idx - 1]['StartPoints'] - start_score[entry['team_name']]

                movement = start_diff - curr_diff

                standings_overview.append({'Name': entry['team_name'],
                                           'StartPoints': start_score[entry['team_name']],
                                           'Points': entry['points']- start_score[entry['team_name']],
                                           'Movement': movement,
                                           'Difference': curr_diff,
                                           'TotalPoints': start_score[entry['team_name']] + (entry['points'] - start_score[entry['team_name']])
                                           })
            idx += 1

        standings_overview[0]['Movement'] = standings_overview[1]['Movement'] * -1

        for item in standings_overview:
            item['StartPoints'] = "{:,}".format(item['StartPoints']).replace(",", ".")
            item['Points'] = "{:,}".format(item['Points']).replace(",", ".")
            item['Movement'] = "{:,}".format(item['Movement']).replace(",", ".")
            item['Difference'] = "{:,}".format(item['Difference']).replace(",", ".")
            item['TotalPoints'] = "{:,}".format(item['TotalPoints']).replace(",", ".")

        cleaned = []
        captains = []

        # MARTIJN
        for item in martijns_players:
            name = item['firstname'] + " " + item['lastname'].lower().capitalize()

            score_today = "-"
            round_no = 0
            total_holes_played = item['total_holes_player']
            if total_holes_played > 0 and total_holes_played < 18:
                round_no = 1
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 18 and total_holes_played < 36:
                round_no = 2
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 36 and total_holes_played < 54:
                round_no = 3
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 54 and total_holes_played < 72:
                round_no = 4
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            return_dct = {'name': name,
                          'position': item['position'],
                          'true_pos': item['true_pos'],
                          'score': 0 if item['score'] is None else item['score'],
                          'scoretoday': score_today,
                          'holestoplay': item['remaining_holes_today'],
                          'onhole': item['on_hole'],
                          'Martijn': "X"}
            if item['captain']:
                if return_dct['name'] in [x['name'] for x in captains]:
                    for entry in captains:
                        if entry['name'] == name:
                            entry['Martijn'] = "X"
                else:
                    captains.append(return_dct)

            else:
                if return_dct['name'] in [x['name'] for x in cleaned]:
                    for entry in cleaned:
                        if entry['name'] == name:
                            entry['Martijn'] = "X"
                else:
                    cleaned.append(return_dct)

        # JOHAN
        for item in johan_players:
            name = item['firstname'] + " " + item['lastname'].lower().capitalize()

            score_today = "-"
            round_no = 0
            total_holes_played = item['total_holes_player']
            if total_holes_played > 0 and total_holes_played < 18:
                round_no = 1
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 18 and total_holes_played < 36:
                round_no = 2
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 36 and total_holes_played < 54:
                round_no = 3
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 54 and total_holes_played < 72:
                round_no = 4
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            return_dct = {'name': name,
                          'position': item['position'],
                          'true_pos': item['true_pos'],
                          'score': 0 if item['score'] is None else item['score'],
                          'scoretoday': score_today,
                          'holestoplay': item['remaining_holes_today'],
                          'onhole': item['on_hole'],
                          'Johan': "X"}
            if item['captain']:
                if return_dct['name'] in [x['name'] for x in captains]:
                    for entry in captains:
                        if entry['name'] == name:
                            entry['Johan'] = "X"
                else:
                    captains.append(return_dct)

            else:
                if return_dct['name'] in [x['name'] for x in cleaned]:
                    for entry in cleaned:
                        if entry['name'] == name:
                            entry['Johan'] = "X"
                else:
                    cleaned.append(return_dct)

        # JOP
        for item in jop_players:
            name = item['firstname'] + " " + item['lastname'].lower().capitalize()

            score_today = "-"
            round_no = 0
            total_holes_played = item['total_holes_player']
            if total_holes_played > 0 and total_holes_played < 18:
                round_no = 1
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 18 and total_holes_played < 36:
                round_no = 2
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 36 and total_holes_played < 54:
                round_no = 3
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 54 and total_holes_played < 72:
                round_no = 4
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            return_dct = {'name': name,
                          'position': item['position'],
                          'true_pos': item['true_pos'],
                          'score': 0 if item['score'] is None else item['score'],
                          'scoretoday': score_today,
                          'holestoplay': item['remaining_holes_today'],
                          'onhole': item['on_hole'],
                          'Jop': "X"}
            if item['captain']:
                if return_dct['name'] in [x['name'] for x in captains]:
                    for entry in captains:
                        if entry['name'] == name:
                            entry['Jop'] = "X"
                else:
                    captains.append(return_dct)

            else:
                if return_dct['name'] in [x['name'] for x in cleaned]:
                    for entry in cleaned:
                        if entry['name'] == name:
                            entry['Jop'] = "X"
                else:
                    cleaned.append(return_dct)

        # NICKY
        for item in my_players:
            name = item['firstname'] + " " + item['lastname'].lower().capitalize()
            score_today = "-"
            round_no = 0
            total_holes_played = item['total_holes_player']
            if total_holes_played > 0 and total_holes_played < 18:
                round_no = 1
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 18 and total_holes_played < 36:
                round_no = 2
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 36 and total_holes_played < 54:
                round_no = 3
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 54 and total_holes_played < 72:
                round_no = 4
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            return_dct = {'name': name,
                          'position': item['position'],
                          'true_pos': item['true_pos'],
                          'score': 0 if item['score'] is None else item['score'],
                          'scoretoday': score_today,
                          'holestoplay': item['remaining_holes_today'],
                          'onhole': item['on_hole'],
                          'Nicky': "X"}
            if item['captain']:
                if return_dct['name'] in [x['name'] for x in captains]:
                    for entry in captains:
                        if entry['name'] == name:
                            entry['Nicky'] = "X"
                else:
                    captains.append(return_dct)

            else:
                if return_dct['name'] in [x['name'] for x in cleaned]:
                    for entry in cleaned:
                        if entry['name'] == name:
                            entry['Nicky'] = "X"
                else:
                    cleaned.append(return_dct)

        # DAVID
        for item in davids_players:
            name = item['firstname'] + " " + item['lastname'].lower().capitalize()

            score_today = "-"
            round_no = 0
            total_holes_played = item['total_holes_player']
            if total_holes_played > 0 and total_holes_played < 18:
                round_no = 1
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 18 and total_holes_played < 36:
                round_no = 2
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 36 and total_holes_played < 54:
                round_no = 3
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            elif total_holes_played > 54 and total_holes_played < 72:
                round_no = 4
                score_today = item['scorecard']['Rounds'][round_no - 1]['ScoreToPar']
            return_dct = {'name': name,
                          'position': item['position'],
                          'true_pos': item['true_pos'],
                          'score': 0 if item['score'] is None else item['score'],
                          'scoretoday': score_today,
                          'holestoplay': item['remaining_holes_today'],
                          'onhole': item['on_hole'],
                          'David': "X"}
            if item['captain']:
                if return_dct['name'] in [x['name'] for x in captains]:
                    for entry in captains:
                        if entry['name'] == name:
                            entry['David'] = "X"
                else:
                    captains.append(return_dct)

            else:
                if return_dct['name'] in [x['name'] for x in cleaned]:
                    for entry in cleaned:
                        if entry['name'] == name:
                            entry['David'] = "X"
                else:
                    cleaned.append(return_dct)

        captains = pandas.DataFrame(captains)
        players = pandas.DataFrame(cleaned)

        captains.sort_values(by=['true_pos'], ascending=True, inplace=True)
        players.sort_values(by=['true_pos'], ascending=True, inplace=True)
        standings_overview = pandas.DataFrame(standings_overview)

        standings_overview.style.format("{:,}")
        # standings_overview.options.display.float_format = '{:,.2f}'.format
        json_standings_overview = json.loads(standings_overview.to_json(orient='records'))

        # Set at PAR when 0
        captains['score'].replace(0, 'PAR', inplace=True)
        players['score'].replace(0, 'PAR', inplace=True)

        json_capt = json.loads(captains.to_json(orient='records'))
        json_players = json.loads(players.to_json(orient='records'))

        return [json_standings_overview, json_capt, json_players]

    else:
        return "Selected players is not present in analysis"


# Main function
if __name__ == '__main__':
    # All players attending this event
    all_players = get_all_players(EVENT_NUMBER)

    # My selected Players
    my_players = get_my_selected_players(all_players, EVENT_NUMBER)

    # Martijns selected players
    rival_players_m = get_rival_players(MARTIJN, EVENT_NUMBER, all_players)

    # Davids selected players
    rival_players_d = get_rival_players(DAVID, EVENT_NUMBER, all_players)

    # Top 100 players
    top_dogs = get_top_dogs('100', EVENT_NUMBER, all_players)

    # players_to_be_cut_my = 0
    # for player in my_players:
    #     if player['below_projected_cut']:
    #         players_to_be_cut_my += 1
    #
    # players_to_be_cut_martijn = 0
    # for player in rival_players_m:
    #     if player['below_projected_cut']:
    #         players_to_be_cut_martijn += 1
    #
    # players_to_be_cut_david = 0
    # for player in rival_players_d:
    #     if player['below_projected_cut']:
    #         players_to_be_cut_david += 1

    # Create DataFrames
    df_top_100_players = pandas.DataFrame(top_dogs['players'])
    df_top_100_captains = pandas.DataFrame(top_dogs['captains'])
    df_my_players = pandas.DataFrame(my_players)
    df_rival_players_m = pandas.DataFrame(rival_players_m)
    df_rival_players_d = pandas.DataFrame(rival_players_d)

    # Write to Excel
    writer = pandas.ExcelWriter('output.xlsx', engine="xlsxwriter")

    # df_my_players.sort_values(by=['score'], ascending=True, inplace=True)
    # df_rival_players_m.sort_values(by=['score'], ascending=True, inplace=True)
    # df_rival_players_d.sort_values(by=['score'], ascending=True, inplace=True)

    df_top_100_players.to_excel(writer, sheet_name='Top100Players', startrow=0, startcol=0)
    df_top_100_captains.to_excel(writer, sheet_name='Top100Captains', startrow=0, startcol=0)

    df_my_players.to_excel(writer, sheet_name='Players', startrow=2, startcol=0)
    worksheet = writer.sheets['Players']
    text1 = 'My players'
    worksheet.write(0, 0, text1)

    df_rival_players_m.to_excel(writer, sheet_name='Players', startrow=12, startcol=0)
    worksheet.write(10, 0, 'Martijns Players')

    df_rival_players_d.to_excel(writer, sheet_name='Players', startrow=22, startcol=0)
    worksheet.write(20, 0, 'Davids Players')

    writer.save()
    print('DataFrame is written successfully to Excel File.')
