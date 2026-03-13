# 4 -Training Optimization with NVIDIA Tools translated

---

Let's review training and optimization. Mixed Precision Training uses lower precision

maths to reduce CPU workload allowing for the deployment of larger networks with the same

amount of memory or reducing memory compared to single or double precision training.

The check pointing reduces memory consumption by storing only a subset of the intermediate

activations and recomputing them during the backward pass. Operator Fusion helps LLM practitioners

combine multiple operations into a single one, reducing memory allocation and the number

of intermediate results. Low rank adaptation or LLM freezes the pre-trained model weights

and injects trainable rank decomposition matrices into each layer of the transformer architecture,

greatly reducing the number of trainable parameters for downstream tasks compared to GPT-3

and 275 billion fine tuned with ADM. LLM can reduce the number of trainable parameters by 10,000

times and the GPU memory requirement by 3 times. LLM performs on par or better than fine tuning in

model quality on Roberta, Deberta, GPT-2 and GPT-3. Despite having fewer trainable parameters,

a higher training throughput and unlike adapters, no additional inference latency.