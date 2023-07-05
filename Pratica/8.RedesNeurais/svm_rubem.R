library (e1071)


diabetes$class = as.factor(diabetes$class)

ind_train = sample(748,500)
ind_test = setdiff((1:748),ind_train)

dados_train = diabetes[ind_train,]
dados_test = diabetes[ind_test,] 

c_params = c(2^(-1), 2^0, 2^(+1),2^(+2),2^(+3))
gamma_params = c(2^(-2),2^(-1), 2^(+0),2^(+1),2^(+2))
resultados = matrix(0,length(c_params),(length(gamma_params)))

best_c = 0
best_gamma = 0
best_acc = 0

i = 1
for (cost in c_params) {
  j = 1
  for (gamma in gamma_params) {
    # train a classification model
    model <- svm(class ~., data=dados_train, cost = cost, gamma = gamma,type = "C-classification")
    
    # use the model on a test dataset
    preds = predict(model,dados_test)
    
    # produce the confusion matrix
    matrix_conf = table(preds, dados_test$class)
    
    # compute the accuracy
    
    acertos = diag(as.matrix(matrix_conf))
    acc = sum(acertos)/length(preds)
    acc
    
    resultados[i, j] = acc
    
    if (acc > best_acc){
      best_c = log(cost,base = 2)
      best_gamma = log(gamma, base = 2)
      best_acc = acc
      
      best_c
      best_gamma
      best_acc
    }
  j = j + 1
  }
i = i + 1
}

resultados
best_c
best_gamma
best_acc

heatmap(resultados, 
        Rowv = NA, 
        Colv = NA, 
        xlab = "gamma", 
        ylab = "C", 
        main = "Accuracy Variation (C and gamma)", 
        col = colorRampPalette(c("white", "blue"))(10))
