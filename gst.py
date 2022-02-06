originalCost= float(input("Enter the original cost : "))
GstRate = int(input("Enter the gst rate percentage :"))

GST = originalCost * (GstRate/100)
Netprice = originalCost+GST
print(GST)
print(Netprice)