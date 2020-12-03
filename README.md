# 2048

There we go I can type now.

So first I make a new directory to put the actual code into. That isn't strictly necessary, but 
it is needed for packaging. 

For example to access numpy you'd call `numpy.whatever` but that's only because they put their 
code in a folder called `numpy`. If they put it at the top level, then you'd need to directly 
import `whatever` and it'd get confusing and messy fast, with name collisions

2048 isn't a valid variable name, so I called it game_2048. That's questionable, I just picked 
something.

I'm not sure if you've seen __init__.py before. It is sort of the entry point for the folder. 
If you import `game_2048` (the name of the directory) what youre actually importing is its init 
file.

If you peek at the git repos for python libraries youll often find their init files import lots 
of other files into the top level with `from blah import *` format. That way you could go 
`import foldername`, `foldername.thing` conveniently, without them needing to actually keep all 
those things in a single file.
anyway

We should design a basic architecture.
Are you able to write?



Game loop

Game state

User input

Graphics