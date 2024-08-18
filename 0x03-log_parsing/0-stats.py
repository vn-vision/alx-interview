#!/usr/bin/python3
'''
This script reads stdin line by line and computes metrics.
Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
                <status code> <file size>
(If the format is not this one, the line must be skipped.)
'''

import sys
import re
import signal

# Pattern to match the required log format
pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/\d+ HTTP/1\.1" \d{3} \d+$'
)

# Initialize the total file size and the status code counts
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

# The number of lines processed
line_count = 0


def print_stats():
    '''Prints the collected statistics'''
    print(f'File size: {total_file_size}')
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f'{code}: {status_code_counts[code]}')


def signal_handler(sig, frame):
    '''Handles the keyboard interruption (CTRL + C)'''
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        line = line.strip()

        if pattern.match(line):
            # Split line into segments
            parts = line.split()
            status_code = parts[-2]  # The second last part of the line
            file_size = int(parts[-1])  # The last part of the line

            # Increment the total file size
            total_file_size += file_size

            # Update the status code count if it is a recognized code
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1  # +1 for each occurrence

            line_count += 1

            if line_count % 10 == 0:  # If 10 lines have been processed
                print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()
    sys.exit(0)

# Final print after reading all lines
print_stats()
