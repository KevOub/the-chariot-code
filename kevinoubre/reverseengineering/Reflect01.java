import java.lang.reflect.*;

class Reflect01
{
    public static void main(String []args) throws Exception
    {
        Test t = new Test();
        Class c = t.getClass();

        System.out.println("the nameof hte class: " + c.getName());
        try{
            
            Constructor con = c.getConstructor();
            System.out.println("constructor: "+ con.getName());
        } catch(Exception e){}

        Method [] methods = c.getMethods();

        for( Method m : methods){
            System.out.println(m);
        }

        System.out.println("-------------------");

        Method [] allmethods = c.getDeclaredMethods();

        for( Method m : allmethods){
            System.out.println(m);
        }

        Method methodcall1 = c.getDeclaredMethod("method3",int.class);
        methodcall1.invoke(t,2);

        Method methodcall2 = c.getDeclaredMethod("method2");
        methodcall2.setAccessible(true);
        methodcall2.invoke(t);
     

    }
}
