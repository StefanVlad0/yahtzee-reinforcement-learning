from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "google/gemma-2-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def generate_dynamic_response(prompt, max_length=250, temperature=0.7):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).to("cuda")

    output = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length,
        temperature=temperature,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    if prompt in response:
        response = response.replace(prompt, "").strip()
        
    return response


def generate_response(intent, user_question):
    if intent == "rules_request":
        with open("rules.txt", "r", encoding="utf-8") as file:
            rules = file.read()
        prompt = (
            f"Userul întreabă: {user_question}\n\n"
            f"Răspunsul trebuie să fie clar și prietenos, maxim 2 randuri, bazat pe regulile:\n{rules}\n\n"
            f"Răspunde detaliat și pe înțelesul tuturor."
        )
        return generate_dynamic_response(prompt)
    elif intent == "best_move_request":
        return "Îmi pare rău, dar pentru a-ți sugera o mutare, am nevoie de informații despre zarurile tale actuale."
    elif intent == "general_help":
        return "Pot răspunde la întrebări despre regulile jocului, strategii sau mutări. Întreabă-mă orice!"
    else:
        return "Îmi pare rău, dar pot răspunde doar la întrebări despre jocul Yahtzee."
