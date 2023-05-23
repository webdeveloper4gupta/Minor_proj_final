from django.shortcuts import render,redirect
from django.contrib import messages
from minorproject import settings
from django.core.mail import send_mail
# here i make the au
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from joblib import load
# here i make the section where i load the model 
kidn=load('./savedModelss/kidney.joblib')
park=load('./savedModelss/parkinsons.joblib')
diabs=load('./savedModelss/diabs.joblib')
hearts=load('./savedModelss/heart.joblib')
brainsmr=load('./savedModelss/brain.joblib')

# Create your views here.

def home(request):
          return render(request,"index.html")
@login_required(login_url="logins")
def brain(request):
          # here i write the backend code for brain dataset
          if request.method=='POST':
                      
                      n5=request.POST.get('file')
                      
                      y_pred=''
                      y_pred=brainsmr.predict([[n5]])
                      print(y_pred)               
          return render(request,"brain_mri.html")

# here i write the concept of login 
def logins(request):
          if request.method=='POST':
                    n1=request.POST.get('name')
                    n2=request.POST.get('email')
                    n3=request.POST.get("password")
                    user = authenticate(request,username=n1, password=n3)
                    request.session ['email'] =n2
                    if user is not None:
                              login(request,user)
                              return render(request,"index.html")
          return render(request,"login.html")
                    
def signout(request):
              logout(request)
          #     messages.success(request,"successfully logout")
              return redirect(home)

def sign(request):
          if request.method=='POST':
                    n1=request.POST.get('name')
                    n2=request.POST.get('firstname')
                    n3=request.POST.get('lastname')
                    n4=request.POST.get('email')
                    n5=request.POST.get('password')
                    if User.objects.filter(username=n1):
                    #   messages.error(request,"usernam already exist")
                      return redirect(sign) 
                    if User.objects.filter(email=n4):
                      messages.error(request,"email already already exist")
                      return redirect(sign) 
                    user=User.objects.create_user(n1,n4)
                    user.set_password(n5)
                    user.first_name=n2
                    user.last_name=n3
                    user.save()          
                    messages.success(request,"succesfully created user")
          return render(request,"sign.html")
@login_required(login_url="logins")
def diab(request):
          # here i write the backend code for diabetes code 
          y_pred=''
          if request.method=='POST':
                    n1=request.POST.get('Pregnancies')
                    n2=request.POST.get('glucose')
                    n3=request.POST.get('blood Pressure')
                    n4=request.POST.get('skin thickness')
                    n5=request.POST.get('insulin')
                    n6=request.POST.get('BMI')
                    n7=request.POST.get('diabetespedigreefunction')
                    n8=request.POST.get('age')
                    y_pred=diabs.predict([[n1,n2,n3,n4,n5,n6,n7,n8]])
                    print(y_pred[0])
                    if y_pred[0]==0:
                              y_pred="nondisease"
                    else:
                              y_pred="disease"
                    email=request.session['email']
                    # here i set the email concept 
                    subject = "Health Report"
                    message = "Hi Welcome to the Health prediction web application , First of all we thank you for using our services. your medical check up result for diabetes is"+ y_pred+"Thank you <br> Have a nice day ahead."
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [email]
                    send_mail(subject, message, from_email,to_email, fail_silently=False)
                              
                   
          return render(request,"diabetes.html",{"y":y_pred})
@login_required(login_url="logins")
def heart(request):
          # here i write the backend of the heart model 
          y_pred=''
          if request.method=='POST':
                    n1=request.POST.get('age')
                    n2=request.POST.get('sex')
                    n3=request.POST.get('cp')
                    n4=request.POST.get('trestbps')
                    n5=request.POST.get('chol')
                    n6=request.POST.get('fbs')
                    n7=request.POST.get('restecg')
                    n8=request.POST.get('thalach')
                    n9=request.POST.get('exang')
                    n10=request.POST.get('oldpeak')
                    n11=request.POST.get('slope')
                    n12=request.POST.get('ca')
                    n13=request.POST.get('thal')
                    y_pred=hearts.predict([[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13]])
                    print(y_pred[0])
                    if y_pred[0]==0:
                              y_pred="non disease"
                    else:
                              y_pred="disease"
                    email=request.session['email']
                    # here i set the email concept 
                    subject = "Health Report"
                    message = "Hi Welcome to the Health prediction web application , First of all we thank you for using our services. your medical check up result for heart disease is"+ y_pred+"Thank you <br> Have a nice day ahead."
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [email]
                    send_mail(subject, message, from_email,to_email, fail_silently=False) 
                   
          return render(request,"heart_disease.html",{"y":y_pred})
