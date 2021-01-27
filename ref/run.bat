echo off
set file_name=%1
FOR /F "delims=" %%G in ('forfiles /m %file_name%.cpp /c "cmd /c echo @fdate @ftime"') do set file_timestamp=%%G
FOR /F "delims=" %%G in ('forfiles /m %file_name%.exe /c "cmd /c echo @fdate @ftime"') do set executable_timestamp=%%G

set build=1
if "%file_timestamp%" LEQ "%executable_timestamp%" set build=0
if "%file_timestamp%" GTR "%executable_timestamp%" set build=1

echo on
if %build% == 1 g++ -std=c++11 -D USE_FILE_IO -g %file_name%.cpp -o %file_name%.exe
%file_name%.exe