import os.path
import glob
import random
import shutil
import subprocess
import threading

THREADS = {
    0: 3,
    1: 3,
}
TEST_SUFFIX = ''
COMPETITION_EXP = True
FL0COMP = [('e2p0fl0r*', '0.5'), ('e2p1fl0r*', '0.5')]
FL1COMP = [('e2p0fl1r*', '0.5'), ('e2p1fl1r*', '0.5')]

TESTS = [
    ('comp_e2p0fl0r', [], FL0COMP),
    ('comp_e2p0fl1r', ['-longevityLandscape=10000,0,1,0.5,0.5',
                  '-fecundityLandscape=0.01,1,0,0.5,0.5'], FL0COMP),
    ('comp_e2p1fl0r', ['-predationProbability=0.0002 '], FL1COMP),
    ('comp_e2p1fl1r', ['-predationProbability=0.0002',
                  '-longevityLandscape=10000,0,1,0.5,0.5',
                  '-fecundityLandscape=0.01,1,0,0.5,0.5'], FL1COMP)
]


def make_competition_command(population_requirements):
    arg = '-loadPopulations='
    for p in population_requirements:
        arg += random.choice(glob.glob(p[0])) + '/saveData/8192000'+','+p[1]+';'
    return arg.rstrip(';')


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
            args = test[1].copy()
            if COMPETITION_EXP:
                args.append(make_competition_command(test[2]))
        return name, args


def run_tests(iterator, device):
    device_arg = '-device=' + device
    for test_name, extra_args in iterator:
        if os.path.isfile(test_name + '\\Iteration8192000save.cmd'):
            continue
        shutil.rmtree(test_name, ignore_errors=True)
        args = (['munch-cuda.exe', '-nogui', '-passiveWaitCPU',
                 '-experimentName=' + test_name, device_arg] + extra_args)
        subprocess.run(args, shell=True, check=True)


counter = Counter(TESTS, TEST_SUFFIX)
for device_number, threads in THREADS.items():
    device_string = str(device_number)
    for i in range(threads):
        thread = threading.Thread(
            target=run_tests,
            kwargs={'iterator': counter, 'device': device_string}
        )
        thread.start()
