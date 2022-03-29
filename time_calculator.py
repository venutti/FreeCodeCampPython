DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_time(start, duration, day=None):
  total_days = 0

  start, ending = start.split()

  hour, minutes = [int(x) for x in start.split(":")]
  add_hour, add_minutes = [int(x) for x in duration.split(":")]
  final_minutes = (minutes+add_minutes)%60
  add_hour += (minutes+add_minutes)//60
  final_hour = (hour+add_hour)%12

  loops = (hour+add_hour)//12

  while loops:
    if ending == "PM":
      ending = "AM"
      total_days += 1
    else:
      ending = "PM"
    loops -= 1

  res = (str(final_hour) if final_hour != 0 else "12") + ":" + (str(final_minutes)).rjust(2, "0") + " " + ending

  if day:
    day = DAY_OF_WEEK.index(day.title())
    day = DAY_OF_WEEK[(day + total_days)%(len(DAY_OF_WEEK))]
    res = res + ", " + day

  final_msj = ""
  if total_days == 1:
    final_msj = "(next day)"
  elif total_days > 1:
    final_msj = f"({total_days} days later)"

  return res + " " + final_msj


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
