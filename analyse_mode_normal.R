setwd("Documents/M2_BI/Bioinfo_struct/projet_structure/modeles3D/RaptorX_models/")


model1 = read.table(file = "601143_model1.localQuality.txt", skip = 2)
model2 = read.table(file = "601143_model2.localQuality.txt", skip = 2)
model3 = read.table(file = "601143_model3.localQuality.txt", skip = 2)
model4 = read.table(file = "601143_model4.localQuality.txt", skip = 2)
model5 = read.table(file = "601143_model5.localQuality.txt", skip = 2)

plot(model1$V3, type = "l", col = "red")
lines(model2$V3, col = "blue")
lines(model3$V3, col = "green")
lines(model4$V3, col = "black")
lines(model5$V3, col = "magenta")

mean(model1$V3)
mean(model2$V3)
mean(model3$V3)
mean(model4$V3)
mean(model5$V3)


library(stringr)


harmo = read.table("temp_anm.nmd.txt", skip = 2, sep = "\n", stringsAsFactors = FALSE)

harmo[8,]
vec_h8 = str_split(harmo[8,], " ")[[1]][-1]
for (num in 1:length(vec_h8)) {
  print(as.integer(vec_h8[num]))
}


