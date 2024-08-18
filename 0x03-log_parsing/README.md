# 0x03-LOG_PARSING

This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data.

The script reads *stdin* line by line and computes metrics:
    - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>.
        (if the format is not this one, the line must be skipped).

    - After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
        1. Total file size: File size: <total size>
            where <total size> is the sum of all previous <file size> (see input format above)
        2. Number of lines by status code:
                - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
                - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
                - format: <status code>: <number>

                *status codes should be printed in ascending order.*
