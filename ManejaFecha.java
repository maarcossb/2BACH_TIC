package MiCodigo;

public class ManejaFecha {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fecha fecha1;
		Fecha fecha2;
		fecha1=new Fecha(6,8,2004);
		fecha2=new Fecha(30,6,2004);
		if(fecha1.esPosterior(fecha2)==true) {
			System.out.println("Fecha1 es posterior a Fecha2");
		}
		else {
			System.out.println("Fecha1 es anterior a Fecha2");
		}
		fecha1.setMonth(2);
		System.out.println("El nuevo mes es "+fecha1.getMonth(0));
		fecha1.setMonth("Enero");
		System.out.println("El nuevo mes es "+fecha1.getMonth(1));
	}
}
