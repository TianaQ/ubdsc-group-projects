df <- read.csv('csv/freelancers_loc_num_skills.csv')
summary(df$dollars_ph)

df_no_outliers <- subset(df, df$dollars_ph <= 66)

table(df_no_outliers$num_of_skills, df_no_outliers$dollars_ph)

write.table(table(df_no_outliers$dollars_ph, df_no_outliers$num_of_skills), file='csv/skills_pph_count.csv', sep = ',')

df_200 <- subset(df, df$dollars_ph <= 200)
write.table(table(df_200$dollars_ph, df_200$num_of_skills), file='csv/skills_pph_200_count.csv', sep = ',')

