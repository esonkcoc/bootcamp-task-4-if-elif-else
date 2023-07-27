swim=(int)(input("Enter your swimming time in minutes."))
cyc=(int)(input("Enter your cycling time in minutes."))
run=(int)(input("Enter your running time in minutes."))
total_time=swim+cyc+run
print("Your total time was "+(str)(total_time)+" minutes.")
if total_time<=100:
    print("Congratulations! You've won Provincial Colours.")
elif (total_time>100)and(total_time<=105):
    print("Congratulations! You've won Half Colours.")
elif (total_time>100)and(total_time<=110):
    print("Congratulations! You've won Provincial Scroll.")
else:
    print("Commisterations. You didn't qualifiy.")