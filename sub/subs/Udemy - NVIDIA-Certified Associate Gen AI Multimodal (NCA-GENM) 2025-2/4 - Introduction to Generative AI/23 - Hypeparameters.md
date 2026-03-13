# 23 - Hypeparameters translated

---

Now, let's review key hyperparameters. The learning rate controls how much to adjust model

weights during training after each update based on the calculated error. It affects the

speed and stability of training. A high learning rate can lead to overshooting, while a low

rate can slow down convergence. Batch size refers to the number of training samples processed

before updating the model's weights. A small batch size leads to more frequent updates

and more variance in weight updates, while a large batch size results in more stable

updates. But may require more memory. Batching inference is used when high throughput is required.

Hardware resources need optimization, or cost savings are important. It processes multiple

requests together, improving efficiency, but potentially introducing slight latency. This

is particularly useful in real-time applications, like recommendation systems. The number of

epochs is the number of complete passes through the entire training data set. A higher number

of epochs allows the model to learn better, but may risk overfitting if too many epochs

are used. Momentum helps accelerate gradient descent by smoothing out updates using past

gradient information to determine the current direction. It helps in faster convergence

and prevents oscillations, especially in complex optimization landscapes. Regularization

parameters include L2 regularization, which adds a penalty proportional to the sum of

squared weights to the loss function, preventing large weights and reducing overfitting by

keeping the weights small. L1 regularization adds a penalty proportional to the sum of absolute

weights, encouraging sparsity and driving some weights to zero, leading to sparse models useful

for feature selection. The dropout rate is the probability of dropping out neurons in a neural

network during training to prevent overfitting. It helps regularize the model by preventing

co-adaptation of neurons. Weight initialization determines how the initial weights of the model are set

such as random, Xavier or he initialization. Proper initialization helps speed up convergence and

avoid issues like vanishing or exploding gradients. The optimizer is the algorithm used to update

model weights based on gradients such as SGD, Adam or RMS prop. It determines how effectively the

model navigates the error surface and converges to an optimal solution. The activation function defines

the nonlinear transformation applied to neurons output like re-LU, sigmoid or TANH. It affects how

the model captures nonlinear patterns and influences gradient flow during back propagation.

Early stopping criteria is a condition to stop training when the model's performance

on a validation set stops improving, preventing overfitting. Learning rate decay reduces the

learning rate over time or after specific conditions are met, helping the model converge more slowly

as training progresses and improving fine tuning near the end of training. Feature engineering

parameters include those related to pre-processing like handling missing values, normalization,

feature selection or creation. They affect how well the model learns patterns in the data and

can significantly improve model performance. The kernel for SVMs defines the function used to

project data into higher dimensional space for nonlinear classification affecting how well support

vector machines separate data in complex feature spaces. Tree-based model parameters for models like

random forest or XG boost include max depth which controls the depth of each decision tree and

impacts model complexity and risk of overfitting. The number of estimators refers to the number of

trees in the ensemble affecting stability and generalization. The learning rate for boosting

methods controls how much each new tree corrects the errors of the previous trees.