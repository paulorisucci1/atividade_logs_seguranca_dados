from Entry import *
log_archives = {
    'system': '/var/log/syslog',
    'auth': '/var/log/auth.log',
    'boot': '/var/log/boot.log',
    'kernel': '/var/log/kern.log',
    'drivers': '/var/log/dmesg',
    'fail_log': '/var/log/faillog',
}


def entry_has_amount_of_lines(entry):
    return len(entry) > 1


while True:
    print(''''Which log would you like to see?'
    Options: 
    - system : General messages, as well as system-related information. Essentially, this log stores all activity data across the global system.
    - auth : Store authentication logs, including both successful and failed logins and authentication methods.
    - boot : A repository of all information related to booting and any messages logged during startup.
    - kernel: Stores Kernel logs and warning data
    - drivers: messages relating to device drivers
    - fail_log: contains information all failed login attempts
    ''')

    entry = Entry()

    entry.read_file()
