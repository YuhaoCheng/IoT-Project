package dao;

import model.User;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;
import org.hibernate.criterion.Restrictions;
import org.hibernate.service.ServiceRegistry;
import org.hibernate.service.ServiceRegistryBuilder;

import java.util.List;

public class UserDAO  {
	private SessionFactory sessionFactory;
	private Session session;
	private Transaction transaction;

	
	private static class UserOPSingletonHolder {
        static UserDAO instance = new UserDAO();
    }

    public static UserDAO getInstance() {
        return UserOPSingletonHolder.instance;
    }
	
	public void init(){
		//创建配置对象
		Configuration config=new Configuration().configure();
		//创建服务注册对象
		ServiceRegistry serviceRegistry=new ServiceRegistryBuilder().applySettings(config.getProperties()).buildServiceRegistry();
		//创建sessionFactory
		sessionFactory=config.buildSessionFactory(serviceRegistry);
		//会话对象
		session=sessionFactory.openSession();
		//开启事务
		transaction=session.beginTransaction();
		
	}
	
	public void destory(){
		transaction.commit();//提交事务
		session.close();//关闭会话
		sessionFactory.close();//关闭会话工厂
		
	}
	
	public List<User> GetStudents(){
		getInstance().init();
		String hql="from User";
		Query query=session.createQuery(hql);
		@SuppressWarnings("unchecked")
		List<User> person=query.list();
		getInstance().destory();
		return person;
	}
	
	public void addStudents(User s){
		getInstance().init();
		session.save(s);//保存对象进入数据库
		getInstance().destory();
	}
	public List<User> searchStudents(String key){
		getInstance().init();
		Criteria crit = session.createCriteria(model.User.class).add( Restrictions.like("userName", "%"+key+"%") );
		crit.setMaxResults(50);
		@SuppressWarnings("unchecked")
		List<User> person = crit.list();
		System.out.println(person);
		getInstance().destory();
		return person;
	}
	
	public void deleteStudents(String id){
		getInstance().init();
		User s=(User)session.get(User.class, id);
		session.delete(s);
		getInstance().destory();
	}


}
