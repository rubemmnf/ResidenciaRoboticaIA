# FUN??O PARA TREINAMENTO DO MODELO DURANTE T ITERA??ES

perceptron <- function(X,Y,T,alpha){  
  
  
  N = nrow(X)  # NUMERO DE EXEMPLOS DE TREINAMENTO
  
  M = ncol(X)   
  
  # TRANSFORMAR DADOS DE TREINAMENTO PARA CONSIDERAR O BIAS COMO UM PESO
  
  X = cbind(X, rep(-1, N))
  
  # INICIALIA??O ALEATORIA DOS PESOS DA REDE COM VALORES ALEAT?RIOS ENTRE -1 E 1
  
  wt = as.matrix(runif(M+1,-1,1))
  
  list_sse = cbind()
  
  # CICLO DE APRENDIZADO
  
  for (t in 1:T){
    
    all_erros = cbind()
    
    for (j in 1:N){
      
      # EXEMPLO ATUAL 
      
      xj = X[j,]
      
      yj = Y[j]
      
      # CALCULO DA SOMA ACUMULADA DOS PESOS
      s = t(wt) %*% xj  
      
      # CALCULO DA SAIDA DO PECEPTRON COM FUN??O DE ATIVAÇÃO SIGMOID  
      fj = 1/(1+exp(-s))  
      
      # CALCULO DO ERRO
      ej = fj - yj   
      
      all_erros = cbind(all_erros,ej)
      
      # REGRA DELTA
      wt = wt - as.numeric(alpha*ej) * xj   
      
      
      
    } # TERMINO DO CICLO
    
    sse_t = sum(all_erros^2)
    writeLines(sprintf("Itera??o: %d. Erro: %.2f.",t,sse_t))
    
    
    list_sse = cbind(list_sse,sse_t)  # SOMA ERROs QUADRADOS BNA ITERACAO t
    
  }  # TERMINO DO APRENDIZADO
  
  
  return(list(modelo = wt, erros = list_sse, sse = list_sse[T]))
  
}  

# DADOS DE TREINAMENTO PARA  PORTA L?GICA 'AND'

X = as.matrix(diabetes[,1:8])

# X = scale(X) # Dificulta interpretação final

Y = diabetes$class

Y = as.factor(Y)

Y = as.numeric(Y) - 1

# TREINAMENTO DO MODELO DURANTE 20 CICLOS E TAXA DE 0.2

T = 200
alpha = 0.2

# SET INITIAL BEST SSE TO INF
best_sse <- Inf

# EXECUTE 20 RUNS OF PERCEPTRON
for(i in 1:20) {
  
  # RANDOM INITIALISATION OF THE DATA SET
  indices <- sample(1:nrow(features))
  
  # SET NUMBER OF ITERATIONS AND ALPHA
  T <- 200
  alpha <- 0.2
  
  # TRAIN MODEL
  modelo <- perceptron(X, Y, T, alpha)
  
  # IF CURRENT MODEL SSE IS BETTER THAN BEST SSE, REPLACE IT
  if(modelo$sse < best_sse){
    best_sse <- modelo$sse
    best_model <- modelo
  }
  
}

# THE BEST MODEL
best_model

# PLOT OF THE SSE FOR THE BEST MODEL
plot(1:T, best_model$erros, type = "l", xlab = "Iteration", ylab = "Sum of Square Errors")

