from dataStructures.myList import myList,studentsList
from Analysis.research import MyAnalysis
print("namaste")

new_list = myList()
new_list.add_item(10)
new_list.add_item(20)
new_list.add_item(30)
new_list.print_list()
new_list.remove_item(20)
new_list.print_list()


new_analysis = MyAnalysis()


new_stdList = studentsList()
new_stdList.add_item("Hem")
new_stdList.add_item("Ram")
new_stdList.add_item("Bheem")

new_stdList.print_list()
new_stdList.remove_item("Bheem")
new_stdList.print_list()