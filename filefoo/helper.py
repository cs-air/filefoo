import time
import threading
import clr
import sys
import humanfriendly
from columnar import columnar    # used to print columnar layouts

DEBUG = False

def dprint(foo):
    if DEBUG:
        print(foo)

def mykwargs(sysargs):
    """ Creates a dictionary of key=value pairs.
        If an argument of format 'k=v' with no spaces is present, it is added 
        to `kwargs dictionary`, otherwise it is added to the `args list`.

        Parameters:
        -----------
        sysargs [list] : list of arguments (usually sys.argv)

        Returns:
        --------
        tuple(dict,list) : kwargs dict and args list
    """
    args = []
    kwargs = {}

    for a in sysargs:
        if '=' in a:
            k, v = a.split('=')
            kwargs[k] = v
        else:
            args.append(a)

    return kwargs, args

class Borg(object):
    _state = {}
    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._state
        return self

class Spinner:
    """ Prints a "progress" of sorts showing a task is still running.
    """
    busy = False
    delay = 0.05
    count = 1
    #spinner_list = ['|','/','-','\\']
    spinner_list = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]

    def __init__(self, counts,delay=None):
        self.spin_time = time.time() 
        self.counts = counts
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            
            self.count += 1

            sys.stdout.write('\r')
            seconds = time.time()-self.spin_time

            minutes = int(seconds / 60)
            seconds = int(seconds - minutes * 60)

            self.counts.minutes = minutes
            self.counts.seconds = seconds

            dots = '.' * seconds # not used
            schar = self.spinner_list[self.count%len(self.spinner_list)]
            f1 = str(self.counts.folders).ljust(8)
            f2 = str(self.counts.files).ljust(8)
            f3 = str(self.counts.found).ljust(8)
            f4 = humanfriendly.format_size(self.counts.size)
            f4 = str(f4).ljust(8)
            diff = f"searching: {clr.bold.magenta(schar)} [ folders:{clr.bold.yellow(f1)} | files:{clr.bold.yellow(f2)} | found:{clr.bold.green(f3)} | size:{clr.bold.blue(f4)}  | time:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}]"
            sys.stdout.write(diff)
            sys.stdout.flush()
            time.sleep(self.delay)
        
    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


class ThrowError(object):
    """ Amazing custom error handler class. Very robust :)
        Parameters:
        -----------
        message [string]        : error message
        error_keyword [bool]    : print "Error" before message
        bail [bool]             : exit program (fatal error)
    """

    def __init__(self, **kwargs):
        msg = kwargs.get('message', None)
        error_keyword = kwargs.get('error_keyword', True)
        bail = kwargs.get('bail', True)

        # Adds red "Error:" to output
        if error_keyword:
            msg = f"{clr.bold.red('Error:')} " + msg
        print(msg)
        if bail:
            sys.exit()

class Usage(object):
    @staticmethod
    def print(classname,commands):
        command_list = []
        for command, description in commands.items():
            command_list.append([' '+clr.green(command), ' '+clr.yellow(description)])

        usage = columnar(command_list, headers=[clr.green.bold(' Command'), clr.yellow.bold(' Description')])

        return f"{classname} Usage:\n" + usage


