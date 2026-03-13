# 14 - AI Visualization translated

---

Data visualization is a critical aspect of data science, enabling practitioners to uncover

patterns, communicate insights and debug machine learning models.

Choosing the correct visualization technique depends on the type of data, the relationships

you want to explore, and the story you wish to convey.

This lecture outlines and compares common data visualization methods, emphasizing when

to use each.

Barcharts display categorical data as rectangular bars, where the height or length represents

the value of the variable.

Grouped barcharts compare multiple metrics within categories, grouping bars side by side

for each category.

Grouped bar charts when comparing values across categories.

Choose grouped bar charts when comparing multiple metrics, such as accuracy, latency, satisfaction,

across categories like regions.

Example, comparing performance metrics, accuracy, latency satisfaction, across regions to identify

disparities in service delivery.

Barcharts connect data points with lines showing trends or changes over time, ideal for

visualizing temporal data or trends over a continuous range, such as hours, days, months.

Useful when monitoring regional performance trends over time.

Example, tracking user satisfaction scores over time for multiple regions to analyze

changes seasonally.

Barcharts represent proportions of a whole using slices.

Each slice corresponds to a category's proportion of the total.

Use when showing how a single metric is distributed among categories.

Avoid bar charts for detailed comparisons or when working with numerous categories.

Example, visualizing the proportion of customer complaints attributed to different product

categories.

Scatter plots display relationships between two or more continuous variables using points.

Each point represents a single observation.

Use scatter plots to identify correlations or patterns between variables.

When you need to visualize multiple metrics per region but without grouping or categorical

emphasis.

Example, analyzing latency versus satisfaction in different regions to explore trends.

Heat maps use color gradients to represent values in a matrix-like format, often visualizing

relationships between two categorical or sequential variables.

To compare magnitudes or distributions within a data set.

The model is usually useful for attention weights in machine learning models to debug where

the model focuses during inference.

Example, visualizing attention weights in a generative AI model to understand which tokens

the model focuses on.

Attention visualizations highlight how machine learning models distribute attention across

input tokens during processing.

They show which parts of the input contribute most to the output, ideal for debugging generative

AI models as they reveal how focus shifts across input tokens.

Example, diagnosing why a language model focuses incorrectly on certain parts of an input

sentence.

Example, visualizing the distribution of response times in a customer service chatbot.

Example, visualizing the distribution of the data set based on five summary statistics,

minimum first quartile, median third quartile and maximum when comparing distributions across

multiple groups.

Useful for spotting outliers and understanding variability.

Example, visualizing the distribution of the data set.

Combining satisfaction scores across regions to identify areas with highly variable user

feedback.

Grouped bar charts are ideal for comparing multiple metrics such as accuracy, latency and satisfaction

regionally.

They allow for side-by-side comparisons, offering clarity, attention visualizations like heat

maps, debug outputs in generative AI by revealing token focus, ensuring interpretability of the

model's decision-making process.

By understanding the strengths and limitations of these visualization techniques, data scientists

can effectively communicate insights, debug models and enhance the interpretability of

complex systems.

You must visualize performance metrics like accuracy, latency and satisfaction across multiple

regions, which visualization best compares these metrics regionally?

A, grouped bar chart, B, pie chart of proportions, C, scatterplot of multiple metrics per region,

D, line chart showing trends over time per region.

Correct answer.

A, grouped bar chart, which is correct, is best for comparing multiple metrics side-by-side

across categories like regions.

It is clear and intuitive for identifying differences.

B, pie chart of proportions focuses on a single metric distribution, making it unsuitable

for comparing multiple metrics.

C, scatterplot is not ideal for regional comparison.

It is better for showing relationships between two continuous variables.

D, line chart, tracks changes over time, but is not suited for direct regional comparisons.

Your generative AI model uses attention visualizations to debug outputs.

These visualizations show, A, how the model shifts focus across input tokens.

B, the hyperparameters of your training.

C, the final classification accuracy.

D, computed numeric outputs for the final layer only.

Correct answer.

A, how the model shifts focus across input tokens, which is correct, as attention visualizations

specifically highlight how attention is distributed over input tokens.

B, the hyperparameters of your training are not related to attention visualizations.

C, the final classification accuracy is a performance metric, not directly tied to attention

visualization.

D, computed numeric outputs for the final layer only focus on intermediate processing, not

final outputs.

You use a heat map to visualize attention weights in a generative model.

What is the primary advantage of using this visualization?

A, it provides exact numeric attention values.

B, it reveals which tokens the model focuses on.

C, it automatically tunes hyperparameters.

D, it directly shows the model's overall accuracy.

Correct answer.

B, reveals which tokens the model focuses on, which is correct, as heat maps make attention,

distributions visually interpretable.

C, tunes hyperparameters, which is incorrect, as heat maps are diagnostic tools, not hyperparameter

tuning mechanisms.

D, shows model accuracy, which is incorrect, as heat maps illustrate attention patterns,

not overall accuracy.

A, provides exact numeric values, which is incorrect as heat maps show relative magnitudes,

but not precise numbers.