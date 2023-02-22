package com.jitendra.springboot.myFirstWebApplication.login;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.SessionAttributes;

import com.jitendra.springboot.myFirstWebApplication.security.SpringSecurityConfiguration;

@Controller
@SessionAttributes("name")
public class WelcomeController {

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String goToWlcomePage(ModelMap model) {
		model.put("name", SpringSecurityConfiguration.getLoggedInUserName());
		return "welcome";
	}
}
