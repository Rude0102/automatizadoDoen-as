class AgenteDiagnostico:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento
        self.sintomas_relatados = []
        self.diagnostico = None

    def sensores(self, sintomas):
        # Coleta os sintomas relatados pelo paciente
        self.sintomas_relatados = sintomas

    def atuadores(self):
        # Retorna o diagnóstico mais provável e recomendações
        print(f"Diagnóstico provável: {self.diagnostico['doenca']}")
        print(f"Confiança: {self.diagnostico['confiança']*100:.2f}%")
        print("Recomendações: Consulte um especialista ou realize os exames sugeridos.")
    
    def funcao_objetivo(self, doenca, sintomas):
        # Calcula a correspondência entre os sintomas relatados e os sintomas da doença
        sintomas_doenca = set(self.base_conhecimento[doenca]['sintomas'])
        correspondencia = len(sintomas_doenca.intersection(sintomas)) / len(sintomas)
        return correspondencia

    def hill_climbing(self):
        melhor_doenca = None
        melhor_correspondencia = 0

        for doenca in self.base_conhecimento:
            correspondencia = self.funcao_objetivo(doenca, self.sintomas_relatados)
            if correspondencia > melhor_correspondencia:
                melhor_correspondencia = correspondencia
                melhor_doenca = doenca
        
        if melhor_doenca:
            self.diagnostico = {
                'doenca': melhor_doenca,
                'confiança': melhor_correspondencia,
                'exames': self.base_conhecimento[melhor_doenca]['exames']
            }
        else:
            self.diagnostico = None

# Base de conhecimento: Doenças e seus sintomas associados
base_conhecimento = {
    "Gripe": {
        "sintomas": ["febre", "tosse", "dor de cabeça", "coriza"],
        "exames": ["Hemograma completo", "PCR"]
    },
    "Covid-19": {
        "sintomas": ["febre", "tosse", "falta de ar", "cansaço"],
        "exames": ["Teste PCR", "Tomografia"]
    },
    "Dengue": {
        "sintomas": ["febre", "dor no corpo", "manchas vermelhas", "cansaço"],
        "exames": ["Hemograma", "Sorologia"]
    },
    "Enxaqueca": {
        "sintomas": ["dor de cabeça", "náusea", "sensibilidade à luz", "zumbido"],
        "exames": ["Consulta neurológica", "Ressonância"]
    }
}

# Simulação
agente = AgenteDiagnostico(base_conhecimento)

# Cenário 1: Sintomas relatados pelo paciente
sintomas_paciente = ["febre", "tosse", "cansaço"]

print("---- Cenário 1 ----")
agente.sensores(sintomas_paciente)
agente.hill_climbing()
agente.atuadores()

# Cenário 2: Sintomas diferentes
sintomas_paciente2 = ["dor de cabeça", "náusea", "sensibilidade à luz"]

print("\n---- Cenário 2 ----")
agente.sensores(sintomas_paciente2)
agente.hill_climbing()
agente.atuadores()
