# Mini Sherlock 🔍

A lightweight username search tool inspired by Sherlock, designed for quick checks across popular platforms.

## Features

- Fast username availability checking
- Supports 26 popular platforms (Work in progress)
- Simple interface
- Lightweight (no heavy dependencies)

### Requirements
1. Git
2. Python3
3. Python3-pip
4. Internet connection
5. Docker (optional)

## Installation

1. Clone git repository:
```bash
git clone https://github.com/Andrey-oss/mini-sherlock.git
cd mini-sherlock
```

2. Install necessary python packages:
```bash
pip3 install -r requirements.txt
```

3. Launch the script:
``` bash
python3 mini-sherlock.py
```

## Docker
Also you can run this app by using docker:

1. Start the service:
```bash
systemctl start docker
```

2. Build container:
```bash
docker build -t mini_sherlock .
```

3. Run mini-sherlock:
```bash
docker run --rm -it mini_sherlock
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

### Note
This is a test and initial implementation of the project that describes the entire process of obtaining information. Don't judge the code too harshly