# Best model = 
# $modelo
# [,1]
# [1,]  309.24845
# [2,]   30.68952
# [3,]  -87.92026
# [4,]  -45.44145
# [5,]   13.51487
# [6,]   32.33978
# [7,]  244.88576
# [8,]  -25.34795
# [9,] 1107.32890
# 
# $erros
# sse_t    sse_t sse_t sse_t
# [1,] 327.1825 334.0002   339   328
# sse_t sse_t    sse_t    sse_t
# [1,]   326   317 330.1162 325.9975
# sse_t sse_t    sse_t    sse_t
# [1,]   322   328 316.9999 326.9962
# sse_t   sse_t sse_t    sse_t
# [1,]   331 320.055   315 333.3032
# sse_t    sse_t   sse_t    sse_t
# [1,] 327.965 319.9976 327.015 313.9879
# sse_t    sse_t sse_t sse_t
# [1,]   335 328.2308   319   331
# sse_t    sse_t    sse_t sse_t
# [1,] 326.0003 317.2394 340.6182   341
# sse_t sse_t sse_t    sse_t
# [1,]   311   335   322 319.5226
# sse_t    sse_t sse_t sse_t
# [1,] 335.1132 338.0404   312   322
# sse_t sse_t sse_t    sse_t
# [1,] 330.9982   318   328 321.0026
# sse_t   sse_t    sse_t
# [1,] 333.5526 331.841 327.8275
# sse_t    sse_t sse_t sse_t
# [1,] 310.9845 318.9368   347   328
# sse_t    sse_t sse_t    sse_t
# [1,] 318.9992 323.9998   317 324.9998
# sse_t sse_t sse_t    sse_t
# [1,] 330.956   324   332 334.9999
# sse_t    sse_t sse_t    sse_t
# [1,]   336 329.9134   326 333.9941
# sse_t sse_t    sse_t sse_t
# [1,]   323   313 320.8873   324
# sse_t    sse_t sse_t    sse_t
# [1,] 340.9999 323.8043   321 328.7431
# sse_t    sse_t sse_t sse_t sse_t
# [1,]   319 328.0084   334   321   328
# sse_t sse_t    sse_t sse_t
# [1,] 317.8102   308 325.0048   316
# sse_t sse_t    sse_t sse_t
# [1,] 330.9997   322 312.0002   324
# sse_t    sse_t sse_t    sse_t
# [1,]   334 316.2959   346 324.0072
# sse_t    sse_t    sse_t    sse_t
# [1,]   312 329.9998 316.9999 330.9878
# sse_t    sse_t sse_t sse_t
# [1,] 321.9997 320.9995   329   330
# sse_t    sse_t    sse_t sse_t
# [1,]   314 312.0211 325.0095   317
# sse_t    sse_t    sse_t sse_t
# [1,]   318 331.9915 301.9391   313
# sse_t sse_t    sse_t  sse_t
# [1,] 301.9958   336 328.9963 316.92
# sse_t sse_t sse_t    sse_t sse_t
# [1,]   321   335   326 314.4791   324
# sse_t    sse_t sse_t sse_t
# [1,] 321.0001 317.4524   304   319
# sse_t    sse_t    sse_t
# [1,] 337.0002 323.2225 333.0193
# sse_t sse_t   sse_t    sse_t
# [1,] 321.9994   313 323.023 326.9115
# sse_t    sse_t    sse_t sse_t
# [1,] 333.9891 326.0004 316.7881   316
# sse_t    sse_t   sse_t
# [1,] 317.1905 328.7642 333.331
# sse_t sse_t sse_t    sse_t
# [1,] 309.9055   318   320 322.9998
# sse_t    sse_t    sse_t
# [1,] 327.5823 307.9934 325.4509
# sse_t sse_t    sse_t   sse_t
# [1,] 320.9882   317 319.9995 307.382
# sse_t    sse_t    sse_t    sse_t
# [1,]   319 315.9984 318.9988 322.0002
# sse_t    sse_t sse_t sse_t
# [1,] 330.0026 314.9988   297   328
# sse_t    sse_t sse_t    sse_t
# [1,]   316 327.9525   332 317.9423
# sse_t    sse_t sse_t    sse_t
# [1,] 327.0382 323.0011   344 314.0004
# sse_t    sse_t sse_t sse_t
# [1,] 326.0134 328.9623   322   331
# sse_t    sse_t sse_t    sse_t
# [1,] 310.998 314.9999 326.6 312.1649
# sse_t sse_t    sse_t    sse_t
# [1,] 312.1471   310 314.0002 332.8252
# sse_t    sse_t sse_t sse_t sse_t
# [1,]   322 312.2329   331   322   324
# sse_t    sse_t    sse_t sse_t
# [1,] 326.0299 318.0001 320.9998   324
# sse_t    sse_t sse_t    sse_t
# [1,] 317.0271 323.6214   328 318.9969
# sse_t    sse_t sse_t    sse_t
# [1,] 328.1077 322.8992   331 327.9978
# sse_t    sse_t sse_t    sse_t
# [1,] 327.8147 309.9669   331 322.9997
# sse_t sse_t sse_t    sse_t
# [1,]   325   335   323 318.9448
# sse_t    sse_t sse_t    sse_t
# [1,] 310.9242 315.9999   348 337.9938
# sse_t sse_t    sse_t sse_t
# [1,] 331.9996   326 322.1565   330
# sse_t
# [1,]   311
# 
# $sse
# [1] 311