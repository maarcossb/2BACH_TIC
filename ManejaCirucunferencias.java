package MiCodigo;

public class ManejaCirucunferencias {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Circunferencia circ1;
		circ1=new Circunferencia(7,9,4.5);
		
		System.out.println("CIRCUNFERENCIA\n");
		System.out.println("Coordenada X: "+circ1.getX());
		System.out.println("Coordenada Y: "+circ1.getY());
		System.out.println("Radio: "+circ1.getRadio());
		
		System.out.println("Area: "+circ1.devuelveArea());
		System.out.println("Longitud: "+circ1.devuelveLongitud());

	}

}
