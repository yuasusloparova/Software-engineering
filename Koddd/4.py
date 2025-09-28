sentence = input("Введите предложение на английском: ")

print(f"Длина предложения: {len(sentence)}")
sentence_lower = sentence.lower()
print(f"В нижнем регистре: {sentence_lower}")

vowels = 'aeiou'
vowel_count = sum(1 for char in sentence_lower if char in vowels)
print(f"Количество гласных: {vowel_count}")

sentence_replaced = sentence.replace('ugly', 'beauty')
print(f"После замены: {sentence_replaced}")

starts_with_the = sentence.startswith('The')
ends_with_end = sentence.endswith('end')
print(f"Начинается с 'The': {starts_with_the}")
print(f"Заканчивается на 'end': {ends_with_end}")
