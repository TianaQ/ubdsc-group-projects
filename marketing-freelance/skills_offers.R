skills_offers <- read.csv('skills_country_freq.csv', sep = '\t')
skills_mean <- read.csv('skills_country_mean.csv', sep = '\t')
skills_median <- read.csv('skills_country_median.csv', sep = '\t')

skills_df <- data.frame(skills = skills_offers$skills, offers = skills_offers$world_num, 
                   world_mean = skills_mean$mean, world_median = skills_median$median)
str(skills_df)

table(skills_df$offers > 200)
table(skills_df$offers > 200)/1710

skills_df$GRB_median <- skills_median$GBR
skills_df$IND_median <-skills_median$IND
skills_df$BGD_median <- skills_median$BGD
skills_df$PAK_median <- skills_median$PAK
skills_df$USA_median <- skills_median$USA
skills_df$KEN_median <- skills_median$KEN
skills_df$PHL_median <- skills_median$PHL
skills_df$ESP_median <- skills_median$ESP
skills_df$CAN_median <- skills_median$CAN

skills_df$GRB_offers <- skills_offers$GBR
skills_df$IND_offers <-skills_offers$IND
skills_df$BGD_offers <- skills_offers$BGD
skills_df$PAK_offers <- skills_offers$PAK
skills_df$USA_offers <- skills_offers$USA
skills_df$KEN_offers <- skills_offers$KEN
skills_df$PHL_offers <- skills_offers$PHL
skills_df$ESP_offers <- skills_offers$ESP
skills_df$CAN_offers <- skills_offers$CAN

skills_df <- skills_df[order(skills_df$offers, decreasing = TRUE), ]

write.csv(skills_df, file='skills_median_offers_top_countries.csv')