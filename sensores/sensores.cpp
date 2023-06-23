#include <DHT.h>
#include <DHT_U.h>
float oxCheck = 1.43; // fator de correção obtido durante a calibração

//projeto medir a temperatura e a umidade com DHT11

#include <DHT.h>//Inclui a biblioteca DHT Sensor Library
#define DHTPIN 2//Pino digital 2 conectado ao DHT11
#define DHTTYPE DHT11//DHT 11

DHT dht(DHTPIN, DHTTYPE); // inicializando o objeto dht do tipo DHT passando como parâmetro o pino (DHTPIN) e o tipo do sensor (DHTTYPE)

void setup() {
  Serial.begin(9600); // inicializa a comunicação serial
  dht.begin(); // inicializa o sensor DHT11
}

void loop() {
  delay(20000);// intervalo de dois segundos entre as medições

  float h = dht.readHumidity(); // lê o valor da umidade e armazena na variável h do tipo float (aceita números com casas decimais)
  float t = dht.readTemperature(); // lê o valor da temperatura e armazena na variável t do tipo float (aceita números com casas decimais)

  if (isnan(h) || isnan(t)) { // verifica se a umidade ou temperatura são ou não um número
    return; // caso não seja um número retorna
  }

  Serial.print("Umidade: "); // imprime no monitor serial a mensagem "Umidade: "
  Serial.print(h); // imprime na serial o valor da umidade
  Serial.println("%"); // imprime na serial o caractere "%" e salta para a próxima linha
  Serial.print("Temperatura: "); // imprime no monitor serial a mensagem "Temperatura: "
  Serial.print(t); // imprime na serial o valor da temperatura
  Serial.println("°C "); // imprime no monitor serial "ºC" e salta para a próxima linha

// projeto medir gases voláteis e oxigênio
 
  int sensorValue = analogRead(A0); // lê o valor analógico presente no pino analógico A0
  
  float voltage = sensorValue * (5.0 / 1023.0); // converte o valor lido para tensão (considerando a alimentação de 5V)
  float oxygenConcentration = voltage * 21.4; // converte a tensão para concentração de oxigênio (fator de conversão típico)
  
  float oxConcentartion = oxygenConcentration * oxCheck; // aplica o "check" de correção de ox
  
  // calcula o valor inverso subtraindo o valor corrigido de 100%
  float concentration = 100.0 - oxConcentartion;
  
  Serial.print("Taxa de oxigênio local: "); // imprime no monitor serial a mensagem "Taxa de oxigênio local: "
  Serial.print(concentration); // imprime o valor da concentração
  Serial.println(" %"); // imprime na serial o caractere "%" e salta para a próxima linha

  Serial.print("Taxa de gases voláteis: "); // imprime no monitor serial a mensagem "Taxa de gases voláteis: "
  Serial.print(oxConcentartion); // imprime o valor da concentração
  Serial.print("%"); // imprime na serial o caractere "%" e salta para a próxima linha

}