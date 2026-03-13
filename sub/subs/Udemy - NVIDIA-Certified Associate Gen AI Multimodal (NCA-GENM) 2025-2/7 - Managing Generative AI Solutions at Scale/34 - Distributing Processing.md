# 34 - Distributing Processing translated

---

Distributed training and distributed data parallelism, data or pipeline parallelism is typically

used when the data does not fit in a single device, like one GPU, for example.

With this technique, the dataset is sharded across multiple devices that contain a copy

of the model.

At the beginning of a training step, a mini-batch is distributed equally in a non-overlapping

manner across all the model replicas.

The replicas are then trained in parallel and model parameters are continuously synchronized

across devices.

Collective communication algorithms and specialized high performance computing or HPC, networking

infrastructures are commonly used to implement parameter synchronization and efficient interdevice

communication.

All reduce enables direct communication between devices.

A parameter server synchronizes local model replicas using push and pull semantics between

a set of dedicated parameter servers.

Using HPC infrastructure components such as elastic fabric adapter or EFA and algorithmic

optimizations, improve the performance of parameter server approaches.

The parameter server-based herring library by Amazon significantly outperformed the

all reduce based approaches and achieved state-of-the-art scaling efficiency of 85% for large

BERT model training across 2048 GPUs.

Distributed model parallelism.

Model parallelism is ideal for situations when the neural network is too big to fit in

a single device such as one GPU or to make the training process less memory intensive.

In model parallelism, the deep learning model is partitioned across multiple devices within

or across instances to effectively utilize the combined GPU memory of the training cluster

and store the entire model in a memory efficient fashion.

Pipeline parallelism.

Pipeline parallelism.

This is the set of model layers or operations across multiple devices and splits the training

mini batch into micro batches.

This creates an artificial pipeline where micro batches are scheduled for forward and backward

computations in an overlapped manner that minimizes device idling times.

Models of parallelism.

In this type of model parallelism, model weights, gradients and optimizer states are split

across devices.

In contrast to pipeline parallelism which keeps individual weights intact but partitions

the set of weights, tensor parallelism splits individual weights.

This typically involves distributed computation of specific operations, modules or layers of

the model.

Tensor parallelism is required in cases in which a single parameter consumes most of the GPU

memory or extremely large models such as GPT-4 that require partitioning over many instances.

This review, inference optimization.