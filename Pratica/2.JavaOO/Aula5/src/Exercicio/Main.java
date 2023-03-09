package Exercicio;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person p = new Person("Rubem Novellino", 28, "M", "12345678900");
		
		System.out.println(p.getCpf());
		System.out.println(p.getIdade());
		
		System.out.println(p.getCpf().equals("123"));
		

	}

}
