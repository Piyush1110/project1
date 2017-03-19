print ("Make a Choice")
print ("1.Student to Teacher")
print ("2.Battleship")
print ("3.Exam Statistics")
choice=int(input("Enter your choice(1,2,3)"))
if choice==1:
    import students_to_teacher
elif choice==2:
    import battleship
elif choice==3:
    import exam_stats
else:
    print "wrong choice entered"
