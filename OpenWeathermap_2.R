install.packages("ggplot2")
library(ggplot2)
install.packages("jsonlite")
library(jsonlite)
install.packages("curl")
library(curl)

# openwethermap
#API call for 7 day weather forecast for Helsinki (see http://openweathermap.org/forecast5 for other calls)
 api_call_1 <- "http://api.openweathermap.org/data/2.5/forecast/daily?q=Helsinki&mode=json&units=metric&cnt=7&APPID="
#add your own API key between ""
 api_key_1 <- "ab369e0ae0c6637484fdc292e8e7043c"

#making the API call 1
hki_json_1 <- fromJSON(paste(api_call_1, api_key_1, sep=""))

#response is .json so we must flatten it to get a data frame
hki_7d <- flatten(as.data.frame(hki_json_1))
hki_7d <- cbind(hki_7d, do.call(rbind.data.frame, hki_7d$list.weather))
hki_7d$date <- seq(as.Date(Sys.Date()), by = "day", length.out = nrow(hki_7d))

#changing the datatype to character so we get the same axis labels as in the data frame
hki_7d$date <- as.character(hki_7d$date)

#making a graph
ggplot(hki_7d,aes(x=date, group=2))+
  geom_line(aes(y=list.temp.day, color="DayTemp"))+
  geom_line(aes(y=list.temp.min,color="NightTemp"))+
  scale_colour_manual(name='',values=c('DayTemp'='orange','NightTemp'='blue'))+ 
  labs(x="Date", y="Temperature (C)", title="Day and Night temperature in Helsinki, Finland")	

# foreca *************
# http://apitest.foreca.net/?lon=24.934&lat=60.1755&key=Dk5RbpMcvZ26JYt4VbZVlZ0hHA&format=json
#API call for 7 day weather forecast for Helsinki (see  for other calls)
api_call_2 <- "http://apitest.foreca.net/?lon=24.934&lat=60.1755&key=&format=json"
#add your own API key between ""
api_key_2 <- "Dk5RbpMcvZ26JYt4VbZVlZ0hHA"

#making the API call 1
hki_json_2 <- fromJSON(paste(api_call_2, api_key_2, sep=""))

#response is .json so we must flatten it to get a data frame
hki_7d <- flatten(as.data.frame(hki_json_2))
hki_7d <- cbind(hki_7d, do.call(rbind.data.frame, hki_7d$list.weather))
hki_7d$date <- seq(as.Date(Sys.Date()), by = "day", length.out = nrow(hki_7d))

#changing the datatype to character so we get the same axis labels as in the data frame
hki_7d$date <- as.character(hki_7d$date)

#making a graph
ggplot(hki_7d,aes(x=date, group=2))+
  geom_line(aes(y=list.temp.day, color="DayTemp"))+
  geom_line(aes(y=list.temp.min,color="NightTemp"))+
  scale_colour_manual(name='',values=c('DayTemp'='orange','NightTemp'='blue'))+ 
  labs(x="Date", y="Temperature (C)", title="Day and Night temperature in Helsinki, Finland")	

