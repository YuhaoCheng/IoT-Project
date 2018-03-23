package model;

public class User {

	
	private String id;
	private String userName;
	private String telephone;
	
	
	public User(){
		
	}
	
	
	public User(String id, String userName, String telephone) {
		super();
		this.id = id;
		this.userName = userName;
		this.telephone = telephone;
	}
	
	@Override
	public String toString() {
		return "User [id=" + id + ", userName=" + userName + ", telephone="
				+ telephone + "]";
	}
	
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getUserName() {
		return userName;
	}
	public void setUserName(String userName) {
		this.userName = userName;
	}
	public String getTelephone() {
		return telephone;
	}
	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}
	
	
}
