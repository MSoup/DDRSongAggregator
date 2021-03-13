# DDRSongAggregator
A script that grabs the song list of all the DDR songs on Wikipedia and find all the existing songs available on spotify

Searches spotify and returns a list of songs available.

Stack: Python 100%

## How it works

- crawls Wikipedia DDR page
- extracts relevant info from table
- cleans the data
- stores the data in json format
- subsequent runs access the json
- outputs cleaned data to text file

## Issues

- apple music integration not yet supported
- dependent on wikipedia page being updated

## To be done

- pull from Konami servers rather than wikipedia? 
- query more music apps?
- connect to front end to allow users to query a series of their choice

## Updates
3/13- gonna clean the extraction process and connect to front end
