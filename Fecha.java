package MiCodigo;

public class Fecha {
	private int day;
	private int month;
	private int year;
	/**
	 * @param day
	 * @param month
	 * @param year
	 */
	public Fecha(int day, int month, int year) {
		super();
		this.day = day;
		this.month = month;
		this.year = year;
	}
	/**
	 * @return the day
	 */
	public int getDay() {
		return day;
	}
	/**
	 * @param day the day to set
	 */
	public void setDay(int day) {
		this.day = day;
	}
	/**
	 * @return the month
	 */
	public int getMonth() {
		return month;
	}
	public String getMonth(int modo) {
		String nombreMonth="";
		if(modo==0) {
			if(this.month==1) nombreMonth="Enero";
			if(this.month==2) nombreMonth="Febrero";
			if(this.month==3) nombreMonth="Marzo";
			if(this.month==4) nombreMonth="Abril";
			if(this.month==5) nombreMonth="Mayo";
			if(this.month==6) nombreMonth="Junio";
			if(this.month==7) nombreMonth="Julio";
			if(this.month==8) nombreMonth="Agosto";
			if(this.month==9) nombreMonth="Septiembre";
			if(this.month==10) nombreMonth="Octubre";
			if(this.month==11) nombreMonth="Noviembre";
			if(this.month==12) nombreMonth="Diciembre";
		}
		if(modo==1) {
			if(this.month==1) nombreMonth="ENERO";
			if(this.month==2) nombreMonth="FEBRERO";
			if(this.month==3) nombreMonth="MARZO";
			if(this.month==4) nombreMonth="ABRIL";
			if(this.month==5) nombreMonth="MAYO";
			if(this.month==6) nombreMonth="JUNIO";
			if(this.month==7) nombreMonth="JULIO";
			if(this.month==8) nombreMonth="AGOSTO";
			if(this.month==9) nombreMonth="SEPTIEMBRE";
			if(this.month==10) nombreMonth="OCTUBRE";
			if(this.month==11) nombreMonth="NOVIEMBRE";
			if(this.month==12) nombreMonth="DICIEMBRE";
		}
		
		return nombreMonth;
	}
	/**
	 * @param month the month to set
	 */
	public void setMonth(int month) {
		this.month = month;
	}
	public void setMonth(String nombreMonth) {
		if(nombreMonth=="Enero") this.month=1;
		if(nombreMonth=="Febrero") this.month=2;
		if(nombreMonth=="Marzo") this.month=3;
		if(nombreMonth=="Abril") this.month=4;
		if(nombreMonth=="Mayo") this.month=5;
		if(nombreMonth=="Junio") this.month=6;
		if(nombreMonth=="Julio") this.month=7;
		if(nombreMonth=="Agosto") this.month=8;
		if(nombreMonth=="Septiembre") this.month=9;
		if(nombreMonth=="Octubre") this.month=10;
		if(nombreMonth=="Noviembre") this.month=11;
		if(nombreMonth=="Diciembre") this.month=12;
	}
	/**
	 * @return the year
	 */
	public int getYear() {
		return year;
	}
	/**
	 * @param year the year to set
	 */
	public void setYear(int year) {
		this.year = year;
	}
	
	boolean esPosterior(Fecha nuevaFecha){
		boolean loEs;
		loEs=false;
		
		if(this.getYear()>nuevaFecha.getYear())
			loEs=true;
		else
			if(this.getYear()==nuevaFecha.getYear())
				if(this.getMonth()>nuevaFecha.getMonth()) 
					loEs=true;
				else 
					if(this.getMonth()==nuevaFecha.getMonth()) 
						if(this.getDay()>nuevaFecha.getDay())
							loEs=true;
		
		return loEs;
	}
}
