import os.path
import shutil
import subprocess

def run_test(iteration, test_type, extra_args):
    test_name = test_type + TEST_SUFFIX + str(iteration)
    if os.path.isfile(test_name + '\\Iteration8192000save.cmd'):
        return
    shutil.rmtree(test_name, ignore_errors=True)
    args = (['munch-cuda.exe', '-nogui', '-experimentName=' + test_name]
            + extra_args)
    subprocess.run(args, shell=True, check=True)

TEST_SUFFIX = 'Brendan_a'        
n = 0

while True:
    run_test(n, 'e2p0fl0r', [])
    run_test(n, 'e2p0fl1r', ['-longevityLandscape=10000,0,1,0.5,0.5',
                             '-fecundityLandscape=0.01,1,0,0.5,0.5'])
    run_test(n, 'e2p1fl0r', ['-predationProbability=0.0002 '])
    run_test(n, 'e2p1fl1r', ['-predationProbability=0.0002',
                             '-longevityLandscape=10000,0,1,0.5,0.5',
                             '-fecundityLandscape=0.01,1,0,0.5,0.5'])
    n += 1
    
