###Baseball Statistics

========================

This repository contains a bunch of data (the stuff in individualYears/) and some scripts to read them and make some sense of them.

info.txt is a copy-pasted text file from the website whence all the stats are explaining each column in the CSV file.

generateCombined.sh is a unix shell file that combines all the stats into a single file that main.py knows how to read. Maybe I'll write a batch file sometime so that the Windows sheeple can use it too. 

main.py is the python script that I use to read and interpret all the data. Right now it just counts up wins and losses, but maybe soon it'll be fancier.
