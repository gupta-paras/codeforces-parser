set folder_name=%1
mkdir %folder_name%
cd  %folder_name%
copy ..\ref\atcoder_ref.cpp a.cpp
copy ..\ref\atcoder_ref.cpp b.cpp
copy ..\ref\atcoder_ref.cpp c.cpp
copy ..\ref\atcoder_ref.cpp d.cpp
copy ..\ref\atcoder_ref.cpp e.cpp
copy ..\ref\atcoder_ref.cpp f.cpp
copy ..\ref\run.bat .
type 0 > input.txt