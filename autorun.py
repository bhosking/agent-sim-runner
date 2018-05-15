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

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            n = self.value
            self.value += 1
        return n


def run_test(test_name, extra_args):
    if os.path.isfile(test_name + '\\Iteration8192000save.cmd'):
        return
    shutil.rmtree(test_name, ignore_errors=True)
    args = (['munch-cuda.exe', '-nogui', '-experimentName=' + test_name]
            + extra_args)
    subprocess.run(args, shell=True, check=True)


def run_tests(iterator):
    for n in iterator:
        suffix = TEST_SUFFIX + str(n)
        run_test('e2p0fl0r' + suffix, [])
        run_test('e2p0fl1r' + suffix, ['-longevityLandscape=10000,0,1,0.5,0.5',
                                       '-fecundityLandscape=0.01,1,0,0.5,0.5'])
        run_test('e2p1fl0r' + suffix, ['-predationProbability=0.0002 '])
        run_test('e2p1fl1r' + suffix, ['-predationProbability=0.0002',
                                       '-longevityLandscape=10000,0,1,0.5,0.5',
                                       '-fecundityLandscape=0.01,1,0,0.5,0.5'])


counter = Counter()
for i in range(THREADS - 1):
    thread = threading.Thread(target=run_tests, kwargs={'iterator': counter})
    thread.start()
run_tests(iterator=counter)
