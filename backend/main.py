import pandas
import calls
import json

# UP Event number accordingly by one
EVENT_NUMBER = 2023112
DAVID = 48269
MARTIJN = 43042
JOHAN = 48912
JOP = 50347


def get_scores():
    return {'16-10-2022': {'Birdy-D': 20764, 'Nickydb12': 21158, 'mvandoor': 21660, 'JopWiel': 19079},
            '23-10-2022': {'Birdy-D': 21719, 'Nickydb12': 22244, 'mvandoor': 22543, 'JopWiel': 19668},
            '9-11-2022': {'Birdy-D': 22765, 'Nickydb12': 23102, 'mvandoor': 23275, 'JopWiel': 20287},
            '14-11-2022': {'Birdy-D': 23614, 'Nickydb12': 23953, 'mvandoor': 24209, 'JopWiel': 21329},
            '19-01-2023': {'Birdy-D': 0, 'Nickydb': 0, 'martijnvandooren': 0, 'Jopwiel': 0, 'Johan': 0},
            '26-01-2023': {'Birdy-D': 1016, 'Nickydb': 853, 'martijnvandooren': 861, 'Jopwiel': 1103, 'Johan': 1044},
            '02-02-2023': {'Birdy-D': 1952, 'Nickydb': 1907, 'martijnvandooren': 1934, 'Jopwiel': 1978, 'Johan': 2074},
            '09-02-2023': {'Birdy-D': 2959, 'Nickydb': 2901, 'martijnvandooren': 2990, 'Jopwiel': 3006, 'Johan': 2942},
            '16-02-2023': {'Birdy-D': 3889, 'Nickydb': 3673, 'martijnvandooren': 3744, 'Jopwiel': 3805, 'Johan': 3684},
            '23-02-2023': {'Birdy-D': 4837, 'Nickydb': 4731, 'martijnvandooren': 5013, 'Jopwiel': 4851, 'Johan': 4813}
            }


def process_player(contender_name, selected_players, captains, cleaned):
    for item in selected_players:
        golfers_name = item['firstname'] + " " + item['lastname'].lower().capitalize()

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
        return_dct = {'name': golfers_name,
                      'position': item['position'],
                      'true_pos': item['true_pos'],
                      'score': 0 if item['score'] is None else item['score'],
                      'scoretoday': score_today,
                      'holestoplay': item['remaining_holes_today'],
                      'onhole': item['on_hole'],
                      contender_name: "X"}
        if item['captain']:
            if return_dct['name'] in [x['name'] for x in captains]:
                for entry in captains:
                    if entry['name'] == golfers_name:
                        entry[contender_name] = "X"
            else:
                captains.append(return_dct)

        else:
            if return_dct['name'] in [x['name'] for x in cleaned]:
                for entry in cleaned:
                    if entry['name'] == golfers_name:
                        entry[contender_name] = "X"
            else:
                cleaned.append(return_dct)


def handle_matchups():
    # Extract selected players for current event
    all_players = calls.get_all_players(EVENT_NUMBER)
    my_players = calls.get_my_selected_players(all_players, EVENT_NUMBER)
    martijns_players = calls.get_rival_players(MARTIJN, EVENT_NUMBER, all_players)
    davids_players = calls.get_rival_players(DAVID, EVENT_NUMBER, all_players)
    johan_players = calls.get_rival_players(JOHAN, EVENT_NUMBER, all_players)
    jop_players = calls.get_rival_players(JOP, EVENT_NUMBER, all_players)

    # Get current standing
    standings = calls.get_current_standings()

    start_score = get_scores()['23-02-2023']



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
                                       'TotalPoints': start_score[entry['team_name']] + (
                                               entry['points'] - start_score[entry['team_name']])
                                       })
        else:
            curr_diff = standings_overview[idx - 1]['StartPoints'] + standings_overview[idx - 1]['Points'] - entry[
                'points']
            start_diff = standings_overview[idx - 1]['StartPoints'] - start_score[entry['team_name']]

            movement = start_diff - curr_diff

            standings_overview.append({'Name': entry['team_name'],
                                       'StartPoints': start_score[entry['team_name']],
                                       'Points': entry['points'] - start_score[entry['team_name']],
                                       'Movement': movement,
                                       'Difference': curr_diff,
                                       'TotalPoints': start_score[entry['team_name']] + (
                                               entry['points'] - start_score[entry['team_name']])
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

    # Processing the data of selected players
    process_player("Martijn", martijns_players, captains, cleaned)
    process_player("Johan", johan_players, captains, cleaned)
    process_player("Jop", jop_players, captains, cleaned)
    process_player("Nicky", my_players, captains, cleaned)
    process_player("David", davids_players, captains, cleaned)

    # Clean up everything for front end processing
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
