# parameters ( tham số )
# def f():
  #  s = "-- Inside f()"
 #   print(s)

#print("before calling f()")
#f()
#print('after calling f()')

def f(qty, item, price):
    print (f" {qty} {item} cost $ {price:2f}")

f(6, "bananas" , 1.74) # truyền đúng vị trí
f( "bananas", 6, 1.74 ) # truyền sai vị trí


def f():
