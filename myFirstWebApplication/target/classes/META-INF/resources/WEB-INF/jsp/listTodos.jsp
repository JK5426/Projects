	<%@ include file="common/header.jspf" %>
	<%@ include file="common/navigation.jspf" %>
	<%@ include file="common/footer.jspf" %>
	<div class="container">
		<h1>${name} todos :</h1>
		<table class="table">
			<thead>
				<tr>
					<th>Description</th>
					<th>Target date</th>
					<th>Is Done ?</th>
					<th></th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				<c:forEach items="${todos}" var="todo">
					<tr>
						<td>${todo.description}</td>
						<td>${todo.targetDate}</td>
						<td>${todo.done}</td>
						<td><a href="update-todo?id=${todo.id}"
							class="btn btn-secondary">UPDATE</a></td>
						<td><a href="delete-todo?id=${todo.id}"
							class="btn btn-warning">DELETE</a></td>
					</tr>
				</c:forEach>
			</tbody>
		</table>
		<a href="add-todo" class="btn btn-success">Add Todo</a>
	</div>
<%@ include file="common/footer.jspf"%>