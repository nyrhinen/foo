#Connecting to dashDB on Bluemix
library(RJDBC)
library(ggplot2)

#Replace the following values with your own info in the code:
#<your_local_path_to_driver> - where you have saved the downloaded dashDB driver package
#<your_host_name> - see the Connect tab in your Bluemix dashDB for this info
#<your_username> - see the Connect tab in your Bluemix dashDB for this info
#<your_password> - see the Connect tab in your Bluemix dashDB for this info

#Connect to dashDB database
message("Creating database connection")
driverName <- "com.ibm.db2.jcc.DB2Driver"
pkgPath <- "<your_local_path_to_driver>/db2jcc4.jar"
#Default database name is BLUDB and the default port is 50000
connectionString <- "jdbc:db2://<your_host_name>:50000/BLUDB"
userName <- "<your_username>"
password <- "<your_password>"
drv <- JDBC(driverName, pkgPath, identifier.quote="'")
conn <- dbConnect(drv, connectionString, userName, password)

#get Twitter data with an SQL Query that selects the fields TS, TWEET and SENTIMENT from table TWEETS
#and orders the result by TS (timestamp) and limits the results to 100 rows
dataTwitter <- dbGetQuery(conn, "SELECT TS, TWEET, SENTIMENT FROM TWEETS ORDER BY TS DESC LIMIT 100")

#Making the sentiment variable discrete
#You can try to draw the graph first without running this code and see how it changes with this
dataTwitter$SENTIMENT <- as.factor(dataTwitter$SENTIMENT)

#Drawing a bar graph with ggplot() to see how the sentiment values are distributed
ggplot(dataTwitter, aes(x=SENTIMENT)) + geom_bar()

#Writing the data to a file
#Option 1: CSV-file
write.csv(dataTwitter, "twitterData.csv", row.names = F)

#Option 2: Excel-file
#You need to download the xlsx or openxlsx package first. Remember to use the library()-command to load the package for use!
write.xlsx(dataTwitter, "twitterData.xlsx", row.names = F)