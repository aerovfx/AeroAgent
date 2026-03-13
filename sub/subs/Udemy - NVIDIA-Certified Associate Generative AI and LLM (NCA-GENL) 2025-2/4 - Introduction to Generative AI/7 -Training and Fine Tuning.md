# 7 -Training and Fine Tuning translated

---

In this lecture, we cover model training and fine tuning within the scope of the certification exam.

Fine tuning, large language models or LLMs, transforms generic pre-trained models into highly specialized tools tailored for specific tasks.

By customizing these models, we enhance their performance, relevance and efficiency, unlocking their full potential for targeted applications.

Before we get into the detail of model pre-training and fine tuning, let's get a high level view of where pre-training and refining fit in to the overall development of a large language model.

LLMs undergo two main training phases, pre-training and fine-tuning.

First, let's talk about pre-training.

The purpose here is to teach the model general language patterns.

To do this, we use massive diverse data sets like Common Crawl and the Pile.

During the pre-training process, the model adjusts its internal weights or settings to predict the next word in any given context.

For example, training the model on the sun rises in the teachers the model to predict east.

Pre-trained models versus training from scratch. Pre-trained models. These models, trained on massive data sets, serve as a foundation for fine tuning.

They excel in general language understanding but require additional refinement for domain specific tasks.

For example, using a general GPT model and fine-tuning it for medical text analysis, training from scratch.

Building a model without pre-training is resource intensive, requiring vast amounts of data and computational power.

Fine-tuning pre-trained models is far more efficient and practical.

Now, let's move on to fine-tuning. The purpose of fine-tuning is to specialise the model for specific tasks or domains.

For this phase, we use smaller, focused data sets tailored to the task.

For instance, training on medical research papers for applications in healthcare.

Advanced fine-tuning methods ensure that the model retains its general knowledge while excelling in specialized areas.

Before we get into the strategies, tools and techniques of training and refining, let's review core aspects of large language models.

Once trained, LLMs generate text by predicting the next word or token based on input.

The process involves analysing the input sequence, assigning a probability score to potential next tokens and selecting the token with the highest probability.

For example, if the input is the weather today, is the model might predict sunny as the highest probability.

This process repeats iteratively, allowing the model to create text of any desired length.

The transformer is a groundbreaking neural network architecture that revolutionise natural language processing, NLP, by efficiently handling sequential data.

Introduced in the paper, attention is all you need. It overcame the limitations of traditional models like recurrent neural networks, RNNs, which struggled with long sequences due to issues like the Vanishing Gradient problem, leading to loss of earlier context.

The core innovation of the transformer is the attention mechanism, which enables the model to focus on relevant parts of a sentence or document, regardless of position.

This capability laid the foundation for advanced models like GPT-4, Claude and Lummer.

Originally designed as an encoder to Coda framework, the transformer processes input text through.

Encoder analyzes input and creates meaningful representations by identifying important elements.

Decoder converts these representations into output text, such as summaries or translations.

The encoder and decoder can function together or independently, providing flexibility for different tasks.

For instance, encoder only models transform text into vectors for tasks like classification.

Decoder only models, foundational to large language models, LLMs, generate coherent and context aware text outputs.

This versatile architecture underpins many of today's leading AI systems, setting new benchmarks for NLP capabilities.

As large language models scale, they develop unexpected capabilities known as emergent abilities.

These include summarizing long texts, solving basic arithmetic problems, and inferring relationships and context without explicit programming.

For example, GPT-4 can summarize an entire novel or identify trends in data sets tasks that go far beyond simple word prediction.

Scaling laws explain how a model's performance is influenced by key factors.

First, the number of parameters.

Parameters are the adjustable components of the model, and more parameters allow the model to learn intricate patterns.

For instance, GPT-4 has significantly more parameters than its predecessors enabling advanced reasoning.

Next, the training data set size.

A larger data set provides more opportunities for the model to learn diverse patterns.

