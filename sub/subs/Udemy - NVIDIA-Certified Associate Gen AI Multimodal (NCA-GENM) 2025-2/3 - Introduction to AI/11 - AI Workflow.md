# 11 - AI Workflow translated

---

The AI workflow, often called the Machine Learning Workflow or Data Science Workflow, provides

a structured sequence for developing AI solutions.

It ensures systematic execution, documentation and effectiveness.

AI workflow typically has four fundamental steps.

Step 1.

Data Preparation

This step involves gathering, cleaning and pre-processing raw data to make it suitable

for AI models.

For example, in an image recognition project, data might include thousands of labeled images

of objects.

Tools like Nvidia Rapids can pre-process large data sets efficiently.

Consider Sarah, an ML engineer at a radiology clinic.

She uses Rapids and its Spark accelerator to pre-process X-rays and CT scans for training

an AI model to detect fractures and tumors.

Step 2.

Model Training

Model training involves feeding data into ML or DL models to identify patterns and relationships.

For instance, Sarah uses frameworks like TensorFlow or PyTorch integrated with Nvidia Rapids

for accelerated training on GPUs.

To optimize this compute-intensive phase, she employs mixed precision training, reducing

memory usage while maintaining accuracy.

Step 3.

Model Optimization

Optimization fine-tunes models for performance and efficiency.

Nvidia Tensor RT can be used to enhance inference performance as Sarah does for her clinic's

AI solution, ensuring quick and accurate diagnostics.

Step 4.

Deployment and inference

In the deployment phase, trained models make predictions on new data.

For example, Sarah uses Nvidia Triton inference server to deploy her image recognition model.

Triton simplifies IT and DevOps tasks like load balancing, ensuring scalability for real-world

usage.

Imagine a research institute focused on developing better diagnostic tools for detecting early-stage

cancers.

Here's how the AI workflow supports this effort, data preparation.

The institute collects and curates large data sets of histopathological images from

multiple sources such as public databases and collaborating hospitals.

Using Nvidia Rapids, researchers clean and normalize these data sets, ensuring consistent

resolution and format while anonymizing patient data for compliance with ethical standards.

Visual training, researchers use PyTorch and TensorFlow frameworks accelerated by Nvidia

GPUs to train a convolutional neural network.

The model is designed to classify tissue samples as malignant or benign.

Mixed precision training is employed to handle the massive data set efficiently.

Optimization

Once trained, the model is optimized using Nvidia Tensor RT, enhancing inference performance

by reducing latency and memory usage.

This ensures the model can process high-resolution images in real-time.

Deployment and inference

The model is deployed using Nvidia Triton inference server to enable seamless integration

with the institute's digital pathology systems.

Researchers can now analyze new tissue samples in real-time, providing rapid and accurate

results to support clinical trials and medical research.

This workflow enables the institute to enhance diagnostic accuracy by detecting subtle

patterns invisible to the human eye.

Reduce analysis time, accelerating the pace of research and discovery.

Support collaborative research efforts by sharing insights and models across institutions.

By combining AI-driven insights with traditional medical expertise, the institute is advancing

cancer research and improving patient outcomes.