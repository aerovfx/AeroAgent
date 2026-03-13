# 3 -NVIDIA Reference Architectures translated

---

In this lecture, we'll explore the concept of reference architectures and their importance

in creating high-performance AI systems relevant to the cert exam.

We'll focus on the NVIDIA, DGX-BASE pod and DGX-Superpod reference architectures and review

practical design scenarios.

A reference architecture is a designed blueprint that outlines best practices for building

and implementing complex systems.

It provides a proven framework for achieving optimal performance while reducing the complexity

of system design.

In dense computing environments where multiple servers, networking fabrics, storage systems,

and management tools must work seamlessly together, reference architectures offer significant

advantages.

This optimization built on best of breed designs to maximize efficiency and reliability.

Reduced complexity simplifies planning by offering a prevalidated framework, customizability.

Provides a foundation that can be tailored to meet specific organizational needs, time

and cost savings, speeds up deployment by minimizing design and planning cycles.

DGX-BASE pod improves reliability and reduces risks through pre-tested configurations.

NVIDIA offers several reference architectures to support AI and high-performance computing

environments.

Two key examples are DGX-BASE pod designed to accelerate AI workloads with a scalable,

full-stack solution.

DGX-Superpod, a modular AI supercomputing infrastructure for large-scale deployments, ideal

for training large-language models like GPT-4.

The DGX-BASE pod is a prevalidated solution designed for efficient deployment and operation

of AI workloads.

It integrates NVIDIA hardware, networking, software, and storage components into a cohesive,

scalable system.

Let's explore its components and configurations.

DGX-B200 features 8 NVIDIA B200 GPUs delivering 72 pedophlops, FP-8 training, and 144 pedophlops

FP-4 inference performance.

Suitable for enterprise AI workloads, DGX-H100 includes 8 NVIDIA-H100 GPUs offering 32

pedophlops FP-8 performance for a versatile AI system.

Both systems support out-of-band management via a baseboard management controller for

remote monitoring.

Even when powered off, connect X7 adapters enable high-speed, infiniband, or ethernet connections.

Infiniband is typically used for compute networks, while ethernet is used for storage and management.

2M-19700, NDR-Infiniband switch with 400 GBP for compute networks, SN5600, ethernet switch

for GPU2 GPU fabrics, supporting up to 800GB per second, SN4600, handle storage and in-band

management with speeds up to 200GB per second, SN2201, provides out-of-band management with

speeds up to 100GB per second.

In-band storage systems from providers like NetApp and Pure Storage ensure high-speed

data access and scalability.

In-video, base command orchestrates workloads and manages the system.

In-video, AI Enterprise provides a robust MLOPS framework for streamlined AI development

and deployment.

The DGX base pod can support 2-16 DGX-H100 systems, or DGX-B200 systems, with NDR-200

GBP in-band connectivity for compute networks and ethernet for storage and management.

This scalable design ensures flexibility for diverse AI workloads.

The DGX Superpod represents the next generation of AI supercomputing.

It introduces scalable units for modular deployment, allowing for configurations of up to 127 nodes

with DGX-B200 or DGX-H100 systems.

This architecture includes Nvidia networking switches, software and storage, creating a

fully integrated platform for large-scale AI training and deployment in-band networking.

Ensures ultra-low latency and high bandwidth for massive data transfers.

AI Optimized software includes Nvidia AI Enterprise for accelerated development and deployment.

Use case, training large language models like GPT-4 in Enterprise and Cloud environments.

We need to be able to recognize key design patterns for the certification exam.

Let's review practical design scenarios.

An e-commerce company deploys a chatbot trained on FAQs to handle high traffic volumes

with minimal latency.

The Nvidia Triton Infraint Server enables dynamic batching and orchestration, ensuring

efficient resource use during peak periods.

A legal team uses iterative prompts to train a model for summarizing lengthy contracts.

Local prompts yielded overly general summaries, but refined prompts focused on key clauses,

improved output, accuracy and relevance.

A retail company deploys a voice chatbot for customer inquiries.

Nvidia Reaver enables speech recognition and language understanding for voice-based chatbots,

enhancing customer interaction.

The chatbot uses Reaver to deliver accurate real-time responses, improving user satisfaction.

A legal firm uses a Nemo-based summarizer to condense contracts into key clauses.

Summarizers condense lengthy texts into key points.

Nemo's fine-tuning capabilities make it suitable for industry-specific needs.

This automation saves time and ensures critical information is not overlooked.

An advisory company uses an NGC blueprint and a Nemo-pre-train model to create a service

chatbot.

The retail company uses Laura to fine-tune a Nemo-pre-train model to handle domain-specific

terminology and query patterns effectively.

A support chatbot retrieves solutions from a repository of user manuals.

Fine-tuning ensures responses are both accurate and contextually relevant.

A financial institution needs an LLM to provide investment advice.

Infrints uses trained models to generate outputs.

Infrints is where the model is deployed after any fine-tuning and made available to users.

Both training and inference requires significant compute resources.

With training and fine-tuning, being generally the most GPU-intensive processes, the pre-training

stage uses general financial documents while fine-tuning focuses on the institution's

proprietary data to ensure relevance.

Evaluation identifies areas for refinement to produce tailored, accurate advice.

The support chatbot retrieves solutions from a repository of user manuals.

Fine-tuning ensures responses are both accurate and contextually relevant.

Fine-tuning is the process of adapting a pre-train model to a specific task by training

it on a smaller domain-specific data set.

This approach is more efficient than training a model from scratch and allows for customisation

without losing the general knowledge of the base model.

Techniques such as low-rank adaptation, Laura are particularly useful as they enable fine-tuning

by updating only a small subset of the model's parameters.

