# 22 - Prompt Engineering translated

---

Prompt Engineering is a critical process in refining the behaviour of large language models.

We need to be able to identify and select prompt engineering techniques for the third exam.

Unlike fine tuning, which adjusts the model's weights, prompt engineering focuses on crafting inputs that guide the model effectively.

This approach is particularly valuable in scenarios where the LLM must deliver consistent, relevant and contextually accurate outputs across diverse use cases.

By carefully crafting prompts, engineers can guide the LLM to produce more accurate and tailored responses, enhancing its performance without the need for extensive model retraining.

This flexibility makes prompt engineering an essential skill in the AI toolbox.

Core principles of prompt engineering, clarity and specificity.

Clearly articulate the task with unambiguous instructions when writing a prompt for generating customer service emails, for example,

ensure you specify the tone and language requirements in the prompt.

For example, compose a polite and empathetic response to a customer complaint using phrases like,

we sincerely apologise and we value your feedback.

Contextual guidance. Provide sufficient background information to enable the model to generate relevant responses.

Iterative refinement. Start with a broad prompt and refine based on the output, adding constraints or examples as needed for concise technical explanations begin with.

Explain the functionality of an API in simple terms.

Refine to. Explain the functionality of the API in 50 words, focusing on its core features and benefits.

Explosive constraints. Use word limits, specific formats or instructions to constrain length and style.

For example, summarize this research article in three sentences focusing on the main findings, prompt engineering strategies, iterative refinement, improving the accuracy of technical troubleshooting responses,

approach, start with a broad prompt and refine iteratively.

Initial prompt. Help a user troubleshoot a connectivity issue. Refined prompt. Guide the user in troubleshooting a Wi-Fi connectivity issue by checking router settings, verifying device connections and restarting the modem in three concise steps.

Few shot prompting drafting, empathetic customer service emails.

Approach. Provide examples of desired outputs. Respond to a customer complaint using the tone of the following examples.

Chain of thought prompting. Summarizing complex legal documents. Approach. Encourage step-by-step reasoning.

Summarize the key clauses of this contract step-by-step, focusing on payment terms, confidentiality and termination conditions.

Dynamic prompts. Generating specific product descriptions for an e-commerce website. Approach. Taylor the prompt. Using structured inputs.

Create a product description for the following item. Product. Noise cancelling headphones. Features. Over-eared design.

40-hour battery life. Bluetooth connectivity. Target audience. Frequent travelers seeking comfort. An immersive sound.

Instructional prompts. Drafting precise legal clauses. Approach. Include detailed instructions in the prompt.

Draft a non-compete clause for an employment contract. Use precise legal terms. Limit the duration to 12 months.

And specify the geographical region as the United States.

Real-world scenarios and solutions. Scenario one. Balancing empathy and professionalism in customer service emails. Problem. Responses are overly formal and lack warmth.

Composal solutions include specific adjectives and phrases that convey empathy. Our prompts should be. Compose a customer service email that is both polite and empathetic. Use phrases like. We sincerely regret any inconvenience. And your satisfaction is our top priority.

Scenario two. Generating concise technical explanations. Problem. Outputs of a boss and lack precision.

Solution. Refined prompts iteratively. Initial prompt. Explain how this API works. Refined prompt. In 50 words or less, explain the core functionality of this API. Focusing on key features.

Impact. More concise and user-friendly outputs. Scenario three. Draft in contextually relevant legal documents. Problem. Irrelevant clauses and excessive legal jargon.

Solution. Use dynamic prompts with detailed client context. Draft a lease agreement clause for a commercial property. Include terms for early termination, maintenance responsibilities and rent escalation.

Zero-shot prompting involves directly instructing the model to perform a task without any prior examples of the desired output.

Zero-shot prompting is suitable for tasks where the model's base training suffices, such as straightforward summaries or definitions.

The prompt provides a clear description of the task, but relies entirely on the model's pre-trained knowledge. Benefits. Quick. Useful for a broad range of tasks.

Leveraging the model's general understanding. Reduces reliance on domain-specific data or examples. Ideal for simple and direct tasks such as factual question answering.

For example, what is the capital of France? One-shot prompting provides the model with a single example of the desired input output pair.

This helps the model align its response more closely with the intended format or tone. Benefits. Adds context without overloading the prompt. Improves performance for tasks requiring basic structure or style guidance.

Maintains simplicity while offering better alignment. Good for tasks like generating responses in a specific style or format.

Helpful when a single example suffices to clarify the desired behavior, such as writing a formal letter, few-shot prompting includes multiple examples within the prompt to help the model understand patterns or context.

These examples serve as a mini-training session within the prompt. Benefits. Provide strong guidance by showing clear patterns.

Enhance accuracy for domain-specific tasks or nuanced outputs. Reduces the need for fine-tuning by leveraging in-context learning.

