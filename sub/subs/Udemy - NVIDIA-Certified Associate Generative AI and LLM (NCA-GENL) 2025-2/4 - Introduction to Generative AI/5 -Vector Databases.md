# 5 -Vector Databases translated

---

Common vector databases used with LLMs.

Vector databases are critical for enabling fast similarity searches

and efficient retrieval augmented generation workflows in LLM applications.

By understanding the strengths and use cases of these databases,

you can choose the best option for any given scenario.

Here are some commonly used vector databases and their key features

FICE, or Facebook AI's similarity search, is an open source library

developed by Meta, optimized for large-scale similarity search

and clustering of dense vectors.

Key features include being highly optimized for performance with GPU acceleration,

supporting approximate nearest neighbor searches for scalability,

and offering flexible indexing structures, such as inverted file,

hierarchical navigable small world, and flattened disease.

Use cases for FICE include large-scale semantic search,

recommendation systems, and retrieval augmented generation applications.

Why use FICE?

It's ideal for high-performance, large-scale environments where GPU acceleration is needed.

Pinecone is a fully managed vector database as a service designed for real-time similarity search,

and AI applications.

Key features include high availability with cloud-based deployment,

built-in support for versioning and metadata filtering,

and the ability to scale seamlessly with demand,

making it suitable for production workloads.

Use cases for Pinecone include real-time personalization, e-commerce recommendations,

and chatbots.

Why use Pinecone is great for teams that prioritize ease of deployment

and need a scalable managed solution.

Weeve8

It's an open-source, schema-based vector database designed for integrating unstructured data

with semantic search capabilities.

It offers built-in support for hybrid search,

which means it combines both vector and keyword search.

It also has native integration with models from OpenAI, CoHeA, and HuggingFace.

This makes it incredibly versatile for various applications.

Another important aspect is its metadata-driven, filtering, and contextual retrieval,

which can be quite useful in many scenarios.

So what are the use cases?

You can use Weeve8 for knowledge graph construction, contextual search in applications,

and even semantic document search.

Why should you use Weeve8?

It's ideal for combining metadata-rich queries with semantic search for both structured and unstructured data.

Milvus

An open-source vector database optimized for high-performance similarity search and machine learning applications.

Key features include support for billions of vectors with distributed storage,

integration with ANN search algorithms like HNSW and IVF,

an easy integration with popular ML tools such as TensorFlow and PyTorch.

Use cases range from image, video, and document retrieval in AI pipelines.

Why use Milvus?

It's excellent for large-scale, high-throughput applications requiring integration with machine learning workflows.

VESPA, a versatile search engine that supports vector search alongside traditional full-text search.

Key features combine approximate nearest-nabour search with advanced filtering and ranking,

support for large-scale data sets with hybrid search capabilities,

and high customization for specific business needs.

Use cases include e-commerce search, recommendation engines, and multimedia search.

Why use VESPA?

It's suitable for applications requiring both traditional search and vector similarity in one system.

QDRADT, an open-source cloud-ready vector search engine optimized for semantic search and similarity matching.

Key features include a restful API for easy integration support for metadata-based filtering and payload storage,

alongside vectors and scalability across distributed systems.

Use cases encompass content-based search customer support chatbots and multimedia retrieval.

Why use QDRADT?

It's ideal for developers looking for a simple-to-deploy open-source solution.

Chroma, a lightweight developer-friendly open-source vector database built for LLM-based applications.

Key features include tight integration with RAAG pipelines and frameworks like Langchain,

a focus on simplicity and fast prototyping and support for metadata filtering and vector storage.

Use cases involve prototyping RAAG workflows, chatbot development, and interactive search systems.

Why use Chroma?

It's perfect for quick integration and prototyping in LLM-based applications.

Sample questions.

Storing large embeddings for semantic search is best done in.

A, a standard relational DB with indexing on text columns, B, a specialized vector database like FAS,

Milvus, Pinecon, C, CSV files, D, Key value store for numeric IDs, correct answer, B,

use a specialist database for storing embeddings.

What would be the best combination of tools for creating a semantic search solution?

A, Spacey and FICE vector database, B, NLTK and SQLite, C, Skykit Learn as SQL Alchemy, D, Numpi and Pandas only.

The correct answer is A, combining Spacey, the Python library with FACE, a robust vector storage database.

Which two design aspects are crucial when storing large embeddings for semantic search across multiple GPUs?

A, using a vector database that supports GPU-based indexing or search, B, storing embeddings in CSV files only.

C, Sharding the vector data across GPUs or nodes for parallel search, D, converting embeddings to text strings.

Correct answers are A and C. This is a tough question as it has multiple options.

So firstly, after the lecture we've just done, remember a vector database specialized for embeddings is crucial in this type of scenario.

Now the second option is a little more difficult. Sharding the data ensures parallel search.

So that's something that we would often want in this type of scenario.

Using CSV files or string conversions can offer a hamper performance and functionality so D would not be an option.

You want to store billions of text embeddings for semantic search across multiple GPUs.

Which specialized database type is recommended.

A, Traditional relational DB, B, Key Value Store with CPU indexing. C, Vector Database Optimized for Embeddings, D, CSV files on disk.

Correct answer is C. Vector databases are optimized for storing vector values and can be accessed from multiple GPUs perfect for the scenario.