<h1>PR3TimeMachine</h1>
The Polish Radio Program 3 used to shape music taste of Polish listeners. Founded in 1982 and hosted by Marek Niedzwiecki,the Charts included songs that weren'taired by any other radio station in Poland. 

This app is meant to be a time machine for all listeners of Polish Radio Program 3, allowing them to listen to the chosen chart songs once again, on Spotify.

<h1>Main functionalities</h1>
<ul>
<li>crawling through a website with the charts of Polish Radio Program 3 and scraping the data of all of them</li>
<li>writing web scraped data to json file</li>
<li>reading json file and find the chart on the date chosen by an user</li>
<li>offering user a choice between the nearest dates if the exact data not found but in the time frame of the charts airing</li>
<li>finding Spotify uri-s of all the songs, using multiple queries options to guarantee the best search results</li>
<li>creating and saving the playlist on an user's account</li>
</ul>

<h1>Used libraries</h1>
<ul>
<li>selenium webdriver module # to serve web crawler</li>
<li>spotipy # to serve new playlists creation</li>
<br>
<li>json # to serve json files</li>
<li>datetime # to serve date search</li>
<li>dotenv # to serve virtual environment variables</li>
<li>pathlib # to serve files paths</li>
<li>logging # to provide logs</li>
<li>os # to serve system system files</li>
<li>time # to serve proper web scraping, ensuring that the entire subpages are loaded</li>
</ul>



<h1>MIT License</h1>
<h2>Copyright (c) [2021] [Magdalena N. Pawlowicz <a href="m.n.pawlowicz@protonmail.com"</href>m.n.pawlowicz@protonmail.com</a>]</h2>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
