### Coffee

A simple [Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12) / Caffeinate alternative written in Python.

This app simulates mouse movement very subtly, every minute, preventing the computer from sleeping.

### Pre-requisites

This package requires Python3 to be installed.

To clone the repo run:

```bash
git clone https://github.com/vinceau/coffee
cd coffee
```


### Running the app

```bash
python3 coffee.py
```


### Building the app

```bash
pip3 install -r requirements.txt
python3 setup.py py2app
```

This builds the `Coffee.app` file in the `./dist` folder.


### Acknowledgements

* Based on the open-source [Pomodoro app](https://github.com/visini/pomodoro) by [Camillo Visini](https://camillovisini.com/coding/create-macos-menu-bar-app-pomodoro)

* Coffee Icon Logo is from [Flat Icon](https://www.flaticon.com/free-icon/coffee_590836?term=coffee&page=1&position=4&origin=search&related_id=590836)
