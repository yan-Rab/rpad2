📘 Predição de Evasão – FastAPI + MVC + Machine Learning

Este projeto implementa uma API de predição de evasão estudantil usando FastAPI organizada no padrão MVC (Model–View–Controller).
O modelo de Machine Learning é treinado com dados sintéticos e carregado pela aplicação para responder previsões em tempo real.

🔹 Models

Camada onde o modelo de ML é carregado e representado (via joblib).

🔹 Services

Contém toda a lógica de negócio, como:

Carregar modelo

Processar entrada

Executar predição

🔹 Controllers

Recebem requisições da view e chamam os serviços.


🧠 Modelo de Machine Learning

O modelo é treinado em dados sintéticos que simulam o risco de evasão com base em fatores como:

Faltas

Média geral

Engajamento

Horas estudadas

Participação em atividades

Idade

Ele utiliza RandomForestClassifier, mas pode ser substituído por qualquer outro algoritmo.

O treinamento é feito pelo script:

python train_model.py


Ele gera o arquivo logistic_model.joblib, que é usado pela API.

🚀 Como rodar o projeto
1️⃣ Instalar dependências
pip install -r requirements.txt

2️⃣ Treinar o modelo
python train_model.py

3️⃣ Executar a API
uvicorn app.main:app --reload

4️⃣ Abrir a documentação interativa

Acesse no navegador:

http://127.0.0.1:8000/docs

📡 Endpoints
POST /predict

Recebe os dados do estudante e retorna o risco de evasão.

Exemplo:

{
  "age": 17,
  "gender": "M",
  "high_school_type": "public",
  "enem_score": 450.5,
  "family_income": 2.0,
  "works": true,
  "weekly_work_hours": 30,
  "first_semester_failures": 2,
  "scholarship_holder": false,
  "distance_to_campus_km": 12.3
}


Retorno:

{
  "prob_evasion": 0.9468198224968778,
  "predicted_class": 1,
  "threshold": 0.5
}

🧪 Testando via cURL
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "age": 17,
  "gender": "M",
  "high_school_type": "public",
  "enem_score": 450.5,
  "family_income": 2.0,
  "works": true,
  "weekly_work_hours": 30,
  "first_semester_failures": 2,
  "scholarship_holder": false,
  "distance_to_campus_km": 12.3
}'

📦 Requirements

O arquivo requirements.txt contém:

fastapi
uvicorn[standard]
pydantic
scikit-learn
pandas
numpy
joblib
python-multipart

🧱 Próximos passos sugeridos

Adicionar Dockerfile e docker-compose.yml

Criar CI/CD

Adicionar testes unitários com pytest

Monitorar desempenho do modelo

Implementar versionamento de modelos

📄 Licença

Uso livre para estudos e demonstrações.
