from datasets import load_dataset, Dataset, DatasetDict
import random

# Load ImageNet-1k from Hugging Face
dataset = load_dataset("ILSVRC/imagenet-1k", split="train")

# Create a dictionary to store sampled indices per class
class_to_samples = {}
for idx, example in enumerate(dataset):
    label = example["label"]
    if label not in class_to_samples:
        class_to_samples[label] = []
    class_to_samples[label].append(idx)

sampled_indices = []
for label, indices in class_to_samples.items():
    sampled_indices.extend(random.sample(indices, min(1, len(indices))))  # Handle edge case for small classes

# Create a new dataset with only sampled images
sampled_dataset = dataset.select(sampled_indices)

hf_dataset_dict = DatasetDict({"train": sampled_dataset})

# Push to Hugging Face Hub (Optional)
hf_dataset_dict.push_to_hub("your_huggingface/imagenet_reduced_trainingset-single_sample")

print("Subset dataset created and uploaded successfully!")
