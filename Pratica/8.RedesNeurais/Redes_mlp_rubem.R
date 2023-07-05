library("nnet")


####### EXPERIMENTOS COM BASE DIABETES

diabetes = as.data.frame(diabetes)
diabetes$class = as.factor(diabetes$class)

ind_train = sample(748,500)
ind_test = setdiff((1:748),ind_train)

dados_train = diabetes[ind_train,]
dados_test = diabetes[ind_test,] 

neuronios = 10
iteracoes = 10

acuracia_neuronio = c()
acuracia_todas = c()

for (n in 1:neuronios){

  for (i in 1:iteracoes){
    # Treinando a rede
    
    nn <- nnet(class ~ ., data = dados_train, size = n, maxit = 2000)
    
    # Calcular Acur?cia de teste
    
    preds_teste = predict(nn,dados_test,type = "class")
    
    matrix_conf_test = table(preds_teste, dados_test$class)
    
    acertos_teste = diag(as.matrix(matrix_conf_test))
    
    acc_teste = sum(acertos_teste)/length(preds_teste)
    
    acuracia_neuronio[i] = acc_teste
  }
  
  acuracia_todas[n] = mean(acuracia_neuronio)
}
acuracia_todas

acuracia_maxima = max(acuracia_todas)
acuracia_maxima

neuronio_max = which.max(acuracia_todas)
neuronio_max