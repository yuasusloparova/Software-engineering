from datetime import datetime
import time

def display_current_time():
  
    
    print("Вывод времени в течение 5 секунд:")
    
    for i in range(5):
        current_time = datetime.now().strftime("%H:%M:%S")
       
        print(f"Текущее время: {current_time}")
        
   
        if i < 4:
            time.sleep(1)
if __name__ == '__main__':
    display_current_time()
