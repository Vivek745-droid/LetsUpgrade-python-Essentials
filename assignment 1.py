alt = int(input("Enter the value of altitude for landing safely :"))
if alt<=1000 :
    print("plz land the plane safely")
elif alt>1000  and alt<5000  :
    print("Bring down to 1000 ft")
elif alt>5000 :
    print("Go around and try later")