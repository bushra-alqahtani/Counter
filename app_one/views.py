import imp
from itertools import count
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.

#Have the root route render a template that displays the number of times the client 
# has visited this site. Refresh the page several times to ensure the counter is working.
#SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, 
# as well as the value of the counter, given the above functionality
def index(request):
     #value count will incrementing when user access the page (so its value assigned to context)
    if "count" in request.session: #if the count exist in our dictionary 
        request.session["count"] +=1
        print("key exists") #if it does just read it from the session 
    else:
        print("key 'key_name' is not exist")
        request.session["count"]=0

    if "visit" in request.session:
         request.session["visit"] +=1
         print("key exists")
    else:
        print("key 'visit' is not exist")
        request.session["visit"]=0
    return render(request,"index1.html")
  

#Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
#Add a Reset button that uses the "/destroy_session" route
def clear(request):
    del request.session['count']
    return redirect('/')
#NINJA BONUS: Add a +2 button underneath the 
# counter and a new route that will increment the counter by 2
def add2(request):
    request.session['count'] += 1
    return redirect('/')

    #SENSEI BONUS: Add a form that allows the user
    # to specify the increment of the counter and have the counter increment accordingly
def add_by(request):
    num=request.POST['num'] 
    print( num)
    request.session['count'] +=(int(num)-1)
    return redirect('/')

