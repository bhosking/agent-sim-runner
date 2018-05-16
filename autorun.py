import os.path
import shutil
import subprocess
import threading

THREADS = 2
TEST_SUFFIX = 'Brendan'

TESTS = [
    ('e2p0fl0r', []),
    ('e2p0fl1r', ['-longevityLandscape=10000,0,1,0.5,0.5',
                  '-fecundityLandscape=0.01,1,0,0.5,0.5']),
    ('e2p1fl0r', ['-predationProbability=0.0002 ']),
    ('e2p1fl1r', ['-predationProbability=0.0002',
                  '-longevityLandscape=10000,0,1,0.5,0.5',
                  '-fecundityLandscape=0.01,1,0,0.5,0.5'])
]


class Counter(object):
    def __init__(self, tests, test_suffix, repeat=0, test_index=0):
        self.tests = tests
        self.repeat = repeat
        self.test_index = test_index
        self.test_suffix = test_suffix
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            test_index = self.test_index
            repeat = self.repeat
            if test_index >= len(self.tests) - 1:
                self.test_index = 0
                self.repeat += 1
            else:
                self.test_index += 1
            test = self.tests[test_index]
            suffix = self.test_suffix
        name = test[0] + suffix + str(repeat)
        args = test[1]
        return name, args


def run_test(test_name, extra_args):
    if os.path.isfile(test_name + '\\Iteration8192000save.cmd'):
        return
    shutil.rmtree(test_name, ignore_errors=True)
    args = (['munch-cuda.exe', '-nogui', '-experimentName=' + test_name]
            + extra_args)
    subprocess.run(args, shell=True, check=True)


def run_tests(iterator):
    for test_name, args in iterator:
        run_test(test_name, args)


counter = Counter(TESTS, TEST_SUFFIX)
for i in range(THREADS - 1):
    thread = threading.Thread(target=run_tests, kwargs={'iterator': counter})
    thread.start()
run_tests(iterator=counter)
