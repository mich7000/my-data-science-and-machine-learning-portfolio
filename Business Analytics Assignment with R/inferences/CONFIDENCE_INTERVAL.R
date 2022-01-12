
# the data contains observation ages of individual in a parts of 
# East African continent.
data= read.csv('ages.csv')


# plot of age distribution
hist(x = data$ï..age_of_respondent)


mean_age = mean(data$ï..age_of_respondent)
std_age = sqrt(var(data$ï..age_of_respondent))
ttest = t.test(data$ï..age_of_respondent)

cat(' Average age: ', mean_age, '\n Standard deviation: ', std_age)

# using chebyshev's rule
cat('75% of the observation has ages between ', round(mean_age-2*std_age,2),' and ' , round(mean_age+2*std_age,2));
cat('88.89% of the observation has ages between ', round(mean_age-3*std_age,2),' and ' , round(mean_age+3*std_age,2))

qqnorm(data$ï..age_of_respondent); qqline(data$ï..age_of_respondent, col='red') # graphical test for normality
