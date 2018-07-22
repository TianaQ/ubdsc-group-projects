df <- read.csv('freelancers_num_skills.csv')
par(cex = 0.8) #font size
hist(df$num_of_skills, main = '', labels = TRUE, col='gray', ylim=c(0, 2500), 
     xlab = 'Skills per person', xlim=c(0, 20), breaks = seq(0, 19, by = 1), 
     right = FALSE, axes = FALSE)
axis(1, at=seq(0, 19, by=1), labels = seq(0, 19, by=1))
axis(2, at = seq(0, 2500, by=500))

summary(df$num_of_skills)

nine_skills <- subset(df, df$num_of_skills == 9)
fourteen_skills <- subset(df, df$num_of_skills == 14)

summary(nine_skills$dollars_ph)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 8.00   10.00   20.00   26.58   33.00  850.00
# outliers > 33 + 1.5*(33 - 10) = 67.5
table(nine_skills$dollars_ph > 67.5) 
# FALSE  TRUE // outliers - 3.9% 
# 2215    89  

summary(fourteen_skills$dollars_ph)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 8.00   14.00   24.00   29.43   40.00  331.00
# outliers > 40 + 1.5*(40 - 14) = 79
table(fourteen_skills$dollars_ph > 79) 
# FALSE  TRUE // outliers - 2.8% 
# 1506    43

sd(nine_skills$dollars_ph)
# 33.94468
sd(fourteen_skills$dollars_ph)
# 24.07466


nine_no_outliers <- subset(nine_skills, nine_skills$dollars_ph <= 67.5)
fourteen_no_outliers <- subset(fourteen_skills, fourteen_skills$dollars_ph <= 79)
hist(nine_no_outliers$dollars_ph, xlab ='usd per hour', xlim = c(0, 80), ylim = c(0, 700), col = 'gray', main = '')
hist(fourteen_no_outliers$dollars_ph, xlab ='usd per hour', xlim = c(0, 80), ylim = c(0, 700), col = 'red', main = '')



