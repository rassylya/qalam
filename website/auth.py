from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth_', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
	data=request.form
	print(data)
	return render_template("login.html")

@auth.route('/logout')
def logout():
	return render_template("base.html")
	 
@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
	if request.method == 'POST':
		email=request.form.get('email')
		firstName = request.form.get('firstName')
		secondName = request.form.get('secondName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		if len(firstName) < 2:
			flash("Атыңыз 2 әріптен көп болу керек", category = 'error')
			
		elif len(secondName) < 2: 
			flash("Тегіңіз 2 әріптен көп болу керек", category = 'error')
			
		elif len(password1) < 8:
			flash("Құпия сөз 8 таңбадан көп болу керек", category = 'error')
			
		elif password1 != password2:
			flash("Құпия сөздер сәйкес келмейді", category = 'error')
		
		else:
			flash("Сәтті тіркелді", category = 'success')
			


	return render_template("sign_up.html")