length=int(input("ENTER LENGTH :"))
width=int(input("ENTER WIDTH :"))

if length>width:
    print("SHAPE IS PORTRAIT")
if length<width:
    print("SHAPE IS LANDSCAPE")
if length==width:
    print("SHAPE IS SQUARE")