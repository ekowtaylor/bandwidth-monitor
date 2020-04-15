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
#### Bandwidth Monitor
Stores and caches results from well-known internet speed test sources like [speedtest.net](http://speedtest.net/ "speedtest.net") and [fast.com](http://fast.com "fast.com").
##### Supported databases:

| Database Name |      Status     |
|:-------------:|:---------------:|
|     SQLite    | Not implemented |
|     MySQL     | Not implemented |
|     PostgreSQL     | Not implemented |
|     Flat File storage     | Not implemented |


## Author
Eyal Berkovich