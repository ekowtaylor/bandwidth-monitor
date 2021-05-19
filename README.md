
# Bandwidth Monitor    
## Description
My internet connection always seems unstable, dropping here and there. To monitor and catch such phenomenas, I decided to build a network bandwidth monitor that fetches download and upload rate based on a given time interval which can be set in the [config file](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json "config file").     

## How to Install & Run
Firstly, please run `pip3 install -r requirements.txt` to install all required modules from [requirements.txt](https://github.com/codekrnl/bandwidth-monitor/blob/master/requirements.txt), to make sure you have all the required modules installed.
After that, you can run `python3 main.py` to run the entry point in the main file.

Because the web panel is running on your machine, it means it runs on a local web server, on your machine. So, to access the web panel, you can go to you web browser and type `localhost:<YOUR_SET_WEB_PORT>`.
If you haven't modified the config file, the default web port is 8600, so the address is: `localhost:8600`.

<details>

<summary> Required Modules </summary>

- speedtest-cli
- redis
- psutil
- flask

</details>

<details>

<summary>Show commands</summary>

- `pip3 install -r requirements.txt` — To install all required modules from [requirements.txt](https://github.com/codekrnl/bandwidth-monitor/blob/master/requirements.txt).

- `python3 main.py` — To run program.

</details>

 ## Project Structure 
 ### 
 Bandwidth Monitor stores and caches results from well-known internet speed test sources like [speedtest.net](https://www.speedtest.net/ "speedtest.net") and [fast.com](http://fast.com "fast.com") automatically, and also offers a slick UI to manage and monitor your collected data.    

| Name | Purpose |  
|--|--|  
| [main.py](https://github.com/codekrnl/bandwidth-monitor/blob/master/main.py) | Program entry point. | 
| [config.json](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json) | Program configuration file. |  
| [/config/](https://github.com/codekrnl/bandwidth-monitor/tree/master/config) | Configuration management files. Currently only json configuration files are supported. |  
| [/measure/](https://github.com/codekrnl/bandwidth-monitor/tree/master/measure) | Responsible for the actual bandwidth measure. Currently, this version only supports [speedtest.net](https://www.speedtest.net/). |  
| [/util/](https://github.com/codekrnl/bandwidth-monitor/tree/master/util) | Contains utility files and functions, e.g: checking for connection availability, parsing time intervals read from config. |  
| [/storage/](https://github.com/codekrnl/bandwidth-monitor/tree/master/storage) | Contains storage management files. |  
 
### Features
|Feature | Description  |
|:--|:--|
| Collect Bandwidth Data | Collect internet bandwidth results from well known services, like [fast.com](https://fast.com/) and [speedtest.net](https://speedtest.net/). |
| Storage | Store all your collected data in a database, implemented storage types can be seen down below. |
| Web Panel | You can view your collected data using a nice Web UI, that runs on a local server on your computer. The port can be set [in the web-port field](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json). |
| CLI | This tool prints your collected information in your terminal |


#### Supported databases:    
|  Database Name  |      Status      |
|:----------------|:----------------|
|     SQLite      |  Implemented 🟢  |
|      MySQL      |Not Implemented 🔴|
|   PostgreSQL    |Not Implemented 🔴|
|Flat File storage|Not Implemented 🔴|

 #### Supported cache systems:    
 | Cache Name |      Status     |
 |:-------------:|:---------------:| 
 |     Redis    | Not Implemented 🔴 |    

## Configuration

| Field | Purpose | 
|:--|:--|
| `check-interval` | The check time interval to collect data. |
| `web-port` 	   | The web panel port |
|`database-name`   | Storage database file name |

### Configurable Time Interval Extensions
You can modify the time interval the program gathers internet bandwidth data.

This can be set in the [program's configuration file](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json) with the `check-interval` field.

> Default check interval is `1m` — every 1 minute.

#### Supported Extensions

| Extension | Description | Example | 
|:---------:|:-----------:|:-------:| 
|     s     |   Seconds   |    2s   | 
|     m     |   Minutes   |    3m   | 
|     h     |    Hours    |   19h   | 
|     d     |     Days    |    5d   | 
|     w     |    Weeks    |    3w   |   

 ## TODO  
* Implement web UI - Implemented on November 7, 2020 🟢  
* Implement running process list information - 🔴
* Implement connection type resolver - 🔴
* Implement auto web UI refresh - 🔴

## Screenshots    
### CLI Tool: 
![CLI Tool](https://github.com/codekrnl/bandwidth-monitor/blob/master/screenshots/cli-monitor.png?raw=true)

### Main Monitor Dashboard:
![Main dashboard](https://github.com/codekrnl/bandwidth-monitor/blob/master/screenshots/bandwidth-monitor-ui.png?raw=true)

## Author
* Eyal Berkovich
