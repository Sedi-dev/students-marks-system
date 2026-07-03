import json
import matplotlib.pyplot as plt

def load_data():
  """Load student data from JSON file."""
  
  try:
    with open("student_data.json", "r") as file:
      data = json.load(file)
      return data
    
  except FileNotFoundError:
    print("Student data not found")
    return []

def get_student_names(students):
  
  std_names = []
  for student in students:
    std_names.append(student["Name"])
  return std_names

def get_student_averages(students):
  
  std_averages = []
  for student in students:
    std_averages.append(student["Average"])
  return std_averages

def plot_student_averages(names, averages):
  """Creating bar graph for students' averages"""
  
  bars = plt.bar(names, averages, color = "pink")
  
  plt.title("Average Marks by Student")
  
  plt.xlabel("Students")
  
  plt.ylabel("Average (%)")
  
  plt.grid(axis = "y", linestyle = "--", alpha = 0.5)
  
  plt.ylim(0, max(averages) + 5)
  
  plt.xticks(rotation = 45)
  
  for bar in bars:
    
    height = bar.get_height()
    center = bar.get_x() + bar.get_width() / 2
    plt.text(center, height + 1 , f"{height:.1f}%", ha = "center")
  
  plt.show()
  plt.tight_layout()
    
def main():
  
    students = load_data()
    names = get_student_names(students)
    averages = get_student_averages(students)
    plot_student_averages(names, averages)
    
    print(f"Loaded {len(students)} student record(s).")
    
    
if __name__=='__main__':
    main()