@login_required(login_url="logins")
def kidney(request):
          # now i start writing the backend of the kidney model
          y_pred=''
          if request.method=='POST':
                    age=request.POST.get('age')
                    bloodpressure=request.POST.get('bloodpressure')
                    specificgravity=request.POST.get('specificgravity')
                    Albumin=request.POST.get('Albumin')
                    Sugar=request.POST.get('Sugar')
                    BloodGlucoseRandom=request.POST.get('BloodGlucoseRandom')
                    Blood_Urea=request.POST.get('Blood Urea')
                    Serum_Creatinine=request.POST.get('Serum Creatinine')
                    Sodium=request.POST.get('Sodium')
                    Potassium=request.POST.get('Potassium')
                    Hemoglobin=request.POST.get('Hemoglobin')
                    Packed_Cell_Volume=request.POST.get('Packed Cell Volume')
                    White_Blood_Cells=request.POST.get('White Blood Cells')
                    Red_Blood_Cells=request.POST.get('Red Blood Cells')
                    Red_Blood_Cells_normal=request.POST.get('Red Blood Cells: normal')
                    Pus_Cells_normal=request.POST.get('Pus Cells: normal')
                    Pus_Cell_Clumps_present=request.POST.get('Pus Cell Clumps: present')
                    Bacteria_present=request.POST.get('Bacteria: present')
                    Hypertension_yes=request.POST.get('Hypertension: yes')
                    Diabetes_Mellitus_yes=request.POST.get('Diabetes Mellitus: yes')
                    Coronary_Artery_Disease_yes=request.POST.get('Coronary Artery Disease: yes')
                    Appetite_poor=request.POST.get('Appetite: poor')
                    Pedal_Edema_yes=request.POST.get('Pedal Edema: yes')
                    Anemia_yes=request.POST.get('Anemia: yes')
                    y_pred=kidn.predict([[age,bloodpressure,specificgravity,Albumin,Sugar,BloodGlucoseRandom,Blood_Urea,Serum_Creatinine,Sodium,Potassium,Hemoglobin,Packed_Cell_Volume,White_Blood_Cells,Red_Blood_Cells,Red_Blood_Cells_normal,Pus_Cells_normal,Pus_Cell_Clumps_present,Bacteria_present,Hypertension_yes,Diabetes_Mellitus_yes,Coronary_Artery_Disease_yes,Appetite_poor,Pedal_Edema_yes,Anemia_yes]])
                    print(y_pred[0])
                    if y_pred[0]==0:
                              y_pred="non disease"
                    else:
                              y_pred="disease"
                    email=request.session['email']
                    # here i set the email concept 
                    subject = "Health Report"
                    message = "Hi Welcome to the Health prediction web application , First of all we thank you for using our services. your medical check up result for Kidney disease is"+ y_pred+"Thank you <br> Have a nice day ahead."
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [email]
                    send_mail(subject, message, from_email,to_email, fail_silently=False)
                   
          return render(request,"kidney.html",{"y":y_pred})
@login_required(login_url="logins")
def parkinson(request):
          # now i write the backend for the parkinsons disease
          y_pred=''
          if request.method=='POST':
                    
                    n1=request.POST.get('MDVP:Fo(Hz)')
                    n2=request.POST.get('MDVP:Fhi(Hz)')
                    n3=request.POST.get('MDVP:Flo(Hz)')
                    n4=request.POST.get('MDVP:Jitter(%)')
                    n5=request.POST.get('MDVP:Jitter(Abs)')
                    n6=request.POST.get('MDVP:RAP')
                    n7=request.POST.get('MDVP:PPQ')
                    n8=request.POST.get('Jitter:DDP')
                    n9=request.POST.get('MDVP:Shimmer')
                    n10=request.POST.get('MDVP:Shimmer(dB)')
                    n11=request.POST.get('Shimmer:APQ3')
                    n12=request.POST.get('Shimmer:APQ5')
                    n13=request.POST.get('MDVP:APQ')
                    n14=request.POST.get('Shimmer:DDA')
                    n15=request.POST.get('NHR')
                    n16=request.POST.get('HNR')
                    n17=request.POST.get('RPDE')
                    n18=request.POST.get('DFA')
                    n19=request.POST.get('spread1')
                    n20=request.POST.get('spread2')
                    n21=request.POST.get('D2')
                    n22=request.POST.get('PPE')
                    y_pred=park.predict([[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22]])
                    print(y_pred[0])
                    if y_pred[0]==0:
                              y_pred="nondisease"
                    else:
                              y_pred="disease"
                    email=request.session['email']
                    # here i set the email concept 
                    subject = "Health Report"
                    message = "Hi Welcome to the Health prediction web application , First of all we thank you for using our services. your medical check up result for parkinsons disease is"+ y_pred+"Thank you <br> Have a nice day ahead."
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [email]
                    send_mail(subject, message, from_email,to_email, fail_silently=False)
                    
          return render(request,"parkinson.html",{"y":y_pred})


def aboutus(request):
          return render(request,"aboutus.html")

@login_required(login_url="logins")
def enquire(request):
          if request.method=='POST':
                    n1=request.POST.get('subject')
                    n2=request.POST.get('enquire')
                    email=request.session['email']
                    # here i set the email concept 
                    subject = n1
                    message = n2
                    from_email = email
                    to_email = [settings.EMAIL_HOST_USER]
                    send_mail(subject, message, from_email,to_email, fail_silently=False)
          return render(request,"enquire.html")
          