with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text1 = text.replace('Вопрос: ', '')
    text2 = text1.replace('Ответ: ', '')
    text3 = text2.replace('Q: ', '')
    text4 = text3.replace('A: ', '')
    with open('textnow.txt', 'w', encoding='utf-8') as file_name:
        file_name.write(text4)