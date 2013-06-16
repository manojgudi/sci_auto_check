###Why the name is so horrible?
> What's in a name

###What does it do?
> Its in the name, checks thousands of scilab(.sc[i,e]) scripts and compares functions of script to list of functions which given scilab-version supports

###Why not simply run all scilab scripts and analyze its output? Wouldn't it be more accurate? Any specific reason for having to use complex parsing and regex code in this project
> I'll give you three: <br/>

1. This project is **fun** (also its fast, scalable and probably interesting way to do things, can integrate yelp to make it more powerful)<br/>
2. Scilab-interpreter is bad, it will hang up the first time it encounters a incompatible function in a script<br/>
3. Scilab-interpreter takes forever to load, make it load special libraries, and you can have afternoon siesta by the time it crawls 27k scripts<br/> Whereas this script crawls in under 10mins. 

###I've one more question...
> Ask me when I write the entire script and have time to do monologues