Few-shot prompting is good for tasks requiring nuanced understanding such as categorization, dialogue creation or technical summaries. Useful for generating consistent and high-quality outputs.

Chain of thought. This technique encourages the model to provide step-by-step reasoning, allowing it to break down complex problems or decisions into smaller logical steps. Benefits. Improves the model's performance on reasoning-intensive tasks.

Makes outputs more interpretable by revealing the logic behind them. Enhance accuracy by avoiding shortcuts in problem-solving.

It's ideal for tasks involving multi-step reasoning such as math problems, troubleshooting or ethical decision-making.

Iterative prompt refinement. This involves starting with a broad or general prompt and iteratively refining it based on the model's outputs, adding constraints or clarifications as needed. Benefits.

It allows continuous improvement to align outputs with specific needs, avoids overloading the initial prompt with unnecessary details, provides flexibility to address unexpected model behaviors, good when the initial results are suboptimal, or the task is complex and requires iterative adjustment, useful for generating summaries, improving tone or refining technical content.

Role prompting for frames. The model is a specific role to guide its behavior and tone, e.g. teacher, customer service agent or legal assistant.

This context helps the model adopt the desired persona. Benefits. Makes outputs. More relevant and aligned with the intended purpose. Enhance's tone consistency for specific professional or creative tasks.

Simplifies the prompt while focusing on role-specific behavior. Role prompting is good for task requiring domain-specific expertise or role-specific tone such as creating legal clauses, answering customer queries or providing educational content.

Example. Prompt. You are a financial advisor. Respond to the following query with professional advice. What is the best way to save for retirement?

Instruction-based prompting provides explicit detailed instructions about what the model should do, leaving minimal room for ambiguity. Benefits. Ensures clear and predictable outputs by explicitly defining the task and constraints, reduces variance in outputs, particularly useful for structured tasks.

When to use. Instruction-based prompting is good for tasks requiring adherence to strict guidelines such as formatting specific structures or constrained outputs.

Instruction-based prompting modifies or adjust prompts dynamically based on input context to guide the model's behavior. Benefits. Enables adaptability to varied inputs and use cases. Improves relevance and output quality for diverse scenarios.

Dynamic prompting is great for tasks with variable inputs such as chatbots handling multi-topic conversations or generating personalized content. Style and tone control embeds instructions or examples in the prompt to guide the model's tone, style or formality level. Benefits. Ensures alignment with brand voice or audience expectations. Enables control over tone consistency across outputs.

Style and tone control is crucial when tone matters such as empathetic customer support, emails or engaging marketing copy.

One to many. Shock. Prompting demonstrates multiple possible outputs for a single input within a single prompt showcasing varied response styles or tones. Benefits. Trains the model to adapt to different styles, tones or sentiments.

Provides flexibility in scenarios requiring varied responses. Good for tasks like generating responses based on sentiment or tailoring outputs to different audiences.

Choosing the best technique. Zero shot and one shot are best for simplicity and low stakes tasks. Few shot and chain of thought excel for nuanced reasoning heavy tasks.

Role and style prompting are ideal for tone specific tasks. Iterative refinement and dynamic prompting are great for refining and personalizing outputs.

Metrics for prompt effectiveness. To ensure prompt engineering efforts yield measurable improvements evaluate the outputs using these metrics.

Relevance. Does the response address the input query effectively precision are the outputs accurate and contextually correct? Consiceness. Does the output avoid unnecessary verbosity?

Adaptability. Does the model adjust appropriately based on the prompt? Safety. Is the content free of hallucinations or incorrect information? Summary.

Through Iterative refinement, domain specific constraints and continuous feedback loops, LLMs can be adapted to diverse real world scenarios with precision and reliability.

Embracing these strategies empowers developers to deploy smarter, safer and more responsive AI solutions.

Prompt engineering is an indispensable skill for refining and optimizing LLM behavior. By applying strategies like iterative refinement, few shot prompting, dynamic prompts and chain of thought reasoning, you can guide LLMs to generate precise, contextually relevant and task specific outputs.

When iteratively refining prompts for a generative AI model, which strategy ensures the model aligns better with your intentions?

A. Start with a highly detailed prompt immediately. B. Keep prompts extremely concise from the start. C. Compare multiple outputs from the same prompt. D. Begin broadly and add specific instructions based on output.

Answer is D. An iterative approach starting broad and then refining helps pinpoint needed clarifications so the model better matches the desired output.

You want to ensure that each tweak to the prompt pushes the model closer to your desired style of polite and empathetic.

After conducting an A-B test on prompt strategies for a chatbot, results show only slight differences. How can you refine the test for more actionable insights?

A. Use identical prompts but change model architecture. B. Increase use account without changing prompts. C. Introduce a third prompt. Blanding elements from the first two. D.

