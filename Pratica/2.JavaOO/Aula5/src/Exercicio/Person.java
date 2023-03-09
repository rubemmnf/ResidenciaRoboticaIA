package Exercicio;

public class Person {
	private String nome;
	private int idade;
	private String sexo = "";
	private String cpf;
	
	public Person(String nome, String cpf) {
		this.nome = nome;
		this.cpf = cpf;
	}

	public Person(String nome, int idade, String sexo, String cpf) {
		this.nome = nome;
		this.idade = idade;
		this.sexo = sexo;
		this.cpf = cpf;
	}



	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}

	public String getSexo() {
		return sexo;
	}

	public void setSexo(String sexo) {
		this.sexo = sexo;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
}
