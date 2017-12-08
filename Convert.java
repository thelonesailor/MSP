import java.io.* ;
import java.util.* ;


class Convert{
	static mylist par[] ;
	static int time[] ;
	static PrintWriter op = new PrintWriter(System.out) ;
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in) ;
		int n = sc.nextInt() ;
		par = new mylist[n] ;		
		time = new int[n] ;
		for(int i=0 ; i<n ; i++) par[i] = new mylist() ;
		for(int i=-1 ; i<n ; i++){
			int tnum = sc.nextInt() ;
			int tt = sc.nextInt() ;
			int npar = sc.nextInt() ;
			mylist ls = new mylist() ;
			for(int j=0 ; j<npar ; j++){
				int val = sc.nextInt() ;
				if(val==0 || val==(n+1)) continue ;
				ls.add(val-1) ;
			}
			if(tnum==0) continue ;
			time[i]=tt ;
			par[i]=ls ;
		}
		int nedges = 0 ;
		for(int i=0 ; i<n ; i++) nedges+=par[i].size() ;
		op.print(n+" "+nedges+" "+5) ;
		op.println();
		for(int i=0 ; i<n ; i++) op.print(time[i]+(i!=(n-1) ? " " : "")) ;
		op.println() ;
		for(int i=0 ; i<n ; i++)
			for(int elem : par[i])
				op.println(elem+" "+i) ;
		op.flush() ;
	}
}
class mylist extends ArrayList<Integer>{}