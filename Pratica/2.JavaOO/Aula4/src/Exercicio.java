import java.util.ArrayList;
import java.util.Arrays;

public class Exercicio {
	public static String replace (String s, char target, char replacement) {
		char sCharArray [] = s.toCharArray();
		for (int i = 0; i < s.length(); i++) {
			if (sCharArray[i] == target) {
				sCharArray[i] = replacement;
			}
		}
		String retorno = Arrays.toString(sCharArray);		
		return retorno;
	}
	
	public static Boolean containsAll(ArrayList<String>list1, ArrayList<String>list2) {
		int k = 0;
		for (int i = 0; i < list1.size(); i++) {
			for (int j = 0; j < list2.size(); j++) {
				if (list1.get(i).equals(list2.get(j))) {
					k++;
				}
			} 
		}
		if (k == list2.size()) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public static void main(String[] args) {
		System.out.println(replace("Java",'a','o'));
	}

}
