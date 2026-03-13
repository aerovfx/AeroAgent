# 36 - Things to remember translated

---

When dealing with highly imbalanced data sets, use SMOTE.

The data augmentation method that generates synthetic samples for minority classes to balance

imbalanced data sets and improve model performance.

Neural networks benefit significantly from data normalization and preprocessing, especially

for categorical features.

Tools like Keras and Numpi are widely used for this purpose.

When handling massive data sets with complex operations, CDF and DASC-HUDF are your best

options, especially when computational performance is crucial.

For text-based AI tasks, Spacey excels in tasks like Named Entity Recognition and Tokenization.

Intuning transformer-based LLMs is critical for domain-specific tasks.

Ensuring outputs remain relevant and accurate, particularly for real-time applications.

XG Boost is a powerful and efficient implementation of the gradient-boosting machine algorithm designed

for speed and performance, and is widely used for structured or tabular data tasks, such

as classification and regression.

Data or pipeline parallelism is typically used when the data does not fit in a single

device.

Model parallelism is ideal for situations when the neural network is too big to fit in

a single device.

NGC, the Envidia catalog of GPU-excelerated AI models and SDKs, helps you infuse AI into

your applications.

The attention is all you need paper, presented a new, simple network architecture called

the Transformer, based solely on attention mechanisms, dispensing with recurrence and

convolutions entirely.

Summary of techniques?

Recursive feature elimination or RFE.

When you need to select important features based on the target variable while retaining

interpretability, pros preserves original features, cons, model specific and can be computationally

expensive for large data sets.

Feature, importance, using random forest or GBM, when you want to built-in automatic feature

selection with interpretability and high accuracy, pros.

Models large data sets efficiently and has built-in feature importance.

Cons may be more complex to interpret in deep trees, lasso or L1 regularization.

When you need to perform feature selection in a linear model with sparse features, pros,

simple and effective for linear problems.

Cons.

Only works well for linear relationships, PCA or principal component analysis.

When you need to reduce dimensionality but are less concerned with feature interpretability,

pros, reduces dimensions effectively, cons.

Transform features are less interpretable.