from datetime import datetime
import time

def waiting_game():
  seconds_to_wait = input("Enter the number of seconds to wait: ")

  try:
    seconds_to_wait = int(seconds_to_wait)
  except ValueError:
    print("Seconds must be integer!")

  if not isinstance(seconds_to_wait, int):
    exit()

  input("Press Enter to start waiting, any other key to cancel: ")

  start_time = datetime.now()
  s = time.perf_counter()
  
  input("Hit any key to end wait...")
    
  stop_time = datetime.now()
  e = time.perf_counter()

  elapsed_time = stop_time.second - start_time.second + (stop_time.microsecond - start_time.microsecond)/1000000

  print(f'Elapsed time: {elapsed_time}')
  print(f'Elapsed time: {e-s}')
    
  if elapsed_time != float(seconds_to_wait):
    print(f"You took {elapsed_time : .3f} seconds instead of {seconds_to_wait} seconds to hit the key to end the waiting game!")
  else:
    print(f"Wow! You took exactly {seconds_to_wait} seconds to hit the key to end the waiting game!")

# commands used in solution video for reference
if __name__ == '__main__':
  waiting_game()