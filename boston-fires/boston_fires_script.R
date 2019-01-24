#Boston Fire Incidents

# go to the directory with csv files
setwd('your_path_to/fire-data/')

# add file namles in the directory to the list
fire_files <- list.files()
 
# create an empty dataframe
fire_2017 <- data.frame()

# create a list of variables for subsetting
subset_names_list <- c("Incident.Number", "Exposure.Number", "Alarm.Date", "Alarm.Time", "Incident.Description", "Estimated.Property.Loss", "Estimated.Content.Loss", 
                "District", "Neighborhood", "Property.Description")

# function to get hour from time string
get_hour <- function(time_str) {
  ts = sapply(strsplit(time_str, ':'), function(xs) as.numeric(xs[1]));
  ts[is.na(ts)] <- time_str[is.na(ts)]
  return(ts)
}

# loop over the files in the list - for (loop range) {loop body}
for (fire_file in fire_files){
  print(fire_file)
  # read file to a dataframe
  fire_month <- read.csv(file=fire_file, header = TRUE, stringsAsFactors =FALSE, sep=",")
  
  # subset the dataframe by variable list
  fire_month <- fire_month[subset_names_list]
  
  # append the dataframe to fire_2017 dataframe by rows
  fire_2017 <- rbind(fire_2017, fire_month)
}

fire_2017$District <- factor(fire_2017$District)

# add Day.Of.Week column based on Alarm.Date column
fire_2017$Day.Of.Week <- weekdays(as.Date(fire_2017$Alarm.Date))
fire_2017$Day.Of.Week <- factor(fire_2017$Day.Of.Week)

#add Hour.Of.Day column based on Alarm.Time column
fire_2017$Hour.Of.Day <- get_hour(fire_2017$Alarm.Time)
fire_2017$Hour.Of.Day <- factor(fire_2017$Hour.Of.Day)

fire_2017$Incident.Description <- sapply(fire_2017$Incident.Description, trimws)
fire_2017$Incident.Description <- as.factor(fire_2017$Incident.Description)

fire_2017$Neighborhood <- sapply(fire_2017$Neighborhood, trimws)
fire_2017$Neighborhood <- as.factor(fire_2017$Neighborhood)

fire_2017$Property.Description <- sapply(fire_2017$Property.Description, trimws)
fire_2017$Property.Description <- as.factor(fire_2017$Property.Description)

# see the structure of fire_2017 dataframe
str(fire_2017)

# see the summary for each variable in fire_2017 dataframe
summary(fire_2017)


#---
# Top incidents causing property loss
fire_2017_prop_loss <- fire_2017[fire_2017$Estimated.Property.Loss >0, ]
sort(table(fire_2017_prop_loss$Incident.Description)[table(fire_2017_prop_loss$Incident.Description) > 0], decreasing = TRUE)

# Top incidents causing content loss
fire_2017_cont_loss <- fire_2017[fire_2017$Estimated.Content.Loss > 0, ]
sort(table(fire_2017_cont_loss$Incident.Description)[table(fire_2017_cont_loss$Incident.Description) > 0], decreasing = TRUE)

# Building fires by neighborhoods
fire_2017_buiding_fire <- fire_2017[fire_2017$Incident.Description == "Building fire",]
sort(table(fire_2017_buiding_fire$Neighborhood))

# Fire incidents in Boston
fire_2017_boston <- fire_2017[fire_2017$Neighborhood == "Boston",]
sort(table(fire_2017_boston$Incident.Description), decreasing = TRUE)

# Good intent calls
fire_2017_good_intent <- fire_2017[fire_2017$Incident.Description == "Good intent call, Other",]
summary(fire_2017_good_intent)
sort(table(fire_2017_good_intent$District))
#----


# write fire_2017 dataframe to a csv file for future use
write.csv(fire_2017, "boston_fire_incidents_2017.csv")


