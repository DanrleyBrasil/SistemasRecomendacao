import java.util.*;

public class RecomendacaoFilmes {

    public static void main(String[] args) {
        Map<String, double[]> usuarios = new HashMap<>();
        usuarios.put("Paulo", new double[]{3.0, 3.5, 1.5, 5.0, 3.0, 3.5});
        usuarios.put("Joao", new double[]{2.5, 3.0, 0.0, 3.5, 0.0, 4.0});
        usuarios.put("Marcia", new double[]{0.0, 3.5, 3.0, 4.0, 2.5, 4.5});
        usuarios.put("Carlos", new double[]{3.0, 4.0, 0.0, 5.0, 3.5, 3.0});
        usuarios.put("Ana", new double[]{2.5, 3.5, 3.0, 3.5, 2.5, 3.0});
        usuarios.put("Mauro", new double[]{0.0, 4.0, 0.0, 4.0, 1.0, 0.0});

    }

    public static double distanciaEuclidiana(double[] usuario1, double[] usuario2) {
        double soma = 0;
        for (int i = 0; i < usuario1.length; i++) {
            soma += Math.pow(usuario1[i] - usuario2[i], 2);
        }
        return Math.sqrt(soma);
    }

    public static List<Recomendacao> recomendarFilmes(String usuarioAlvoNome, Map<String, double[]> usuarios, int k) {
        double[] usuarioAlvo = usuarios.get(usuarioAlvoNome);

        // Calcular distâncias
        List<Distancia> distancias = new ArrayList<>();
        for (Map.Entry<String, double[]> entry : usuarios.entrySet()) {
            String nome = entry.getKey();
            if (!nome.equals(usuarioAlvoNome)) {
                double dist = distanciaEuclidiana(usuarioAlvo, entry.getValue());
                distancias.add(new Distancia(nome, dist));
                System.out.printf("Distância euclidiana entre %s e %s: %.2f%n", usuarioAlvoNome, nome, dist);
            }
        }

        // Ordenar por distâncias
        distancias.sort(Comparator.comparingDouble(Distancia::getDistancia));

        // Selecionar os k usuários mais similares
        List<String> usuariosSimilares = new ArrayList<>();
        for (int i = 0; i < k && i < distancias.size(); i++) {
            usuariosSimilares.add(distancias.get(i).getNome());
        }

        // Recomendar filmes
        Map<Integer, List<Double>> recomendacoes = new HashMap<>();
        for (String usuario : usuariosSimilares) {
            double[] avaliacoesSimilar = usuarios.get(usuario);
            for (int i = 0; i < avaliacoesSimilar.length; i++) {
                if (usuarioAlvo[i] == 0) { // Se Mauro não assistiu o filme
                    recomendacoes.putIfAbsent(i, new ArrayList<>());
                    recomendacoes.get(i).add(avaliacoesSimilar[i]);
                }
            }
        }

        // Calcular média das notas
        List<Recomendacao> recomendacoesFinais = new ArrayList<>();
        for (Map.Entry<Integer, List<Double>> entry : recomendacoes.entrySet()) {
            int filme = entry.getKey();
            List<Double> notas = entry.getValue();
            double media = notas.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
            recomendacoesFinais.add(new Recomendacao(filme, media));
        }

        // Ordenar recomendações
        recomendacoesFinais.sort((r1, r2) -> Double.compare(r2.getNota(), r1.getNota()));

        return recomendacoesFinais;
    }
}

class Distancia {
    private final String nome;
    private final double distancia;

    public Distancia(String nome, double distancia) {
        this.nome = nome;
        this.distancia = distancia;
    }

    public String getNome() {
        return nome;
    }

    public double getDistancia() {
        return distancia;
    }
}

class Recomendacao {
    private final int filme;
    private final double nota;

    public Recomendacao(int filme, double nota) {
        this.filme = filme;
        this.nota = nota;
    }

    public int getFilme() {
        return filme;
    }

    public double getNota() {
        return nota;
    }
}
