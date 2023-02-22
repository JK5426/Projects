package com.jitendra.springboot.myFirstWebApplication.hello;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class SayHelloController {

	@GetMapping("/hello")
	@ResponseBody
	public String sayHello() {
		return "Hello world";
	}
	
	@GetMapping("/say-hello-jsp")
	public String sayHelloJsp() {
		return "sayHello";
	}
}
