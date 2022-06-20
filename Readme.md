# R実行手順
d <-  “movie_14.csv”
datasum <- data.matrix(read.csv(d))
databar <- t(datasum)
source("pca.txt")
result_s <- pca(datasum[, -c(1,19)])

# 平均値（mean）
write.csv(result_s$mean, "mean.csv")
# 不偏分散値（variance）
write.csv(result_s$variance, "variance.csv")
# 標準偏差（standard deviation）
write.csv(result_s$standard.deviation, "standard.deviation.csv")
# 相関係数行列
write.csv(result_s$r, "r.csv")
# 固有値
write.csv(result_s$eval, "eval.csv")
# 寄与率
write.csv(result_s$contribution, "contribution.csv")
# 累積寄与率
write.csv(result_s$cum.contribution, "cum.contribution.csv")
# 主成分負荷量
write.csv(result_s$factor.loadings, "factor.loadings.csv")
# 主成分得点
write.csv(result_s$fs, "fs.csv")

source("mreg.txt", encoding = "utf-8")
data_fs1 <- data.matrix(read.csv("fs.csv")[c(2:i, i+1:n+1)])

data_fs2 <- data.matrix(read.csv(d)[1])
data_fs <- cbind(data_fs1, data_fs2)
result_j <- mreg(data_fs)
write.csv(result_j$Rs, "Rs.csv")
write.csv(result_j$anova, "anova.csv")
write.csv(result_j$result, "result.csv")

cdata <- data.matrix(read.csv(d))
cdata <- t(cdata)
hc <- hclust(dist(cdata), "ward.D2")
plot(hc, hang=-1)
dev.copy(png, file="cluster.png")
dev.off()
