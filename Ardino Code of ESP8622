#include <ESP8266WiFi.h>
#include <ESPAsyncWebServer.h>
#include <ESPAsyncTCP.h>

const char* ssid = "6944";
const char* password = "76543218";

AsyncWebServer server(80);

// SAFE GPIOs
const int thumbLedPin = 16;  // D0
const int indexLedPin = 5;   // D1
const int middleLedPin = 4;  // D2
const int ringLedPin = 14;   // D5
const int pinkyLedPin = 12;  // D6

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(thumbLedPin, OUTPUT);
  pinMode(indexLedPin, OUTPUT);
  pinMode(middleLedPin, OUTPUT);
  pinMode(ringLedPin, OUTPUT);
  pinMode(pinkyLedPin, OUTPUT);

  digitalWrite(thumbLedPin, LOW);
  digitalWrite(indexLedPin, LOW);
  digitalWrite(middleLedPin, LOW);
  digitalWrite(ringLedPin, LOW);
  digitalWrite(pinkyLedPin, LOW);

  Serial.println("Connecting to WiFi...");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(1000);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected!");
    Serial.println(WiFi.localIP());

    // HTTP endpoints
    server.on("/led/thumb/on", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(thumbLedPin, HIGH);
      request->send(200, "text/plain", "Thumb LED ON");
    });
    server.on("/led/thumb/off", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(thumbLedPin, LOW);
      request->send(200, "text/plain", "Thumb LED OFF");
    });

    server.on("/led/index/on", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(indexLedPin, HIGH);
      request->send(200, "text/plain", "Index LED ON");
    });
    server.on("/led/index/off", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(indexLedPin, LOW);
      request->send(200, "text/plain", "Index LED OFF");
    });

    server.on("/led/middle/on", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(middleLedPin, HIGH);
      request->send(200, "text/plain", "Middle LED ON");
    });
    server.on("/led/middle/off", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(middleLedPin, LOW);
      request->send(200, "text/plain", "Middle LED OFF");
    });

    server.on("/led/ring/on", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(ringLedPin, HIGH);
      request->send(200, "text/plain", "Ring LED ON");
    });
    server.on("/led/ring/off", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(ringLedPin, LOW);
      request->send(200, "text/plain", "Ring LED OFF");
    });

    server.on("/led/pinky/on", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(pinkyLedPin, HIGH);
      request->send(200, "text/plain", "Pinky LED ON");
    });
    server.on("/led/pinky/off", HTTP_GET, [](AsyncWebServerRequest *request){
      digitalWrite(pinkyLedPin, LOW);
      request->send(200, "text/plain", "Pinky LED OFF");
    });

    server.begin();
    Serial.println("Server started");
  } else {
    Serial.println("\n❌ WiFi Connection Failed");
  }
}

void loop() {}
