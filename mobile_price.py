price = int(input("Enter the mobile price:"))
og = 0
if price > 100000:
    gst = float((price * 18) / 100)

    og = price - gst
    print("GST is:", gst)
    print(f"Original price after GST is: {og} INR")
elif price > 50000 and price < 100000:
    gst = float((price * 15) / 100)
    og = price - gst
    print("GST is:", gst)
    print(f"Original price after GST is: {og}INR")
else:
    gst = float((price * 10) / 100)
    og = price - gst
    print("GST is:", gst)
    print(f"Original price after GST is: {og}INR") 









# we can do this type also


# cost_price = float(input("Enter the cost price of the mobile: "))

# if cost_price > 100000:
#     gst = cost_price * 0.18
#     gst_percentage = 18
# elif cost_price > 50000:
#     gst = cost_price * 0.15
#     gst_percentage = 15
# else:
#     gst = cost_price * 0.1
#     gst_percentage = 10

# print(f"GST to be paid is: {gst} INR")
# print(f"GST percentage is: {gst_percentage}%") 





  

