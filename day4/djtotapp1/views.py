from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("This is home page")

# def aboutus(r):
# 	return HttpResponse("<h2>This is about us page</h2>")

# now add css

def aboutus(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px '>This is about us page</h2>")


def Indu(i,name):
	return HttpResponse("<h2> Hi Welcome {}".format(name))

	# above we gave format name in url we gave name is diplayed like Hi welcome Indupriya



def MyTable(request,num):
	j=""
	for m in range(1,11):
		j +="{} X {:02} = {:02}".format(num,m,num*m)+ "<br/>"
	# print(j)
	return HttpResponse(j)

def Twoparams(request,name,age):
	#print(name,age)
	#print is displayed only in server so we use return
	# now i want to pass the values directly in 
	# here we didnt have templetes folder so now create template folder
	# and add newfolder and file adrress which created inside templates
	return render(request,'newfolder/user.html',{'n':name,'a':age})
	#or
	#return render(request,'newfolder/user.html',)
	

def Threeparams(request,name,age,org):
	#print(name,age)
	#print is displayed only in server so we use return
	# now i want to pass the values directly in 
	# here we didnt have templetes folder so now create template folder
	# and add newfolder and file adrress which created inside templates
	# return render(request,'newfolder/user.html',{'n':name,'a':age,'o':org,'s':sal})
	#here sal is not suported becz it will take in float so it shows error
	return render(request,'newfolder/user.html',{'n':name,'a':age,'o':org})
	#or
	#return render(request,'newfolder/user.html',)


def cssexample(request):
	return render(request,"newfolder/csseg1.html")
	