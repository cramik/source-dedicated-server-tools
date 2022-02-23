Allows you to output player data for all source dedicated servers for any source game in a format similar to exampledata.txt

## Issues:
For some reason, it duplicates servers when you query for like 10+ servers (this might only be for gmod). I haven't implemented a fix for this so until I do, you have to run serverlist.py, use some form of text dedupe (ie sort -u ) then continue onto running servercheck.py

## Todo:
- Script to loop and check for player name
- Temp workaround for dupe servers (might simplify the dedupe process by calling a sort subprocess in the python itself, this would limit it to people with GNUtools or Linux but would at least simplify it to one file)
- Fix dupe servers (either add to some python data structure and dedupe their or find why its duping in the first place)
