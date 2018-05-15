import os.path
import shutil
import subprocess
import threading

THREADS = 2
TEST_SUFFIX = 'Brendan'


class Counter(object):
    def __init__(self, value=0):
        self.value = value
        self.lock = threading.Lock()

    def next(self):
        with self.lock:
            n = self.value
            self.value += 1
        return n


def run_test(iteration, test_type, extra_args):
    test_name = test_type + TEST_SUFFIX + str(iteration)
    if os.path.isfile(test_name + '\\Iteration8192000save.cmd'):
        return
    shutil.rmtree(test_name, ignore_errors=True)
    args = (['munch-cuda.exe', '-nogui', '-experimentName=' + test_name]
            + extra_args)
    subprocess.run(args, shell=True, check=True)


def run_tests(iterator):
    while True:
        n = iterator.next()
        run_test(n, 'e2p0fl0r', [])
        run_test(n, 'e2p0fl1r', ['-longevityLandscape=10000,0,1,0.5,0.5',
                                 '-fecundityLandscape=0.01,1,0,0.5,0.5'])
        run_test(n, 'e2p1fl0r', ['-predationProbability=0.0002 '])
        run_test(n, 'e2p1fl1r', ['-predationProbability=0.0002',
                                 '-longevityLandscape=10000,0,1,0.5,0.5',
                                 '-fecundityLandscape=0.01,1,0,0.5,0.5'])


counter = Counter()
for i in range(THREADS - 1):
    thread = threading.Thread(target=run_tests, kwargs={'iterator': counter})
    thread.start()
run_tests(iterator=counter)
