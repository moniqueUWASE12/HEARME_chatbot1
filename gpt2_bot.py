from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import os

# Load model & tokenizer
model_path = os.path.join(os.path.dirname(__file__), "ai_model")

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Make sure model is in eval mode
model.eval()

def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(input_ids)

    with torch.no_grad():
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=100,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.replace(prompt, "").strip()
