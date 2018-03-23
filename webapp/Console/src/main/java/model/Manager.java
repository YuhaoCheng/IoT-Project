package model;

public class Manager {
    private String managerID;
    private String password;

    public Manager(){

    }

    public Manager(String managerID, String password){
        super();
        this.managerID = managerID;
        this.password = password;
    }

    @Override
    public String toString(){
        return "Manger [mangerID=" + managerID + ", password=" + password + "]";
    }

    public String getManagerID() {
        return managerID;
    }

    public void setManagerID(String managerID){this.managerID = managerID;}

    public String getPassword() {
        return password;
    }

    public void setPassword(String password){this.password = password;}

}
