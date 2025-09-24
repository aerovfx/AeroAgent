import json
from datasets import load_dataset, DatasetDict
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import evaluate
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

# Thay repo_name
repo_name = "aerovfx/edu_datasetv7"  # e.g., "vietchung/quiz-tech12h"

# Load dataset (giả sử đã có train/validation splits từ fix trước)
ds = load_dataset(repo_name)
if "validation" not in ds:
    # Tạo split nếu chưa có
    split_ds = ds["train"].train_test_split(test_size=0.1, seed=42)
    ds = DatasetDict({"train": split_ds["train"], "validation": split_ds["test"]})

print(f"Train: {len(ds['train'])}, Val: {len(ds['validation'])}")

# Map labels: A=0, B=1, C=2, D=3 (nếu answer là string)
def map_labels(example):
    label_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'Unknown': 0}  # Fallback A nếu Unknown
    example['labels'] = label_map.get(example['answer'], 0)
    # Format input
    opts = example['options']
    options_str = f"A. {opts[0]} B. {opts[1]} C. {opts[2]} D. {opts[3]}" if len(opts) >= 4 else " ".join(opts)
    example['text'] = f"Question: {example['question']} Options: {options_str}"
    return example

ds = ds.map(map_labels)

# Tokenizer: PhoBERT
model_name = "vinai/phobert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(examples):
    return tokenizer(examples['text'], truncation=True, padding=True, max_length=256)

tokenized_ds = ds.map(tokenize, batched=True)

# Model: 4-class classification
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=4)

# Metrics
accuracy = evaluate.load("accuracy")
f1 = evaluate.load("f1")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    preds = np.argmax(predictions, axis=1)
    return {
        'accuracy': accuracy.compute(predictions=preds, references=labels)['accuracy'],
        'f1': f1.compute(predictions=preds, references=labels, average='weighted')['f1']
    }

# Training args (nhỏ cho dataset)
training_args = TrainingArguments(
    output_dir="./phobert-quiz-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=50,
    weight_decay=0.01,
    logging_dir="./logs",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    report_to=None  # No WandB
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["validation"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# Train
trainer.train()

# Eval
eval_results = trainer.evaluate()
print(f"Eval Accuracy: {eval_results['eval_accuracy']:.4f}")
print(f"Eval F1: {eval_results['eval_f1']:.4f}")

# Save & Push HF
trainer.save_model()
model.push_to_hub("aerovfx/physic", token="hf_xxxxxxxxx")  # Thay token nếu push
tokenizer.push_to_hub("aerovfx/physic", token="hf_xxxxxxxxx")

print("Fine-tune hoàn tất! Model saved at './phobert-quiz-finetuned'.")