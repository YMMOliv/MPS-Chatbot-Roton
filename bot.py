import regex as re
from database import database, menu


def generate_answer(question):
  keyword = get_key_word(question)
  order = confirm_order(keyword, question)
  try:
    answer = database[keyword]
    answer += order
  except:
    return database['default'] # se não houver uma resposta pronta, retorna uma resposta padrão, ex: "não entendi"
  else:
    return answer


# recebe a pergunta(str) e retorna uma lista de palavras-chave encontradas na pergunta
def get_key_word(question):
  question = question.lower()
  #question.translate(question.maketrans("áéíóú", 'aeiou'))
  keyword = ''
  keylist = database.keys()
  for key in keylist:
    if match := re.search(key, question):
      keyword = key
  return keyword


order = ''

def confirm_order(keyword, question):
  global order
  if keyword in ['oi|ola|olá', 'descartar', 'tchau|adeus|encerrar|fim']:
    order = 'Carrinho: \t\nTotal: 0 reais\n'+\
            'Forma de pagamento: pay\nEndereço de entrega: addr'''
  elif keyword in menu.keys():
    order = order.replace('\t', keyword+' \t')
    total = int(re.search('[0-9]+', order).group())
    total += menu[keyword]
    order = re.sub('[0-9]+', str(total), order)
  elif keyword in ['cartao|cartão', 'dinheiro']:
    order = order.replace('pay', question)
  elif keyword == 'rua':
    order = order.replace('addr', question)
    return order
  return ''



#debug
def main():
  question = ''
  while question != 'fim':
    question = input()
    answer = generate_answer(question)
    print(answer)

if __name__ == "__main__":
  main()
