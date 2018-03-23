package action;

import com.opensymphony.xwork2.ActionSupport;
import manager.UserManager;
import model.User;

import java.util.List;

public class UserAction extends ActionSupport {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String key;
	private String id;
	private String name;
	private String telephone;
	private List<User> userList;

	public String execute(){
		userList= UserManager.GetStudents();
		return SUCCESS;
	}
	
	public String searchGroup(){
		userList= UserManager.SearchStudents(this.key);
		return SUCCESS;
	}
	
	public String addUsers(){
		User s = new User();
		s.setTelephone(this.telephone);
		s.setUserName(this.name);
		/*
		 * 生成不重复的用户ID
		 */
		userList= UserManager.GetStudents();
		boolean flag=true;
		int count=0;
		int newId=0;
		while(flag){
			newId=(int) (Math.random()*999);
			for(User user:userList){
				int judge=Integer.parseInt(user.getId());
				if(judge!=newId){
					count++;
				}			
			}
			if(count==userList.size()){
				flag=false;
			}
		}
		String Id = String.valueOf(newId);
		s.setId(Id);
		
		UserManager.AddStudents(s);
	
		return SUCCESS;
	}
	
	public String deleteUsers(){
		UserManager.DeleteStudents(this.id);
		return SUCCESS;
	}

	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getKey() {
		return key;
	}

	public void setKey(String key) {
		this.key = key;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getTelephone() {
		return telephone;
	}

	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}

	public List<User> getUserList() {
		return userList;
	}

	public void setUserList(List<User> userList) {
		this.userList = userList;
	}
	
	
}
