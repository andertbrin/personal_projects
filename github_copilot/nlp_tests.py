import spacy
import re
import transformers



def valid_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    else:
        return False


def valid_phone(phone):
    if re.match(r'^\+?[0-9]{8,15}$', phone):
        return True
    else:
        return False

# print(valid_email('inovabra@bradesco.com.br'))


# remove stop words from a string with spacy for portuguese
def remove_stop_words(text):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop])


print(remove_stop_words('Olá, eu sou um programador fazendo teste com uma'
                        ' plataforma para auxiliar na criação de código com python.'))


# load roberta-large-mnli model using automodel
model = transformers.AutoModelForSequenceClassification.from_pretrained('roberta-large-mnli')

# load the tokenizer
tokenizer = transformers.AutoTokenizer.from_pretrained('roberta-large-mnli')

# tokenize the input
input_ids = tokenizer.encode("Hello, my dog is cute", return_tensors="pt")

# make predictions
predictions = model(input_ids)

# print the predictions
print(predictions)





