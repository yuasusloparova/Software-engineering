import random

def dice_roll(attempt=1):

    roll = random.randint(1, 6)
    print(f"Попытка {attempt}: выпало {roll}")
    
    
    if roll == 5 or roll == 6:
        print("Вы победили!")
    elif roll == 3 or roll == 4:
        print("Повторный бросок...")
        
        dice_roll(attempt + 1)
    elif roll == 1 or roll == 2:
        print("Вы проиграли")

if __name__ == '__main__':
    dice_roll()