Finally, compute power, measured in floating point operations per second, or flops.

Higher computational power allows the model to process data faster and more effectively, but it does require greater resources.

The context size of an LLM defines how much text it can process in a single pass.

It directly impacts the model's ability to handle complex inputs and maintain coherence.

For example, small models handle around 1000 tokens. On the other hand, GPT-3.5 can process up to 16,000 tokens.

Advanced models, like GPT-4, can handle up to 128,000 tokens.

Larger context sizes enable tasks like summarizing lengthy documents or understanding detailed conversations.

Now let's dive deeper into the options, strategies, and techniques of training and fine tuning.

Hyperparameters play a critical role in defining how a model learns and performs.

These are the tunable parameters that dictate the behavior of the training process, and directly influence the model's ability to generalize, optimize, and converge efficiently.

Here's a detailed breakdown of key hyperparameters and their impact.

These are important concepts for the exam.

One, learning rate. Learning rate governs the magnitude of weight updates during training based on the gradient of the loss function.

High learning rate results in faster learning, but risks overshooting the optimal point causing instability.

Low learning rate offers more stable convergence, but increases training time and risks getting stuck in local minima.

For example, a learning rate of 0.1 means weights are updated by 10% of the calculated gradient per step.

Practical tip. Use learning rate schedulers to dynamically adjust the learning rate during training.

Two, batch size.

Batch size is the number of samples processed before updating the model weights.

Small batch size leads to higher variance in weight updates, can lead to faster convergence, but noisier gradients.

Large batch size results in more stable updates, but requires more memory, and may generalize poorly.

For example, using a batch size of 32 balances speed and memory usage for most datasets.

Three, number of epochs.

Number of epochs is the total number of times the model processes the entire training dataset.

Two few epochs result in underfitting, as the model hasn't learned enough.

Too many epochs lead to overfitting, where the model memorizes the training data instead of generalizing.

Practical tip.

Use early stopping criteria to terminate training when performance on validation data stops improving.

Four, momentum.

Momentum accelerates gradient descent by incorporating a fraction of the past gradient direction into the current update.

It helps models escape local minima and smoothens oscillations in rugged optimization landscapes.

For example, momentum is often set to 0.9 in stochastic gradient descent, SGD, for effective learning.

Five, regularization parameters.

L2 regularization, also known as ridge, adds a penalty proportional to the sum of squared weights, reducing overfitting by discouraging large weights.

L1 regularization, also known as lasso, adds a penalty proportional to the sum of absolute weights, encouraging sparsity, making it useful for feature selection.

Six, dropout rate.

Dropout rate is the probability of dropping out neurons during training to prevent overfitting.

It regularizes the model by preventing reliance on specific neurons.

For example, a dropout rate of 0.5 randomly deactivates 50% of neurons in each layer during training.

Seven, weight initialization.

Weight initialization is the strategy for setting initial values for model weights.

Random initialization can lead to vanishing or exploding gradients.

Xavier or he initialization is optimized for specific activation functions like relu.

Proper initialization ensures faster convergence and avoids gradient-related issues.

Eight, optimizer.

The optimizer is the algorithm used to update model weights based on gradients.

Common choices include SGD, which is effective for large data sets but slower in convergence, add them,

which combines momentum and adaptive learning rates for faster and more stable training,

and RMS prop, which is well suited for recurrent neural networks, RNNs.

The optimizer significantly influences convergence speed and final performance.

Nine, activation functions.

Activation functions introduce non-linearity to the model, enabling it to learn complex patterns.

Types include relu, which is efficient and widely used for deep networks,

sigmoid, used for binary classification but prone to vanishing gradients,

and tan, which centers data around 0 but suffers from gradient saturation.

The choice of activation function affects gradient flow and learning efficiency.

Ten, early stopping.

Early stopping is a technique to halt training when validation performance stops improving,

preventing overfitting by stopping training at the optimal point.

