from transformers import AutoTokenizer, AutoModel
import torch

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

model.eval()


def get_embedding(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=False
    )

    with torch.no_grad():
        outputs = model(**inputs)

    # CLS token embedding
    embedding = outputs.last_hidden_state[:, 0, :]

    return embedding.squeeze().numpy()