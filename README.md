# Bandwidth Monitor  
  
## Description  
My internet connection always seems unstable, dropping here and there. To monitor and catch such phenomenas, I decided to build a network bandwidth monitor that fetches download and upload rate based on a given time interval which can be set in the [config file](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json "config file").   
  
Here's a table of supported time interval extensions:  
  
| Extension | Description | Example |  
|:---------:|:-----------:|:-------:|  
|     s     |   Seconds   |    2s   |  
|     m     |   Minutes   |    3m   |  
|     h     |    Hours    |   19h   |  
|     d     |     Days    |    5d   |  
|     w     |    Weeks    |    3w   |  
  
## Project Structure  
### Bandwidth Monitor  
Stores and caches results from well-known internet speed test sources like [speedtest.net](http://speedtest.net/ "speedtest.net") and [fast.com](http://fast.com "fast.com").  

| Name | Purpose |
|--|--|
| /config/ | Configuration management files. Currently only json configuration files are supported. |
| /measure/ | Responsible for the actual bandwidth measure. Currently only supported [speedtest.net](speedtest.net). |
| /util/ | Contains utility functions e.g: checking for available internet connection, parsing time intervals read from config. |
| /storage/ | Contains storage management files. |
| [config.json](https://github.com/codekrnl/bandwidth-monitor/blob/master/config.json) | Main configuration file. |
| [main.py](https://github.com/codekrnl/bandwidth-monitor/blob/master/main.py) | Program entry point. |

  
#### Supported databases:  
  
| Database Name |      Status     |  
|:-------------:|:---------------:|  
|     SQLite    | Implemented ✅ |  
|     MySQL     | Not implemented |  
|     PostgreSQL     | Not implemented |  
|     Flat File storage     | Not implemented |  
  
#### Supported cache systems:  
  
| Cache Name |      Status     |  
|:-------------:|:---------------:|  
|     Redis    | Not implemented |  
  
## Author  
- Eyal Berkovich