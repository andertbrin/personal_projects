import spacy
import re
import transformers


def valid_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    else:
        return False


def valid_phone(phone):
    if re.match(r'^\+?[0-9]{10,15}$', phone):
        return True
    else:
        return False


# remover stopwords usando spacy para português
def remove_stopwords(text):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop])

print(remove_stopwords('Olá, eu sou um programador fazendo teste com uma'
                        ' plataforma para auxiliar na criação de código com python.'))




