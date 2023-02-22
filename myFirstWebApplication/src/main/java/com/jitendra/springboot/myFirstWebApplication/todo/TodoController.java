package com.jitendra.springboot.myFirstWebApplication.todo;

import java.time.LocalDate;
import java.util.List;

import org.springframework.ui.ModelMap;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;

import com.jitendra.springboot.myFirstWebApplication.security.SpringSecurityConfiguration;

import jakarta.validation.Valid;

//@Controller
@SessionAttributes("name") // if we want to keep model attribute value "name" from one page to another page
public class TodoController {
	
	private TodoService todoService;	
	
	public TodoController(TodoService todoService) {
		super();
		this.todoService = todoService;
	}

	@RequestMapping("list-todos")
	public String listAllTodos(ModelMap model) {
		String user = SpringSecurityConfiguration.getLoggedInUserName();
		List<Todo> todos = todoService.findByUserName(user);
		model.put("name", user);
		model.addAttribute("todos", todos);
		return "listTodos";
	}
	@GetMapping("add-todo")
	public String showNewTodoPage(ModelMap model) { // 2-way validation
		Todo todo = new Todo(0,(String)model.get("name"),"Default Description",LocalDate.now(),false);
		model.put("todo", todo);
		return "todo";
	}
	
	@PostMapping("add-todo")
	public String addNewTodo(ModelMap model, @Valid Todo todo, BindingResult result) {
		if(result.hasErrors()){
			return "todo";
		}
		todoService.addTodo((String) model.get("name"),todo.getDescription() , LocalDate.now().plusYears(1), false);
		return "redirect:list-todos";
	}
	@RequestMapping("delete-todo")
	public String deleteTodo(@RequestParam int id) {
		todoService.deleteById(id);
		return  "redirect:list-todos";
	}
	@RequestMapping(value = "update-todo", method = RequestMethod.GET)
	public String showUpdateTodo(@RequestParam int id,ModelMap model) {
		Todo todo = todoService.findById(id);
		model.put("todo",todo);
		return  "todo";
	}
	@RequestMapping(value = "update-todo", method = RequestMethod.POST)
	public String updateTodo(@RequestParam int id,ModelMap model,@Valid Todo todo,BindingResult result) {
		if(result.hasErrors()){
			return "todo";
		}
		todoService.updateTodo(todo);
		return  "redirect:list-todos";
	}
}