Eleven, learning rate decay or scheduler.

Learning rate decay gradually reduces the learning rate during training, improving fine tuning and ensuring stable convergence.

For example, step decay reduces the learning rate by a fixed factor after every few epochs.

Twelve, feature engineering parameters.

Feature engineering parameters control pre-processing tasks like handling missing values,

normalization, and feature selection, enhancing data quality and significantly influencing model performance.

13, kernel for SVMs.

Kernel defines the mathematical function used to project data into higher-dimensional space.

Common kernels include linear, polynomial, and radial basis function, RBF.

Kernel choice determines how well support vector machines, SVMs, can separate complex data.

14, tree-based model parameters.

Max depth restricts the depth of decision trees, controlling model complexity.

Number of estimators in ensemble methods defines the number of trees used, such as in random forest or XG boost.

Learning rate and boosting methods adjusts how much each tree corrects errors from previous iterations.

Tuning hyperparameters is as much an art as it is a science, while automated tools like grid search,

ambasion, optimization, help understanding the underlying impact of each hyperparameter is crucial for making informed decisions.

By carefully balancing these parameters, you can create models that are both accurate and efficient, ready to tackle real world challenges.

Techniques for fine-tuning with Envidia Namo.

Nemo simplifies fine-tuning by offering a robust framework for customizing pre-trained LLMs.

For example, fine-tuning a conversational AI model for customer service tasks, ensuring responses are contextually relevant and industry specific.

Training optimization techniques.

Optimizing the training process ensures that models are both efficient and capable of handling large-scale tasks without excessive resource consumption.

Mixed Precision Training.

Reduces memory usage by using lower precision arithmetic, such as FP16 or FP8 instead of standard FP32.

Benefits.

Deploy larger networks with the same hardware resources or reduce memory requirements significantly.

Practical use case. Training a deep neural network for image recognition on GPUs with limited memory.

Gradient check pointing.

Stores only a subset of intermediate activations during the forward pass and recomputes them during the backward pass.

Benefits.

Reduces memory consumption at the cost of slightly increased computation time.

Practical use case.

Training massive transformer models like GPT-4 on memory constrained systems.

Operator fusion combines multiple computational operations into a single operation to minimize memory allocation and the number of intermediate results.

Benefits.

Enhance his efficiency and speeds up training.

Practical use case.

Optimizing GPU workloads for large-scale LLM training.

Low-rank adaptation or Laura.

Freezes pre-trained model weights and introduces trainable rank decomposition matrices into each transformer layer.

Benefits.

Reduces trainable parameters by up to 10,000 times compared to traditional fine tuning.

Decreases GPU memory usage by threefold without sacrificing quality.

Laura has shown superior performance on models like GPT-3 and Roberta with minimal computational overhead.

When to use fine tuning.

Fine tuning a model doesn't give it new knowledge but rather learns the writing style you are giving.

Some common use cases where fine tuning can improve results include setting the style, tone, format or other qualitative aspects.

Improving reliability at producing a desired output.

Correcting failures to follow complex prompts.

Handling many edge cases in specific ways.

And performing a new skill or task that's hard to articulate in a prompt.

Measuring.

Model accuracy in large language models or LLMs.

Evaluating the performance of large language models is a complex task due to their diverse applications.

Such as text generation, summarisation, translation and question answering.

Traditional accuracy metrics used in classification tasks are often inadequate for assessing LLMs.

Instead, a variety of task specific metrics are employed to gauge performance.

Here's an overview of the most commonly used methods.

One, perplexity or PPL.

Perplexity measures how well a model predicts a sequence of words reflecting the uncertainty in its predictions.

A lower perplexity indicates better fluency in generated text.

Ideal for tasks like text generation where linguistic fluency is critical.

Formula.

Perplexity equals E to the power of the negative sum of the log probabilities of the words divided by the total number of words.

Example.

Evaluating a chatbot's ability to produce grammatically correct and coherent sentences.

