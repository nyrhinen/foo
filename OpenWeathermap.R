library(ggplot2)
library(jsonlite)

#API call for 7 day weather forecast for Helsinki (see http://openweathermap.org/forecast5 for other calls)
api_call <- "http://api.openweathermap.org/data/2.5/forecast/daily?q=Helsinki&mode=json&units=metric&cnt=7&APPID="
#add your own API key between ""
api_key <- "<APIkey>"

#making the API call
hki_json <- fromJSON(paste(api_call, api_key, sep=""))

#response is .json so we must flatten it to get a data frame
hki_7d <- flatten(as.data.frame(hki_json))
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