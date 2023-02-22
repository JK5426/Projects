<html>
<head>
<link href="webjars/bootstrap/5.2.3/css/bootstrap.min.css"
	rel="stylesheet">
<title>Login Page</title>
</head>

<body>
	<div class="conatiner p-5 my-5 border">
		<h1>Login</h1>
		<pre>${errorMessage}</pre>

		<form method="post">
			<div class="mb-3 mt-3 ">
				<label for="name">Name</label>
				 <input type="text" id="name" class="form-control"
					name="name" placeholder="Enter you name">
			</div>
			<div class="mb-3">
				<label for="password">Password</label>
				 <input type="password" class="form-control"
					id="password" name="password" placeholder="Enter password">
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
		</form>
	</div>
</body>
</html>