Two, blue or bilingual evaluation understudy.

Blue evaluates the similarity between generated text and reference text by analysing the precision of N-grams or sequences of words.

It is widely used for machine translation but also applies to summarisation and paraphrasing.

Comparing machine translated sentences to human translations for accuracy and fluency, key feature,

adjusts for brevity to prevent models from generating unnaturally short outputs.

Example.

Assessing the quality of translated text in multilingual chat applications.

Three, Rouge or recall-oriented understudy for gistening evaluation.

Rouge measures overlap between generated and reference text focusing on recall of N-grams.

It is especially effective for tasks like summarisation.

Types include Rouge N which measures overlap of N-grams, Rouge L which evaluates the longest common subsequence and Rouge W which weighs subsequences for relevance.

Evaluating the quality of generated summaries against human created summaries.

Example.

Using Rouge to determine the accuracy of automated news summarisation systems.

Four, exact match or EM.

Exact match measures how often the model's output matches the reference text word for word.

Frequently applied in question answering tasks where precise answers are critical.

Example.

In the squad benchmark EM evaluates whether the predicted answer is an exact match with the correct answer.

Five, F1 score.

F1 score is a metric that balances precision or correctness and recall or completeness using their harmonic mean.

Useful for tasks like question answering where partial correctness is still valuable.

Example.

Evaluating a model's ability to identify the correct entities in a passage with partial matches receiving partial credit.

Six, Human Evaluation.

Human Evaluation involves human review as assessing the quality of generated text based on fluency, coherence and relevance.

Essential for tasks requiring subjective judgement such as creative writing or open-ended chatbot conversations.

Criteria may include categories like grammatical correctness, coherence, relevance, creativity and overall user satisfaction.

Example.

Comparing user feedback on chatbot responses in customer service.

Seven, Winnegrad, Schema.

Challenge and Reasoning benchmarks.

Winnegrad, Schema Challenge.

Test the model's ability to understand context, ambiguity and common sense reasoning.

Evaluates advanced capabilities in reasoning such as handling nuanced language or logical scenarios.

Example.

Determining whether an AI can resolve ambiguous sentences like, the trophy doesn't fit in the suitcase because it's too big or small.

Eight, Task-specific metrics.

The question answering, use exact match and F1 score for precision and recall-based evaluations.

For summarisation, employ Rouge and Blue to compare generated and reference summaries.

The text generation, combine, Poplexity, BLEU and Human Evaluation to assess fluency, coherence and creativity.

Summary.

The accuracy and performance of LLMs are assessed through a variety of metrics tailored to specific tasks.

Poplexity evaluates language fluency.

BLEU and Rouge measure text, similarity for summarisation and translation.

Exact match and F1 score assess precision and recall in tasks like question answering.

Human Evaluation captures subjective quality metrics for tasks requiring creativity or nuance.

Choosing the appropriate metric depends on the task, ensuring that LLMs are evaluated holistically for their intended use cases.

Sample questions.

Which two elements of prompt engineering can make large language model outputs more aligned with the user's style or goals?

A. Providing a system or role prompt with explicit context.

B. Requesting the model to produce random nonsense.

C. Iteratively refining the prompt based on model responses.

D. Using the model's default configuration only.

Correct answers.

A. C. A system prompt sets the style, tone or role the model should adopt.

Iterative refinement means adjusting instructions after seeing results to align output.

Random nonsense or leaving the model at default reduce alignment.

Which two aspects are crucial to preventing overfitting on a small domain specific data set?

A. Using the entire huge model with no regularisation.

B. Early stopping using a validation set.

C. Data augmentation or synthetic examples.

D. Deploying on a single CPU.

Correct answers.

B. C. Explanation.

Early stopping halt training before memorising the data set.

Data augmentation expands the effective data set size.

Using the entire large model without regularisation can cause overfitting.

CPU deployment is unrelated.