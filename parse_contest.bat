set folder_name=%1
python parse_contest.py %1
cd  %folder_name%
copy ..\ref\* .
type 0 > input.txt