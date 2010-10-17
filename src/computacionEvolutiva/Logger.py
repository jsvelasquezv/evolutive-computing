"""
Capture print statments and write them to a log file
but still allow them to be printed on the screen.
Usage:  see if __name__=='__main__': section below.
"""
import time

class Logger:
    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.logfile = file(filename, 'a')
        self.logfile.write('\n\nNew run at %s\n\n' % time.ctime())
    def write(self, text):
        self.stdout.write(text)
        self.logfile.write(text)
        self.logfile.flush()
    def close(self):
        self.stdout.close()
        self.logfile.close()
