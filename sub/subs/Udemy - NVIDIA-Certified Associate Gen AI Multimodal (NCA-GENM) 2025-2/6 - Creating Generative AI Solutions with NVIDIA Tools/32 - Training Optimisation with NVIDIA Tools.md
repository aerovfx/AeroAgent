# 32 - Training Optimisation with NVIDIA Tools translated

---

Let's review training and optimization. Mix Precision Training uses lower precision

maths to reduce CPU workload allowing for the deployment of larger networks with the

same amount of memory or reducing memory compared to single or double precision training.

Gradient Checkpointing reduces memory consumption by storing only a subset of the intermediate

activations and recomputing them during the backward pass. Operator Fusion helps LLM practitioners

combine multiple operations into a single one, reducing memory allocation and the number of

intermediate results. Low Rank Adaptation or LLM freases the pre-trained model weights and

injects trainable rank decomposition matrices into each layer of the transformer architecture,

greatly reducing the number of trainable parameters for downstream tasks.

Compared to GPT-3 175 billion fine-tuned with Adam, LLM can reduce the number of trainable

parameters by 10,000 times and the GPU memory requirement by three times. LLM performs on-par

or better than fine-tuning in model quality on Roberta, Deberta, GPT-2 and GPT-3.

Despite having fewer trainable parameters, a higher training throughput and, unlike adapters,

no additional inference latency.