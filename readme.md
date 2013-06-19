####Why the name is so horrible?
> What's in a name?

####What does it do?
> Its in the name, checks thousands of scilab(.sc[i,e]) scripts and compares functions of script to list of functions which given scilab-version supports. By default it outputs function-centric incompatibility.

####Why not simply run all scilab scripts and analyze its output? Wouldn't it be more accurate? Any specific reason for having to use complex parsing and regex code in this project
> I'll give you three: <br/>

1. This project is **fun** (also its fast, scalable and probably interesting way to do things, can integrate yelp to make it more powerful)<br/>
2. Scilab-interpreter is bad, it will hang up the first time it encounters a incompatible function in a script<br/>
3. Scilab-interpreter takes forever to load; make it load special libraries, and you can have afternoon siesta by the time it crawls 27k scripts.<br/> Whereas this script crawls in under *3mins*. 

####How do I use this?
> Good question

1.Download all these files<br/>
`git clone https://github.com/manojgudi/sci_auto_check.git` <br>
2.Install w3m<br>
`sudo apt-get install w3m`<br/>
3. Generating list of functions in *xyz* version (ex. *5.4.1*) Scilab version<br>
`./get_list 5.4.1`<br>
4. Using *check* script to crawl a path where all scilab scripts have been stored(for ex. ./dummy_scripts)<br>
`./check ./dummy_scripts` 

* Optionally, to increase speed and dump the entire info for further analysis, try:<br/>
`./check ./dummy_scripts > dumpfile`<br>

* Moreover, to analyze these scripts further, you can use yelp along with this:<br/>
`./check -y dummy_scripts/`

* To increase verbose or get a file centric issues, use `-v` as an option:<br/>
`./check -v dummy_scripts/`

####What is this *yelp* you are referring to?
> **yelp** is sanity-check script for scilab scripts, [read more](https://github.com/manojgudi/yelp) <br/>

####I've one {more question, problem, doubt, suggestion}
> Please email me.
