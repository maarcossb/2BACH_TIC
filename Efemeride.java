package MiCodigo;

public class Efemeride extends Fecha {
	private String quePaso;
	
	public Efemeride(int day, int month, int year, String quePaso) {
		super(day, month, year);
		// TODO Auto-generated constructor stub
		this.setQuePaso(quePaso);
	}

	public String getQuePaso() {
		return quePaso;
	}

	public void setQuePaso(String quePaso) {
		this.quePaso = quePaso;
	}
 
}
