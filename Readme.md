# Minimalist Codeforces Parser

## What is it?
A lightweight, easy to customize contest parser and pretests runner

## <br>
## What's the need?
During programming contest of stringent time limits, even few seconds matter. It is time consuming to copy past test cases and execute the code on local again and again.

Using this tool in a 2-word command (parse_contest X) it will download and create a folder structure with all the pretests (Sample Testcases) for that programming contest. 

Also using a 2-word (test Y) command it will execute all pretests for any problem.

In other words it will remove all manual effort in copy pasting inputs and comparing outputs for all pretests (Sample Testcases).

## <br>
## How to use?

Step-1: Navigate to the project folder.

Step-2: run command: [sample command : <b> parse_contest 1427</b> ] : <br>It will create directory structure like below: (with cpp files generated using template in ref folder)
<pre>
└───1427
   │    A.cpp
   │    B.cpp
   └───pretests
       ├───A
       │       input_0.txt
       │       output_0.txt
       │
       └───B
              input_0.txt
              input_1.txt
              input_2.txt
              input_3.txt
              output_0.txt
              output_1.txt
              output_2.txt
              output_3.txt
</pre>

Step-3: Running testcases: [sample command : <b> test B</b> ]
<br>
<pre>

<b>> test B
<span style="color: green;">------------------------------
pretest - 0: PASSED</span>
<span style="color: yellow;">6
ac?b?c</span>
24
<span style="color: green;">24</span>
<span style="color: green;">------------------------------
pretest - 1: PASSED</span>
<span style="color: yellow;">7
???????</span>
2835
<span style="color: green;">2835</span>
<span style="color: green;">------------------------------
pretest - 2: PASSED</span>
<span style="color: yellow;">9
cccbbbaaa</span>
0
<span style="color: green;">0</span>
<span style="color: red;">------------------------------
pretest - 3: Failed</span>
<span style="color: yellow;">4
????</span>
12
<span style="color: red;">13</span>
</b></pre>

<br>

## Color scheme

| Entity      | Color |
| :---        |    :----:   |
| Pretest Status      | Green if success else Red       |
| Pretest Input   | Yellow        |
| Expected Output  | White        |
| Programs Output  | Green if success else Red          |

