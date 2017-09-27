# Night Owls Detector

This script works with DEVMAN.org. It detects who sent last task for review after today's midnight. Uses pendulum for faster and easier working with timezones. Prints following information about each found user:
1) Username on DEVMAN.org
2) Date and time at which user submitted task for review

# Quickstart

Place seek_dev_nighters.py somewhere. Then run command line, go to folder in which you moved script and execute it.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python seek_dev_nighters.py <path to file>

```

Output data example:

```#!bash

1) pavel.sofrony submitted task for review at 2017-09-27 12:23:35

2) pavel.sofrony submitted task for review at 2017-09-27 12:16:06

3) tonycross submitted task for review at 2017-09-27 10:12:43

4) artem7lomonosov submitted task for review at 2017-09-27 09:23:14

5) RamusikValery submitted task for review at 2017-09-27 08:43:03

6) RamusikValery submitted task for review at 2017-09-27 08:29:02

7) ДмитрийВоронов submitted task for review at 2017-09-27 07:48:59
......

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
