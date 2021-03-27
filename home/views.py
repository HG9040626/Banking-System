from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from home.models import AccountDetail,Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def accounts(request):
    
    tasks=AccountDetail.objects.all()
    context={'alltasks':tasks}
    if request.method=="POST":
        
        fromac=request.POST['fromac']
        toac=request.POST['toac']
        ifsc_c=request.POST['ifsc_c']
        comment=request.POST['comment']
        amount=request.POST['amount']
        receiver=AccountDetail.objects.get(acn=toac)
        sender=AccountDetail.objects.get(acn=fromac)
        amount=int(amount)
        if ifsc_c == receiver.ifsc:
            print(sender.amt,receiver.amt)
            sender.amt-=amount
            receiver.amt+=amount
            print(sender.amt,receiver.amt)
            sender.save()
            receiver.save()
    return render(request,'accounts.html',context)
def about(request):

    return render(request,'about.html')  
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        ins=Contact(name=name,email=email,phone=phone,subject=subject)
        ins.save()

    return render(request,'contact.html')      
     

