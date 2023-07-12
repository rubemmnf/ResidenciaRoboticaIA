library (e1071)
library(rpart)
library(rpart.plot)

diabetes$class = as.factor(diabetes$class)

ind_train = sample(748,500)
ind_test = setdiff((1:748),ind_train)

dados_train = diabetes[ind_train,]
dados_test = diabetes[ind_test,] 

# train a classification model
model <- svm(class ~.,data=dados_train,cost=10,gamma = 0.01,type = "C-classification")

# use the model on a test dataset
preds = predict(model,dados_test)

# produce the confusion matrix
matrix_conf = table(preds, dados_test$class)

# compute the accuracy

acertos = diag(as.matrix(matrix_conf))
acc = sum(acertos)/length(preds)
acc

novo_dados = dados_test[,-length(dados_test)]

novo_dados = cbind(novo_dados, preds)

dt = rpart(preds~., data = novo_dados)
rpart.plot(dt)
