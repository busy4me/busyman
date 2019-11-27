# busy
🐙 busy commands set - to manage personal "Genius Assistant" 🌐

### based on StratumOS  

basic usage
``` shell
busy [--option=value]... [:place]
```

or

``` shell
busy [sub_command] [--option=value]... [:place]
```

# Available options:
🚧 Under construction

## --like
``` shell
--like[="URL"] # to like something eg. post, profile
```
⭐️ EXAMPLE: Active profile will like specific post in socialportal.com, executed in DISPLAY:0
``` shell
busy --like="https://socialportal.com/fanpage/post" :0
```

## --follow
``` shell
--follow[="URL"] # to follow profile from URL
```
☝️ TIP: option without value will will be executed in current opened URL  
⭐️ EXAMPLE: Active profile will follow other profile in socialportal.com, executed in DISPLAY:02
``` shell
busy --like="https://socialportal.com/fanpage/post" :02
```

## --post
``` shell
--post[="database.table.record"] # to prepare and publish a post
```
☝️ TIP: option without value will put the oldest post from defult table from default database  
⭐️ EXAMPLE: Active profile will put a post in socialportal.com, from database "roy_visar_db", table "fb_posts", record "4276", executed in DISPLAY:5
``` shell
busy --like="roy_visar_db.fb_posts.4276" :5
```

## --live
``` shell
--live[=start|=stop|=status] --url[="URL"]
# live streaming to specific rtmp socket
```
☝️ TIP: _live_ option without value will _start_ live streaming eg. "busy --live"  
☝️ TIP: with no _url_ option, default url socket will be used  
⭐️ EXAMPLE: Start Live streaming of DISPLAY:0 to blablavideo.com portal
``` shell
busy --live=start --url="rtmp://live-api.blablavideo.com:80/api=1&key=As4fRws8Q" :0
```

## --login
``` shell
--login[=login_name] # to login in specific portal
```
⭐️ EXAMPLE: Active profile will login in socialportal.com, executed in DISPLAY:1
``` shell
busy --login="https://socialportal.com" :1
```  

## --share
``` shell
--share[="URL"] # to share something
```
⭐️ EXAMPLE: Active profile will share something in Group "group_name" in socialportal.com, executed in DISPLAY:1
``` shell
busy --share="https://somethingcool.co" --url="https://socialportal.com/group_name" :1
```  

## --join
``` shell
--join[="URL"] # to join somewhere
```
⭐️ EXAMPLE: Active profile will join somewhere
``` shell
busy --join="https://socialportal.com/group_name" :1
```  

## --invite
``` shell
--invite[=database.table] --url=["URL"]# to invite others
```
⭐️ EXAMPLE: Active profile will invite others
``` shell
busy --invite[=roy_visar_db.fb_friends] --url="https://socialportal.com/group_name" :1
```  

## --subscribe
``` shell
busy --subscribe[="URL"] # to subscribe
```
⭐️ EXAMPLE: Active profile will subscribe
``` shell
busy --subscribe="https://somethingcool.co" :1
```  

## --cron
``` shell
busy --cron[=on|=off|=status] # to operate in crontab
```

## --db
``` shell
busy --db[=add] --table[="database.table"] # add table in database
```
``` shell
busy --db[=drop] --table[="database.table"] # drop table in database
```
``` shell
busy --db[=add] --record[="database.table.record"] # add record in database
```
``` shell
busy --db[=delete] --record[="database.table.record"] # delete record in database
```
``` shell
busy --db[=show] --table[="database.table.record"] # show records in database
```

# NOTES
🔥 Hot: last update  
⚠️ Caution: use carefully  

# Wiki
busy4me Wiki 🚧 Under construction
