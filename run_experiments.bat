REM Each of these blocks is a set of experiments, please complete all experiments in a set before starting another.
REM The only thing you'll change in these sets is the number directly after %USERNAME% to increment the set of experiments
REM if you want to run with the GUI enabled delete the -nogui. This defaults to 32 iterations per frame which can be decreased with '-' and increased with '+'

REM with GUI enabled you can pause the simulation with 'p'. Whilst paused the simulation uses very little resources.

REM if you need to exit the simulation for some reason, and have GUI enabled, then press 'p' then right click and select save, then exit.
REM this save can be loaded again by opening the folder and double clicking the most recent .cmd file.

REM if for some reason a simulation fails to complete (there will be no Iteration8192000save.cmd in the folder) then delete the entire folder and before running the simulation again.
munch-cuda.exe -nogui -experimentName=e2p0fl0r%USERNAME%0 
munch-cuda.exe -nogui -experimentName=e2p0fl1r%USERNAME%0 -longevityLandscape=10000,0,1,0.5,0.5 -fecundityLandscape=0.01,1,0,0.5,0.5
munch-cuda.exe -nogui -experimentName=e2p1fl0r%USERNAME%0 -predationProbability=0.0002 
munch-cuda.exe -nogui -experimentName=e2p1fl1r%USERNAME%0 -predationProbability=0.0002  -longevityLandscape=10000,0,1,0.5,0.5 -fecundityLandscape=0.01,1,0,0.5,0.5

REM munch-cuda.exe -nogui -experimentName=e2p0fl0r%USERNAME%1 
REM munch-cuda.exe -nogui -experimentName=e2p0fl1r%USERNAME%1 -longevityLandscape=10000,0,1,0.5,0.5 -fecundityLandscape=0.01,1,0,0.5,0.5
REM munch-cuda.exe -nogui -experimentName=e2p1fl0r%USERNAME%1 -predationProbability=0.0002 
REM munch-cuda.exe -nogui -experimentName=e2p1fl1r%USERNAME%1 -predationProbability=0.0002  -longevityLandscape=10000,0,1,0.5,0.5 -fecundityLandscape=0.01,1,0,0.5,0.5

REM etc...