Deploy both prompts in production and let model pick.

Find tuning a generative model to generate polite and empathetic emails. The model is too formal.

Next best approach in prompt engineering? A. Make prompt more vague to allow creativity? B. Provide explicit adjectives, phrases for warmth. C. Increase the model's context window. D. Decrease model size.

Answer is B, including specific tone or style instructions. E.G. Warm. Empathetic. Or using synonyms that reflect informality, steers outputs toward that style.

Your model categorizes support emails. It struggles with jargon. Best fix. A. Parallel rule-based system. B. Retrain from scratch with a bigger vocab. C. Find tune on a labeled data set, including jargon D. Increase batch size for training. Answer is C. Exposing the model to labeled examples containing domain specific jargon.

Teach is it to classify such emails more accurately. You have two LLMs for sentiment analysis. Model A, lower cross entropy. F1 and 0.8.2. Model B, higher CE for F1 and 0.86. Which do you deploy? A. Model A due to lower loss. B. Model B due to better F1, precision, recall balance. C. Neither since loss is more critical. D. Model A, since low loss always means that the model is not a single.

Since low loss always means better. Answer is B. A higher F1 indicates better overall balance of precision and recall, which is typically the priority in sentiment tasks.

A handy way to think about the F1 score is that it measures how well your model balances precision, how many of the items you predicted are correct, and recall how many of the correct items you actually predicted.

A. F1 score of 1.0 means perfect precision and recall, while 0 means the classifier didn't manage to get both metrics right in any useful way.

Cross entropy is a way to measure the distance between what the model says, predicted probabilities, and what the truth is, actual label distribution.

By trying to minimize this distance, you guide the model to produce probabilities that better reflect the true labels.

For domain adaption, you keep the base large language model weights frozen and add small adapter layers.

This concept is known as A. Full model training. B. Laura or adaptor based fine tuning. C. 0 shot inference. D. Distillation.

The correct answer is B. Laura. Low rank adaption. It works by adding lightweight pieces to the original model, as opposed to changing the entire model, for example.

So this helps us quickly expand to use cases and so specialise for domain specific tasks or knowledge.

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

You

Core techniques in prompt engineering. One to many shot, prompting for sentiment specific responses.

Senario

A research team is developing a virtual assistant that tailors responses based on customer sentiment,

positive, neutral, or negative. Approach, use one to many shot prompting to include examples

for each sentiment type within a single prompt. This enables the LLM to adapt its response

style dynamically based on the detected sentiment.

Impact

This technique enhances customer engagement and satisfaction by providing responses that

match the customer's emotional state.

Senario

A healthcare provider uses an LLM to assist clinicians in summarising patient cases.

Approach

Implement prompt engineering to constrain the model's output to recognised medical terminology.

This significantly reduces hallucinations, ensuring that generated content aligns with

medical standards. Instances of hallucinated medical procedures pose a safety risk.

By constraining the model to establish medical treatments and procedures, we avoid introducing

new terms or unverified information.

Alternative technique

Integrate a controlled vocabulary by pre-defining acceptable terms in the prompt.

Ensuring adherence to validated medical practices.

Impact

This approach enhances patient safety by ensuring accurate and reliable AI-generated medical

summaries.

Scenario-based applications for prompt engineering demonstrate the versatility and power of this

technology.

A, rapid application development for financial chatbots.

A financial company needs a customer support chatbot capable of adapting quickly to new

financial planning queries.

Solution

Use iterative prompt engineering to refine the chatbot's responses based on real-world feedback.

Prompt

Example

You are a financial assistant.

Provide concise and empathetic advice on financial planning topics like budgeting, savings

and retirement.

Impact

This approach allows rapid iterations and scalable deployment of improved responses.

B, conversational chatbot using hugging face

Problem

Developers want to experiment with pre-trained conversational LLMs from hugging face efficiently.

Solution

First, install transformers and data sets libraries.

Next, load a conversational model like DialogPT and define the conversational context dynamically.

Impact

This approach streamlines experimentation and deployment of conversational capabilities.

C, email classification with few-shot learning.

Problem

A company wants to classify customer emails into categories like billing, technical support

and product inquiry with minimal training time.

Solution

Use few-shot learning to quickly train the system on email classification.

Prompt example

Classify the following email into one of these categories.

Billing

Technical support

Product inquiry

Impact

Few-shot learning accelerates deployment while maintaining high accuracy in email classification.

D,

Legal-Document Summarization

Problem

Summarizing legal documents concisely while retaining key details.

Solution

Use prompt engineering to create targeted summaries focusing on specific aspects of legal documents.

Prompt example

Summarize the key terms of this employment contract.

Focusing on salary,

Benefits

and termination conditions.

Impact

This approach ensures summaries are concise, relevant and contextually accurate.

