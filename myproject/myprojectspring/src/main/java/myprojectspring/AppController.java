package myprojectspring;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping("/")
public class AppController 
{
	
	public AppController()
	{
		System.out.println("AppController Constructor called");
	}

	//@RequestMapping(method = RequestMethod.GET)
	@RequestMapping("/test")
	public String AppControl(Model model)
	{
		System.out.println("AppControl method called");
		model.addAttribute("message", "nou dan is dit de output");
		return "test";
	}
	
}
