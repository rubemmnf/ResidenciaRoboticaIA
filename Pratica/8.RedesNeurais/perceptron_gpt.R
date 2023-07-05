# LOAD CSV FILE
data <- diabetes

# CONVERT CLASS TO NUMERICAL
data$class <- ifelse(data$class == "tested_positive", 1, 0)

# SCALE FEATURES
features <- scale(data[,-ncol(data)])

# TARGETS
targets <- as.matrix(data$class)

# SET INITIAL BEST SSE TO INF
best_sse <- Inf

# EXECUTE 20 RUNS OF PERCEPTRON
for(i in 1:20) {
  
  # RANDOM INITIALISATION OF THE DATA SET
  indices <- sample(1:nrow(features))
  
  # SET NUMBER OF ITERATIONS AND ALPHA
  T <- 20
  alpha <- 0.2
  
  # TRAIN MODEL
  modelo <- perceptron(features[indices,], targets[indices], T, alpha)
  
  # IF CURRENT MODEL SSE IS BETTER THAN BEST SSE, REPLACE IT
  if(modelo$sse < best_sse){
    best_sse <- modelo$sse
    best_model <- modelo
  }
  
}

# THE BEST MODEL
best_model
best_sse

# PLOT OF THE SSE FOR THE BEST MODEL
plot(1:T, best_model$erros, type = "l", xlab = "Iteration", ylab = "Sum of Square Errors")
