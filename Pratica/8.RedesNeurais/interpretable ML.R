library(readr)
library(nnet)
library (e1071)
library(iml)
library(partykit)
library(rpart)
library(rpart.plot)


# separando dados de treino e teste

diabetes$class = as.factor(diabetes$class)

ind_train = sample(748,500)
ind_test = setdiff((1:748),ind_train)

dados_train = diabetes[ind_train,]
dados_test = diabetes[ind_test,] 

# treinando um modelo

model = nnet(class ~., data = dados_train, size = 5, maxit = 2000)

# verificando a qualidade do modelo nos dados de teste

preds = predict(model,dados_test,type = "class")

###### produzindo a matriz de confus?o
matrix_conf = table(preds, dados_test$class)

###### calculando a acuracia

acertos = diag(as.matrix(matrix_conf))
acc = sum(acertos)/length(preds)


# interpretando o modelo com o pacote IML

##### global surrogate

mod <- Predictor$new(model, data = dados_test)

dt <- TreeSurrogate$new(mod,maxdepth = 3)

# Plot the resulting leaf nodes
plot(dt)


##### PDP

##### criando um objeto IML com as predicoes do modeos 
mod <- Predictor$new(model, data = dados_test)

#### Criando um PDP com uma feature
eff <- FeatureEffect$new(mod, feature = "age", grid.size = 100,,method ="pdp")

eff$plot()

##### Criando um PDP com duas features

eff <- FeatureEffect$new(mod, feature = c("age","preg"), grid.size = 10, method ="pdp")

eff$plot()


##### LIME com pacote IML

lm = LocalModel$new(mod, x.interest = dados_test[2,-9],k=2)

lm$results
plot(lm)

##### Shapley com pacote IML

sp <- Shapley$new(mod, x.interest = dados_test[2,-9])
sp$results
plot(sp)







