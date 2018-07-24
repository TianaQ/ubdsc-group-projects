skills_offers <- read.csv('csv/skills_country_offers.csv', sep = '\t')
skills_mean_pph <- read.csv('csv/skills_country_mean_pph.csv', sep = '\t')
skills_median_pph <- read.csv('csv/skills_country_median_pph.csv', sep = '\t')

skills_df <- data.frame(skills = skills_offers$skills, offers = skills_offers$w_offers, 
                   world_mean = skills_mean$w_mean_pph, world_median = skills_median$w_median_pph)
str(skills_df)

table(skills_df$offers > 200)
table(skills_df$offers > 200)/1710

skills_df$GRB_median_pph <- skills_median_pph$GBR
skills_df$IND_median_pph <- skills_median_pph$IND
skills_df$BGD_median_pph <- skills_median_pph$BGD
skills_df$PAK_median_pph <- skills_median_pph$PAK
skills_df$USA_median_pph <- skills_median_pph$USA
skills_df$KEN_median_pph <- skills_median_pph$KEN
skills_df$PHL_median_pph <- skills_median_pph$PHL
skills_df$ESP_median_pph <- skills_median_pph$ESP
skills_df$CAN_median_pph <- skills_median_pph$CAN

skills_df$GRB_offers <- skills_offers$GBR
skills_df$IND_offers <- skills_offers$IND
skills_df$BGD_offers <- skills_offers$BGD
skills_df$PAK_offers <- skills_offers$PAK
skills_df$USA_offers <- skills_offers$USA
skills_df$KEN_offers <- skills_offers$KEN
skills_df$PHL_offers <- skills_offers$PHL
skills_df$ESP_offers <- skills_offers$ESP
skills_df$CAN_offers <- skills_offers$CAN

skills_df <- skills_df[order(skills_df$offers, decreasing = TRUE), ]

write.csv(skills_df, file='csv/skills_top_countries_offers_median_pph.csv')