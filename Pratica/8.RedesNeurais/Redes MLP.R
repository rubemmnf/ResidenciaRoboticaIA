
install.packages("nnet")
library("nnet")


# EXPERIMENTOS PARA MODELAGEM DA  PORTA LÓGICA 'XOR'

X = matrix(0,4,2)

X[1,] = c(0,0)
X[2,] = c(0,1)
X[3,] = c(1,0)
X[4,] = c(1,1)

Y =  c(0,1,1,0)

dataset = as.data.frame(cbind(X,Y)) 

dataset$Y = as.factor(dataset$Y)

nn <- nnet(Y ~ ., data = dataset, size = 2, maxit = 100)

nn$wts

preds = predict(nn,dataset)

preds = predict(nn,dataset,type ="class")


####### EXPERIMENTOS COM BASE DIABETES
 
 diabetes = as.data.frame(diabetes)
 diabetes$class = as.factor(diabetes$class)
 
 ind_train = sample(748,500)
 ind_test = setdiff((1:748),ind_train)
 
 dados_train = diabetes[ind_train,]
 dados_test = diabetes[ind_test,] 
 
 # Treinando a rede durante 500 iteracoes
 
 nn <- nnet(class ~ ., data = dados_train, size = 5, maxit = 500)
 
 
 # Calcular Acurácia de Treinamento

 preds = predict(nn,dados_train,type = "class")
 
 matrix_conf = table(preds, dados_train$class)
 
 acertos = diag(as.matrix(matrix_conf))
 
 acc_train = sum(acertos)/length(preds)
 
 
 # Calcular Acurácia de teste
 
 preds_teste = predict(nn,dados_test,type = "class")
 
 matrix_conf_test = table(preds_teste, dados_test$class)
 
 acertos_teste = diag(as.matrix(matrix_conf_test))
 
 acc_teste = sum(acertos_teste)/length(preds_teste)
 
 