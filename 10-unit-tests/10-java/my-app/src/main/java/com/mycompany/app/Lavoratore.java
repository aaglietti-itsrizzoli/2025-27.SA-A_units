package com.mycompany.app;

public class Lavoratore extends Persona {
	private double salario;
	public Lavoratore(String nome, String cognome) {
		super(nome, cognome);
	}
	public Lavoratore(String nome, String cognome, double salario) {
		super(nome, cognome);
		this.salario = salario;
	}
	public double getSalario() {
		return salario;
	}
	public void setSalario(double salario) {
		this.salario = salario;
	}
	public void Presentati() {
		System.out.println("Ciao mi chiamo "+ super.getNome()+ " "+super.getCognome()+" , il mio salario è di "+ getSalario());
	}
	
	
	@Override
	public String toString() {
		return "Lavoratore [salario=" + salario + super.toString()+"]";
	}
	
}

