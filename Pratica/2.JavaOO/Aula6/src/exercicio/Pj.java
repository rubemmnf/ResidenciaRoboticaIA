package exercicio;

public class Pj {
	private String nome;
	private String razão;
	private String cnpj;
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getRazão() {
		return razão;
	}
	public void setRazão(String razão) {
		this.razão = razão;
	}
	public String getCnpj() {
		return cnpj;
	}
	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	
	@Override
	public String toString() {
		return "Empresa [nome=" + nome + ", razão=" + razão + ", cnpj=" + cnpj + "]";
	}
	
	public Pj(String nome, String razão, String cnpj) {
		this.nome = nome;
		this.razão = razão;
		this.cnpj = cnpj;
	}	
	
}
