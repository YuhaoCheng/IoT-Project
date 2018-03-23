package manager;

import dao.UserDAO;
import model.User;

import java.util.List;

public class UserManager {
	
	public UserManager(){}
    private static UserManager instance = new UserManager();
    public static UserManager getInstance() { return instance;}
	private static UserDAO getDAOInstance() { return UserDAO.getInstance(); }
	
	public static List<User> GetStudents(){
        return getDAOInstance().GetStudents();
    }
	
	public static List<User> SearchStudents(String key){
        return getDAOInstance().searchStudents(key);
    }
	
	public static void AddStudents(User s){
        getDAOInstance().addStudents(s);
    }

    public static void DeleteStudents(String id){
        getDAOInstance().deleteStudents(id);
    }
}
