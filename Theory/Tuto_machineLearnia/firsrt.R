library(tidyverse)
library(palmerpenguins)
library(ggthemes)
ggplot(penguins,aes(x=species))+geom_bar()
ggplot(penguins,aes(x=fct_infreq(species)))+geom_bar()
ggplot(penguins,aes(x=body_mass_g))+geom_histogram(binwidth = 200)
ggplot(penguins, aes(x=flipper_length_mm,y=body_mass_g))+
  geom_point(aes(color=bill_depth_mm))+geom_smooth(method = "loess")
ggplot(penguins, aes(x = body_mass_g)) +geom_histogram(binwidth = 200)

ggplot(penguins, aes(x = body_mass_g))+geom_density()
ggplot(penguins, aes(x = body_mass_g)) +
geom_histogram(bins = 200)
ggplot(penguins, aes(y = species))+geom_bar()

ggplot(penguins, aes(x = species)) +
  geom_bar(color = "red")

ggplot(penguins, aes(x = species)) +
  geom_bar(fill = "red")
ggplot(diamonds,aes(x=carat))+geom_histogram(binwidth = 0.1)
ggplot(penguins,aes(x=body_mass_g,color=species, fill = species)) + geom_density(alpha = 0.5)
mpg
ggplot(mpg,aes(x=hwy,y=displ,color=cty))+geom_point(aes(size=cty))
ggplot(penguins, aes(x = island, fill = species)) +
  geom_bar(position = "fill")
ggplot(penguins, aes(x = species, fill = island)) +
  geom_bar(position = "fill")
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point()
ggsave(filename = "penguin-plot.png")
ggplot(mpg, aes(x = class)) +
  geom_bar()
ggplot(mpg, aes(x = cty, y = hwy)) +
  geom_point()
ggsave("mpg-plot.pdf")

ggplot(penguins, aes(x=flipper_length_mm,y=body_mass_g))+
  geom_point(aes(color=bill_depth_mm))+geom_smooth(method = "lm")
# creation d'un vecteur de nombres premiers
primes <- c(2,3)

