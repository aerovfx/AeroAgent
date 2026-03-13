# 6 -AI Storage translated

---

In this lecture, we'll explore storage requirements for AI workloads, the types of storage file systems,

and the role of validated storage partners in AI data centers.

Why storage matters for AI?

Deep learning and AI thrive on vast amounts of data, and storage plays a vital role in ensuring data is accessible, manageable, and scalable.

For example, image classification, training data sets can include millions or billions of images.

Autonomous driving, a single 1080p camera generates half a terabyte of data in 30 minutes.

NLP tasks, billions of records such as emails and tweets are created daily requiring robust storage systems, requirements, high speed access,

storage must support fast read and write operations measured in IOPS and bandwidth.

Resiliency, data must be protected from corruption or loss with mechanisms for recovery.

Scalability, systems must accommodate growing data sets without compromising performance.

Accessibility, data should be easily retrievable and visible across the infrastructure for seamless use.

Questions to evaluate storage solutions. When designing a storage solution, consider.

How will the data be written and read? How frequently will it be accessed?

Can the storage system handle the required throughput? Who needs access and how will privacy be ensured?

How should failures and data retention be managed?

Types of storage systems for AI, local storage, pros, fast and simple, ideal for single node setups, cons, data cannot be shared across multiple applications or nodes.

Example, caching data locally for quick access during model training, network file systems, or NFS.

Provides a shared local like view of data across servers, uses POSIX for standardized data access, like open, read and close.

Example, NFS enables teams to collaboratively access data sets for training models.

In video partners include NetApp, Pure Storage and Dell.

Parallel and distributed file systems designed for high speed, scalable storage by distributing data across multiple storage units.

Example, AI applications that require massive parallel read and write operations like HPC simulations.

In video partners in this space are data direct networks, IBM and Weaker. Object storage scales to petabytes or even exabytes with no directory structure, files are accessed using REST APIs.

Example, cloud storage for archiving vast amounts of unstructured data like video streams.

Providers include Amazon S3, Google Cloud Storage and Microsoft Azure Blob, databases, whether SQL or no SQL.

Used for structured data requiring fast queries and updates, example, real-time data retrieval for recommendation engines.

Validated storage partners. Validated storage partners collaborate with Nvidia to ensure compatibility and optimize performance.

Key benefits include seamless integration which ensures smooth deployment with Nvidia systems like DGX Superpod and BasePod.

In hearts performance, as fine-tuned storage solutions, unlock higher IOPS and throughput.

Scalability. Meaning solutions grow with your data center needs, from terabytes to exabytes.

Security features protect data from unauthorized access with enterprise-grade safeguards, cost optimization with tailored solutions reducing the need for expensive customizations.

Check the Nvidia website for the latest additions to the Nvidia storage partner program.

Practical storage strategies. Multitired storage hierarchies. Combined fast local storage, such as RAM or SSD, for frequently accessed data with slower object storage for archiving.

For example, cache training data sets locally while storing historical data in the cloud. Caching for performance.

During deep learning training, data is accessed repeatedly in random order. Efficient caching can significantly improve read, write speeds.

For example, using local disk or RAM to cache frequently accessed data boosts training efficiency. Read and write optimization.

AI workloads often emphasize read performance, but as models grow, write performance becomes equally critical.

For example, large-scale NLP models require fast writes for intermediate results during training.

Case study. Storage in autonomous vehicles. In autonomous driving, sensors like cameras and lidar generate massive amounts of data.

A resilient, high-speed storage solution is crucial to process and analyze this data in real time.

Combining distributed file systems for speed and object storage for long-term archiving ensures efficient data management and accessibility.

Summary.

Storage is a foundational component of AI data centers. Understanding different storage systems and leveraging validated solutions enables organizations to achieve optimal performance, ensure data security and scalability and minimize deployment risks.

Choose storage based on workload requirements from NFS for shared environments to object storage for scalability.

Validated storage partners provide reliable, high-performance solutions tailored to Nvidia systems, optimize storage by prioritizing read, write speeds, caching and distributed architectures.

OK, let's practice some sample questions to get ourselves familiar with the Nvidia products and services.

A new security requirement mandates data encryption at rest for your model's training sets, which step meets compliance.

Is it A, storing data in plain text on the server, B, using encrypted storage, for example, disk-level encryption and secure keys,

C, only encrypting partial logs or D. No change needed for compliance. The correct answer is B, using encrypted storage and secure keys.

You are storing intermediate results of a large training job for reproducibility.

A good HPC practice is to A, save all data in local ephemeral storage, B, use a distributed file system or HPC grade parallel storage solution, C, rely on the developer's local laptop or D, discard logs to save space.

The correct answer is B, use a distributed file system or HPC grade parallel storage solution.