This reduces the computational cost and storage requirements while maintaining high accuracy.

For the technical support chatbot, Laura can be used to fine-tune a Nemo pre-trained model

to handle domain-specific terminology and query patterns effectively.

This ensures that the chatbot can provide accurate and contextually relevant responses

to technical queries.

Beyond the DGX, BasePod and SuperPod Nvidia offers other reference architectures tailored

for specific applications Nvidia, AI Enterprise, reference architecture, optimised for general

purpose AI workloads in enterprise environments Cloudera, data platform reference architecture,

designed for big data analytics and machine learning workflows.

These architectures provide comprehensive guides including node configurations, network

topology and deployment best practices.

In video reference architectures provide a structured approach to building high performance

AI systems.

By leveraging Nvidia's DGX BasePod and SuperPod designs, organisations can reduce complexity,

accelerate deployment and achieve optimal performance.

Reference architectures can be found in the Nvidia NGC catalog.

Nvidia Blueprints reduce start-up time and improve efficiency, reliability and flexibility.

To illustrate the value of reference architectures, consider the following examples, Accelerated

Deployment.

A financial services firm uses the DGX BasePod reference architecture to deploy an AI-driven

fraud detection system.

The prevalidated design reduces deployment time by 40%.

Scalability for AI training.

A research institution leverages the DGX SuperPod to train large language models scaling

from 16 to 127 nodes seamlessly using Nvidia's modular SU design.

Reduced complexity.

A healthcare organisation deploys Nvidia AI Enterprise with reference architecture

to streamline medical image analysis, avoiding costly trial and error system configurations.

Okay, well done ninjas.

Now let's practice a few sample questions to help us prepare for answering questions in

the exam.

During distributed training communication overhead is high among GPUs.

A high speed interconnect solution recommended for HPC is A.

Wi-Fi B.

One GBPS Ethernet.

C.

Infiniband or NVLink.

D.

USB 2.0.

Okay, you know the correct answer to this one?

It's C.

Infiniband or NVLink.

Do you remember how those two provide very, very high bandwidth between GPUs and CPUs?

So way different from one GBPS Ethernet connection, much more powerful than that.

And of course Wi-Fi and USB 2 wouldn't work.

So just remember fast connectivity equals Infiniband or NVLink, especially with the DGX system.

Your e-commerce recommendation engine is overfitting user preferences, showing users only

items similar to their past choices, creating a filter bubble, which tactic best diversifies

recommendations.

Here are the choices, ignoring user preferences entirely, injecting random products at every

recommendation, introducing a coverage or diversity penalty in the loss function, and increasing

the batch size during training.

The correct answer is introducing a coverage or diversity penalty in the loss function.

This model is explicitly encouraged then to recommend a broader range of items.

And this tactic balances personalization with exploration, mitigating overfitting, which

is the key thing for those questions.

At break into filter bubble, while still considering user preferences.

So it's a good mix of scenarios to get that solution that we want.

That's the most effective way and that's why it's correct answer.

Now looking at ignoring user preferences entirely, now that's going to lead to relevant recommendations

that fail to really engage users.

And while it avoids overfitting, it negates the purpose of a recommendation engine, which

is to tailor response suggestions and responses based on user behavior and preferences.

Creating random products at every recommendation introduces randomness into recommendations which

can increase diversity, but risks recommending items that are irrelevant or unappealing.

So this approach can confuse users and reduce the overall effectiveness of the recommendation

engine, making it unsuitable as a primary solution.

Creating the batch size during training can stabilize gradient updates and improve generalization,

but does not directly address the diversity problem.

It focuses on training efficiency and model performance.

So more about optimization, not on diversifying recommendations or preventing filter bubbles.

When building a generative AI assistant for healthcare, which external verification step

is essential?

A, let the LLM guess all diagnoses.

B, add a rule based or professional oversight layer to confirm medical statements.

C, summarize disclaimers only.

D, force the user to accept incorrect answers.

Correct answer B.

Employing LLM in healthcare with HIPAA compliance and quick responses.

Here are the options.

Edge devices in hospitals, public cloud with shared resources, local desktops per facility,

an on-prem server with GPUs and encrypted storage.

The correct answer is on-prem server with GPUs and encrypted storage.

A healthcare organization must analyse sensitive patient data to predict disease risk.

Which principle helps ensure data privacy while still enabling insights.

Using synthetic data without privacy measures, collecting data from social media, adopting

differential privacy techniques and explicit patient consent and publishing patient data

publicly for open source collaboration.

The correct answer is adopting differential privacy techniques and explicit patient consent.

You notice that the summaries of legal documents generated by your LLM occasionally admit

disclaimers.

You fix this by A, telling the model explicitly which disclaimers to include.

B, lowering in temperature.

C, removing disclaimers from training.

D, doubling context length.

The correct answer is A, telling the model explicitly which disclaimers to include.

This is the correct answer because explicitly instructing the model to include specific

disclaimers ensures they are incorporated into the output.

Bromps that lack such details can lead to admissions.

So providing clear instructions resolves the issue directly by guiding the model's behaviour

during inference.

Using the temperature reduces randomness in the model's responses, making them more

deterministic.

However, this does not address the underlying issue of missing disclaimers since the problem

lies in the prompt's content, not in the variability of the output.

Removing disclaimers from training, while this approach is counterproductive as it would

make the model less likely to generate disclaimers, exasperating the problem instead of solving

it.

Training should aim to include disclaimers where relevant, not exclude them.

Increasing the context length does allow the model to process larger inputs, but it does

not solve the issue of missing disclaimers.

If the prompt does not explicitly instruct the model to include those.

Context length only impacts the amount of information the model can consider at once.