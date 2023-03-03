
public class BJL {
	public static void main (String[] args) {
		// primitive types
		int x = 10;
		float f = 12.5f;
		double d = 12.5;
		char c = 'C';
			// x. não aparece nada
		
		x = (int) d;
		
		System.out.println(x);
		
		//Object types
		String s = "Java";
			//Aspas duplas obrigatórias, aspas simples para caracteres
			//s. aparece vários métodos
		
		System.out.println(s);
		System.out.println(s.charAt(0));
		System.out.println(s.length());
		System.out.println();
		
		for (int i = 0; i < s.length(); i++) {
			System.out.println(s.charAt(i));
		}
		
	}

}
