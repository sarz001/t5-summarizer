from transformers import T5ForConditionalGeneration, T5Tokenizer
from functools import lru_cache

MODEL_PATH = "t5_finetuned"   # ← this is your downloaded model folder

@lru_cache(maxsize=1)
def load_model():
    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
    return model, tokenizer

# simple response cache
_cache = {}

def summarize(text: str):
    text = text.strip()
    if text in _cache:
        return _cache[text]

    model, tokenizer = load_model()

    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    summary_ids = model.generate(
        inputs,
        max_length=128,
        min_length=30,
        num_beams=4,
        early_stopping=True,
    )

    result = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    _cache[text] = result
    return result