Saving time and improving understanding of legal documents.

Interative prompt engineering.

A practical guide.

Step-by-step approach.

Start broad and refine.

Begin with a general prompt to explore the model's behavior.

Refine iteratively by adding constraints based on output evaluation.

Example

Initial prompt

Summarize this article

Refined

Prompt

Summarize this article in three sentences focusing on the main findings.

Incorporate specific constraints.

Use domain-specific vocabulary and style guidelines to guide output.

Example

For health care,

Applications

Include constraints like

Use only established medical terms and exclude speculative treatments.

Leverage feedback for continuous improvement.

Analyze

User interactions or generated outputs to identify improvement areas.

Update prompts to address observed gaps.

Creating a cycle of continuous improvement in your prompt engineering process.

Evaluation

Metrics for prompt effectiveness.

To ensure prompt engineering efforts yield measurable improvements,

evaluate the outputs using these metrics.

Relevance.

Does the response address

the input query effectively?

Precision.

Are the outputs accurate and contextually correct?

Consisteness.

Does the output avoid unnecessary verbosity?

Adaptability.

Does the model adjust appropriately based on the prompt?

Safety.

Is the content free of hallucinations or incorrect information?

Summary.

Through iterative refinement,

domain-specific constraints,

and continuous feedback loops,

LLMs can be adapted to diverse real-world scenarios with precision and reliability.

Embracing these strategies empowers developers to deploy smarter, safer,

and more responsive AI solutions.

Prompt engineering is an indispensable skill for refining and optimizing LLM behavior.

By applying strategies like iterative refinement,

few-shot prompting, dynamic prompts,

and chain of thought reasoning,

you can guide LLMs to generate precise,

contextually relevant, and task-specific outputs.

When iteratively refining prompts for a generative AI model,

which strategy ensures the model aligns better with your intentions?

A.

Start with a highly detailed prompt immediately.

B.

Keep prompts extremely concise from the start.

C.

Compare multiple outputs from the same prompt.

D.

Begin broadly and add specific instructions based on output.

Answer is D.

An iterative approach, starting broad and then refining,

helps pinpoint needed clarifications,

so the model better matches the desired output.

You want to ensure that each tweak to the prompt pushes the model closer

to your desired style of polite and empathetic.

After conducting an A, B test on prompt strategies for a chatbot,

results show only slight differences.

How can you refine the test for more actionable insights?

A. Use identical prompts but change model architecture.

B.

Increase user count without changing prompts.

C. Introduce a third prompt, blending elements from the first two.

D.

Deploy both prompts in production and let model pick.

Answer is B.

A combined third prompt can isolate which aspects of each original prompt

improve chatbot performance.

You create prompt strategy A, focused on empathy, and prompt strategy.

B.

Focused on concise explanation.

After testing with real or simulated user queries,

both yield similar user satisfaction.

To move forward, you combine the best elements,

the empathic language from A plus the clarity of B into a new prompt C

for further comparison.

Fine tuning a generative model to generate polite and empathetic emails.

The model is too formal.

Next best approach in prompt engineering.

A. Make prompt more vague to allow creativity.

B. Provide explicit adjectives, phrases for warmth.

C. Increase the model's context window.

D. Decrease model size.

Answer is B, including specific tone or style instructions.

E.G. Warm.

Empathetic.

Or using synonyms that reflect informality,

steers outputs toward that style.

The new combined prompt produces better structure,

but still sounds too official.

Realising from user feedback that the model is too formal.

You incorporate direct instructions and example phrases to guide warmth.

Your model categorizes support emails.

It struggles with jargon.

Best fix.

A. Parallel rule-based system.

B.

Retrain from scratch with a bigger vocab.

C. Fine tune on a labelled dataset, including jargon D.

Increase batch size for training.

Answer is C. Exposing the model to labelled examples.

Containing domain specific jargon teaches it to classify such emails more accurately.

You have two LLMs for sentiment analysis.

Model A, lower cross entropy.

F1 and 0.82.

Model B, higher CE for F1 and 0.86.

Which do you deploy?

A. Model A, due to lower loss.

B. Model B, due to better F1, precision recall balance.

C. Neither since loss is more critical.

D. Model A, since low loss, always means better.

Answer is B.

A higher F1 indicates better overall balance of precision and recall,

which is typically the priority in sentiment tasks.

A handy way to think about the F1 score is that it measures how well your model balances

precision, how many of the items you predicted are correct, and recall how many of the correct

items you actually predicted.

An F1 score of 1.0 means perfect precision and recall, while 0 means the classifier didn't

manage to get both metrics right in any useful way.

Class entropy is a way to measure the distance between what the model says, predicted probabilities,

and what the truth is, actual label distribution.

By trying to minimize this distance, you guide the model to produce probabilities that better

reflect the true labels.