import calls


def check_none(element):
    return 0 if element is None else element


def process_custom_data(db, my_players, tournament_no, captain):
    my_lineup = []

    for player_loop in my_players:
        my_lineup.append(db[player_loop])

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
                'scorecard': calls.get_player_scorecard(tournament_no, sel_player['id'])
                }

        possible_scores = ['albatross',
                           'eagles',
                           'birdies',
                           'pars',
                           'bogeys',
                           'double_bogeys',
                           'triple_bogeys_or_worse']

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

        finishing_hole_today = 0
        if total_holes_played < 18:
            finishing_hole_today = 18
        elif total_holes_played >= 18 and total_holes_played < 36:
            finishing_hole_today = 36
        elif total_holes_played >= 36 and total_holes_played < 54:
            finishing_hole_today = 54
        else:
            finishing_hole_today = 72

        remaining_holes_to_be_played = finishing_hole_today - total_holes_played

        data['total_holes_player'] = total_holes_played
        data['remaining_holes_today'] = remaining_holes_to_be_played
        data['on_hole'] = on_hole

        event_stats.append(data)
        counter += 1
    return event_stats
