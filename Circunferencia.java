package MiCodigo;

public class Circunferencia {
	
	//ATRIBUTOS
	private MiParejaNumeros centroCirculo;
	private double radio;
	/**
	 * @param x
	 * @param y
	 * @param radio
	 */
	
	//CONSTRUCTOR
	public Circunferencia(int x, int y, double radio) {
		super();
		centroCirculo=new MiParejaNumeros(x,y);
		this.radio = radio;
	}
	
	//MÉTODOS
	/**
	 * @return the x
	 */
	public int getX() {
		return centroCirculo.getNum1();
	}
	/**
	 * @param x the x to set
	 */
	public void setX(int x) {
		centroCirculo.setNum1(x);
	}
	/**
	 * @return the y
	 */
	public int getY() {
		return centroCirculo.getNum2();
	}
	/**
	 * @param y the y to set
	 */
	public void setY(int y) {
		centroCirculo.setNum2(y);
	}
	/**
	 * @return the radio
	 */
	public double getRadio() {
		return radio;
	}
	/**
	 * @param radio the radio to set
	 */
	public void setRadio(double radio) {
		this.radio = radio;
	}
	

	
	public double devuelveArea(){
		double area;
		area=Math.PI*Math.pow(radio, 2);
		return area;
	}
	
	public double devuelveLongitud() {
		double longitud;
		longitud=2*Math.PI*radio;
		return longitud;
	}
	
	
	
}
