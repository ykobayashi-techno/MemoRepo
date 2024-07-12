import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model_id = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True) 

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

messages = [
    {"role": "system", "content": "あなたはWebアプリのアシスタントです。日本語で応答してください。"},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.8,
    "do_sample": True,
}

while True:
    input_text = input("あなた: ")
    if input_text == "exit":
        break
    
    messages.append({"role": "user", "content": input_text})

    # モデルへの入力を適切な形式に変換
    prompt = ""
    for message in messages:
        if message["role"] == "user":
            prompt += f"User: {message['content']}\n"
        else:
            prompt += f"Assistant: {message['content']}\n"

    output = pipe(prompt, **generation_args)
    print("AI: ", output[0]['generated_text'])

    messages.append({"role": "assistant", "content": output[0]['generated_text']})