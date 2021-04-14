import java.lang.reflect.*;


class Reflect02
{
    public static void main(String [] args)
    {
        Countdown c = new Countdown();


        Field [] fields = Countdown.class.getDeclaredFields();

        int cycle;

        try{
            fields[0].setAccessible(true);
            cycle = (int) fields[0].get(c);
            fields[0].set(c,10);
            c.main(null);
            System.out.println("field[0] is a " + fields[0] +  " and has a value of " + cycle);

        }catch(Exception e){
        }
/*
        for(Field f: fields){
    
            System.out.println(f);
        }
*/
        
        

    }
}

