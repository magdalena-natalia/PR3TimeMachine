import datetime
import lpJson as lp
import filesHandler as fh
import interactions
import lookups
from os import path
from spotifyPlaylist import SpotifyPlaylist


def main():
    """ Use data from the charts of the Polish Radio Program 3 to create a playlist on the user's Spotify page. """

    # Check if json with charts data exists. If not, create one.
    charts_path = 'lp.json'
    if not path.isfile(charts_path):
        lp.scrape_charts(charts_path)

    # Load charts data and find a chart on given date or on a proximate one
    charts = fh.read_json(charts_path)['chart']
    u_date = interactions.ask_for_date('Give the date to which you would like to travel (dd.mm.yyyy). ')
    dates = [datetime.datetime.strptime(chart['date'], '%d.%m.%Y') for chart in charts]
    chart = lookups.find_index_or_nearest(dates, u_date)
    not_chart_found_msg = 'There was not a chart on the given date.'
    chart = lookups.check_if_exact_result(result=chart,
                                          iterable=charts,
                                          iterable_key='date',
                                          message=not_chart_found_msg)
    # chart = int(chart)

    # Create a playlist with the chart data
    titles = chart['titles']

    artists = chart['artists']
    chart_date = chart['date']

    REDIRECT_URI = "http://example.com"
    scope = 'playlist-modify-public'
    cache_path = 'token.txt'
    playlist = SpotifyPlaylist(spotipy_client_id='SPOTIPY_CLIENT_ID',
                               spotipy_client_secret='SPOTIPY_CLIENT_SECRET',
                               redirect_uri=REDIRECT_URI,
                               scope=scope,
                               cache_path=cache_path,
                               titles=titles,
                               artists=artists,
                               date=chart_date)
    playlist.find_tracks_uris()
    playlist.save(title='Lista przebojów Trójki')


if __name__ == '__main__':
    main()
