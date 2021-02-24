# About python-components
This is the source repository for the Python components related to my Programming the Internet of Things book and Connected Devices IoT course. These are shell wrappers ONLY and are not a solution set (which is a separately repository, not yet released). For convenience to the reader, some basic functionality has already been implemented (such as configuration logic, consts, interfaces, and test cases).

The code in this repository is largely comprised of shell classes that are designed to be implemented by the reader and are NOT solutions. These shell classes and their relationships respresent a notional design that aligns with the requirements listed in [Programming the IoT Requirements](https://github.com/orgs/programming-the-iot/projects/1). These requirements encapsulate the programming exercises presented in my book [Programming the Internet of Things: An Introduction to Building Integrated, Device to Cloud IoT Solutions](https://learning.oreilly.com/library/view/programming-the-internet/9781492081401).

## How to use this repository
If you're reading [Programming the Internet of Things: An Introduction to Building Integrated, Device to Cloud IoT Solutions](https://learning.oreilly.com/library/view/programming-the-internet/9781492081401), you'll see a tie-in with the exercises described in each chapter and this repository. Most of the code in the main src tree is NOT implemented by design. It's intended for you - as the reader of my book (and possibly a student in one of my IoT courses) - to implement by filling in the implementation details as you work through each exercise.

A solution set is available, although I haven't yet released it. Stay tuned for updates on this topic.

## This repository aligns to exercises in Programming the Internet of Things
These components are all written in Python3, and correlate to the exercises designed for the Constrained Device Application (CDA) specified in my book [Programming the Internet of Things: An Introduction to Building Integrated, Device to Cloud IoT Solutions](https://learning.oreilly.com/library/view/programming-the-internet/9781492081401).

Since Python is also used for various cloud computing activities, there are other components that may be introduced as Cloud Service Functions (CSF) in the future, as they will share some of the common data management code written for the CDA exercises.

## How to navigate the directory structure for this repository
The CURRENT* source repository is comprised of the following top level paths:
- [config](https://github.com/programming-the-iot/python-components/tree/alpha001/config): Contains basic configuration file(s).
- [exercises](https://github.com/programming-the-iot/python-components/tree/alpha001/exercises): Contains a directory structure for storing student lab module write-ups.
- [src/main/python](https://github.com/programming-the-iot/python-components/tree/alpha001/src/main/python): The main source tree for python-components. Keep in mind that most of these classes are shell representations ONLY and must be implemented as part of the exercises referenced above.
- [src/test/python](https://github.com/programming-the-iot/python-components/tree/alpha001/src/test/python): The test source tree for python-components. These are designed to perform very basic unit and integration testing of the implementation of the exercises referenced above. This tree is sectioned by part - part01, part02, part03, and part04 - which correspond to the structure of my book mentioned above.

Here are some other files at the top level that are important to review:
- [basic_imports.txt](https://github.com/programming-the-iot/python-components/blob/alpha001/basic_imports.txt): The core library dependencies - use pip to install.
- [cv_imports.txt](https://github.com/programming-the-iot/python-components/blob/alpha001/cv_imports.txt): The optional CV library dependencies - STILL BEING TESTED - use pip to install.
- [README.md](https://github.com/programming-the-iot/python-components/blob/alpha001/README.md): This README.
- [LICENSE](https://github.com/programming-the-iot/python-components/blob/alpha001/LICENSE): The repository's LICENSE file.

Lastly, there are some '.' files pertaining to dev environment setup that might be useful (or not - if so, just delete them after cloning the repo):
- [.gitignore](https://github.com/programming-the-iot/python-components/blob/alpha001/.gitignore): The obligatory .gitignore that you should probably keep in place, with any additions that are relevant for your own cloned instance.
- [.project](https://github.com/programming-the-iot/python-components/blob/alpha001/.project): The Eclipse IDE project configuration file that may / may not be useful for your own cloned instance. Note that using this file to help create your Eclipse IDE project will result in the project name 'piot-python-components' (which can be changed, of course).
- [.pydevproject](https://github.com/programming-the-iot/python-components/blob/alpha001/.pydevproject): The Eclipse IDE and PyDev-specific configuration file for your Python environment that may / may not be useful for your own cloned instance.

* NOTE: The directory structure and all files are subject to change based on feedback I receive from readers of my book and students in my IoT class, as well as improvements I find to be helpful for overall repo betterment.

# Other things to know

## Pull requests
PR's are disabled while the codebase is being developed.

## Updates
Much of this repository, and in particular unit and integration tests, will continue to evolve, so please check back regularly for potential updates.

# REFERENCES
This repository has external dependencies on other open source projects. I'm grateful to the open source community and authors / maintainers of the following libraries:

Core exercises:

- [aiocoap](http://github.com/chrysn/aiocoap/)
  - Reference: Amsüss, Christian and Wasilak, Maciej. aiocoap: Python CoAP Library. Energy Harvesting Solutions, 2013–. http://github.com/chrysn/aiocoap/.
- [apscheduler](https://github.com/agronholm/apscheduler)
  - Reference: A. Grönholm. APScheduler. (2020) [Online]. Available: https://pypi.org/project/APScheduler/.
- [psutil](https://github.com/giampaolo/psutil)
  - Reference: G. Rodola. Psutil. (2009 – 2020) [Online]. Available: https://psutil.readthedocs.io/en/latest/.
- [numpy](https://numpy.org/)
  - Reference: NumPy. NumPy. (2020) [Online]. Available: https://numpy.org/.
- [matplotlib](https://matplotlib.org/)
  - Reference: [J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.](https://ieeexplore.ieee.org/document/4160265)
  - DOI: https://doi.org/10.5281/zenodo.592536
- [Sense-Emu](https://sense-emu.readthedocs.io/en/v1.1/)
  - Reference: The Raspberry Pi Foundation. Sense HAT Emulator. (2016) [Online]. Available: https://sense-emu.readthedocs.io/en/v1.0/.
- [pisense](https://pisense.readthedocs.io/en/release-0.2/#)
  - Reference: D. Jones. Pisense. (2016 – 2018) [Online]. Available: https://pisense.readthedocs.io/en/release-0.2/.
- [paho-mqtt](https://www.eclipse.org/paho/)
  - Reference: R. Light. paho-mqtt. (2020) [Online]. Available: https://pypi.org/project/paho-mqtt/.
- [CoAPthon](https://github.com/Tanganelli/CoAPthon3)
  - Reference: G.Tanganelli, C. Vallati, E.Mingozzi, "CoAPthon: Easy Development of CoAP-based IoT Applications with Python", IEEE World Forum on Internet of Things (WF-IoT 2015)

Additional exercises:

- [imutils](https://github.com/jrosebr1/imutils)
  - Reference: A. Rosebrock. imutils. (2020) [Online]. Available: https://pypi.org/project/imutils/.
- [opencv-python](https://github.com/skvark/opencv-python)
  - Reference: O. Heinisuo. opencv-python. (2020) [Online]. Available: https://pypi.org/project/opencv-python/.
- [opencv-python-headless](https://pypi.org/project/opencv-python-headless/)
  - Reference: See opencv-python
- [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python/)
  - Reference: See opencv-python
- [rtsp](https://github.com/statueofmike/rtsp)
  - Reference: M. Stewart. rtsp. (2020) [Online]. https://pypi.org/project/rtsp/.

NOTE: This list will be updated as others are incorporated.

# DISCLAIMER
DISCLAIMER: This code base is still under active development - some tests and code samples may be broken.

# LICENSE
Please see [LICENSE](https://github.com/programming-the-iot/python-components/blob/alpha001/LICENSE) if you plan to use this code.
