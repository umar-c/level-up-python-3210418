import sched
import time

def schedule_function(target_time, func, *args):
  print(f"{func.__name__}() scheduled for {time.asctime(time.localtime(target_time))}")
  while (time.time() <= target_time):
    continue
  func(args)

def _schedule_function(target_time, func, *args):
   schedule = sched.scheduler(time.time, time.sleep)
   schedule.enterabs(target_time, 1, func, argument=args)
   print(f"{func.__name__}() scheduled for {time.asctime(time.localtime(target_time))}")
   schedule.run()

# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')

    _schedule_function(time.time() + 1, print, 'Howdy!')
    _schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
