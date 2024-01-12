# bot_logic.py
import spacy
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import wikipedia

class BotLogic:
    def __init__(self, model_path='./gpt2-finetuned-science'):
        self.fine_tuned_model = GPT2LMHeadModel.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path, pad_token='<pad>')
        self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, question):
        doc = self.nlp(question)
        named_entities = [ent.text for ent in doc.ents]
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]
        keywords = named_entities + nouns
        return keywords

    def generate_response(self, prompt, max_length=80):
        keywords = self.extract_keywords(prompt)
        core_query = ' '.join(str(elem) for elem in keywords)

        optimal_prompt = "What is " + core_query + "?"

        input_ids = self.tokenizer.encode(optimal_prompt, return_tensors='pt', max_length=max_length, truncation=True)
        attention_mask = input_ids.ne(self.tokenizer.pad_token_id).long()

        output = self.fine_tuned_model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, num_return_sequences=1)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        splitted = generated_text.split()
        pos = splitted.index("Support:")
        ans = ' '.join(str(elem) for elem in splitted[pos+1:])
        out = ans.split(".")
        final_output = out[0]+"."

        for keyword in keywords:
            if keyword.lower() not in generated_text.lower().split(" "):
                top_result = wikipedia.summary(core_query).split(".")[0] + wikipedia.summary(core_query).split(".")[1]
                return f"Sorry, I don't have information on that. Here's what I found on Wikipedia:\n{top_result}."
        return final_output

