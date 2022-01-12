
# observations
obs1 = c(12.2,33.33, 111.11, 34.44, 122.3, 11.2,11.1, 56.2)
obs2= c(15, 67, 11, 141, 67, 81, 11, 22)

# scatterplot of the observations
plot(obs1, obs2)

# correlation between obs1 and obs2
cor(obs1, obs2)

# test for correlation between variables
# h0: correlation is equal to 0.
# reject h0 if pvalue< 0.05
#else h1: correlation is not equal to zero
cor.test(obs1, obs2) 

# test for diffrences in means
#null hypothesis: there is no diffrences in mean
#alpha= 0.05
# if pvalue < alpha, reject null hypothesis.
t.test(obs1, obs2)


# test for diffrences in means
#null hypothesis: there is no diffrences in mean
#alpha= 0.05
# if pvalue < alpha, reject null hypothesis.
var.test(obs1, obs2)
cat('vaiance of obs1: ',var(obs1))
cat('vaiance of obs2: ',var(obs2))

