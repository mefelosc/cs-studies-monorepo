 public class PilhaSimples {
        
    public static void main(String[] args) {
    	simularPilha();
    }
 
    public static void simularPilha() {
    	
    	// Empilhe: 5, 8, 4, 7 (nesta ordem)
    	// Desempilhe duas vezes
    	// Consulte o topo
    	// Desempilhe mais duas vezes
        int topo = -1;
        int[] pilha = new int[3]; // Pilha com capacidade para 3 elementos
        // Empilhe 4 elementos
        if (topo == 2) System.out.println("Pilha cheia!"); else pilha[++topo] = 5;
        if (topo == 2) System.out.println("Pilha cheia!"); else pilha[++topo] = 8;
        if (topo == 2) System.out.println("Pilha cheia!"); else pilha[++topo] = 4;
        if (topo == 2) System.out.println("Pilha cheia!"); else pilha[++topo] = 7;
        // Desempilhe duas vezes
        if (topo == -1) System.out.println("Pilha vazia!"); else System.out.println("Desempilhado: " + pilha[topo--]);
        if (topo == -1) System.out.println("Pilha vazia!"); else System.out.println
        ("Desempilhado: " + pilha[topo--]);
        // Consulte o topo
        if (topo == -1) System.out.println("Pilha vazia!"); else System.out.println("Topo: " + pilha[topo]);
        // Desempilhe mais duas vezes
        if (topo == -1) System.out.println("Pilha vazia!"); else System.out.println("Desempilhado: " + pilha[topo--]);
        if (topo == -1) System.out.println("Pilha vazia!"); else System.out.println("Desempilhado: " + pilha[topo--]);
        
                
        }
	}
