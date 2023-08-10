#!/usr/bin/python3
import sys
import subprocess

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
    while 1:
        write_stdout('READY\n')

        line = sys.stdin.readline()
        write_stderr(line)

        # read event payload and print it to stderr
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len']))
        write_stderr(data)

        if headers['eventname'] == 'SUPERVISOR_STATE_CHANGE_STOPPING' or headers['eventname'] == 'TICK_60':
            subprocess.run(["/usr/bin/admin-mgr", "lsn-checkpoint-push"])

        write_stdout('RESULT 2\nOK')

if __name__ == '__main__':
    main()